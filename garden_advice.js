// --------------------------------------------------------------
// 🌱 Garden Advice App (JavaScript Version)
// --------------------------------------------------------------
// This script gives gardening tips based on the user's entered
// season and plant type. It uses structured data, modular
// functions, and basic user interaction via prompt().
// --------------------------------------------------------------

// --- Advice Data Structure ---
const adviceData = {
  season: {
    summer: "Water your plants regularly and provide some shade.",
    winter: "Protect your plants from frost with covers.",
    spring: "Plant new seeds and enjoy the blooming season.",
    autumn: "Prepare your garden for the colder months ahead."
  },
  plant: {
    flower: "Use fertiliser to encourage beautiful blooms.",
    vegetable: "Keep an eye out for pests and harvest regularly."
  }
};

// --- Functions ---
/**
 * Returns advice for the entered season.
 * @param {string} season - The current season entered by the user.
 * @returns {string} - Season-specific advice.
 */
function getSeasonAdvice(season) {
  return adviceData.season[season] || "No advice available for this season.";
}

/**
 * Returns advice for the entered plant type.
 * @param {string} type - The type of plant entered by the user.
 * @returns {string} - Plant-specific advice.
 */
function getPlantAdvice(type) {
  return adviceData.plant[type] || "No advice available for this type of plant.";
}

// --- Main Program Execution ---
const season = prompt("Enter the current season (e.g., summer, winter, spring, autumn):").toLowerCase();
const plantType = prompt("Enter the plant type (e.g., flower, vegetable):").toLowerCase();

// Combine and display advice
const finalAdvice = `${getSeasonAdvice(season)}\n${getPlantAdvice(plantType)}`;
console.log("🌿 Gardening Advice 🌿\n" + finalAdvice);
