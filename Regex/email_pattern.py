import re
e_mail = input("Enter email: ")
with open('recognized_mails.txt', 'r') as file:
    recognized_domains = file.read().splitlines()  # Read all lines as a list
try:
    local_part, domain_part = e_mail.split('@', 1)
except ValueError:
    print("Invalid email format. Missing '@' symbol.")
    exit()
if domain_part not in recognized_domains:
    print(f"Adding domain {domain_part} to database.")
    recognized_domains.append(domain_part)
    with open("recognized_mails.txt", "a") as file1:
        file1.write(f'{domain_part}\n')

domain_pattern = '|'.join(re.escape(domain) for domain in recognized_domains)
pattern = rf'^[a-zA-Z0-9_.+-]+@({domain_pattern})$'

if re.match(pattern, e_mail):
    print("E-mail is valid.")
else:
    print("E-mail is invalid.")
