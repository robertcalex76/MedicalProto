import pandas as pd
import requests
from sqlalchemy import create_engine

def download_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content

def clean_data(data):
    df = pd.read_csv(pd.compat.StringIO(data.decode('utf-8')))
    # Perform any necessary cleaning steps here
    return df

def load_data_to_db(df, db_url):
    engine = create_engine(db_url)
    df.to_sql('nursing_homes', con=engine, if_exists='replace', index=False)

def ingest_cms_data(url, db_url):
    raw_data = download_data(url)
    cleaned_data = clean_data(raw_data)
    load_data_to_db(cleaned_data, db_url)