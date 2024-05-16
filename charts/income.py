# /project_folder/charts/income.py
import pandas as pd
import plotly.express as px

def plot_income_by_program_and_year(df, selected_years, selected_programs):
    # Filter by educational year
    df = df[df['Educational Year'].isin(selected_years)]

    # Further filter by selected programs if provided
    if selected_programs:
        df = df[df['Product Name'].isin(selected_programs)]

    # Ensure the 'Order Subtotal Amount' column is numeric
    df['Order Subtotal Amount'] = pd.to_numeric(df['Order Subtotal Amount'], errors='coerce')

    # Group by 'Educational Year' and 'Product Name' and sum the income
    summary = df.groupby(['Educational Year', 'Product Name'])['Order Subtotal Amount'].sum().reset_index(
        name='Total Income')

    # Create a bar chart
    fig = px.bar(summary, x='Total Income', y='Educational Year', color='Product Name', orientation='h',
                 title='Income per Year Depending on the Program Type')

    # Customize layout to improve readability
    fig.update_layout(
        xaxis_title='Total Income',
        yaxis_title='Educational Year',
        margin=dict(t=50, b=50, l=50, r=50),
        legend_title_text='Program Type'
    )

    return fig