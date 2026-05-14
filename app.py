import streamlit as st
import pandas as pd

st.title("月別売上ダッシュボード")

df = pd.read_csv("data/sales.csv", index_col="月")

st.header("売上推移グラフ")
st.line_chart(df)

st.header("売上データ一覧")
st.dataframe(df, use_container_width=True)

st.header("月別合計")
st.bar_chart(df.sum(axis=1))
