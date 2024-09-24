import os
import importlib
import requests
from string import Template
import pandas as pd

_fontes = {}

def listar():
    return _fontes.keys()

def __getattr__(key):
    if key in _fontes:
        return _fontes.get(key)
    raise AttributeError(f"A fonte de dados <'{key}'> não existe.")

class Fonte:
    def __init__(self, id, config):
        self.id = id
        self.config = config
        self.pesquisas = {}
        self.buffer = {}

    def __getattr__(self, key):
        if key in self.pesquisas:
            return self.pesquisas[key]
        if key in self.config.__dict__:
            return self.config.__dict__[key]
        raise AttributeError(f"A pesquisa <'{key}'> não existe na fonte {self.nome}.")

    def __str__(self):
        return f"<Fonte de Dados: {self.nome}>"


class Pesquisa:
    def __init__(self, id, config, fonte):
        self.id = id
        self.config = config
        self.fonte = fonte

    def preparar_caminho(self, consulta):
        consulta_config = self.config.consultas[consulta]
        return self.caminho + consulta_config['caminho']

    def preparar_url(self, consulta):
        return self.fonte.base_url + self.preparar_caminho(consulta)

    def __getattr__(self, key):
        if key in self.config.consultas:
            consulta_config = self.config.consultas[key]
            def consulta_method(**params):
                url = self.preparar_url(key)
                if 'params' in consulta_config:
                    params_dict = {}
                    for param in consulta_config['params']:
                        if param not in params:
                            if 'params_defaults' not in consulta_config or param not in consulta_config['params_defaults']:
                                raise TypeError(f"O parâmetro {param} não foi fornecido para a consulta {key}.")
                            else:
                                params_dict[param] = consulta_config['params_defaults'][param]
                        else:
                            params_dict[param] = params[param]
                    url = Template(url).substitute(params_dict)
                querystring = ""
                if 'query_params' in consulta_config:
                    for param in consulta_config['query_params']:
                        if param in params:
                            querystring += f"{param}={params[param]}&"
                        elif 'params_defaults' in consulta_config and param in consulta_config['params_defaults']:
                            querystring += f"{param}={consulta_config['params_defaults'][param]}&"
                if querystring:
                    url += f"?{querystring}"

                # print(url)

                buffer_key = f"[{key}]{url}"
                if buffer_key in self.fonte.buffer:
                    return self.fonte.buffer[buffer_key]

                response = requests.get(url)
                response.raise_for_status()
                dados = response.json()
                if 'tabular' in consulta_config and callable(consulta_config['tabular']):
                    dados = consulta_config['tabular'](dados)
                dataframe = pd.DataFrame.from_dict(
                    pd.json_normalize(dados),
                    orient = 'columns')
                
                self.fonte.buffer[buffer_key] = dataframe
                
                return dataframe
            return consulta_method
        if key in self.config.__dict__:
            return self.config.__dict__[key]
        raise AttributeError(f"O endpoint <'{key}'> não existe na pesquisa {self.nome}.")

    def __str__(self):
        return f"<Pesquisa: {self.nome}>"

def carregar_pesquisas(fonte):
    fonte_dir = os.path.dirname(fonte.config.__file__)
    
    # Varre o diretório da fonte para encontrar as pesquisas
    for arquivo in os.listdir(fonte_dir):
        if arquivo.endswith('.py') and not arquivo.startswith('__'):
            pesquisa_id = arquivo[:-3]  # Nome do arquivo sem a extensão
            pesquisa_config = importlib.import_module(f'inteligencia_popular.config.{fonte.id}.{pesquisa_id}')
            fonte.pesquisas[pesquisa_id] = Pesquisa(pesquisa_id, pesquisa_config, fonte)


def carregar_fontes():
    base_dir = os.path.join(os.path.dirname(__file__), 'config')
    
    # Varre o diretório de configurações para encontrar fontes
    for fonte_id in os.listdir(base_dir):
        fonte_dir = os.path.join(base_dir, fonte_id)
        if os.path.isdir(fonte_dir) and not fonte_id.startswith('__'):
            try:
                fonte_config = importlib.import_module(f'inteligencia_popular.config.{fonte_id}')
                fonte = Fonte(fonte_id, fonte_config)
                pesquisas = carregar_pesquisas(fonte)
                _fontes[fonte_id] = fonte
            except ModuleNotFoundError as e:
                print(f"Erro ao carregar a fonte {fonte_id}: {e}")


# Carrega fontes disponíveis
carregar_fontes()