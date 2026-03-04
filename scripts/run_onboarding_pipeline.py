import os
import json
import re
from extract_onboarding import extract_onboarding_data
from update_memo import update_memo
from generate_agent import generate_agent

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FOLDER = os.path.join(BASE_DIR, "inputs", "onboarding_calls")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs", "accounts")


def run():
    print("--- Running Pipeline B (Onboarding Calls) ---")
    files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.txt')]

    for file in files:
        account_num = re.search(r'\d+', file).group()
        account_id = f"acct_{account_num}"

        print(f"\nProcessing {file} -> {account_id}")

        path = os.path.join(INPUT_FOLDER, file)
        with open(path, "r", encoding="utf-8") as f:
            transcript = f.read()

        memo_path = os.path.join(OUTPUT_FOLDER, account_id, "v1", "memo.json")
        if not os.path.exists(memo_path):
            print(f"Error: v1 memo not found for {account_id}. Run Pipeline A first.")
            continue

        with open(memo_path, "r", encoding="utf-8") as f:
            old_memo = json.load(f)

        updates = extract_onboarding_data(transcript)
        new_memo = update_memo(old_memo, updates)
        new_agent = generate_agent(new_memo)

        save_path = os.path.join(OUTPUT_FOLDER, account_id, "v2")
        os.makedirs(save_path, exist_ok=True)

        with open(os.path.join(save_path, "memo.json"), "w", encoding="utf-8") as f:
            json.dump(new_memo, f, indent=2)

        with open(os.path.join(save_path, "agent.json"), "w", encoding="utf-8") as f:
            json.dump(new_agent, f, indent=2)

        # Generate Changelog
        changelog = []
        for key in old_memo:
            if key in new_memo and old_memo[key] != new_memo[key]:
                changelog.append({
                    "field": key,
                    "old_value": old_memo[key],
                    "new_value": new_memo[key],
                    "reason": "Updated based on onboarding transcript"
                })

        with open(os.path.join(save_path, "changes.json"), "w", encoding="utf-8") as f:
            json.dump(changelog, f, indent=2)

        print(f"Generated v2 and changelog successfully for {account_id}")


if __name__ == "__main__":
    run()