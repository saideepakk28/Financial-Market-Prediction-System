# Financial Market Prediction System

An AI-powered stock prediction system that forecasts future stock prices using deep learning (LSTM/PatchTST). It features a real-time web interface to visualize historical trends alongside future predictions.

## 🚀 Features
- **Advanced AI Model**: Uses Long Short-Term Memory (LSTM) / PatchTST architecture for time-series forecasting.
- **Interactive Dashboard**: Web-based UI to view stock history and generate forecasts on demand.
- **Real-Time Visualization**: Seamlessly plots historical data and future predictions on the same chart.
- **Dynamic Forecasting**: Predict custom durations (e.g., next 7 days, 30 days).

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.8 or higher
- Pip (Python package manager)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/saideepakk28/Financial-Market-Prediction-System.git
   cd Financial-Market-Prediction-System
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ How to Run

1. **Start the Flask Application:**
   ```bash
   python app.py
   ```
   You should see output indicating the server is running (usually at `http://0.0.0.0:5000`).

2. **Access the Dashboard:**
   Open your browser and navigate to:
   [http://localhost:5000](http://localhost:5000)

## 📉 Usage
1. Enter the number of days you want to predict (e.g., `10`).
2. Click **"Predict"**.
3. The chart will update to show:
   - **Gray Line**: The last 30 days of actual historical prices.
   - **Blue Line**: The AI's predicted future path.

## 🧠 Model & Data Details
- **Data Source**: Historical stock data (e.g., AAPL) processed from Yahoo Finance.
- **Preprocessing**: Data is cleaned and scaled. Normalization is handled during training to ensure the model learns robust patterns.
- **Prediction Logic**: The model looks at the previous 30 days of market behavior to predict the next day. This process is repeated autoregressively to generate multi-day forecasts.

### Note on "Downward" Predictions
If the market has been trending downwards in the most recent historical data (e.g., the last few days of the dataset), the model will likely predict a continued decline in the short term. This reflects the momentum it observes in the recent context window.

## 🔧 Troubleshooting
- **Missing Dependencies**: Run `pip install -r requirements.txt` again.
- **Port In Use**: If port 5000 is busy, modify `app.py` to use a different port (e.g., `app.run(port=5001)`).
