import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

#data ingestion step
url_data = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"

#data preparation step
df = pd.read_csv(url_data)
print("Columns:", df.columns.to_list())

X = df[['Pregnancies', 'Glucose', 'BloodPressure','BMI', 'Age',]]
Y = df[['Outcome']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, Y_train)

joblib.dump(model, "model.pkl")
print("Model saved as model.pkl in the current directory")