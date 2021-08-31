from sqlalchemy import create_engine

def create_table_from_df(db_uri, table_name, df):
    try:
        engine = create_engine(db_uri, echo=True)
        df.to_sql(table_name,
                  engine,
                  if_exists='replace',
                  index=True,
                  chunksize=500)
        return 'success'
    except Exception as e:
        return repr(e)

