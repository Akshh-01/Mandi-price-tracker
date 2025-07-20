import pandas as pd
import matplotlib.pyplot as plt

# 👇 Add this line to fix plot display
plt.switch_backend('TkAgg')

def load_data(path="data/prices.csv"):
    return pd.read_csv(path)

def plot_prices(df):
    crops = df["Crop"].unique()
    for crop in crops:
        crop_data = df[df["Crop"] == crop]
        plt.plot(crop_data["Date"], crop_data["Price"], marker='o', label=crop)

    plt.xlabel("Date")
    plt.ylabel("Price (INR)")
    plt.title("Mandi Price Trends")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_data()
    plot_prices(df)
