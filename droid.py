from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv
from request_body import *
import json
import requests
from requests.auth import HTTPBasicAuth
import sys

# Validate the input by ensuring provided title has at least 3 words and 10 characters
def validate_input(input):
    return len(input.split()) >= 3 and len(input) > 10

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 droid.py 'Engineering task title with at least 3 words, 10 characters'")
        sys.exit(1)
    
    title = sys.argv[1]

    # Validate the provided title
    if not validate_input(title):
        print("Error: Provided title must have at least 3 words and 10 characters.")
        sys.exit(1)


    # Ensure OpenAI client and env variables are loaded in properly
    try:
        load_dotenv()
        # Will utilize key labeled in .env file as OPENAI_API_KEY
        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

        payload = json.dumps(build_task(client, title, ""), indent=4)

        with open("task.json", "w") as json_file:
            json_file.write(payload)

        # Utilize the following commented code if you wish to connect and create ticket in JIRA

        # url = "https://" + os.environ.get("ATLASSIAN_DOMAIN") +".atlassian.net/rest/api/3/issue"
        
        # login_email = os.environ.get("ATLASSIAN_EMAIL")
        # atlassian_api_key = os.environ.get("ATLASSIAN_API_KEY")
        # auth = HTTPBasicAuth(login_email, atlassian_api_key)

        # headers = {
        #     "Accept": "application/json",
        #     "Content-Type": "application/json"
        # }
        # # Generate the payload using build_task (which utilizes ChatGPT to generate the fields of the
        # # issue)
        # project_key = os.environ.get("PROJECT_KEY")
        # payload = json.dumps(build_task(client, "Fix product price filter", project_key))

        # response = requests.request(
        #     "POST",
        #     url,
        #     data=payload,
        #     headers=headers,
        #     auth=auth
        # )

        # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    except OpenAIError as e:
        print("OpenAI API Client Setup Error:", e)
    except Exception as e:
        print("Error generating task:", e)