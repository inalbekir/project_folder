import plotly.express as px

def plot_language_preference_bar_chart(df, selected_languages):
    # No need to read the CSV here since we are passing the dataframe directly

    # Filter the dataframe based on selected languages
    if selected_languages:
        df = df[df['Student Preferred Language'].isin(selected_languages)]

    summary = df.groupby(['Educational Year', 'Student Preferred Language']).size().reset_index(
        name='Number of Students')

    fig = px.bar(summary, x='Educational Year', y='Number of Students', color='Student Preferred Language',
                 title='Number of Students Depending on the Preferred Language')
    return fig
