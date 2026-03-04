import os
import json
from extract_demo import extract_demo_data
from generate_agent import generate_agent
from mock_task_tracker import create_asana_task

INPUT_FOLDER = "inputs/demo_calls"
OUTPUT_FOLDER = "outputs/accounts"

def run():

    files = os.listdir(INPUT_FOLDER)

    for i, file in enumerate(files):

        path = f"{INPUT_FOLDER}/{file}"

        with open(path) as f:
            transcript = f.read()

        memo = extract_demo_data(transcript)
        agent = generate_agent(memo)

        account_id = f"acct_{i+1}"

        save_path = f"{OUTPUT_FOLDER}/{account_id}/v1"

        os.makedirs(save_path, exist_ok=True)

        with open(f"{save_path}/memo.json", "w") as f:
            json.dump(memo, f, indent=2)

            with open(f"{save_path}/agent.json", "w") as f:
                json.dump(agent, f, indent=2)

                create_asana_task("acct_1",memo.get("company_name", "Unknown Company"), save_path)

        print(f"Processed {file}")

if __name__ == "__main__":
    run()