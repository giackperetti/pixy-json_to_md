import json
import os

input_file = "pixel-tracker.json"

with open(input_file, "r") as file:
    data = json.load(file)

output_directory = "markdown"
os.makedirs(output_directory, exist_ok=True)

tag_mapping = {
    "1": "family",
    "2": "friends",
    "3": "love",
    "4": "sport",
    "5": "relax",
    "6": "reading",
    "7": "music",
    "8": "sleep early",
    "9": "studying",
    "10": "homework",
    "11": "gym",
    "12": "watching series/movies",
    "13": "computer science stuff",
    "14": "nature",
    "15": "linux stuff",
    "16": "social media",
    "17": "school",
    "18": "travel",
    "19": "shopping",
}

for item in data["items"]:
    date = item["date"]
    markdown_filename = os.path.join(output_directory, f"{date}.md")

    markdown_content = f"# Entry for {date}\n\n"
    markdown_content += f"**Date:** {item['date']}\n\n"
    markdown_content += f"**Rating:** {item['rating']}\n\n"

    emotions = [f"#{emotion}" for emotion in item["emotions"]]
    markdown_content += f"**Emotions:** {', '.join(emotions)}\n\n"

    tags = [
        tag_mapping[tag["id"]]
        for tag in item.get("tags", [])
        if tag["id"] in tag_mapping
    ]
    tag_tags = [f"#{tag}" for tag in tags]
    markdown_content += (
        f"**Tags:** {', '.join(tag_tags) if tag_tags else 'No tags provided'}\n\n"
    )

    markdown_content += (
        f"**Message:**\n{item.get('message', 'No message provided')}\n\n"
    )

    with open(markdown_filename, "a") as md_file:
        md_file.write(markdown_content)

print("Markdown files created successfully in the 'markdown' directory.")
