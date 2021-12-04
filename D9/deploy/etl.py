# -*- coding: utf-8 -*-
import pandas as pd
from D9.deploy.defs import PROJECT_ID, BIGQUERY_DATASET, BIGQUERY_TABLE, CENTROID_URL, BANDEIRAS_URL, SERVICE_ACCOUNT_FILE_PATH
from D9.deploy.queries import query_pibpercapita, query_consumo_energia
from D9.deploy.deploy_util import merge_chave_menor, save_to_bigquery


def load_centroid():
    df_xlsx = pd.read_excel(CENTROID_URL, dtype={"CD_GEOCODM,C,20": str})
    dfxlsx_geo = df_xlsx[['CD_GEOCODM,C,20', 'NM_CATEGOR,C,50', 'LONG,N,24,6', 'LAT,N,24,6']].rename(
        columns={'CD_GEOCODM,C,20': "cod_ibge", 'NM_CATEGOR,C,50': "categoria", 'LONG,N,24,6': "long", 'LAT,N,24,6': "lat"})
    dfxlsx_geo['categoria'] = dfxlsx_geo['categoria'].str.strip()
    dfxlsx_geo = dfxlsx_geo[dfxlsx_geo['categoria'] == 'CIDADE']
    dfxlsx_geo['lat_long'] = dfxlsx_geo[['lat', 'long']].apply(lambda x: f"{str(x['lat']).replace(',', '.')},{str(x['long']).replace(',', '.')}", axis=1)
    return dfxlsx_geo


def load_pibpercapita():
    df_pibpercapita = pd.io.gbq.read_gbq(query_pibpercapita, project_id=PROJECT_ID)
    return df_pibpercapita


def load_bandeiras():
    dfb = pd.read_excel(BANDEIRAS_URL, usecols=['ufNome', 'uf', 'Bandeira'])
    return dfb


def load_consumo_energia():
    df_energia = pd.io.gbq.read_gbq(query_consumo_energia, project_id=PROJECT_ID)
    return df_energia


def merge_datasets():
    df_geo = load_centroid()
    df_pibpercapita = load_pibpercapita()
    df_merge = df_pibpercapita.merge(df_geo[['cod_ibge', 'lat_long']], how='left', left_on='id_municipio', right_on='cod_ibge')
    del df_geo
    del df_pibpercapita
    del df_merge['cod_ibge']
    dfb = load_bandeiras()
    df_merge = df_merge.merge(dfb, left_on='sigla_uf', right_on='uf')
    df_energia = load_consumo_energia()
    dfm = merge_chave_menor(df_merge, df_energia, ['ano', 'sigla_uf'])
    return dfm


if __name__ == "__main__":
    dfm = merge_datasets()
    save_to_bigquery(dfm, PROJECT_ID, BIGQUERY_DATASET, BIGQUERY_TABLE, SERVICE_ACCOUNT_FILE_PATH)


