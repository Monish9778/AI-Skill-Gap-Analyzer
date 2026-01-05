def generate_resume_tips(resume_text, missing_skills):
    tips = []

    if "skills" not in resume_text:
        tips.append("Add a dedicated SKILLS section.")

    if len(resume_text.split()) < 300:
        tips.append("Resume content is too short. Add project details.")

    for skill in missing_skills:
        tips.append(f"Include projects or experience related to {skill}.")

    return tips
