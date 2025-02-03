import ollama
import os
import random


def load_previous_stories(file_path="previous_stories.txt"):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return [line.strip() for line in lines if not line.startswith("Here is a one-sentence summary of the story")]
    return []


def save_previous_story(summary, file_path="previous_stories.txt"):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(summary + "\n")


def save_story_to_file(story, file_path="story.txt"):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(story)


def save_story_theme(story_type, file_path="last_story_theme.txt"):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(story_type)


def determine_story_type():
    story_types = ["Personal Drama", "Scandals", "Relationship Stories", "mystery", "Humorous Mishaps", "Fictional Storytelling", "Time Travel"]
    return random.choice(story_types)


def chat_with_ollama(messages):
    response = ollama.chat(model='gemma2', messages=messages)
    return response['message']['content']


def clean_story(raw_story):
    unwanted_phrases = [
        "What do you think? Would you like me to continue the story or explore a different direction?",
        "Here's a science fiction story that I hope will captivate your attention:"
    ]
    for phrase in unwanted_phrases:
        raw_story = raw_story.replace(phrase, "").strip()
    return raw_story


def generate_story(story_type, previous_summaries):
    prompt = f"You are a creative storyteller. Write a {story_type} story that captivates attention. Avoid themes like these: {', '.join(previous_summaries)}. Keep the story relevant while also keeping the viewers attention."
    messages = [{"role": "system", "content": "You are a creative storyteller."}, {"role": "user", "content": prompt}]
    raw_story = chat_with_ollama(messages)
    return clean_story(raw_story)


def generate_story_summary(story):
    prompt = f"Summarize this story into one short sentence: {story}"
    messages = [{"role": "system", "content": "You are a summarization expert."}, {"role": "user", "content": prompt}]
    summary = chat_with_ollama(messages)
    return summary.strip()


def main():
    story_type = determine_story_type()
    previous_summaries = load_previous_stories()
    story = generate_story(story_type, previous_summaries)
    summary = generate_story_summary(story)
    save_story_to_file(story)
    save_previous_story(summary)
    save_story_theme(story_type)


if __name__ == "__main__":
    main()
