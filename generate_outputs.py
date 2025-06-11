"""
This script loads Jinja2 templates, applies them to a test dataset, sends them to OpenAI's API (mocked here),
and saves the results to a CSV file for evaluation. It also includes a refined prompt re-run for comparison.
"""

import csv
from jinja2 import Template

# Sample test dataset
test_cases = [
    "The product stopped working after 3 days and no one is responding to my emails.",
    "I was charged twice for the same item and need a refund ASAP.",
    "The delivery was late and the item was damaged.",
    "Support promised a callback that never happened.",
    "The website keeps crashing when I try to check out."
]

# Load original prompt variants
with open("prompt_variants.j2", "r") as f:
    prompts = f.read().split("{#")[1:]

# Extract only the template body (skipping comments)
def extract_template(prompt_block):
    content_start = prompt_block.find("#}") + 2
    return prompt_block[content_start:].strip()

# Simulated response function (replace with OpenAI API call if needed)
def fake_llm_response(prompt):
    return "Simulated response for: " + prompt[:60] + "..."

# Create a log file for all prompt variant outputs
with open("outputs_log.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Prompt_Variant", "Input", "Output"])
    for idx, block in enumerate(prompts):
        template = Template(extract_template(block))
        for case in test_cases:
            filled_prompt = template.render(complaint=case)
            output = fake_llm_response(filled_prompt)
            writer.writerow([f"Prompt_{idx+1}", case, output])

# Refined version of Prompt 3
refined_prompt = """
You are a complaint analysis assistant. Summarize the issue and action clearly.
Format:
Issue: <summary of the problem>
Action: <recommended next step>
Complaint: {{ complaint }}
"""

# Log refined prompt outputs
with open("refined_outputs_log.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Prompt_Variant", "Input", "Output"])
    template = Template(refined_prompt)
    for case in test_cases:
        filled_prompt = template.render(complaint=case)
        output = fake_llm_response(filled_prompt)
        writer.writerow(["Refined_Prompt_3", case, output])
