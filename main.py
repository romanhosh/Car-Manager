import csv
import os

# list to store car dictionaries
car_collection = []


# Load cars from CSV
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

# Save cars to CSV
def save_cars():
    try:
        with open("car_collection.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Make", "Model", "Year", "Price"])

            for car in car_collection:
                writer.writerow([car["make"], car["model"], car["year"], car["price"]])

        print("Collection saved successfully!\n")

    except Exception as e:
        print(f"Error saving file: {e}\n")

# Display all cars


def view_all_cars():
    if not car_collection:
        print("Your collection is empty.\n")
        return

    print("\n--- Your Car Collection ---")
    for i, car in enumerate(car_collection, 1):
        print(f"{i}. {car['year']} {car['make']} {car['model']} - ${car['price']:,.2f}")
    print()



# Add a new car

def add_car():
    print("\n--- Add New Car ---")

    make = input("Enter make: ").strip()
    model = input("Enter model: ").strip()

    year = get_valid_int("Enter year: ")
    price = get_valid_float("Enter price: ")

    new_car = {"make": make, "model": model, "year": year, "price": price}
    car_collection.append(new_car)

    print(f"\n{year} {make} {model} added!\n")



# Remove a car



