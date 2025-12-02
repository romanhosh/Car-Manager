import csv
import os

# list to store car dictionaries
car_collection = []


# -----------------------------
# Load cars from CSV
# -----------------------------
def load_cars():
    if not os.path.exists("car_collection.csv"):
        print("No saved data found. Starting with an empty collection.\n")
        return

    try:
        with open("car_collection.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    car = {
                        "make": row["Make"],
                        "model": row["Model"],
                        "year": int(row["Year"]),
                        "price": float(row["Price"])
                    }
                    car_collection.append(car)
                except (ValueError, KeyError):
                    # Skip malformed rows
                    continue

        print(f"Loaded {len(car_collection)} cars from file.\n")

    except Exception as e:
        print(f"Error loading file: {e}\n")
