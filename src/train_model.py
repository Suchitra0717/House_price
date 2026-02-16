from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
from data_processing import load_and_process_data

X, y = load_and_process_data("D:/house_price/data.csv")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=600, max_depth=30,min_samples_split=3,min_samples_leaf=1,random_state=42,n_jobs=-1)
model.fit(X_train,y_train)

pickle.dump(model, open("D:/house_price/house_model.pkl", "wb"))

with open("model_columns.pkl","wb") as f:
    pickle.dump(X.columns.tolist(),f)

print("Model trained and saved!")