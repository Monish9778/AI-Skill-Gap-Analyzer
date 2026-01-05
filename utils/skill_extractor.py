import json
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills(resume_text):
    with open("data/skills.json") as f:
        skills_db = json.load(f)

    doc = nlp(resume_text)
    found_skills = set()

    for token in doc:
        if token.text.lower() in skills_db:
            found_skills.add(token.text.lower())

    return found_skills
