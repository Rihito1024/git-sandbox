# 月別売上ダッシュボード

Git 練習用のサンドボックスリポジトリです。

---

## アプリの起動

```bash
cd git-sandbox
source .venv/bin/activate
streamlit run app.py
```

---

## 依頼内容

縦積みになっているグラフが見づらいので、横並びに変更してほしい。

修正後は内容が反映されていることを確認してから、プルリクエストを作成すること。

> コードを修正したら、ブラウザ側でリロードすれば更新される。

---

## 修正ヒント

現在は「グラフ → テーブル → 棒グラフ」と縦積みになっています。  
`st.columns()` を使うと横並びにできます。

```python
col1, col2 = st.columns(2)
with col1:
    st.header("売上推移")
    st.line_chart(df)
with col2:
    st.header("データ一覧")
    st.dataframe(df)
```
