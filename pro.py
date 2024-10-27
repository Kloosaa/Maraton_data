import pandas as pd


def load_and_clean_data(file_path):
    """
    Load and clean race data from a CSV file.

    Parameters:
    ----------
    file_path : str
        The path to the CSV file.

    Returns:
    -------
    pd.DataFrame
        Cleaned DataFrame with relevant race data.
    """
    # Load data from CSV file
    df = pd.read_csv(file_path)
    print(df.head(10))

    # Filter for specific event distances and year (remove USA restriction)
    fltrdf = df[
        (df["Event distance/length"].isin(["50km", "50mi", "100km", "100mi"]))
        & (df["Year of event"] == 2010)
    ]

    print(fltrdf.head(10))

    # Clean event names by removing the part in parentheses
    fltrdf["Event name"] = fltrdf["Event name"].str.split("(").str.get(0).str.strip()

    # Calculate athlete age based on birth year
    if "Athlete year of birth" in df.columns:
        fltrdf["athlete_age"] = 2010 - fltrdf["Athlete year of birth"]

    # Drop irrelevant columns except nationality
    fltrdf = fltrdf.drop(
        [
            "Athlete club",
            "Athlete year of birth",
            "Athlete age category",
        ],
        axis=1,
    )

    # Remove rows with missing values
    fltrdf = fltrdf.dropna()
    fltrdf = fltrdf.reset_index(drop=True)

    # Convert data types for age and average speed
    fltrdf["athlete_age"] = fltrdf["athlete_age"].astype(int)
    fltrdf["Athlete average speed"] = fltrdf["Athlete average speed"].astype(float)

    # Rename columns for clarity
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
            "Athlete country": "athlete_country",  # Keep nationality
        }
    )

    # Select relevant columns for the final DataFrame
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
            "athlete_country",  # Include nationality
        ]
    ]

    return fltrdf2
