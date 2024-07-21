import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from sqlalchemy.exc import SQLAlchemyError

# Define the connection parameters for TiDB Cloud
db_user = '2yasPb2k6DKrXZH.root'
db_password = 'E28f3eorNGjxx6K4'
db_host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com'
db_port = '4000'
db_name = 'test'
ca_path = '<CA_PATH>'  # Replace <CA_PATH> with the actual path to your CA certificate

# Create the connection string with SSL parameters
connection_string = (
    f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?'
    f'ssl_ca={ca_path}&ssl_verify_cert=true'
)

try:
    # Initialize connection
    engine = create_engine(connection_string)
    conn = engine.connect()

    # Perform query
    df = pd.read_sql('SELECT * FROM user', conn)

    # Close connection
    conn.close()

    # Print results
    for row in df.itertuples():
        st.write(f"{row.name} has a :{row.pet}:")

    # Close the engine
    engine.dispose()

except SQLAlchemyError as e:
    st.error(f"An error occurred: {str(e)}")
