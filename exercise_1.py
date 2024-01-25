# File 1: Prompt and elicit response from OPENAI API and store in csv.

from openai import OpenAI
import csv
import random
import datetime
import os
import personas_and_topics

# Check Working Directory
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Ensure the CSV file is prepared with header
filename = 'LLM_responses.csv'
if not os.path.isfile(filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Persona Description', 'Prompt', 'Response'])

# Function to store data in a CSV file
def store_data(filename, persona_description, prompt, response):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now(), persona_description, prompt, response])

# Function to get a response from the OpenAI API
def get_response(prompt):
    try:
        response = client.completions.create(
          model="gpt-3.5-turbo-instruct",  # or another model
          prompt=prompt,
          max_tokens=200
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to generate a prompt
def generate_prompt(persona, topic):
    return (f"As a {persona['age']}-year-old {persona['description']} interested in "
            f"{persona['interests']}, I'm looking for advice on {topic}.")

# Generate prompts and responses for each persona and store them
for persona in personas_and_topics.personas:
    random.shuffle(personas_and_topics.topics)  # Shuffle the topics for each persona
    for topic in personas_and_topics.topics:
        prompt = generate_prompt(persona, topic)
        response = get_response(prompt)
        store_data(filename, persona['description'], prompt, response)

print("Data generation complete. Check the CSV file for all the prompts and responses.")