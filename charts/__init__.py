from .line import plot_students_per_year
from .language import plot_language_preference_bar_chart
from .product import plot_program_types
from .courses import plot_students_by_period_and_program
from .age import plot_students_by_program_and_age
from .income import plot_income_by_program_and_year
from .pie import plot_how_students_found_us
from .donut import plot_parent_occupation
from .heatmap import plot_student_heatmap

CHARTS = {
    'Student Enrollment': plot_students_per_year,
    'Preferred Language': plot_language_preference_bar_chart,
    'Program Types': plot_program_types,
    'Students by Program and Period': plot_students_by_period_and_program,
    'Students by Program and Age': plot_students_by_program_and_age,
    'Income by Program and Year': plot_income_by_program_and_year,
    'How Did You Find Us': plot_how_students_found_us,
    'Parent Occupation': plot_parent_occupation,
    'Student Heatmap': plot_student_heatmap
}
