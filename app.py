# /project_folder/app.py
import streamlit as st
import pandas as pd
from charts import CHARTS


def main():
    st.title("Student Data Visualization")
    df = pd.read_csv('data/updated_coderminds.csv')

    with st.sidebar:
        selected_chart = st.selectbox("Select a chart to display", options=list(CHARTS.keys()))

        # Initialize variables to store selected items
        selected_languages = []
        selected_programs = []
        selected_periods = []

        if selected_chart == 'Preferred Language':
            language_options = df['Student Preferred Language'].unique().tolist()
            selected_languages = st.multiselect('Select preferred languages', language_options,
                                                default=language_options)
        elif selected_chart == 'Program Types':
            program_options = df['Product Name'].unique().tolist()
            selected_programs = st.multiselect('Select programs', program_options, default=program_options)
        elif selected_chart == 'Students by Period':
            period_options = df['Period'].unique().tolist()
            selected_periods = st.multiselect('Select periods', period_options, default=period_options)

    chart_function = CHARTS[selected_chart]

    # Apply conditional arguments based on the selected chart
    if selected_chart == 'Preferred Language':
        fig = chart_function(df, selected_languages)
    elif selected_chart == 'Program Types':
        fig = chart_function(df, selected_programs)
    elif selected_chart == 'Students by Period':
        fig = chart_function(df, selected_periods)
    else:
        fig = chart_function(df)  # Only pass df for charts that don't need additional args

    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    st.set_page_config(page_title="Student Data Visualization", layout='wide')
    main()
