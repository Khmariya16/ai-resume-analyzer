from flask import Flask, render_template, request
import os

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from similarity import calculate_similarity, recommend_skills, resume_suggestions, ats_keyword_scan


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

# create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["resume"]
    job_description = request.form["job_description"]

    # save uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # extract text from resume
    resume_text = extract_resume_text(filepath)

    # extract skills
    resume_skills = extract_skills(resume_text)
    

    # calculate similarity
    score = calculate_similarity(resume_text, job_description)

    # example missing skills (you can improve later)
    missing_skills = recommend_skills(resume_text, job_description)

    # suggestions based on score
    suggestion = resume_suggestions(score, missing_skills)
    
    
    found_keywords, missing_keywords = ats_keyword_scan(resume_text, job_description)
    
    return render_template(
        "index.html",
        score=score,
        skills=resume_skills,
        missing_skills=missing_skills,
        suggestion=suggestion,
        found_keywords=found_keywords,
        missing_keywords=missing_keywords
        
    )


if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
# Runs web app
# connects all modules
