# combine_lines.py
import json

with open('output/output.txt') as f:
    lines = f.read().strip().split('\n')

# Combine lines into coherent sentences
result = []
current_text = ""

for line in lines:
    if line.strip():  # If line is not empty
        current_text += " " + line.strip()
    else:
        if current_text:
            result.append({"text": current_text.strip()})
            current_text = ""

# Add the last collected text if any
if current_text:
    result.append({"text": current_text.strip()})

# Write to JSON file
with open('output/Martin_Miller_resume.json', 'w') as f:
    json.dump(result, f, indent=2)
