import os
import snowflake.connector

snowflake.connector.paramstyle='qmark'

with snowflake.connector.connect(
        user=os.environ['SNOWFLAKE_USER'],
        password=os.environ['SNOWFLAKE_PASSWORD'],
        account=os.environ['SNOWFLAKE_ACCOUNT'],
        database='SNOWFLAKE_SAMPLE_DATA',
        schema='TPCH_SF1'
    ) as con:

    with con.cursor(snowflake.connector.DictCursor) as cur: # (1)
        cur.execute("SELECT C_NAME, C_NATIONKEY, C_ACCTBAL FROM CUSTOMER WHERE C_MKTSEGMENT = ? LIMIT 3", ['BUILDING'])
        rows = cur.fetchall() # (2)
        print(type(rows))
        print(len(rows))
        for row in rows:
            print(type(row))
            print(row)
            print(f'{row["C_NAME"]=}, {row["C_NATIONKEY"]=}, {row["C_ACCTBAL"]=}') # (3)
