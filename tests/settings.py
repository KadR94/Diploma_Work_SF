import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
valid_phone = os.getenv('valid_phone')
valid_login = os.getenv('valid_login')
valid_ls = os.getenv('valid_ls')

invalid_email = os.getenv('invalid_email')
invalid_password = os.getenv('invalid_password')
invalid_phone = os.getenv('invalid_phone')
invalid_phone_short = os.getenv('invalid_phone_short')
invalid_login = os.getenv('invalid_login')
invalid_ls = os.getenv('invalid_ls')


new_valid_email = os.getenv('new_valid_email')
new_valid_phone = os.getenv('new_valid_phone')
new_valid_login = os.getenv('new_valid_login')
new_valid_ls = os.getenv('new_valid_ls')

name = os.getenv('name')
last_name = os.getenv('last_name')