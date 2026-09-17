def garden_advice(season="spring"):
    seasonal_advice = {
        "spring": "Plant seeds and prepare the soil.",
        "summer": "Water plants regularly.",
        "autumn": "Collect fallen leaves for compost.",
        "winter": "Protect plants from frost.",
    }

    print(seasonal_advice.get(season, "Choose a valid season."))

    # TODO: Add advice for different plant types.


if __name__ == "__main__":
    garden_advice()