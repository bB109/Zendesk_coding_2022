import requests
import json
from auth import get_email, get_pwd, get_domain

# Set the request parameters
domain = ""
email = ""
pwd = ""

# Update the requst parameters
def update_account():
    global domain
    global email
    global pwd
    domain = f"https://{get_domain()}.zendesk.com/api/v2"
    email = get_email()
    pwd = get_pwd()

# Get request data
def get_data(url):
    response = requests.get(url, auth=(email, pwd))
    response.raise_for_status()
    return response.json()

# Get the json data for list of tickets
def get_ticket_list(page_number):
    page_size = 25
    url = f"{domain}/tickets.json?per_page={page_size}&page={page_number}"
    return get_data(url)

# Get the json data for one ticket
def get_ticket_detail(ticket_id):
    url = f"{domain}/tickets/{ticket_id}.json"
    return get_data(url)

# Convert json list data to dictionary
def dict_ticket_list(data):
    tickets = [dict_ticket_detail(t, True) for t in data["tickets"]]
    return tickets

# Convert json detail data to dictionary
def dict_ticket_detail(data, isList):
    if isList is False:
        data = data["ticket"]
    
    ticket = {
    "ID": data["id"],
    "Status": data["status"],
    "Priority": data["priority"],
    "Due_at": data["due_at"],
    "Recipient": data["recipient"],
    "Subject": data["subject"],
    "Description": data["description"],
    "Tags": data["tags"],
    "Created_at": data["created_at"],
    "Requester_id": data["requester_id"],
    "URL": data["url"]
    }
    return ticket