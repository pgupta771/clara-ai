def extract_onboarding_data(transcript):

    updates = {}

    if "24/7" in transcript or "24 hours" in transcript:
        updates["business_hours"] = "24/7"

    if "HVAC" in transcript:
        updates["services_supported"] = [
            "sprinkler service",
            "fire alarm service",
            "HVAC service"
        ]

    if "after hours emergency" in transcript:
        updates["emergency_definition"] = [
            "caller reports emergency",
            "after hours emergency"
        ]

    return updates