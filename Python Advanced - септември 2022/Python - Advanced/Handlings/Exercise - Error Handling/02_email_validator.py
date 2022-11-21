# import module
import re


# creating classes with a built-in argument "Exception" for all non-exit exceptions.
class NameTooShort(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


# regex pattern with the given valid domains
pattern = r'([\w\.\_]{5,})@(\w+)\.(com|bg|net|org)\b'
valid_domains = ['com', 'bg', 'org', 'net']

# additional data statements
while True:
    email = input()
    if email == "End":
        break

    valid = re.findall(pattern, email)

    if valid:
        print(email)
    else:
        if '@' not in email:
            raise MustContainAtSymbolError("Email must contain @")

        username = email[:email.index('@')]
        mail_server = email[email.index('@') + 1:email.index('.', email.index(
            '@'))]  # --> tracking the mail server with a slice notation from the '@' + 1(step forward) index to the
        #  domain dot index with an optional argument to search after the '@' in case of '.' in the username
        domain = email[email.index(mail_server[-1]) + 2:]

        if len(username) < 5:
            raise NameTooShort("Name must be more than 4 characters")
        if domain not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
