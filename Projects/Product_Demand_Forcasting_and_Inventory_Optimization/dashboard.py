from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Load data
historical_data = pd.read_csv('historical_demand_trends.csv')
forecasted_data = pd.read_csv('forecasted_demand.csv')
safety_stock_data = pd.read_csv('safety_stock_levels.csv')

# Create figures
fig1 = px.line(historical_data, x='Sales_Date', y='Quantity_Sold', color='Region',
               title='Historical Demand Trends')

fig2 = px.line(forecasted_data, x='ds', y='yhat', color='Category', facet_col='Region',
               title='Forecasted Demand by Region and Product Category')

fig3 = px.bar(safety_stock_data, x='Product_ID', y='safety_stock',
              title='Safety Stock Levels for Top 10 Products',
              labels={'product_id': 'Product ID', 'safety_stock': 'Safety Stock Level'})

# Create the Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Inventory Optimization Dashboard"),

    # Historical demand trends
    html.Div([
        html.H2("Historical Demand Trends"),
        dcc.Graph(figure=fig1),
    ]),

    # Forecasted demand
    html.Div([
        html.H2("Forecasted Demand by Region and Product Category"),
        dcc.Graph(figure=fig2),
    ]),

    # Safety stock levels
    html.Div([
        html.H2("Safety Stock Levels"),
        dcc.Graph(figure=fig3),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)

