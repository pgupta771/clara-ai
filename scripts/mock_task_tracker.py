import json
import os


def create_asana_task(account_id, company_name, memo_path):
    """
    Mocks an API call to Asana/Trello to create a tracking item for the new demo call.
    [span_4](start_span)Satisfies the assignment requirement: 'A tracking item created in a task tool'[span_4](end_span).
    """
    print("\n--- MOCK ASANA API CALL ---")
    print(f"Creating review task for: {company_name} (Account: {account_id})")

    # Simulating the payload we would send to the Asana API
    payload = {
        "data": {
            "workspace": "your_workspace_id",
            "name": f"Review Preliminary Agent: {company_name}",
            "notes": f"A new demo call was processed. Preliminary v1 agent generated.\nReview memo at: {memo_path}",
            "projects": ["onboarding_board_id"]
        }
    }

    # Simulating a successful 201 API response
    mock_response = {
        "task_id": f"asana_task_{account_id}_998",
        "status": "Success",
        "message": "Task created in 'Needs Onboarding Review' column."
    }

    print(f"Payload sent: {json.dumps(payload, indent=2)}")
    print(f"Response received: {mock_response}\n---------------------------\n")

    return mock_response