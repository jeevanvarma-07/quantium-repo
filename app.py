from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px


df = pd.read_csv("formatted_sales_data.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.groupby("date")["sales"].sum().reset_index()
df = df.sort_values("date")

fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Sales"
    }
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Soul Foods Pink Morsel Sales Visualiser",
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)