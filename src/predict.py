import pandas as pd
import joblib

model = joblib.load("D:/house_price/house_model.pkl")
model_columns = joblib.load("D:/house_price/src/model_columns.pkl")

def predict_price(input_data):
    df = pd.DataFrame([input_data])

    # Add missing columns
    df = df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(df)
    return prediction[0]


if __name__ == "__main__":
    sample = {
        "Area": 1200,
        "BED": 2
    }

    price = predict_price(sample)
    print("Predicted Price:", price)