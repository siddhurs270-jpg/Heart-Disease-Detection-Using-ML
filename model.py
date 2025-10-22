import os
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import xgboost as xgb
from config import HEART_FILE, MODEL_FILE, SCALER_FILE

def load_or_train_model():
    if not os.path.exists(HEART_FILE):
        raise FileNotFoundError(f"❌ {HEART_FILE} not found.")

    df = pd.read_csv(HEART_FILE)
    print(f"✅ Loaded {HEART_FILE} with {df.shape[0]} rows and {df.shape[1]} columns")

    if df["sex"].dtype == object:
        df["sex"] = df["sex"].map({"Male": 1, "Female": 0})

    features = df.drop("target", axis=1).columns.tolist()

    if os.path.exists(MODEL_FILE) and os.path.exists(SCALER_FILE):
        model = joblib.load(MODEL_FILE)
        scaler = joblib.load(SCALER_FILE)
        print("✅ Model loaded from disk")
    else:
        X = df.drop("target", axis=1).values
        y = df["target"].values
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )
        model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="logloss")
        model.fit(X_train, y_train)

        joblib.dump(model, MODEL_FILE)
        joblib.dump(scaler, SCALER_FILE)
        print("✅ Model trained and saved")

    return model, scaler, features
