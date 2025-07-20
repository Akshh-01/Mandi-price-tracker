import pandas as pd
import datetime
import os

# Mock data for simulation
mock_prices = {
    "Wheat": 2100,
    "Rice": 1800,
    "Maize": 1600,
    "Cotton": 6200
}

today = datetime.date.today().isoformat()

def fetch_prices():
    data = []
    for crop, price in mock_prices.items():
        data.append({"Date": today, "Crop": crop, "Price": price})
    return pd.DataFrame(data)

def save_to_csv(df, path="data/prices.csv"):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(path):
        df.to_csv(path, mode='a', header=False, index=False)
    else:
        df.to_csv(path, index=False)

if __name__ == "__main__":
    df = fetch_prices()
    save_to_csv(df)
    print("✅ Prices saved to CSV.")
