import os
import pandas as pd
from config import DATA_FILE

def view_records():
    if not os.path.exists(DATA_FILE):
        print("❌ No patient records found.")
        return
    df = pd.read_csv(DATA_FILE)
    print("\n--- Stored Patient Records ---")
    print(df)

def search_patient():
    if not os.path.exists(DATA_FILE):
        print("❌ No patient records found.")
        return
    df = pd.read_csv(DATA_FILE)
    name = input("Enter patient name to search: ").strip().lower()
    results = df[df["Name"].str.lower().str.contains(name)]
    if results.empty:
        print(f"❌ No patient found with name: {name}")
    else:
        print("\n--- Search Results ---")
        print(results)
