# /project_folder/charts/__init__.py
from .line import plot_students_per_year
from .language import plot_language_preference_bar_chart
from .product import plot_program_types
from .courses import plot_students_by_period  # Make sure this is added correctly

CHARTS = {
    'Students by Period': plot_students_by_period  # Add this line for the new chart
}
