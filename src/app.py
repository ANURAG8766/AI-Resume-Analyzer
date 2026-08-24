import streamlit as st
import matplotlib.pyplot as plt

import os
from resume_parser import extract_text
from ats_score import calculate_score, skills
from interview_questions import generate_questions
from job_recommender import recommend_roles
from resume_ranker import rank_resume
from ai_feedback import get_ai_feedback

# PASTE YOUR GEMINI API KEY HERE

API_KEY = os.getenv("GEMINI_API_KEY")

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

    score, found_skills = calculate_score(text)

    rank = rank_resume(score)

    missing_skills = [
        skill for skill in skills
        if skill not in found_skills
    ]

    st.subheader("📊 ATS Score")

    st.progress(score / 100)

    st.metric(
        label="Resume Score",
        value=f"{score}%"
    )

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
        "",
        text,
        height=300
    )