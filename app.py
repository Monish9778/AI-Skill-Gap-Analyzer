import streamlit as st
from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.skill_gap_analyzer import analyze_skill_gap
from utils.resume_tips import generate_resume_tips
from utils.email_sender import send_email

st.title("AI Skill Gap Analyzer (Automation-Based)")

email = st.text_input("Enter your email")
company = st.selectbox("Select Company", ["TCS", "Infosys"])
role = st.selectbox("Select Role", ["Python Developer"])

uploaded_file = st.file_uploader("Upload Resume (PDF)")

if st.button("Analyze") and uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    user_skills = extract_skills(resume_text)

    matched, missing, optional_missing, score = analyze_skill_gap(
        user_skills, company, role
    )

    tips = generate_resume_tips(resume_text, missing)

    st.subheader("Results")
    st.write("Matched Skills:", matched)
    st.write("Missing Skills:", missing)
    st.write("Job Readiness Score:", score)

    email_content = f"""
    <h2>Skill Gap Report</h2>
    <p><b>Score:</b> {score}%</p>
    <p><b>Matched:</b> {', '.join(matched)}</p>
    <p><b>Missing:</b> {', '.join(missing)}</p>
    <p><b>Tips:</b></p>
    <ul>
    {''.join(f'<li>{t}</li>' for t in tips)}
    </ul>
    """

    send_email(email, "Your Skill Gap Analysis Report", email_content)
    st.success("Analysis completed & email sent successfully!")
