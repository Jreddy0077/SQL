import streamlit as st
import pymysql

# Fetch database credentials from Streamlit secrets
db_credentials = st.secrets["connections"]["mysql"]

def fetch_data():
    try:
        conn = pymysql.connect(
            host=db_credentials["host"],
            user=db_credentials["username"],
            password=db_credentials["password"],
            database=db_credentials["database"],
            port=int(db_credentials["port"]),
            charset=db_credentials["query"]["charset"]
        )
        c = conn.cursor()
        c.execute("SELECT Color FROM phones LIMIT 1")
        result = c.fetchall()
        conn.close()
        return result
    except pymysql.MySQLError as e:
        st.error(f"Database connection failed: {e}")
        return None

# Fetch data
data = fetch_data()

# Display the result in Streamlit
if data:
    st.write("Fetched data from database:")
    st.write(data)
else:
    st.write("No data found or failed to fetch data.")
