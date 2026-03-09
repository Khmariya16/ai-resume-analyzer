import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

skills = pd.read_csv("skills.csv", header=None)[0].tolist()


def extract_skills(resume_text):

    resume_text = resume_text.lower()

    doc = nlp(resume_text)

    tokens = [token.text for token in doc]

    found_skills = []

    for skill in skills:

        skill_lower = skill.lower()

        if skill_lower in tokens or skill_lower in resume_text:

            found_skills.append(skill)

    return list(set(found_skills))