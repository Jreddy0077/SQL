# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection('test', type='sql')

# Perform query.
df = conn.query('SELECT * from user;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Define the connection parameters for TiDB Cloud
db_user = "2yasPb2k6DKrXZH.root"
db_password ="E28f3eorNGjxx6K4"
db_host ="gateway01.ap-southeast-1.prod.aws.tidbcloud.com"
db_port = '4000'
db_name = 'test'

# Create the connection string
connection_string = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

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

