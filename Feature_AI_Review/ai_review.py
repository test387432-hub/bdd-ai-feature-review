import requests
import os

# Get current directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Feature folder path
feature_folder = os.path.join(base_dir, "feature_files")

# Read guidelines once
with open(os.path.join(base_dir, "guidelines.txt"), "r") as f:
    guidelines = f.read()

# Loop through all feature files
for file in os.listdir(feature_folder):

    if file.endswith(".feature"):

        print("\n==================================")
        print(f"Reviewing Feature File: {file}")
        print("==================================\n")

        file_path = os.path.join(feature_folder, file)

        # Read feature file
        with open(file_path, "r") as f:
            feature_text = f.read()

        # Create prompt
        prompt = f"""
You are a QA automation expert.

Review the following BDD feature file strictly based on the guidelines.

STRICT VALIDATION RULES:
- Only validate based on the provided guidelines.
- Do NOT invent new rules.
- Do NOT suggest improvements unless a rule is violated.
- If all guidelines are satisfied, respond with "No issues found".

GUIDELINES:
{guidelines}

FEATURE FILE:
{feature_text}

Provide:
1. Issues found
2. Suggested improvements
"""

        # Send request to local AI
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()["response"]

        # Print structured output
        print("🤖 AI Feature Review Report")
        print(f"📄 File: {file}")
        print("----------------------------")
        print(result)
        print("\n")

        # Save results to file
        with open(os.path.join(base_dir, "review_results.txt"), "a") as r:
            r.write("\n\n=================================\n")
            r.write("AI FEATURE REVIEW REPORT\n")
            r.write(f"File: {file}\n")
            r.write("=================================\n")
            r.write(result)
            r.write("\n")