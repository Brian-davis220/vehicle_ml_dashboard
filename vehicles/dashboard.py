import plotly.express as px
import plotly.offline as opy
import plotly.graph_objects as go

import pandas as pd


def frequency_table(df):
    # Simple counts
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']

    # Convert to HTML using the correct method name: .to_html()
    table_html = manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center'
    )
    return table_html


def manufacturer_chart(df):
    # Bar chart of the same manufacturer counts
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']

    fig = px.bar(
        manufacturer_counts,
        x='Manufacturer',
        y='Count',
        title='Vehicles per Manufacturer',
        text='Count'
    )
    fig.update_traces(marker_color='#2f3136')
    fig.update_layout(template='plotly_white')
    return opy.plot(fig, auto_open=False, output_type='div')
