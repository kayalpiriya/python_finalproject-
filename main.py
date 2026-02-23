import os
from utils import check_priority

plants = []
high_priority = []
medium_priority = []
low_priority = []


# -----------------------------
# Load plants from file
# -----------------------------
def load_initial_stock():
    if not os.path.exists("initial_stock.txt"):
        print("initial_stock.txt not found!")
        choice = input("Create new file? (y/n): ")

        if choice.lower() == "y":
            open("initial_stock.txt", "w").close()
            print("File created.")
        return

    with open("initial_stock.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            plant = {
                "plant_ID": int(data[0]),
                "species": data[1],
                "water_interval": int(data[2]),
                "last_watered_day": int(data[3])
            }

            plants.append(plant)


# -----------------------------
# Get current day
# -----------------------------
def get_current_day():
    while True:
        try:
            day = int(input("Enter current day (1-30): "))
            if 1 <= day <= 30:
                return day
            else:
                print("Enter number between 1 and 30")
        except:
            print("Invalid input")


# -----------------------------
# Categorize plants
# -----------------------------
def categorize_plants(current_day):
    high_priority.clear()
    medium_priority.clear()
    low_priority.clear()

    for plant in plants:
        priority = check_priority(
            current_day,
            plant["last_watered_day"],
            plant["water_interval"]
        )

        if priority == "HIGH":
            high_priority.append(plant)
        elif priority == "MEDIUM":
            medium_priority.append(plant)
        else:
            low_priority.append(plant)


# -----------------------------
# Show priority
# -----------------------------
def show_priority():
    print("\nHIGH PRIORITY:")
    for p in high_priority:
        print(p["plant_ID"], "-", p["species"])

    print("\nMEDIUM PRIORITY:")
    for p in medium_priority:
        print(p["plant_ID"], "-", p["species"])

    print("\nLOW PRIORITY:")
    for p in low_priority:
        print(p["plant_ID"], "-", p["species"])


# -----------------------------
# Water single plant
# -----------------------------
def water_plant(current_day):
    plant_id = int(input("Enter plant ID: "))

    for plant in plants:
        if plant["plant_ID"] == plant_id:
            plant["last_watered_day"] = current_day
            print("Plant watered!")
            return

    print("Plant not found")


# -----------------------------
# Water by species
# -----------------------------
def water_by_species(current_day):
    species_name = input("Enter species name: ")

    for plant in plants:
        if plant["species"].lower() == species_name.lower():
            plant["last_watered_day"] = current_day

    print("All matching plants watered!")


# -----------------------------
# Generate daily care file
# -----------------------------
def generate_daily_care_plan():
    with open("daily_care_plan.txt", "w") as file:
        file.write("Plants Needing Water Today:\n\n")

        for plant in high_priority + medium_priority:
            file.write(f"{plant['plant_ID']} - {plant['species']}\n")

    print("daily_care_plan.txt created!")


# -----------------------------
# Save updates to file
# -----------------------------
def save_to_file():
    with open("initial_stock.txt", "w") as file:
        for plant in plants:
            file.write(
                f"{plant['plant_ID']},"
                f"{plant['species']},"
                f"{plant['water_interval']},"
                f"{plant['last_watered_day']}\n"
            )


# -----------------------------
# Menu
# -----------------------------
def menu():
    load_initial_stock()

    while True:
        print("\n--- Green Thumb Forecaster ---")
        print("1. Check Priority")
        print("2. Water a Plant")
        print("3. Water by Species")
        print("4. Generate Daily Care Plan")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            day = get_current_day()
            categorize_plants(day)
            show_priority()

        elif choice == "2":
            day = get_current_day()
            water_plant(day)
            save_to_file()

        elif choice == "3":
            day = get_current_day()
            water_by_species(day)
            save_to_file()

        elif choice == "4":
            generate_daily_care_plan()

        elif choice == "5":
            save_to_file()
            print("Program exited")
            break

        else:
            print("Invalid choice")


# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    menu()
