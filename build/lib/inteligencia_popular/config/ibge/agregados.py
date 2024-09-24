nome = "Agregados"
caminho = "/v3/agregados"

def tabularResultados(dados):
    from slugify import UniqueSlugify
    custom_slugify = UniqueSlugify(to_lower=True)

    colunas = None
    resultados = []
    for d in dados:
        if colunas is None:
            colunas = {}
            for ref, col in d.items():
                colunas[ref] = custom_slugify(col.replace(' (Código)', '-id'))
        else:
            r = {}
            for ref, col in colunas.items():
                r[col] = d[ref]
            resultados.append(r)
    return resultados

consultas = {

    # AGREGADOS ###########################################################

    'disponiveis': {
        'caminho': '',
        'query_params': [
            'periodo',
            'assunto',
            'classificacao',
            'periodicidade',
            'nivel'],
        'tabular': lambda dados: [
            {
                'pesquisa-id': pesquisa['id'],
                'pesquisa-nome': pesquisa['nome'],
                'agregado-id': agregado['id'],
                'agregado-nome': agregado['nome']
            }
            for pesquisa in dados
            for agregado in pesquisa['agregados']
        ]
    },
    'localidadesPorAgregado': {
        'caminho': '/${agregado}/localidades/${nivel}',
        'params': [ 'agregado', 'nivel' ],
    },
    'periodosPorAgregado': {
        'caminho': '/${agregado}/periodos',
        'params': [ 'agregado' ],
    },

    # METADADOS ###########################################################

    'metadados': {
        'caminho': '/${agregado}/metadados',
        'params': ['agregado'],
        'tabular': lambda dados: [
            { 'col': 'id', 'val': dados['id'] },
            { 'col': 'nome', 'val': dados['nome'] },
            { 'col': 'sidra', 'val': dados['URL'] },
            { 'col': 'pesquisa', 'val': dados['pesquisa'] },
            { 'col': 'assunto', 'val': dados['assunto'] },
            { 'col': 'frequencia', 'val': dados['periodicidade']['frequencia'] },
            { 'col': 'inicio', 'val': dados['periodicidade']['inicio'] },
            { 'col': 'fim', 'val': dados['periodicidade']['fim'] },
        ]
    },
    'nivelTerritorial': {
        'caminho': '/${agregado}/metadados',
        'params': ['agregado'],
        'tabular': lambda dados: [{
                'divisao': 'Administrativo',
                'niveis': niveis
            } for niveis in dados['nivelTerritorial']['Administrativo'] ]
            + [{
                'divisao': 'Especial',
                'niveis': niveis
            } for niveis in dados['nivelTerritorial']['Especial'] ]
            + [{
                'divisao': 'IBGE',
                'niveis': niveis
            } for niveis in dados['nivelTerritorial']['IBGE'] ]
    },
    'variaveis': {
        'caminho': '/${agregado}/metadados',
        'params': ['agregado'],
        'tabular': lambda dados: [
            variavel for variavel in dados['variaveis']
        ]
    },
    'classificacoes': {
        'caminho': '/${agregado}/metadados',
        'params': ['agregado'],
        'tabular': lambda dados: [
            {
                'classificacao-id': classificacao['id'],
                'classificacao-nome': classificacao['nome'],
                'categoria-id': categoria['id'],
                'categoria-nome': categoria['nome'],
                'categoria-unidade': categoria['unidade'],
                'categoria-nivel': categoria['nivel'],
            } for classificacao in dados['classificacoes']
                for categoria in classificacao['categorias']
        ]
    },

    # RESULTADOS ##########################################################

    'resultados': {
        'caminho': '/${agregado}/variaveis/${variaveis}',
        'params': [
            'agregado',
            'variaveis' ],
        'query_params': [
            'localidades',
            'classificacao',
            'view' # json, OLAP, flat
        ],
        'params_defaults': {
            'view': 'flat'
        },
        'tabular': tabularResultados
    },
    'resultadosPorPeriodo': {
        'caminho': '/${agregado}/periodos/${periodos}/variaveis/${variaveis}',
        'params': [
            'agregado',
            'periodos',
            'variaveis' ],
        'query_params': [
            'localidades',
            'classificacao',
            'view' # json, OLAP, flat
        ],
        'params_defaults': {
            'view': 'flat'
        },
        'tabular': tabularResultados
    },
}
