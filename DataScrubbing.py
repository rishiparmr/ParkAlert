import openai
import os

openai.api_key = '*****'

# Read the text file
with open('output.txt', 'r') as f:
    text = f.read()

# Define the question
question = "Examine the provided parking ticket details and locate the due date and cost. If these elements are present, format your response as follows: 'Due Date: [due date], Cost: [cost]'. If either the due date or the cost is missing or cannot be identified, output the response as 'Due Date: N/A' or 'Cost: N/A' respectively. Please note that the due date is typically in the format MM/DD/YYYY and the cost is generally denoted with a dollar sign ($)." 

# Combine text with question
prompt = f"{text}\n{question}"

# Use OpenAI's API to get an answer
response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=150)

print(response.choices[0].text.strip())