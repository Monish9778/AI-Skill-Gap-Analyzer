import json

def analyze_skill_gap(user_skills, company, role):
    with open("data/companies.json") as f:
        companies = json.load(f)

    role_data = companies[company][role]

    mandatory = set(role_data["mandatory"])
    optional = set(role_data["optional"])

    matched = user_skills & mandatory
    missing = mandatory - user_skills
    optional_missing = optional - user_skills

    score = int((len(matched) / len(mandatory)) * 100)

    return matched, missing, optional_missing, score
