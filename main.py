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


# Show statistics

def show_statistics():
    if not car_collection:
        print("Collection is empty.\n")
        return

    total_cars = len(car_collection)
    total_value = sum(car["price"] for car in car_collection)
    avg_price = total_value / total_cars

    most_expensive = max(car_collection, key=lambda c: c["price"])
    cheapest = min(car_collection, key=lambda c: c["price"])

    print("\n--- Statistics ---")
    print(f"Total Cars: {total_cars}")
    print(f"Total Value: ${total_value:,.2f}")
    print(f"Average Price: ${avg_price:,.2f}\n")

    print("Most Expensive:")
    print(f"{most_expensive['year']} {most_expensive['make']} {most_expensive['model']} - ${most_expensive['price']:,.2f}\n")

    print("Cheapest:")
    print(f"{cheapest['year']} {cheapest['make']} {cheapest['model']} - ${cheapest['price']:,.2f}\n")


# Helpers

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


# Main Menu

def main_menu():
    load_cars()

    while True:
        print("=== Car Collection Manager ===")
        print("1. View All Cars")
        print("2. Add Car")
        print("3. Remove Car")
        print("4. Sort Cars")
        print("5. Statistics")
        print("6. Save and Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            view_all_cars()
        elif choice == "2":
            add_car()
        elif choice == "3":
            remove_car()
        elif choice == "4":
            sort_cars()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            save_cars()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


# Entry point
if __name__ == "__main__":
    main_menu()

