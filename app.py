# /project_folder/app.py
import streamlit as st
import pandas as pd
from charts import CHARTS

def main():
    st.title("Student Data Visualization")
    df = pd.read_csv('data/updated_coderminds.csv')

    with st.sidebar:
        selected_chart = st.selectbox("Select a chart to display", options=list(CHARTS.keys()))

        # Universal filter: Educational Years
        year_options = df['Educational Year'].unique().tolist()
        selected_years = st.multiselect("Select Educational Years", options=year_options, default=year_options)

        # Initialize variables to store selected items
        selected_languages = []
        selected_programs = []
        selected_periods = []

        if selected_chart == 'Preferred Language':
            language_options = df['Student Preferred Language'].unique().tolist()
            selected_languages = st.multiselect('Select preferred languages', language_options, default=language_options)
        elif selected_chart == 'Program Types' or selected_chart == 'Students by Program and Period':
            program_options = df['Product Name'].unique().tolist()
            selected_programs = st.multiselect('Select programs', program_options, default=program_options)
        if selected_chart == 'Students by Program and Period':
            period_options = df['Period'].unique().tolist()
            selected_periods = st.multiselect('Select periods', period_options, default=period_options)

    df_filtered = df[df['Educational Year'].isin(selected_years)]

    chart_function = CHARTS[selected_chart]
    if selected_chart == 'Preferred Language':
        fig = chart_function(df_filtered, selected_languages)
    elif selected_chart == 'Program Types':
        fig = chart_function(df_filtered, selected_programs)
    elif selected_chart == 'Students by Program and Period':
        fig = chart_function(df_filtered, selected_periods, selected_programs)
    else:
        fig = chart_function(df_filtered)

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    st.set_page_config(page_title="Student Data Visualization", layout='wide')
    main()