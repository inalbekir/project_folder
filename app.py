# /project_folder/app.py
import streamlit as st
import pandas as pd
from charts import CHARTS

def main():
    st.title("Student Data Visualization")
    df = pd.read_csv('data/updated_coderminds.csv')

    with st.sidebar:
        # Sidebar for selecting charts
        selected_chart = st.selectbox("Select a chart to display", options=list(CHARTS.keys()))

        # Universal filter: Select educational years
        year_options = df['Educational Year'].unique().tolist()
        selected_years = st.multiselect("Select Educational Years", options=year_options, default=year_options)

        # Filters specific to each chart type
        selected_languages = selected_programs = selected_periods = []
        if selected_chart == 'Preferred Language':
            language_options = df['Student Preferred Language'].unique().tolist()
            selected_languages = st.multiselect('Select preferred languages', options=language_options, default=language_options)
        elif selected_chart == 'Program Types':
            program_options = df['Product Name'].unique().tolist()
            selected_programs = st.multiselect('Select programs', options=program_options, default=program_options)
        elif selected_chart == 'Students by Period':
            period_options = df['Period'].unique().tolist()
            selected_periods = st.multiselect('Select periods', options=period_options, default=period_options)

    # Filter the DataFrame for selected educational years
    df_filtered = df[df['Educational Year'].isin(selected_years)]

    # Determine which chart function to call and with which filters
    chart_function = CHARTS[selected_chart]
    if selected_chart == 'Preferred Language':
        fig = chart_function(df_filtered, selected_languages)
    elif selected_chart == 'Program Types':
        fig = chart_function(df_filtered, selected_programs)
    elif selected_chart == 'Students by Period':
        fig = chart_function(df_filtered, selected_periods)
    else:
        fig = chart_function(df_filtered)  # For charts that don't need additional filters

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    st.set_page_config(page_title="Student Data Visualization", layout='wide')
    main()
