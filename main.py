from model import load_or_train_model
from patient import submit
from records import view_records, search_patient

if __name__ == "__main__":
    # Load dataset & train model automatically
    model, scaler, features = load_or_train_model()

    while True:
        print("\n--- Heart Disease Detection ---")
        print("1. Add Patient & Predict")
        print("2. View All Patients")
        print("3. Search Patient by Name")
        print("4. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            submit(model, scaler, features)
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice, try again.")
