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
    "8": "sleep_early",
    "9": "studying",
    "10": "homework",
    "11": "gym",
    "12": "watching_series-movies",
    "13": "computer_science",
    "14": "nature",
    "15": "linux_stuff",
    "16": "social_media",
    "17": "school",
    "18": "travel",
    "19": "shopping",
}

good_emotions = {
    "calm",
    "balanced",
    "content",
    "happy",
    "comfortable",
    "excited",
    "optimistic",
    "energized",
    "motivated",
    "focused",
    "inspired",
    "hopeful",
    "enthusiastic",
    "proud",
    "grateful",
    "loved",
    "relieved",
    "satisfied",
    "thankful",
    "appreciated",
    "supported",
    "connected",
    "productive",
}

neutral_emotions = {
    "bored",
    "tired",
    "uneasy",
    "concerned",
    "confused",
    "heard",
    "nervous",
}

bad_emotions = {
    "unmotivated",
    "frustrated",
    "disappointed",
    "annoyed",
    "depressed",
    "irritated",
    "sad",
    "angry",
    "exhausted",
    "fragile",
    "hopeless",
    "insecure",
    "overwhelmed",
    "pessimistic",
    "stressed",
    "vulnerable",
    "weak",
}


def classify_emotion(emotion):
    if emotion in good_emotions:
        return f"#emotions/good/{emotion}"
    elif emotion in neutral_emotions:
        return f"#emotions/neutral/{emotion}"
    elif emotion in bad_emotions:
        return f"#emotions/bad/{emotion}"
    else:
        return f"#emotions/unknown/{emotion}"


for item in data["items"]:
    date = item["date"]
    markdown_filename = os.path.join(output_directory, f"{date}.md")

    markdown_content = f"**Overall Mood:** #mood/{item['rating']}\n\n"

    emotions = [classify_emotion(emotion) for emotion in item["emotions"]]
    markdown_content += f"**Emotions:** {', '.join(emotions)}\n\n"

    tags = [
        tag_mapping[tag["id"]]
        for tag in item.get("tags", [])
        if tag["id"] in tag_mapping
    ]
    tag_tags = [f"#activities/{tag}" for tag in tags]
    markdown_content += (
        f"**Activities:** {', '.join(tag_tags) if tag_tags else 'No tags provided'}\n\n"
    )

    markdown_content += (
        f"**Message:**\n{item.get('message', 'No message provided')}\n\n"
    )

    with open(markdown_filename, "a") as md_file:
        md_file.write(markdown_content)

print("Markdown files created successfully in the 'markdown' directory.")
