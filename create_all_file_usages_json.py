# ... (truncated) ...
import requests
import json

# Define API parameters
params = {
    "action": "query",
    "list": "allfileusages",  # Get all file usages
    "afunique": "",  # Retrieve unique file usages
    "aflimit": "max",  # Get the maximum number of results per request
    "format": "json"  # Output in JSON format
}

all_file_usages = []  # Store all file usages here
next_request_params = {}  # Store the API's continuation parameters
total_files = 0  # Track the total number of files retrieved

# Keep making requests until all file usages are retrieved
while True:
    # Send request to the API
    print(f"Sending request to the API... (Total files retrieved so far: {total_files})")
    response = requests.get(api_url, params={**params, **next_request_params})
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful!")
    else:
        print(f"Request failed! HTTP Status Code: {response.status_code}")
        break

    # Parse the JSON response
    data = response.json()

    # Accumulate the file usages retrieved
    file_usages_in_response = len(data['query']['allfileusages'])
    all_file_usages.extend(data['query']['allfileusages'])
    total_files += file_usages_in_response

    # Provide feedback on the number of file usages retrieved
    print(f"{file_usages_in_response} file usages retrieved. Total files so far: {total_files}")

    # Check if the API has a "continue" parameter to get more data
    if 'continue' in data:
        next_request_params = data['continue']

# New function to fetch and log PRs related to PartDesign Workbench features

def fetch_partdesign_prs():
    pr_url = 'https://api.github.com/repos/FreeCAD/FreeCAD/pulls'
    response = requests.get(pr_url)
    if response.status_code == 200:
        prs = response.json()
        with open('partdesign_prs.json', 'w', encoding='utf-8') as f:
            json.dump(prs, f, ensure_ascii=False, indent=4)
        print('Fetched and saved PartDesign PRs successfully.')
    else:
        print(f'Failed to fetch PRs! HTTP Status Code: {response.status_code}')

# Call the new function to fetch PRs
fetch_partdesign_prs()
# ... (truncated) ...