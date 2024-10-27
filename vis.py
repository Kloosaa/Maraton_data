import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Function to plot histogram
def plot_histogram(data, column, title, xlabel, ylabel, bins=20):
    plt.figure(figsize=(10, 5))
    sns.histplot(data[column], bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


# Function to plot histogram by gender
def plot_histogram_by_gender(data, column, title, xlabel, ylabel, bins=20):
    plt.figure(figsize=(10, 5))
    sns.histplot(data, x=column, hue="athlete_gender", bins=bins, multiple="stack")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


# Function to plot average speed distribution
def plot_average_speed_distribution(data, distances):
    plt.figure(figsize=(14, 10))
    for i, distance in enumerate(distances, start=1):
        plt.subplot(2, 2, i)
        sns.histplot(
            data[data["race_length"] == distance]["athlete_average_speed"],
            bins=20,
            kde=True,
        )
        plt.title(f"Average Speed Distribution for {distance}")
        plt.xlabel("Average Speed (km/h)")
        plt.ylabel("Number of Athletes")
        plt.grid(True)
    plt.tight_layout()
    plt.show()


# Function to plot violin plot
def plot_violin(data):
    plt.figure(figsize=(10, 5))
    sns.violinplot(
        data=data,
        x="race_length",
        y="athlete_average_speed",
        hue="athlete_gender",
        split=True,
        inner="quart",
        linewidth=1,
    )
    plt.title("Average Speed by Race Length and Gender")
    plt.xlabel("Race Length")
    plt.ylabel("Average Speed (km/h)")
    plt.grid(True)
    plt.show()


# Function to plot linear regression
def plot_linear_regression(data):
    sns.lmplot(
        data=data,
        x="athlete_age",
        y="athlete_average_speed",
        hue="athlete_gender",
        height=5,
        aspect=2,
    )
    plt.title("Average Speed vs. Athlete Age by Gender")
    plt.xlabel("Athlete Age")
    plt.ylabel("Average Speed (km/h)")
    plt.grid(True)
    plt.show()


# Function to plot average speed by season
def plot_average_speed_by_season(data):
    plt.figure(figsize=(12, 6))
    mean_speeds = (
        data.query('race_length == "50mi"')
        .groupby("race_season")["athlete_average_speed"]
        .mean()
        .reset_index()
    )
    sns.barplot(data=mean_speeds, x="race_season", y="athlete_average_speed")
    plt.title("Average Speed in Season for 50mi Races")
    plt.xlabel("Season")
    plt.ylabel("Average Speed (km/h)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


# Function to plot runners count by age group
def plot_runners_count_by_age_group(data):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x="Age Group", y="Number of Runners")
    plt.title("Number of Runners Below and Above 50 Years Old")
    plt.xlabel("Age Group")
    plt.ylabel("Number of Runners")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
