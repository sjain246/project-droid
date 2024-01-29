Setup:
Please setup a python virtual environment (potentially using venv) and install the 
following dependencies if not already present:
1. datetime
2. openai
3. load-dotenv
4. requests

Create an OpenAI account if you don't already have one and ensure you have enough credits 
to make requests.
Add a .env file that will contain a line with your OpenAI API Key:
OPENAI_API_KEY=<key goes here>

Now you are setup!
Invoke the program with the following structure:
python3 droid.py "<Title of engineering task>"
Note that the program enforces that this engineering task title must be at least 3 words and 
10 characters to ensure proper output.

The resulting task will be outputted to the task.json file in the format of the request body payload
that can be passed to the JIRA Create Issue API (https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post) to create a JIRA task/issue.
Specifically, the following fields are included in this payload:
1. summary --> The title provided to the program
2. description --> Detailed description of the task
3. acceptance_criteria --> Acceptance criteria for the task
4. assumptions --> Assumptions for the task
5. labels --> Any relevant labels for the task
6. priority --> Priority of the task (Highest, High, Low, Lowest)
7. issuetype --> Type of the task (Bug, Feature, Task)
8. duedate --> Due date of the task in YYYY-MM-DD format
9. reproductionsteps --> Steps to reproduce the bug (Will only exist for bug tasks)

Additionally, for each created ticket, the GPT generated output for each field will be logged
to the gptlogger.txt file to enable easier access of individual field outputs.

Error Handling/Input Validation:
1. The program enforces that this engineering task title must be at least 3 words and 
10 characters to ensure proper output.
2. Any error while generating GPT output is caught and handled
3. Any error while setting up OpenAI client is caught and handled
4. Output validations are performed for many GPT outputted fields of the JIRA task. For example,
we check to ensure the tasktype is indeed among Bug and Feature, and otherwise we set it to 
the generic Task type.
5. Catching ValueError if GPT outputted due date is in the wrong format when checking using
datetime module.

(Optional) Connecting to JIRA:

Unfortunately, I was unable to completely connect to JIRA as I was getting JIRA API-related errors
and was subject to restricted time availability. However, if you wish to try to connect to JIRA and 
create a corresponding ticket with the generated request body, please comment out the code in the main
function of droid.py and perform the following configurations: 

Add the following parameters to the .env file:
1. ATLASSIAN_DOMAIN  --> The domain of your Atlassian account
2. ATLASSIAN_EMAIL --> The email you use to login to your Atlassian account
3. ATLASSIAN_API_KEY --> The API Key for your Atlassian account
4. PROJECT_KEY --> The project key for the project in which you wish to add the task

In Jira/Atlassian Settings, for your current project, add the Issue Types for Bug and Feature. 
Ensure that they are connected to the Jira project where you would like the Issues to be created.
Additionally, create the following custom Issue fields:
1. Acceptance Criteria - Paragraph (supports rich text)
2. Assumptions - Paragraph (supports rich text)
3. Reproduction Steps - Paragraph (supports rich text)

Associate all custom Issue fields to the appropriate screens as desired, or all screens to ensure
it will appear everywhere. Ensure that these fields are connected to the Jira project where you
would like the Issues to be created.

The following Issue fields should exist by default (ensure that they do):
1. Project
2. Issue Type
3. Summary
4. Due Date
5. Description
6. Priority
7. Labels

Ensure you have the required permissions to create a JIRA Issue by going into the project settings
and checking to ensure you have Create Issues permissions. 
