from google.oauth2 import service_account


def merge_chave_menor(df_mais_granular, df_menos_granular, chaves_comuns):
    df_mais_granular['rank'] = df_mais_granular.groupby(chaves_comuns).cumcount()
    df_menos_granular['rank'] = 0
    chaves_com_rank = chaves_comuns.append('rank')
    dfr = df_mais_granular.merge(df_menos_granular, on=chaves_com_rank, how='left')
    del dfr['rank']
    return dfr


def save_to_bigquery(df, project_id, dataset, table, service_account_path, if_exists='replace', chunksize=4000):
    credentials = service_account.Credentials.from_service_account_file(service_account_path)
    df.to_gbq(f"{dataset}.{table}",
              project_id,
              chunksize=chunksize,
              if_exists=if_exists,
              credentials=credentials
              )
