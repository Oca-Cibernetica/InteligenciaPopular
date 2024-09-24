nome = "Localidades"
caminho = "/v1/localidades"

consultas = {

    # DISTRITOS ###########################################################

    'distritos': {
        'caminho': '/distritos',
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'distritosPorIdentificador': {
        'caminho': '/distritos/${id}',
        'params': [ 'id' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'distritosPorUF': {
        'caminho': '/estados/${uf}/distritos',
        'params': [ 'uf' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'distritosPorMesorregiao': {
        'caminho': '/mesorregioes/${mesorregiao}/distritos',
        'params': [ 'mesorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'distritosPorMicrorregiao': {
        'caminho': '/microrregioes/${microrregiao}/distritos',
        'params': [ 'microrregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'distritosPorMunicipio': {
        'caminho': '/municipios/${municipio}/distritos',
        'params': [ 'municipio' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'distritosPorRegiaoImediata': {
        'caminho': '/regioes-imediatas/${regiao_imediata}/distritos',
        'params': [ 'regiao_imediata' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'distritosPorRegiaoIntermediaria': {
        'caminho': '/regioes-intermediarias/${regiao_intermediaria}/distritos',
        'params': [ 'regiao_intermediaria' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'distritosPorRegiao': {
        'caminho': '/regioes/${macrorregiao}/distritos',
        'params': [ 'macrorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },

    # MESORREGIÕES ########################################################

    'mesorregioes': {
        'caminho': '/mesorregioes',
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'mesorregioesPorIdentificador': {
        'caminho': '/mesorregioes/${mesorregiao}',
        'params': [ 'mesorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'mesorregioesPorUF': {
        'caminho': '/estados/${uf}/mesorregioes',
        'params': [ 'uf' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'mesorregioesPorRegiao': {
        'caminho': '/regioes/${macrorregiao}/mesorregioes',
        'params': [ 'macrorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },

    # MICRORREGIÕES #######################################################

    'microrregioes': {
        'caminho': '/microrregioes',
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'microrregioesPorIdentificador': {
        'caminho': '/microrregioes/${microrregiao}',
        'params': [ 'microrregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'microrregioesPorUF': {
        'caminho': '/estados/${uf}/microrregioes',
        'params': [ 'uf' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'microrregioesPorMesorregiao': {
        'caminho': '/mesorregioes/${mesorregiao}/microrregioes',
        'params': [ 'mesorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'microrregioesPorRegiao': {
        'caminho': '/regioes/${macrorregiao}/microrregioes',
        'params': [ 'macrorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },

    # MUNICÍPIOS ##########################################################

    'municipios': {
        'caminho': '/municipios',
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'municipiosPorIdentificador': {
        'caminho': '/municipios/${municipio}',
        'params': [ 'municipio' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'municipiosPorUF': {
        'caminho': '/estados/${uf}/municipios',
        'params': [ 'uf' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'municipiosPorMesorregiao': {
        'caminho': '/mesorregioes/${mesorregiao}/municipios',
        'params': [ 'mesorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'municipiosPorMicrorregiao': {
        'caminho': '/microrregioes/${microrregiao}/municipios',
        'params': [ 'microrregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'municipiosPorRegiaoImediata': {
        'caminho': '/regioes-imediatas/${regiao_imediata}/municipios',
        'params': [ 'regiao_imediata' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'municipiosPorRegiaoIntermediaria': {
        'caminho': '/regioes-intermediarias/${regiao_intermediaria}/municipios',
        'params': [ 'regiao_intermediaria' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'municipiosPorRegiao': {
        'caminho': '/regioes/${macrorregiao}/municipios',
        'params': [ 'macrorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },

    # PAÍSES ##############################################################

    'paises': {
        'caminho': '/paises',
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
            'lang', # EN ou ES
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'paisesPorIdentificador': {
        'caminho': '/paises/${pais}',
        'params': [ 'pais' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
            'lang', # EN ou ES
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },

    # REGIÕES #############################################################

    'regioes': {
        'caminho': '/regioes',
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'regioesPorIdentificador': {
        'caminho': '/regioes/${macrorregiao}',
        'params': [ 'macrorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },

    # REGIÕES IMEDIATAS ###################################################

    'regioesImediatas': {
        'caminho': '/regioes-imediatas',
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'regioesImediatasPorIdentificador': {
        'caminho': '/regioes-imediatas/${regiao_imediata}',
        'params': [ 'regiao_imediata' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'regioesImediatasPorUF': {
        'caminho': '/estados/${uf}/regioes-imediatas',
        'params': [ 'uf' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'regioesImediatasPorRegiao': {
        'caminho': '/regioes/${macrorregiao}/regioes-imediatas',
        'params': [ 'macrorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },

    # REGIÕES INTEGRADAS DE DESENVOLVIMENTO ###############################

    'regioesIntegradasDeDesenvolvimento': {
        'caminho': '/regioes-integradas-de-desenvolvimento',
        'query_params': [
            'orderBy',
            'municipio',
        ],
    },
    'regioesIntegradasDeDesenvolvimentoPorIdentificador': {
        'caminho': '/regioes-integradas-de-desenvolvimento/${regiao_integrada}',
        'params': [ 'regiao_integrada' ],
        'query_params': [
            'orderBy',
        ],
    },

    # REGIÕES INTERMEDIÁRIAS ##############################################

    'regioesIntermediarias': {
        'caminho': '/regioes-intermediarias',
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'regioesIntermediariasPorIdentificador': {
        'caminho': '/regioes-intermediarias/${regiao_intermediaria}',
        'params': [ 'regiao_intermediaria' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'regioesIntermediariasPorUF': {
        'caminho': '/estados/${uf}/regioes-intermediarias',
        'params': [ 'uf' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'regioesIntermediariasPorRegiao': {
        'caminho': '/regioes/${macrorregiao}/regioes-intermediarias',
        'params': [ 'macrorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },

    # REGIÕES METROPOLITANAS ##############################################

    'regioesMetropolitanas': {
        'caminho': '/regioes-metropolitanas',
        'query_params': [
            'orderBy',
            'municipio',
        ],
    },
    'regioesMetropolitanasPorIdentificador': {
        'caminho': '/regioes-metropolitanas/${regiao_metropolitana}',
        'params': [ 'regiao_metropolitana' ],
        'query_params': [
            'orderBy',
        ],
    },
    'regioesMetropolitanasPorUF': {
        'caminho': '/estados/${uf}/regioes-metropolitanas',
        'params': [ 'uf' ],
        'query_params': [
            'orderBy',
        ],
    },
    'regioesMetropolitanasPorRegiao': {
        'caminho': '/regioes/${macrorregiao}/regioes-metropolitanas',
        'params': [ 'macrorregiao' ],
        'query_params': [
            'orderBy',
        ],
    },

    # SUBDISTRITOS ########################################################

    'subdistritos': {
        'caminho': '/subdistritos',
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'subdistritosPorIdentificador': {
        'caminho': '/subdistritos/${subdistrito}',
        'params': [ 'subdistrito' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'subdistritosPorUF': {
        'caminho': '/estados/${uf}/subdistritos',
        'params': [ 'uf' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'subdistritosPorDistrito': {
        'caminho': '/distritos/${distrito}/subdistritos',
        'params': [ 'distrito' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'subdistritosPorMunicipio': {
        'caminho': '/municipios/${municipio}/subdistritos',
        'params': [ 'municipio' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'subdistritosPorMicrorregiao': {
        'caminho': '/microrregioes/${microrregiao}/subdistritos',
        'params': [ 'microrregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'subdistritosPorMesorregiao': {
        'caminho': '/mesorregioes/${mesorregiao}/subdistritos',
        'params': [ 'mesorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'subdistritosPorRegiaoImediata': {
        'caminho': '/regioes-imediatas/${regiao_imediata}/subdistritos',
        'params': [ 'regiao_imediata' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'subdistritosPorRegiao': {
        'caminho': '/regioes/${macrorregiao}/subdistritos',
        'params': [ 'macrorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },

    # ESTADOS #############################################################

    'estados': {
        'caminho': '/estados',
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'estadosPorIdentificador': {
        'caminho': '/estados/${uf}',
        'params': [ 'uf' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },
    'estadosPorRegiao': {
        'caminho': '/regioes/${macrorregiao}/estados',
        'params': [ 'macrorregiao' ],
        'query_params': [
            'orderBy',
            'view', # nivelado ou json
        ],
        'params_defaults': {
            'view': 'nivelado'
        },
    },

}
