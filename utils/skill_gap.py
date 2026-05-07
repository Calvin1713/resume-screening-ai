def load_skills(file_path):

    with open(file_path, 'r') as file:
        skills = [
            line.strip().lower()
            for line in file.readlines()
        ]

    return skills


def skill_analysis(
    resume_text,
    job_description,
    skills_list
):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    matched_skills = []
    missing_skills = []

    for skill in skills_list:

        if (
            skill in resume_text
            and skill in job_description
        ):
            matched_skills.append(skill)

        elif (
            skill in job_description
            and skill not in resume_text
        ):
            missing_skills.append(skill)

    return matched_skills, missing_skills