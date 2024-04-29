# /project_folder/app.py
import streamlit as st
import pandas as pd
from charts import CHARTS



def main():
    st.title("Student Data Visualization")

    # Define the path to your CSV file once, at the beginning
    csv_file = 'data/updated_coderminds.csv'  # Adjust the path as necessary

    # Load the dataframe outside of the conditional logic so it's always available
    df = pd.read_csv(csv_file)

    # Initialize an empty list for selected_languages and selected_programs
    selected_languages = []
    selected_programs = []

    with st.sidebar:
        selected_chart = st.selectbox("Select a chart to display", options=list(CHARTS.keys()))

        # Sidebar configuration for language preferences
        if selected_chart == 'Preferred Language':
            language_options = df['Student Preferred Language'].unique().tolist()
            selected_languages = st.multiselect('Select preferred languages', language_options,
                                                default=language_options)

        # Sidebar configuration for program types
        elif selected_chart == 'Program Types':
            program_options = df['Product Name'].unique().tolist()
            selected_programs = st.multiselect('Select programs', program_options, default=program_options)

    # Call the appropriate chart function with necessary parameters
    chart_function = CHARTS[selected_chart]

    # Check which chart is being requested and display accordingly
    fig = None
    if selected_chart == 'Preferred Language':
        fig = chart_function(df, selected_languages)
    elif selected_chart == 'Program Types':
        fig = chart_function(df, selected_programs)
    elif selected_chart == 'Student Enrollment':
        fig = chart_function(df)

    if fig:
        st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    st.set_page_config(page_title="Student Data Visualization", layout='wide')
    main()
