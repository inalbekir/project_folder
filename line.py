# /project_folder/charts/line.py
import plotly.express as px

def plot_students_per_year(df):

    summary = df.groupby('Educational Year')['StudentID'].nunique().reset_index(name='Number of Students')

    fig = px.line(summary, x='Educational Year', y='Number of Students',
                  title='Number of Students per Educational Year', markers=True)

    return fig
