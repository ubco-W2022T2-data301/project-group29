from .. import project_functions # This is called a relative import
from analysis.code.project_functions import load_and_process

df = project_functions.load_and_process("../data/raw/mxmh_survey_results.csv")
df