import json
import os

input_file = "pixel-tracker.json"
with open(input_file, "r") as file:
    data = json.load(file)

output_directory = "markdown"
os.makedirs(output_directory, exist_ok=True)

for item in data["items"]:
    date = item["date"]
    markdown_filename = os.path.join(output_directory, f"{date}.md")

    markdown_content = f"# Entry for {date}\n\n"
    markdown_content += f"**ID:** {item['id']}\n\n"
    markdown_content += f"**Date:** {item['date']}\n\n"
    markdown_content += f"**DateTime:** {item['dateTime']}\n\n"
    markdown_content += f"**Rating:** {item['rating']}\n\n"
    markdown_content += f"**Emotions:** {', '.join(item['emotions'])}\n\n"
    markdown_content += (
        f"**Message:**\n{item.get('message', 'No message provided')}\n\n"
    )

    with open(markdown_filename, "a") as md_file:
        md_file.write(markdown_content)

print("Markdown files created successfully in the 'markdown' directory.")
