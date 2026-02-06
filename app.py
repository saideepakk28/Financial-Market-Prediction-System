from flask import Flask, request, jsonify, render_template
import torch
import numpy as np
from predict import predict_future
from train_model import load_data
from flask import Flask, jsonify, request



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET"])
def predict():
    days = int(request.args.get("days", 10))  # Default: 10 days
    predictions = predict_future(days)
    
    # Get historical data for context
    close_prices, scaler = load_data()
    
    # Inverse transform to get real prices back
    real_prices = scaler.inverse_transform(close_prices.reshape(-1, 1)).flatten()
    history = real_prices[-30:].tolist() # Last 30 days history in real prices
    
    return jsonify({
        "predictions": predictions.tolist(),
        "history": history
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

