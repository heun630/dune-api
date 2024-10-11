import datetime
import pandas as pd
from heun.config import dune
from dune_client.query import QueryBase

QUERY_ID = 4105281

query = QueryBase(
    query_id=QUERY_ID
)

def fetch_dune_data(query):
    try:
        print("Fetching data from Dune API...")
        df = dune.run_query_dataframe(query=query)
        print("Data fetched successfully!")
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    df = fetch_dune_data(query)
    current_date = datetime.datetime.now().strftime('%Y%m%d')
    if df is not None:
        print(df.head())

        df.to_csv(f'data/{QUERY_ID}_{current_date}.csv', index=False)
        print("Data saved to dune_output.csv")
    else:
        print("No data fetched.")

if __name__ == "__main__":
    main()