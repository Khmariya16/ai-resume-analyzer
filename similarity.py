from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import re

skills = pd.read_csv("skills.csv", header=None)[0].tolist()


def calculate_similarity(resume_text, job_description):

    text = [resume_text, job_description]

    cv = CountVectorizer()

    matrix = cv.fit_transform(text)

    similarity_score = cosine_similarity(matrix)[0][1]

    return round(similarity_score * 100, 2)


def recommend_skills(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    resume_skills = []
    job_skills = []

    for skill in skills:

        skill_lower = skill.lower()

        if skill_lower in resume_text:
            resume_skills.append(skill)

        if skill_lower in job_description:
            job_skills.append(skill)

    missing = list(set(job_skills) - set(resume_skills))

    return missing


def resume_suggestions(score, missing_skills):

    suggestions = []

    if score < 30:
        suggestions.append("Your resume needs improvement. Add more relevant skills from the job description.")

    elif score < 60:
        suggestions.append("Your resume partially matches the job description.")

    else:
        suggestions.append("Good match! Your resume aligns well with the job description.")

    if missing_skills:
        suggestions.append("Add these important skills: " + ", ".join(missing_skills))

    suggestions.append("Include quantified achievements (e.g., improved system efficiency by 20%).")

    suggestions.append("Add relevant project experience related to the job role.")

    suggestions.append("Use strong action verbs like developed, implemented, optimized.")

    return suggestions


def ats_keyword_scan(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    found_keywords = []
    missing_keywords = []

    for skill in skills:

        skill_lower = skill.lower()

        # check if skill exists in job description
        if skill_lower in job_description:

            # check if resume contains it
            if skill_lower in resume_text:
                found_keywords.append(skill)

            else:
                missing_keywords.append(skill)

    return found_keywords, missing_keywords