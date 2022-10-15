#!/usr/bin/env python
# coding: utf-8

"""
Download parquet format data and upload it to PostgreSQL database

Usage 
python ingest_data_my.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table=yellow_taxi_data2 \
    --url=https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet

"""

import argparse
import os
from sqlalchemy import create_engine
from pyarrow.dataset import dataset
import pandas as pd

from time import time

def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table = params.table
    url = params.url

    # input_file = "yellow_tripdata_2021-01.parquet"
    # table_name = "yellow_taxi_data2"

    if not url.endswith('.parquet'):
        raise ValueError("url parameter should point to teh parquet file!")

    data_file = "ny_taxi_data.parquet"

    # Download NY Taxi data
    os.system(f"wget {url} -O {data_file}")


    # Create an engine to connect to postgresql
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    engine.connect()


    # Drop table
    query = f"""DROP TABLE IF EXISTS "{table}";"""
    engine.execute(query)

    def transform(df):
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


    # Read the file by chunks
    ds = dataset(data_file, format="parquet")

    print("Start ingesting of the data...")

    batches = ds.to_batches()

    for batch in batches:

        try:
        
            t_start = time()

            df = batch.to_pandas()
            transform(df)
            df.to_sql(name=table, con=engine, if_exists='append')
            
            t_end = time()
            print(f"Inserted {df.shape[0]} rows, took {(t_end - t_start):.2f}")
            
        except KeyboardInterrupt:
            print("Ingesting data into the postgres database was interrupted!")
            break

    print("Finished ingesting data into the postgres database")



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Download parquet format data and upload it to PostgreSQL database.')
    parser.add_argument("--user", help='user to postgresql')
    parser.add_argument("--password", help='password to postgresql')
    parser.add_argument("--host", help='host to postgresql')
    parser.add_argument("--port", help='port to postgresql')
    parser.add_argument("--db", help='db to postgresql')
    parser.add_argument("--table", help='table to postgresql')
    parser.add_argument("--url", help='input file to postgresql')

    args = parser.parse_args()

    main(args)