# File 2: Append sentiment scores to the csv

import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Function to analyze sentiment using VADER
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score['compound']  # Returning the compound score

# Read data from the existing CSV file
filename = 'LLM_responses.csv'
with open(filename, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

# Analyze sentiment and append scores
updated_data = []
for row in data[1:]:  # Skipping the header row
    response = row[3]  # Assuming the response is in the fourth column
    sentiment_score = analyze_sentiment(response)
    updated_row = row + [sentiment_score]
    updated_data.append(updated_row)

# Write the updated data back to the CSV file with an additional column for sentiment scores
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(data[0] + ['Sentiment Score'])  # Writing the header with an additional column
    writer.writerows(updated_data)

print("Sentiment scores appended to the CSV file.")
