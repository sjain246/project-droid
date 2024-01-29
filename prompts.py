from datetime import datetime
# File specifying all prompts to be used in generating ticket fields via ChatGPT's completions API

# Prompt specifying the system (GPT's) role
def system_prompt():
    return "You will be given a title of an engineering task and will be tasked with creating various fields of the corresponding ticket. Respond as if you are an engineer raising the issue or a product manager requesting a new feature. Please be brief yet precise in your responses."

# Prompt to derive description from ticket title
def description_prompt(title):
    return "Give me a paragraph (no more than 5 sentences) expanded description of the task with the title:" + title

# Prompt to derive acceptance criteria from ticket title
def acceptance_prompt(title):
    return "Please define the acceptance criteria. In other words, please describe (in no more than 5 sentences) in a measurable and specific manner what functionality and behavior is expected from this task: " + title

# Prompt to derive assumptions relevant to engineering task specified by given title
def assumptions_prompt(title):
    return "Please define the assumptions relevant to the following task. In particular, what can the engineer assume about the end user's behavior, environment, and the provided data format for the task: " + title

# Prompt to derive type of the engineering task specified by given title
def type_prompt(title):
    return "In one word, please state whether the task with the following title is a BUG or FEATURE: " + title

# Prompt to derive labels of the engineering task specified by given title
def labels_prompt(title):
    return "Please provide any labels or tags (each 1-2 words, no more than 4 labels/tags) that might be relevant to the task with the following title. Each label/tag should be seperated by a comma :" + title

# Prompt to derive reproduction steps for a BUG engineering task specified by given title
def reproduction_prompt(title):
    return "The following task indicates a bug, so please provide steps to reproduce the bug, including environment details, detailed description to derive the bug, and expected & actual behavior: " + title

# Prompt to derive priority for engineering task specified by given title
def priority_prompt(title):
    return "In one word, please state whether the task with the following title is HIGHEST, HIGH, LOW, or LOWEST priority: " + title

# Prompt to derive due date for engineering task specified by given title
def due_date_prompt(title, priority):
    # Get the current date
    current_date = datetime.now()
    # Format the current date as YYYY-MM-DD
    formatted_date = current_date.strftime('%Y-%m-%d')
    return "Based on the fact that the priority of the following task is " + priority + "and the current date is " + formatted_date + ", please indicate a due date in YYYY-MM-DD format. Only provide the date, nothing else: " + title