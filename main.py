from pro import load_and_clean_data
from vis import (
    plot_histogram,
    plot_histogram_by_gender,
    plot_average_speed_distribution,
    plot_violin,
    plot_linear_regression,
    plot_average_speed_by_season,
    plot_runners_count_by_age_group,
    plot_nationality_distribution,
)
import pandas as pd

# Load and process data
file_path = "TWO_CENTURIES_OF_UM_RACES.csv"
fltrdf2 = load_and_clean_data(file_path)

# Visualizations
plot_histogram(
    fltrdf2,
    "race_length",
    "Histogram of Race Length",
    "Race Length",
    "Number of Athletes",
)
plot_histogram_by_gender(
    fltrdf2,
    "race_length",
    "Histogram of Race Length by Gender",
    "Race Length",
    "Number of Athletes",
)
plot_average_speed_distribution(fltrdf2, ["50km", "50mi", "100km", "100mi"])
plot_violin(fltrdf2)
plot_linear_regression(fltrdf2)

# Add race month and season
fltrdf2["race_month"] = fltrdf2["race_day"].str.split(".").str.get(1).astype(int)
fltrdf2["race_season"] = fltrdf2["race_month"].apply(
    lambda x: (
        "winter"
        if x == 12 or x <= 2
        else (
            "spring"
            if 3 <= x <= 5
            else "summer" if 6 <= x <= 8 else "fall" if 9 <= x <= 11 else "unknown"
        )
    )
)

# Visualize average speed by season
plot_average_speed_by_season(fltrdf2)

# Categorize runners by age groups
age_counts = fltrdf2.copy()
age_counts["Age Group"] = age_counts["athlete_age"].apply(
    lambda x: "Below 50" if x < 50 else "50 and Above"
)
age_counts = (
    age_counts.groupby("Age Group").size().reset_index(name="Number of Runners")
)
plot_runners_count_by_age_group(age_counts)
plot_nationality_distribution(fltrdf2)
