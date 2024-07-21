# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection('test', type='sql')

# Perform query.
df = conn.query('SELECT * from user;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
