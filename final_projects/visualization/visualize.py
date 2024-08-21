import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def covid_time_series(data_frame: pd.DataFrame):
    sns.lineplot(data=data_frame, x="date", y="value", hue="country_region")

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series")


def covid_bar(data_frame: pd.DataFrame):
    sns.barplot(
        data=data_frame,
        x="value",
        y="country_region",
        hue="country_region",
        palette=data_frame["color"].tolist(),
    )
    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context")
