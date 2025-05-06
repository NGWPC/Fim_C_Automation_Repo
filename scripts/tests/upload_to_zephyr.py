import requests
import requests.auth import HTTPBasicAuth

JIRA_BASE_URL = 'https://jira.nextgenwaterprediction.com'
USERNAME = ""
PASSWORD = "
PROJECT_KEY = "NGWPC"
CYCLE_NAME = ""
VERSION_ID = "-1"

def upload_xml _results():
    url = f"{JIRA_BASE_URL}/rest/zapi/latest/import/execution/junit?projectKey={PROJECT_KEY}&versionId={VERSION_ID}&cycleName={CYCLE_NAME}"
    headers = {"Content-Type":"multipart/form-data"}

    with open("reslt.xml","rb") as file:
        files = {
            "file": ("results.xml", file, "application/xml")

        }
        response = requests.post(url, auth=HTTPBasicAuth(USERNAME,PASSWORD), files = files)
    if response.status_code == 200:
        print("Test results uploaded successfully")
    else:
        print(f"Upload unsuccessful due to {response.status_code}")
        print(response.text)    