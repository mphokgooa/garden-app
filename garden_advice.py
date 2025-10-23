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

# --- Main Program Execution ---
season = input("Enter the current season (e.g., summer, winter, spring, autumn): ").lower()
plant_type = input("Enter the plant type (e.g., flower, vegetable): ").lower()

# Combine and display advice
final_advice = f"{get_season_advice(season)}\n{get_plant_advice(plant_type)}"
print("\n🌿 Gardening Advice 🌿")
print(final_advice)
