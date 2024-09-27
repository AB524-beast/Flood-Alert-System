document.addEventListener('DOMContentLoaded', function() {
    // Check the current hour
    const currentHour = new Date().getHours();

    // If the time is between 18:00 (6 PM) and 6:00 (6 AM), enable dark mode
    if (currentHour >= 18 || currentHour < 6) {
        document.body.classList.add('dark-mode');
    }
});

// Function to simulate sending the location data to the backend and getting a prediction
function checkFloodPrediction() {
    const location = document.getElementById("location").value;

    if (!location) {
        alert("Please enter a valid location.");
        return;
    }

    document.getElementById("prediction-output").innerText = "Fetching prediction for " + location + "...";

    // Simulate an API call to the backend
    setTimeout(() => {
        const floodPrediction = predictFloodForLocation(location);
        document.getElementById("prediction-output").innerText = floodPrediction;
    }, 2000);
}

// Mock function to simulate backend flood prediction logic based on location
function predictFloodForLocation(location) {
    const predictions = {
        "New York": "Low risk of flood in the next 7 days.",
        "Los Angeles": "No risk of flood in the next 7 days.",
        "Miami": "High risk of flood in the next 48 hours.",
        "Chicago": "Moderate risk of flood in the next 3 days."
    };

    return predictions[location] || "Prediction not available for this location.";
}
