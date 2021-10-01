#To dispaly the excel sheet in a webpage
import streamlit as st
import pandas as pd
from gsheetsdb import connect

st.write("My First Streamlit Web App")

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)

#connect to the excel file
st.title("Connect to Google Sheets")
#gsheet_url = "https://docs.google.com/spreadsheets/d/1ixMrhGV1TPn14_oTyEIFjszuwuwO9xkbsc1WEBJH3N0/edit?usp=sharing"
gsheet_url = "https://docs.google.com/spreadsheets/d/1W_DmVE5JhacJ7xwpGtp69_XHN9_3agckDffoiR5EoZU/edit#gid=0"
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)

