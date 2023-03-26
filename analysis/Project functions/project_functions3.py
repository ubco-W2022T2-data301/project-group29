import pandas as pd

df = pd.read_csv(r"C:\Users\Burkely Theriault\DATA301\project-group29\data\raw\mxmh_survey_results.csv")

processed_df = (
    df
    .loc[lambda x: x['Fav genre'].str.lower() == 'pop']
    .replace({"Yes": 1, "No": 2})
    .assign(Primary_streaming_service=lambda x: x['Primary streaming service'].replace({'YouTube Music': 1, 'Apple Music': 2, 'I do not use a streaming service.': 4, 'Spotify': 3}))
    .dropna(subset=['Primary_streaming_service'])
    [['Age', 'Hours per day', 'While working', 'Instrumentalist', 'Composer', 'Exploratory', 'Foreign languages', 'BPM', 'Anxiety', 'Depression', 'Insomnia', 'OCD', 'Fav genre', 'Primary_streaming_service']]
    .dropna()
)

print(processed_df)

