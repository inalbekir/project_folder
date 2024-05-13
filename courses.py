# /project_folder/charts/period.py
import pandas as pd
import plotly.express as px


def plot_students_by_period(df, selected_periods):
    if selected_periods:
        df = df[df['Period'].isin(selected_periods)]

    summary = df.groupby(['Educational Year', 'Period'])['StudentID'].nunique().reset_index(name='Number of Students')
    fig = px.bar(summary, x='Educational Year', y='Number of Students', color='Period',
                 title='Numbers of Students in Regular Courses Depending on Periods')
    return fig
