def garden_advice(season="spring", plant_type="vegetables"):
    seasonal_advice = {
        "spring": "Plant seeds and prepare the soil.",
        "summer": "Water plants regularly.",
        "autumn": "Collect fallen leaves for compost.",
        "winter": "Protect plants from frost.",
    }

    plant_advice = {
        "vegetables": "Water vegetables regularly and remove weeds.",
        "flowers": "Remove dead flowers and provide suitable sunlight.",
    }

    print(seasonal_advice.get(season, "Choose a valid season."))
    print(plant_advice.get(plant_type, "Choose vegetables or flowers."))

    # TODO: Move the advice data into a separate configuration file.
    # TODO: Add input validation for season and plant_type.


if __name__ == "__main__":
    garden_advice()