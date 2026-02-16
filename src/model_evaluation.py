import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from data_processing import load_and_process_data

X, y = load_and_process_data("D:/house_price/data.csv")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = pickle.load(open("D:/house_price/house_model.pkl", "rb"))

pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, pred))