import requests
import re

from utils.helpers import generate_user_registration_data

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36'})
resp = session.get('https://nop-qa.portnov.com/register')

# name=__RequestVerificationToken type=hidden value=CfDJ8MKnMKoNeiNNsJ9ht1yMURoJnyPzX-UyhRBfJt2-B6UflvfocMYAu2IOAY6jrpPEU5NqnbkibOcyaaVCYBMJUlDu0ld0vfTX5iAB3D7mSOfasP3ovQm7ahR0U4ldZo74-9gzGamsLTS6MyY_Bc0PvL4
token_value = re.search(r'name=__RequestVerificationToken type=hidden value=(.+?)>', resp.text).group(1)

user = generate_user_registration_data()
payload = {
"Gender": "F",
"FirstName": user.first_name,
"LastName": user.last_name,
"DateOfBirthDay": user.birth_date.day,
"DateOfBirthMonth": user.birth_date.month,
"DateOfBirthYear": user.birth_date.year,
"Email": user.email,
"Company": user.company,
"Newsletter": "false",
"Password": user.password,
"ConfirmPassword": user.password,
"__RequestVerificationToken": token_value
}

print(user.email, user.password)

registration_response = session.post('https://nop-qa.portnov.com/register', data=payload)
pass