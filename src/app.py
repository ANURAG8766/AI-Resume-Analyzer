import streamlit as st
import matplotlib.pyplot as plt

import os
from resume_parser import extract_text
from ats_score import calculate_score, skills
from interview_questions import generate_questions
from job_recommender import recommend_roles
from resume_ranker import rank_resume
from ai_feedback import get_ai_feedback
import pandas as pd

# PASTE YOUR GEMINI API KEY HERE

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    try:
        API_KEY = st.secrets["GEMINI_API_KEY"]
    except:
        API_KEY = None

st.set_page_config(
    page_title="AI Resume Analyzer & Interview Coach",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer & Interview Coach")

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text(uploaded_file)
    word_count = len(text.split())
    char_count = len(text)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Words", word_count)

    with col2:
        st.metric("Characters", char_count)

    score, found_skills = calculate_score(text)

    rank = rank_resume(score)

    missing_skills = [
        skill for skill in skills
        if skill not in found_skills
    ]

    st.subheader("📊 ATS Score")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ATS Score", f"{score}%")

    with col2:
        st.metric("Skills Found", len(found_skills))

    with col3:
        st.metric("Missing Skills", len(missing_skills))
    st.progress(score / 100)


    st.subheader("🏆 Resume Rank")
    st.success(rank)

    st.subheader("✅ Detected Skills")

    if found_skills:
        for skill in found_skills:
            st.write(f"✅ {skill}")
    else:
        st.write("No skills detected.")

    st.subheader("❌ Missing Skills")

    for skill in missing_skills:
        st.write(f"❌ {skill}")

    st.subheader("💡 Suggestions")

    if score < 50:
        st.warning(
            "Add more projects, certifications, internships and technical skills."
        )
    elif score < 75:
        st.info(
            "Good resume. Add more industry-relevant skills to improve ATS score."
        )
    else:
        st.success(
            "Excellent ATS score. Resume is well optimized."
        )

    st.subheader("🎯 Interview Questions")

    questions = generate_questions(found_skills)

    if questions:
        for q in questions:
            st.write(f"👉 {q}")

    st.subheader("🚀 Recommended Career Roles")

    roles = recommend_roles(found_skills)

    for role in roles:
        st.write(f"🎯 {role}")

    st.subheader("📈 Skill Analytics")

    present = len(found_skills)
    missing = len(missing_skills)

    fig, ax = plt.subplots()

    ax.pie(
        [present, missing],
        labels=["Detected", "Missing"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

    st.subheader("🤖 AI Resume Feedback")

    try:
        feedback = get_ai_feedback(
            text,
            API_KEY
        )

        st.write(feedback)

    except Exception as e:
        st.error(
            f"AI Feedback Error: {e}"
        )

    st.subheader("📄 Resume Preview")

    st.text_area(
        "Resume Text",
        text,
        height=300
    )
    st.download_button(
    "Download Feedback",
    feedback,
    file_name="resume_feedback.txt"
)
    st.sidebar.title("AI Resume Analyzer")

    st.sidebar.info(   

"""
Built by Anurag Yadav

B.Tech AIML
ADGIPS
"""
)