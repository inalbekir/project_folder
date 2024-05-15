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

        # Filters specific to each chart type
        selected_languages = selected_programs = selected_periods = []
        age_range = [df['Student Age'].min(), df['Student Age'].max()]

        if selected_chart == 'Preferred Language':
            language_options = df['Student Preferred Language'].unique().tolist()
            selected_languages = st.multiselect('Select preferred languages', options=language_options, default=language_options)
        elif selected_chart in ['Program Types', 'Students by Program and Period', 'Students by Program and Age', 'Income by Program and Year']:
            program_options = df['Product Name'].unique().tolist()
            selected_programs = st.multiselect('Select programs', options=program_options, default=program_options)
        if selected_chart == 'Students by Program and Period':
            period_options = df['Period'].unique().tolist()
            selected_periods = st.multiselect('Select periods', options=period_options, default=period_options)
        if selected_chart == 'Students by Program and Age':
            age_range = st.slider('Select age range', min_value=int(df['Student Age'].min()), max_value=int(df['Student Age'].max()), value=(int(df['Student Age'].min()), int(df['Student Age'].max())))

    df_filtered = df[df['Educational Year'].isin(selected_years)]

    chart_function = CHARTS[selected_chart]
    if selected_chart == 'Preferred Language':
        fig = chart_function(df_filtered, selected_languages)
    elif selected_chart == 'Program Types':
        fig = chart_function(df_filtered, selected_programs)
    elif selected_chart == 'Students by Program and Period':
        fig = chart_function(df_filtered, selected_periods, selected_programs)
    elif selected_chart == 'Students by Program and Age':
        fig = chart_function(df_filtered, selected_years, selected_programs, age_range)
    elif selected_chart == 'Income by Program and Year':
        fig = chart_function(df_filtered, selected_years, selected_programs)
    elif selected_chart == 'How Did You Find Us':
        fig = chart_function(df_filtered)
    else:
        fig = chart_function(df_filtered)

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    st.set_page_config(page_title="Student Data Visualization", layout='wide')
    main()
