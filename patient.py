import os
import pandas as pd
import matplotlib.pyplot as plt
from config import DATA_FILE
from utils import get_risk_level, give_recommendations

def submit(model, scaler, features):
    name = input("Enter Patient Name: ").strip()
    if name == "":
        print("❌ Error: Please enter Patient Name")
        return

    user_input = []
    for f in features:
        while True:
            try:
                if f == "sex":
                    val = input("Enter sex (Male/Female): ").strip().capitalize()
                    if val not in ["Male", "Female"]:
                        raise ValueError
                    val_num = 1 if val == "Male" else 0
                    user_input.append(val_num)
                else:
                    val = float(input(f"Enter {f}: "))
                    if val < 0:
                        raise ValueError
                    user_input.append(val)
                break
            except:
                print(f"Invalid input! Try again.")

    # Save with sex in words
    user_df = pd.DataFrame([user_input], columns=features)
    user_df.insert(0, "Name", name)
    user_df["sex"] = ["Male" if x == 1 else "Female" for x in user_df["sex"]]

    # Lifestyle inputs
    smoking = input("Do you smoke? (Yes/No): ").strip().lower()
    alcohol = input("Do you drink alcohol? (Yes/No): ").strip().lower()
    exercise = input("Exercise (hours per week): ").strip()

    user_df["Smoking"] = [smoking.capitalize()]
    user_df["Alcohol"] = [alcohol.capitalize()]
    user_df["ExerciseHours"] = [exercise]

    # Save record
    if os.path.exists(DATA_FILE):
        user_df.to_csv(DATA_FILE, mode="a", header=False, index=False)
    else:
        user_df.to_csv(DATA_FILE, index=False)

    # ML prediction
    ml_df = user_df.copy()
    ml_df["sex"] = ml_df["sex"].map({"Male": 1, "Female": 0})
    x_scaled = scaler.transform(ml_df[features].values)
    prob = model.predict_proba(x_scaled)[0][1]

    risk = get_risk_level(prob)

    print(f"\n--- Prediction Result ---")
    print(f"Patient: {name}")
    print(f"Risk: {risk}")
    print(f"Confidence: {prob:.2f}")

    print("\n--- Lifestyle Recommendations ---")
    give_recommendations(smoking, alcohol, exercise)

    # Visualization
    labels = ["No Risk", "Mild Risk", "Moderate Risk", "High Risk"]
    values = [max(0, 1 - prob), prob * 0.33, prob * 0.33, prob * 0.33]
    plt.figure(figsize=(5, 3))
    plt.bar(labels, values, color=["green", "yellow", "orange", "red"])
    plt.title(f"Risk Visualization for {name}")
    plt.ylabel("Confidence")
    plt.show()
