# 🌾 Mandi Price Tracker

A simple Python-based project to help track and visualize agricultural commodity (mandi) prices.  
Built for farmers and rural users to better understand market trends over time.

---

## 📌 Features

- 📊 Track daily prices of key crops (e.g., Wheat, Rice, Maize, Cotton)
- 🗂️ Save data to CSV format
- 📈 Visualize price trends using Matplotlib
- ✅ Fully offline & lightweight – ideal for rural deployment
- 🔧 Easy to extend with live data scraping or SMS alerts

---

## 📁 Project Structure

mandi-price-tracker/
├── data/
│ └── prices.csv # Stores mandi price data
├── scraper.py # Simulates fetching mandi prices
├── analyze.py # Plots price trends for crops
├── .gitignore # Prevents unnecessary files from being committed
└── README.md # You're reading it!

yaml

---

## ▶️ How to Run

### 1. Clone the repo (or download the ZIP)


git clone https://github.com/Akshh-01/Mandi-price-tracker.git
cd Mandi-price-tracker
2. Install dependencies

pip install -r requirements.txt
If requirements.txt doesn't exist, install manually:

pip install pandas matplotlib
3. Run the scraper (simulate today’s prices)

python scraper.py
4. Visualize the data

python analyze.py
📊 Sample Output
The system plots mandi prices over time like this:


🛠️ Future Ideas
🛰️ Scrape live prices from Agmarknet or government portals

📱 Add SMS support to query prices via mobile

🌐 Build a web interface using Streamlit or Flask

📈 Predict future prices using machine learning

🙌 Acknowledgements
Inspired by real challenges faced by rural farmers

Built with ❤️ in Python using VS Code

📃 License
This project is open-source and free to use under the MIT License.

yaml

