import re

def extract_demo_data(transcript):
    memo = {
        "account_id": None,
        "company_name": None,
        "business_hours": None,
        "office_address": None,
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": None,
        "non_emergency_routing_rules": None,
        "call_transfer_rules": None,
        "integration_constraints": [],
        "after_hours_flow_summary": None,
        "office_hours_flow_summary": None,
        "questions_or_unknowns": [],
        "notes": None
    }

    text = transcript.lower()

    if "sprinkler" in text:
        memo["services_supported"].append("sprinkler service")

    if "fire alarm" in text:
        memo["services_supported"].append("fire alarm service")

    hours_pattern = r'(\d{1,2}\s?(am|pm)\s?-\s?\d{1,2}\s?(am|pm))'

    match = re.search(hours_pattern, text)

    if match:
        memo["business_hours"] = match.group()
    else:
        memo["questions_or_unknowns"].append("Business hours not mentioned")

    if "emergency" in text:
        memo["emergency_definition"].append("Caller reports emergency")

    return memo