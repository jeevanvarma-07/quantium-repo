from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Soul Foods Pink Morsel Dashboard",
        className="title"
    ),

    html.Div([

        html.Label(
            "Select Region:",
            className="label"
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"}
            ],
            value="all",
            inline=True
        )

    ], className="radio-container"),

    dcc.Graph(id="sales-chart")

])


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[
            filtered_df["region"] == selected_region
        ]

    chart_df = (
        filtered_df
        .groupby("date")["sales"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    fig = px.line(
        chart_df,
        x="date",
        y="sales",
        title=f"Sales Trend - {selected_region.title()}",
        labels={
            "date": "Date",
            "sales": "Sales"
        }
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)