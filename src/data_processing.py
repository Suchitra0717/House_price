import pandas as pd
path="D:/house_price/data.csv"
def load_and_process_data(path):
    data = pd.read_csv(path)

    # Convert total_sqft if exists
    if "total_sqft" in data.columns:
        data["total_sqft"] = pd.to_numeric(data["total_sqft"], errors="coerce")

    # Fill missing values
    data = data.dropna()

    data=data[data["Price"]<data["Price"].quantile(0.99)]
    data=data[data["Area"]<data["Area"].quantile(0.99)]
    
    data["Price_per_sqft"] = data["Price"]/data["Area"]

    # Convert text columns into numbers
    data = pd.get_dummies(data, drop_first=True)

    # Features and target
    X = data.drop("Price", axis=1)
    y = data["Price"]

    return X, y
