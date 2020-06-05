import os
import snowflake.connector

snowflake.connector.paramstyle='qmark' # (4)

with snowflake.connector.connect( # (1)
        user=os.environ['SNOWFLAKE_USER'], # (2)
        password=os.environ['SNOWFLAKE_PASSWORD'],
        account=os.environ['SNOWFLAKE_ACCOUNT'],
        database='SNOWFLAKE_SAMPLE_DATA',
        schema='TPCH_SF1'
    ) as con:

    with con.cursor() as cur: # (3)
        cur.execute("SELECT C_NAME, C_NATIONKEY, C_ACCTBAL FROM CUSTOMER WHERE C_MKTSEGMENT = ? LIMIT 3", ['BUILDING']) # (4)
        for row in cur:
            print(type(row))
            name, nationkey, acctbal = row
            print(f'{name=}, {nationkey=}, {acctbal=}')
