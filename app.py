from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("house_price_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form inputs
        longitude = float(request.form["longitude"])
        latitude = float(request.form["latitude"])
        housing_median_age = float(request.form["housing_median_age"])
        total_rooms = float(request.form["total_rooms"])
        total_bedrooms = float(request.form["total_bedrooms"])
        population = float(request.form["population"])
        households = float(request.form["households"])
        median_income = float(request.form["median_income"])

        # Feature engineering
        rooms_per_household = total_rooms / households
        people_per_household = population / households
        bedrooms_per_room = total_bedrooms / total_rooms

        # Ocean proximity
        ocean = request.form["ocean_proximity"]

        ocean_inland = 1 if ocean == "INLAND" else 0
        ocean_near_bay = 1 if ocean == "NEAR BAY" else 0
        ocean_near_ocean = 1 if ocean == "NEAR OCEAN" else 0
        ocean_less_than_1h = 1 if ocean == "<1H OCEAN" else 0
        ocean_island = 1 if ocean == "ISLAND" else 0

        features = np.array([[
            longitude,
            latitude,
            housing_median_age,
            total_rooms,
            total_bedrooms,
            population,
            households,
            median_income,
            rooms_per_household,
            people_per_household,
            bedrooms_per_room,
            ocean_inland,
            ocean_near_bay,
            ocean_near_ocean,
            ocean_less_than_1h
        ]])

        prediction = model.predict(features)[0]

        return render_template(
            "index.html",
            prediction_text=f"Predicted House Price: ${prediction:,.2f}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)
