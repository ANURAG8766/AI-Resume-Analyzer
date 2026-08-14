skills = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "power bi",
    "tableau",
    "excel",
    "pandas",
    "numpy",
    "tensorflow",
    "pytorch",
    "data analysis",
    "nlp",
    "streamlit"
]

def calculate_score(text):

    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    score = (len(found_skills) / len(skills)) * 100

    return round(score, 2), found_skills