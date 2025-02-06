# ai-talent-matcher
 AI Talent Matcher using Python, Flask, and Scikit-learn. This prototype will include:

A basic Flask API for talent matching
A sample dataset (community members with skills and performance history)
K-means clustering to group similar talents
A recommendation engine to suggest the best team members for a given project



## Folder Structure

![image](https://github.com/user-attachments/assets/3c2fbf1e-8405-47fc-8e70-afd473ec346f)


## Running the Demo

A. Install Dependencies
> pip install flask pandas scikit-learn

B. Start Flask App
> python main.py

C. Test API with a Sample Request

> curl -X POST "http://127.0.0.1:5000/match" -H "Content-Type: application/json" -d '{"skills": ["Python", "ML"]}'


D. Expected JSON Response


{
  "matches": [
    {"name": "Alice", "skills": "Python;ML", "performance": 4.5},
    {"name": "Dave", "skills": "Python;DataScience", "performance": 4.7}
  ]
}
________________________________________

E. Containerization (Dockerfile)

FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]



