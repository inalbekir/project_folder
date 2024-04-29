import plotly.express as px

def plot_program_types(df, selected_programs):
    # No need to read the CSV here, as 'df' is the dataframe passed directly to the function

    # Filter the dataframe based on the selected programs
    if selected_programs:
        df = df[df['Product Name'].isin(selected_programs)]

    summary = df.groupby(['Educational Year', 'Product Name'])['StudentID'].nunique().reset_index(name='Number of Students')

    fig = px.bar(summary, x='Educational Year', y='Number of Students', color='Product Name',
                 title='Numbers of Students in Different Program Types')
    return fig
