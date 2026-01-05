# AI-Skill-Gap-Analyzer


An intelligent automation system that analyzes a user’s resume, compares it with company-specific job requirements, identifies skill gaps, provides resume improvement tips, generates a learning roadmap, and sends a clear report via email.

---

## Problem
Freshers and job seekers often do not know:
- What skills companies expect
- Why their resume gets rejected
- What exactly to learn next

---

## Solution
This project automatically compares **user skills vs company expectations** using NLP and rule-based analysis, then provides clear guidance and recommendations.

---

## Features
- Resume parsing (PDF)
- NLP-based skill extraction
- Company & role-based skill analysis
- Skill gap detection
- Job readiness score
- Resume & ATS improvement tips
- Learning roadmap
- Automated email report

---

## Tech Stack
- Python
- Streamlit
- spaCy (NLP)
- JSON datasets
- SMTP Email Automation

---

## Workflow
Upload Resume → Extract Skills → Analyze Company Needs → Detect Skill Gaps → Generate Tips & Roadmap → Send Email Report

---

## How to Run
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
