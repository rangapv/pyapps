# import module
import pandas as pd
import streamlit as st
# Title
st.title("This is Title line")
# Header
st.header("This is a header")
# Subheader
st.subheader("This line belongs to a subheader")
# Text
st.text("This line belongs to a text")
# Markdowns
st.markdown("### This is a markdown")
st.markdown("## This is a markdown")
st.markdown("# This is a markdown")


# Reading the CSV file
df = pd.read_csv("./patients_test.txt")
# Putting title
st.title("View of the Data shown below:")
# To visualize the data
st.write(df)
