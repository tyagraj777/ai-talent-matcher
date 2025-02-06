from flask import Flask, request, jsonify
from app.match import match_talent

app = Flask(__name__)

@app.route("/match", methods=["POST"])
def match():
    """Endpoint to find the best talent match for a project."""
    data = request.json
    project_skills = data.get("skills", [])
    matched_talents = match_talent(project_skills)
    return jsonify({"matches": matched_talents})

if __name__ == "__main__":
    app.run(debug=True)
