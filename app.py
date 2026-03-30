from flask import Flask, render_template, request
import os
from utils.analyzer import extract_text, analyze_resume

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    skills = []

    if request.method == "POST":
        file = request.files["resume"]
        job_desc = request.form["job_desc"]

        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        text = extract_text(path)
        score, skills = analyze_resume(text, job_desc)

    return render_template("index.html", score=score, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)
