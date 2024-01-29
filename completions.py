# File specifying all completions API calls to be used in generating ticket fields via ChatGPT's completions API
from prompts import *
from openai import OpenAIError
from datetime import datetime

# General method for creating a completion from given prompt to generate ticket field and provided OpenAI client
def generate_completion(client, prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt()},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except OpenAIError as e:
        print("OpenAI API Error while generating completion:", e)
    except Exception as e:
        print("An unexpected error occurred while generating OpenAI completion:", e)

# Method to generate description of task given title
def generate_description(client, title):
    return generate_completion(client, description_prompt(title))

# Method to generate acceptance critera of task given title
def generate_acceptance(client, title):
    return generate_completion(client, acceptance_prompt(title))

# Method to generate assumptions relevant to engineering task specified by given title
def generate_assumptions(client, title):
    return generate_completion(client, assumptions_prompt(title))

# Method to generate type of the engineering task specified by given title
def generate_type(client, title):
    task_type = generate_completion(client, type_prompt(title))
    # Ensure that task type is either bug or feature, otherwise set it to generic Task type
    if task_type.lower() != "bug" and task_type.lower() != "feature":
        return "Task"
    return task_type.title()

# Method to generate labels of the engineering task specified by given title
def generate_labels(client, title):
    labels = generate_completion(client, labels_prompt(title))
    # Split labels string by commas to form list of the different labels
    splitted_labels = labels.split(",")
    return splitted_labels

# Method to generate reproduction steps for a BUG engineering task specified by given title
def generate_reproduction(client, title):
    return generate_completion(client, reproduction_prompt(title))

# Method to generate priority for an engineering task specified by given title
def generate_priority(client, title):
    priority = generate_completion(client, priority_prompt(title))
    # Ensure that priority is either HIGHEST, HIGH, LOW, or LOWEST, otherwise default set it to Low
    if priority.lower() not in ["highest", "high", "low", "lowest"]:
        return "Low"
    return priority.title()

# Method to generate due date for engineering task specified by given title
def generate_due_date(client, title, priority):
    due_date = generate_completion(client, due_date_prompt(title, priority))
    # Ensure that returned date is in YYYY-MM-DD format, otherwise return empty string
    try:
        datetime.strptime(due_date, '%Y-%m-%d')
        return due_date
    except ValueError:
        return ""
