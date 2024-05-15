# /project_folder/charts/__init__.py
from .line import plot_students_per_year
from .language import plot_language_preference_bar_chart
from .product import plot_program_types
from .courses import plot_students_by_period_and_program
from .age import plot_students_by_program_and_age  # New function

CHARTS = {
    'Student Enrollment': plot_students_per_year,
    'Preferred Language': plot_language_preference_bar_chart,
    'Program Types': plot_program_types,
    'Students by Program and Period': plot_students_by_period_and_program,
    'Students by Program and Age': plot_students_by_program_and_age  # Add the new chart
}
