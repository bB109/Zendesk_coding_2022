import click
import sys
import json
from rich_dataframe import prettify
import pandas as pd
from auth import get_account_info, get_email
from tickets import get_ticket_list, get_ticket_detail, dict_ticket_list, dict_ticket_detail, update_account


# Print list of dict as table
def print_list(data):
	df = pd.DataFrame.from_dict(data)
	click.echo(df)

# Print detail using the default json pretty print
def print_detail(data):
	click.echo(json.dumps(data, indent=4, sort_keys=True))


click.echo("Welcome to the viewer.")
# Get user email, password, and subdomain information
get_account_info()
update_account()
click.echo("Type 'menu' to view options or 'quit' to exit.")
cmd = ""

# Keep asking for user input until user quit the program
while(True):
	cmd = click.prompt('Please enter a command')
	# Command menu
	if(cmd == 'menu'):
		click.echo("1) Press 1 to view all tickets.")
		click.echo("2) Press 2 to view the detail of specific ticket.")
	# Quit the porgam
	elif(cmd == "quit"):
		click.echo("Bye. Have a great day!")
		sys.exit()
	# User checks the ticket list
	elif(cmd == "1"):
		data = get_ticket_list(1)
		print_list(dict_ticket_list(data))
		while(True):
			page_number = click.prompt("Please enter a <page number> or <any other letter> to quit the tickets' list")
			try:
				val = int(page_number)
			except ValueError:
				break;
			page = get_ticket_list(page_number)
			print_list(dict_ticket_list(page))
	# User checks the details of a ticket
	elif(cmd == "2"):
		ticket_id = click.prompt("Please enter a ticket ID")
		ticket = get_ticket_detail(ticket_id)
		print_detail(dict_ticket_detail(ticket, False))
	# All other input are invalid
	else:
		click.echo("Invalid command.")
