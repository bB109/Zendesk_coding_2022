import click

user_email = ""
user_pwd = ""
user_domain = ""

# updates the global variable
def get_account_info():
	global user_email
	global user_pwd
	global user_domain
	user_email = click.prompt("Please enter your email")
	user_pwd = click.prompt("Please enter your password")
	user_domain = click.prompt("Please enter your sub-domain. (i.e. if your subdomain is xxx.zendesk.com, please enter xxx)")

# using get functions to prevent other file from modifying the information
def get_email():
	return user_email


def get_pwd():
	return user_pwd


def get_domain():
	return user_domain