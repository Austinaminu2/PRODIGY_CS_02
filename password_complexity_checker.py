import re

def check_password_complexity(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r"[A-Z]", password) is not None
    lower_criteria = re.search(r"[a-z]", password) is not None
    number_criteria = re.search(r"[0-9]", password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, number_criteria, special_criteria ])

    if criteria_met == 5:
        return ("Strong Password")
    elif 3 <= criteria_met < 5:
        return ("Moderate Password")
    else:
        return ("Weak Password")

password = input("Enter a password to check it complexity: ")
complexity = check_password_complexity(password)
print(f"Password complexity : {complexity}")