import os
import csv
import pandas as pd

nome = "IBGE"
base_url = "https://servicodados.ibge.gov.br/api"
identificadores = {}
identificadoresPorCodigo = {}
identificadoresPorId = {}

def identificador(tipo, cod = None, *, id = None):
    """
    Função para recuperar um identificador com base no tipo
    e no código. Alternativamente, pode-se usar o id em vez
    do código, o que é útil para descobrir o código e o nome
    quando o id é conhecido.
    """
    if cod is None and id is None:
        raise ValueError("Para recuperar os dados do identificador, é necessário informar o código ou o id.")
    dicionario = identificadoresPorCodigo if cod is not None else identificadoresPorId
    chave = cod if cod is not None else id
    return dicionario[tipo][chave]

identificadores_dir = os.path.join(os.path.dirname(__file__), 'identificadores')
def carregarIdentificadores(tipo, idNumerico = False):
    """
    Função utilizada para ler a tabela de identificadores e
    carregar seu conteúdo no dicionário de identificadores.
    """
    identificadores[tipo] = []
    identificadoresPorCodigo[tipo] = {}
    identificadoresPorId[tipo] = {}
    with open(f'{identificadores_dir}/{tipo}.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            identificador = {
                'cod': row[0],
                'id': row[1] if not idNumerico else int(row[1]),
                'nome': row[2],
            }
            identificadores[tipo].append(identificador)
            identificadoresPorCodigo[tipo][identificador['cod']] = identificador
            identificadoresPorId[tipo][identificador['id']] = identificador
    identificadores[tipo] = pd.DataFrame(identificadores[tipo])

carregarIdentificadores('assuntos', True)
carregarIdentificadores('classificacao', True)
carregarIdentificadores('nivel_geografico')
carregarIdentificadores('periodicidade')

def createCods(tipo_de_identificador, idNumerico = False):
    """
    Função utilizada para gerar, nas tabelas de identificadores,
    os códigos a serem usados como chaves legíveis, a partir de
    seus respectivos nomes.
    """
    from slugify import UniqueSlugify
    custom_slugify = UniqueSlugify(to_lower=True, separator='_')
    new_data = []
    with open(f'{identificadores_dir}/{tipo_de_identificador}.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            row[0] = custom_slugify(row[2])
            if idNumerico:
                row[1] = int(row[1])
            new_data.append(row)
    with open(f'{identificadores_dir}/{tipo_de_identificador}.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_STRINGS)
        spamwriter.writerows(new_data)

# createCods('assuntos', True)
# createCods('classificacao', True)
# createCods('nivel_geografico')
# createCods('periodicidade')


