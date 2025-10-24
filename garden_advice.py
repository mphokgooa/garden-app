# --------------------------------------------------------------
# 🌱 Garden Advice App (Python Version)
# --------------------------------------------------------------
# This program gives gardening tips based on user input for
# season and plant type. It uses structured data, functions,
# and input() for interaction in the terminal.
# --------------------------------------------------------------

# --- Advice Data Structure ---
advice_data = {
    "season": {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers.",
        "spring": "Plant new seeds and enjoy the blooming season.",
        "autumn": "Prepare your garden for the colder months ahead."
    },
    "plant": {
        "flower": "Use fertiliser to encourage beautiful blooms.",
        "vegetable": "Keep an eye out for pests and harvest regularly."
    }
}

# --- Functions ---

def get_season_advice(season):
    """Return advice for the entered season."""
    return advice_data["season"].get(season, "No advice available for this season.")

def get_plant_advice(plant_type):
    """Return advice for the entered plant type."""
    return advice_data["plant"].get(plant_type, "No advice available for this type of plant.")
# garden_advice.py

def get_watering_schedule(plant_type):
    """
    Returns a recommended watering schedule based on plant type.
    """
    plant_type = plant_type.lower()

    if plant_type in ["cactus", "succulent"]:
        return "Water once every 2–3 weeks. Avoid overwatering."
    elif plant_type in ["flower", "rose", "tulip"]:
        return "Water 2–3 times a week, especially in warm weather."
    elif plant_type in ["vegetable", "herb"]:
        return "Water daily or every other day depending on soil moisture."
    else:
        return "Water when the top 2–3 cm of soil feels dry."


def main():
    print("🌿 Welcome to the Garden Advice Program!")
    plant = input("Enter your plant type (e.g., cactus, flower, vegetable): ")

    print("\n🌱 Here’s your general garden advice:")
    print("- Make sure your plant gets enough sunlight.")
    print("- Use nutrient-rich soil for better growth.")
    print("- Remove weeds regularly.")

    # NEW FEATURE: Include watering advice
    schedule = get_watering_schedule(plant)
    print(f"\n💧 Watering advice for your {plant}: {schedule}")


if __name__ == "__main__":
    main()

# --- Main Program Execution ---
season = input("Enter the current season (e.g., summer, winter, spring, autumn): ").lower()
plant_type = input("Enter the plant type (e.g., flower, vegetable): ").lower()

# Combine and display advice
final_advice = f"{get_season_advice(season)}\n{get_plant_advice(plant_type)}"
print("\n🌿 Gardening Advice 🌿")
print(final_advice)
