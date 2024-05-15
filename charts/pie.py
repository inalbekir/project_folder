# /project_folder/charts/pie.py
import pandas as pd
import plotly.express as px

def plot_how_students_found_us(df):
    # Group by the column indicating how students found the program and count the occurrences
    summary = df['How did you find us?'].value_counts().reset_index()
    summary.columns = ['How did you find us?', 'Count']

    # Create a pie chart
    fig = px.pie(summary, values='Count', names='How did you find us?', title='How Did You Find Us')

    # Customize layout to improve readability
    fig.update_layout(
        margin=dict(t=50, b=50, l=50, r=50),
        legend_title_text='Source'
    )

    return fig
