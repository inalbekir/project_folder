# /project_folder/charts/donut.py
import pandas as pd
import plotly.express as px

def plot_parent_occupation(df):
    # Group by the column indicating parent occupation and count the occurrences
    summary = df['Parent Occupation'].value_counts().reset_index()
    summary.columns = ['Parent Occupation', 'Count']

    # Aggregate smaller categories into 'Other'
    threshold = 2  # Define a threshold for aggregation
    small_categories = summary[summary['Count'] < threshold]
    summary = summary[summary['Count'] >= threshold]
    if not small_categories.empty:
        other_sum = small_categories['Count'].sum()
        other_row = pd.DataFrame({'Parent Occupation': ['Other'], 'Count': [other_sum]})
        summary = pd.concat([summary, other_row], ignore_index=True)

    # Create a donut chart
    fig = px.pie(summary, values='Count', names='Parent Occupation', hole=0.4, title='Parent Occupation')

    # Customize layout to improve readability
    fig.update_layout(
        margin=dict(t=50, b=50, l=50, r=50),
        legend_title_text='Occupation'
    )

    return fig
