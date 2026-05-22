# 📊 Algorithmic Portfolio Intelligence Engine
### *An End-to-End Financial Analytics & Risk Infrastructure Dashboard*

---

## 🚀 Project Overview
This repository contains a high-performance, production-ready **Financial Portfolio Analytics Dashboard** built using Python, Streamlit, and Pandas. The intelligence engine dynamically simulates financial transactions across multiple asset classes (Stocks, Crypto, Gold, Bonds), aggregates the real-time active holdings, calculates capital concentration, and provides interactive risk filters for financial analysts.

### 🔥 Key Engineering Features:
* **Dynamic Simulation Engine:** Generates and processes transactional logs seamlessly without performance trade-offs.
* **Vectorized Data Aggregation:** Uses high-performance Pandas groupby operations to separate BUY/SELL actions, calculate net invested capital, and determine active asset allocation.
* **Interactive Filtering Architecture:** Built a dynamic multi-select sidebar framework allowing corporate users to isolate specific asset classes in real-time.
* **Financial Data Visualizations:** Integrated custom Seaborn and Matplotlib visualization pipelines to render asset diversification ratios (Pie Chart) and capital concentration metrics (Bar Chart).

---

## 🛠️ Tech Stack & Infrastructure
* **Language:** Python 3.x
* **Dashboard Framework:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Visualization Layer:** Matplotlib, Seaborn

---

## ⚙️ Installation & Local Execution

To run this financial infrastructure dashboard locally on your workstation, follow these steps:

1. **Clone the repository or download the project files:**
   ```bash
   cd Financial_Portfolio_Analytics
   pip install -r requirements.txt
   streamlit run app.py
