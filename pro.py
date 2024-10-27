import pandas as pd


# Function to load and clean data
def load_and_clean_data(file_path):
    # Load data from CSV file
    df = pd.read_csv(file_path)
    print(df.head(10))

    # Data processing and cleaning
    fltrdf = df[
        (df["Event distance/length"].isin(["50km", "50mi", "100km", "100mi"]))
        & (df["Year of event"] == 2018)
    ]

    print(fltrdf.head(10))

    # Extract race name and clean up
    fltrdf["Event name"] = fltrdf["Event name"].str.split("(").str.get(0).str.strip()

    # Calculate athlete age
    if "Athlete year of birth" in df.columns:
        fltrdf["athlete_age"] = 2018 - fltrdf["Athlete year of birth"]

    # Drop unnecessary columns
    fltrdf = fltrdf.drop(
        [
            "Athlete club",
            "Athlete country",
            "Athlete year of birth",
            "Athlete age category",
        ],
        axis=1,
    )

    fltrdf = fltrdf.dropna()
    fltrdf = fltrdf.reset_index(drop=True)

    # Ensure correct data types
    fltrdf["athlete_age"] = fltrdf["athlete_age"].astype(int)
    fltrdf["Athlete average speed"] = fltrdf["Athlete average speed"].astype(float)

    # Rename columns for consistency
    fltrdf = fltrdf.rename(
        columns={
            "Year of event": "year",
            "Event dates": "race_day",
            "Event name": "race_name",
            "Event distance/length": "race_length",
            "Event number of finishers": "race_number_of_finishers",
            "Athlete performance": "athlete_performance",
            "Athlete gender": "athlete_gender",
            "Athlete average speed": "athlete_average_speed",
            "Athlete ID": "athlete_id",
        }
    )

    # Select relevant columns
    fltrdf2 = fltrdf[
        [
            "race_day",
            "race_name",
            "race_length",
            "race_number_of_finishers",
            "athlete_id",
            "athlete_gender",
            "athlete_age",
            "athlete_performance",
            "athlete_average_speed",
        ]
    ]
    fltrdf2 = fltrdf2[fltrdf2["athlete_gender"] != "X"]
    return fltrdf2
