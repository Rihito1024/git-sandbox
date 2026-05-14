import streamlit as st
import pandas as pd

st.title("月別売上ダッシュボード")

df = pd.read_csv("data/sales.csv", index_col="月")

col1, col2 = st.columns(2)
with col1:
    st.header("売上推移")
    st.line_chart(df)
with col2:
    st.header("データ一覧")
    st.dataframe(df)

st.header("月別合計")
st.bar_chart(df.sum(axis=1))
