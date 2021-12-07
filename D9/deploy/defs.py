import os

PROJECT_ID = os.environ.get('PROJECT_ID') or 'enap-331414'
BIGQUERY_DATASET = os.environ.get('BIGQUERY_DATASET') or 'enapdatasets'
BIGQUERY_TABLE = os.environ.get('BIGQUERY_TABLE') or 'municipios'
SERVICE_ACCOUNT_FILE_PATH = os.environ.get('SERVICE_ACCOUNT_FILE_PATH') or '../key/enap-331414_editor.json'
CENTROID_URL = os.environ.get('CENTROID_URL') or 'https://github.com/alexlopespereira/enapespcd2021/raw/main/data/originais/centroide_municipios/BR_Localidades_2010_v1.xlsx'
BANDEIRAS_URL = os.environ.get('BANDEIRAS_URL') or "https://github.com/alexlopespereira/enapespcd2021/raw/main/data/originais/bandeiras/bandeiras.xlsx"







