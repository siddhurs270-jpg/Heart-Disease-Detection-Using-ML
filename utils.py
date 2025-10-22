def get_risk_level(prob):
    if prob < 0.25:
        return "No Risk ✅"
    elif prob < 0.5:
        return "Mild Risk 🙂"
    elif prob < 0.75:
        return "Moderate Risk ⚠️"
    else:
        return "High Risk 🚨"

def give_recommendations(smoking, alcohol, exercise):
    if smoking == "yes":
        print("⚠️ Smoking increases heart disease risk. Try quitting.")
    if alcohol == "yes":
        print("⚠️ Limit alcohol consumption for better heart health.")
    try:
        if float(exercise) < 3:
            print("🏃 Increase exercise (3+ hours/week recommended).")
        else:
            print("✅ Good job! Keep maintaining regular exercise.")
    except:
        print("⚠️ Invalid exercise input, skipping advice.")
