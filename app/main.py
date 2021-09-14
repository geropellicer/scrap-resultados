import pandas as pd
from pandas.core.frame import DataFrame
import requests
import logging
from .utils import find_in_array, get_codigo_mesa, get_url_final
from .settings import (
    codigos_fitu_partido,
    codigos_lista_mst,
    codigos_lista_pts,
    RESULTS_COLUMNS,
    ERRORES_SEGUIDOS_PERMITIDOS,
)
from pprint import pprint

logging.basicConfig()
logging.root.setLevel(logging.INFO)
logger = logging.getLogger("app")


def scrap_provincia(prov_id: int, mun_inicial:int= None, mesa_inicial:int = None):
    errores_seguidos = 0

    mun_id = mun_inicial or 1
    mesa_inicial = mesa_inicial or 1
    prov_results = DataFrame(columns=RESULTS_COLUMNS)
    
    while errores_seguidos < ERRORES_SEGUIDOS_PERMITIDOS:
        mun_results, ultima_mesa_anterior = scrap_municipio(prov_id, mun_id, mesa_inicial=mesa_inicial)
        num_rows = mun_results.shape[0]
        errores_seguidos = 0

        if num_rows < 5: 
            errores_seguidos += 1
        else:
            prov_results = prov_results.append(mun_results)

        if prov_id != 2:
            mesa_inicial = ultima_mesa_anterior + 1
        else:
            mesa_inicial = 0
        mun_id += 1

    prov_results.to_csv("./resultados/resultados_{}.csv".format(prov_id), index=False)

        


def scrap_municipio(
    prov_id: int, mun_id: int, mesa_inicial: int = 1, mesa_final: int = None
):

    mesa_actual = mesa_inicial
    results = pd.DataFrame(columns=RESULTS_COLUMNS)
    errores_seguidos = 0

    while errores_seguidos < ERRORES_SEGUIDOS_PERMITIDOS and (
        mesa_actual <= mesa_final if mesa_final else True
    ):
        try:
            codigo_mesa_actual = get_codigo_mesa(mesa_actual, prov_id, mun_id)
            url_final = get_url_final(codigo_mesa_actual)
            response = requests.get(url_final).json()

            dict_fitu = find_in_array(
                response["partidos"], "code", codigos_fitu_partido[prov_id]
            )
            votos_fitu = dict_fitu["votos"]
            votos_pts = find_in_array(
                dict_fitu["listas"], "code", codigos_lista_pts[prov_id]
            )["votos"]
            votos_mst = find_in_array(
                dict_fitu["listas"], "code", codigos_lista_mst[prov_id]
            )["votos"]
            total_votos = response["totalVotos"]
            total_votos_afirmativos = response["afirmativos"]
            total_votos_validos = response["valid"]

            row = pd.DataFrame(
                [
                    [
                        codigo_mesa_actual,
                        votos_fitu,
                        votos_pts,
                        votos_mst,
                        total_votos,
                        total_votos_afirmativos,
                        total_votos_validos,
                    ]
                ],
                columns=RESULTS_COLUMNS,
            )
            results = results.append(row)

            logger.info(
                [
                    codigo_mesa_actual,
                    votos_fitu,
                    votos_pts,
                    votos_mst,
                    total_votos,
                    total_votos_afirmativos,
                    total_votos_validos,
                ]
            )
            errores_seguidos = 0

        except Exception as e:
            logger.error(
                "Error en mesa {} de {} de {}".format(mesa_actual, mun_id, prov_id)
            )
            logger.error(e)
            errores_seguidos += 1

        mesa_actual += 1
    
    results.to_csv("./resultados/resultados_{}_{}.csv".format(mun_id, prov_id), index=False)
    return results, mesa_actual
