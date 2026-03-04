 🚀 Clara AI — Enterprise Agent Onboarding Automation
Executive Summary

This repository implements a code-first automation pipeline for onboarding and evolving Clara AI Voice Agents from raw call transcripts.

The system ingests unstructured conversation transcripts from customer calls, extracts operational intelligence, and generates version-controlled AI agent configurations while preserving a structured internal knowledge layer.

Unlike typical no-code automation solutions, this architecture emphasizes:

Deterministic data extraction

Version-controlled agent evolution

Stateful memory separation

Human-auditable configuration outputs

Zero-cost infrastructure

The final result is a reproducible pipeline capable of transforming raw call conversations into production-ready AI agent configurations with full traceability and change history.

🧠 Design Philosophy

The system follows three key engineering principles:

1. Code-First Reliability

Instead of relying solely on visual automation tools, the core intelligence layer is implemented in Python to ensure:

deterministic logic

debuggability

version control

predictable outputs

2. Separation of Knowledge and Behavior

The architecture strictly separates:

Layer	Purpose
memo.json	Internal knowledge extracted from transcripts
agent.json	AI agent instructions derived from that knowledge

This prevents prompt contamination and ensures clean prompt hygiene.

3. Stateful Agent Evolution

Agents are never overwritten.

Each update generates a new version:

v1 → v2 → v3

This guarantees:

full auditability

reversible changes

operational transparency

🏗 System Architecture

The automation engine is divided into two deterministic pipelines.

Pipeline A — Initial Agent Generation

Processes demo call transcripts and produces the first version of an AI agent configuration.

Steps

1️⃣ Transcript Ingestion

inputs/demo_calls/*.txt

Demo call transcripts are processed as raw text.

2️⃣ Information Extraction

A deterministic parser extracts key operational fields:

company name

supported services

business hours

emergency definitions

The extracted intelligence is stored in:

memo.json

Example:

{
 "business_hours": "8am - 5pm",
 "services_supported": [
  "sprinkler service",
  "fire alarm service"
 ],
 "emergency_definition": [
  "caller reports emergency"
 ]
}

3️⃣ Agent Configuration Generation

The system transforms the internal knowledge (memo.json) into a production-ready AI agent configuration.

This configuration enforces strict prompt hygiene:

the agent must never mention internal function calls

emergency detection follows defined business logic

caller address collection is prioritized during emergencies

Output:

agent.json

4️⃣ Human Review Task Trigger

The pipeline simulates an operational workflow by triggering a mock Asana task, representing a real-world human review stage before deployment.

🔁 Pipeline B — Evolutionary Agent Updates

Real businesses evolve.
Operational policies change.

This pipeline processes onboarding calls and updates existing agent configurations.

Step 1 — Delta Detection

The system scans onboarding transcripts for operational changes such as:

new services added

updated emergency rules

extended support hours

Example detected change:

"We now provide HVAC services and support 24/7 emergencies."

Extracted updates:

{
 "business_hours": "24/7",
 "services_supported": [
  "sprinkler service",
  "fire alarm service",
  "HVAC service"
 ]
}
Step 2 — Memo Update

Instead of overwriting existing knowledge, the system patches the memo state.

v1 memo + updates → v2 memo

This preserves all previously known information.

Step 3 — Agent Regeneration

A new agent configuration is synthesized from the updated memo.

v2/agent.json
Step 4 — Change Tracking

The pipeline automatically generates a changelog artifact describing the evolution between versions.

Example:

changes.json
{
 "services_added": ["HVAC service"],
 "business_hours_updated": "24/7"
}

This creates a transparent audit trail of agent evolution.

⚙️ Orchestration Layer

The system uses n8n as a workflow orchestrator.

Why n8n?

visual observability

event driven workflows

simple integration with APIs

Docker deployable

zero cost

The orchestration logic is exported as:

workflows/My_workflow.json

The workflow coordinates:

Transcript ingestion
→ Python processing
→ Agent generation
→ Task creation
📂 Project Structure
clara-agent-automation
│
├ inputs
│   ├ demo_calls
│   └ onboarding_calls
│
├ outputs
│   └ accounts
│        └ acct_1
│             ├ v1
│             │   ├ memo.json
│             │   └ agent.json
│             │
│             └ v2
│                 ├ memo.json
│                 └ agent.json
│
├ scripts
│   ├ extract_demo.py
│   ├ extract_onboarding.py
│   ├ generate_agent.py
│   ├ update_memo.py
│   ├ run_pipeline.py
│   └ run_onboarding_pipeline.py
│
└ workflows
    └ My_workflow.json
📈 Scalability Considerations

The pipeline was designed with production scenarios in mind.

Key capabilities:

✔ Batch processing of multiple accounts
✔ Stateless pipeline execution
✔ Version controlled outputs
✔ Deterministic data extraction
✔ Human-readable artifacts

To validate this, the system was tested against multi-account scenarios (acct_1 → acct_5) simulating diverse customer onboarding conversations.

💰 Zero-Cost Architecture

The entire solution runs without paid services.

Components used:

Component	Purpose
Python 3.10+	Data processing
n8n	Workflow orchestration
Docker	Containerized workflow engine

This design ensures the pipeline can run locally or in lightweight cloud environments without operational cost.

🧪 Running the Pipelines
Pipeline A — Demo Processing
python scripts/run_pipeline.py
Pipeline B — Onboarding Updates
python scripts/run_onboarding_pipeline.py
🧩 Running the Orchestrator

Start n8n locally using Docker:

docker run -it --rm \
-p 5678:5678 \
--name n8n \
n8nio/n8n

Open:

http://localhost:5678

Import the workflow:

workflows/My_workflow.json
🏁 Final Thoughts

This project demonstrates a hybrid automation architecture combining:

deterministic code pipelines

visual orchestration

version-controlled AI configuration

The design intentionally prioritizes:

reliability

traceability

operational clarity

over opaque automation logic.

The result is a scalable onboarding system capable of evolving AI agents safely as business operations change.
