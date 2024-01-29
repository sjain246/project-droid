from completions import *
# File specifying all methods to generate request body for JIRA ticket request

# Method to generate request body for paragraph JIRA field
def generate_paragraph(text):
    return {"content": [{"content": [{"text": text, "type": "text"}], "type": "paragraph"}], "type": "doc", "version": 1} 

# Build the JSON payload for the JIRA Issue Request
def build_task(client, title, project_key):
    payload = {
        "update": {}
    }
    fields = {}
    # Opening and printing to logger file to keep track of all GPT output
    with open("gptlogger.txt", "a") as logger_file:

        logger_file.write("Starting GPT log for task with title: " + title)

        description = generate_description(client, title)
        logger_file.write("Generated Description: \n" + description)
        fields["description"] = generate_paragraph(description)

        acceptance = generate_acceptance(client, title)
        logger_file.write("Generated Acceptance: \n" + acceptance)
        fields["acceptancecriteria"] = generate_paragraph(acceptance)

        assumptions = generate_assumptions(client, title)
        logger_file.write("Generated Assumptions: \n" + assumptions)
        fields["assumptions"] = generate_paragraph(assumptions)

        labels = generate_labels(client, title)
        logger_file.write("Generated Labels: \n" + str(labels))
        fields["labels"] = labels

        priority = generate_priority(client, title)
        logger_file.write("Generated Priority: \n" + priority)
        fields["priority"] = {"name": priority}

        task_type = generate_type(client, title)
        logger_file.write("Generated Type: \n" + task_type)
        fields["issuetype"] = {"name": task_type}

        due_date = generate_due_date(client, title, priority)
        logger_file.write("Generated Due Date: \n" + due_date)
        # Ensure that due date is not an empty string (i.e. it was properly generated)
        if due_date:
            fields["duedate"] = due_date
        
        if task_type == "Bug":
            reproduction = generate_reproduction(client, title)
            logger_file.write("Generated Reproduction Steps: \n" + reproduction)
            fields["reproductionsteps"] = generate_paragraph(reproduction)
        
        fields["summary"] = title
        if project_key:
            fields["project"] = {"key": project_key}
        payload["fields"] = fields

    return payload

