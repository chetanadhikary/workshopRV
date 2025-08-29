import streamlit as st
import pandas as pd

df = pd.read_csv(
    "datasets/chipotle.tsv",
    sep="\t"
)

col_selected = st.selectbox(
    "Select a column to get value counts",
    df.columns
)

st.write(df[col_selected].value_counts())


quantity_val = st.select_slider(
    "Please select a quantity",
    options = range(1,10)
)

item_name = st.text_input(
    "Select a item name",
    "Canned Soft Drink")

ser_selected = df.loc[
    (
        df["quantity"]>quantity_val)
       & (df["item_name"]== item_name
          )
]

st.write(ser_selected)


