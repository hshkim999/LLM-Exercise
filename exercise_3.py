# File 3: Build visualization

import pandas as pd
import matplotlib.pyplot as plt
from personas_and_topics import personas

# Function to map persona description to age
def get_age_from_description(description):
    for persona in personas:
        if persona['description'] == description:
            return persona['age']
    return None

# Read the updated CSV file into a pandas DataFrame
filename = 'LLM_responses.csv'
df = pd.read_csv(filename)
df['Age'] = df['Persona Description'].apply(get_age_from_description)

# Convert the 'Sentiment Score' to a numeric type for plotting
df['Sentiment Score'] = pd.to_numeric(df['Sentiment Score'], errors='coerce')

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Sentiment Score'], alpha=0.5)
plt.title('Age vs Sentiment Score')
plt.xlabel('Age')
plt.ylabel('Sentiment Score')
plt.grid(True)
plt.savefig('Age_vs_Sentiment_Score.png', bbox_inches='tight')
plt.show()