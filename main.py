import csv
import os

# Error messages for invalid interger and float inputs
def get_validated_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_validated_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Price cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")



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
# error handling
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

def remove_car():
    if not car_collection:
        print("Collection is empty.\n")
        return

    view_all_cars()

    choice = get_valid_int("Enter number of car to remove: ")

    if 1 <= choice <= len(car_collection):
        removed = car_collection.pop(choice - 1)
        print(f"Removed {removed['year']} {removed['make']} {removed['model']}\n")
    else:
        print("Invalid selection.\n")

# Sort cars

def sort_cars():
    if not car_collection:
        print("Collection is empty.\n")
        return

    print("\n--- Sort Cars ---")
    print("1. Price Low → High")
    print("2. Price High → Low")
    print("3. Year Oldest → Newest")
    print("4. Year Newest → Oldest")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        sorted_list = sorted(car_collection, key=lambda c: c["price"])
    elif choice == "2":
        sorted_list = sorted(car_collection, key=lambda c: c["price"], reverse=True)
    elif choice == "3":
        sorted_list = sorted(car_collection, key=lambda c: c["year"])
    elif choice == "4":
        sorted_list = sorted(car_collection, key=lambda c: c["year"], reverse=True)
    else:
        print("Invalid choice.\n")
        return

    print()
    for i, car in enumerate(sorted_list, 1):
        print(f"{i}. {car['year']} {car['make']} {car['model']} - ${car['price']:,.2f}")
    print()





