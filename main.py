# resume_builder/main.py

from utils.validator import validate_email, validate_phone
from utils.pdf_generator import generate_pdf
import json

def main():
    print(" Welcome to the Resume Builder!\n")

    name = input("Enter your full name: ")
    email = input("Enter your email: ")
    while not validate_email(email):
        print("❌ Invalid email format. Try again.")
        email = input("Enter your email: ")

    phone = input("Enter your phone number: ")
    while not validate_phone(phone):
        print("❌ Invalid phone number. Try again.")
        phone = input("Enter your phone number: ")

    linkedin = input("LinkedIn URL: ")
    github = input("GitHub URL: ")
    objective = input("Write your career objective: ")

    print("\n💡 Enter your skills (comma separated):")
    skills = [s.strip() for s in input().split(",")]

    print("\n🎓 Enter your education (type 'done' to stop):")
    education = []
    while True:
        degree = input("Degree: ")
        if degree.lower() == "done":
            break
        institution = input("Institution: ")
        year = input("Year: ")
        education.append({"degree": degree, "institution": institution, "year": year})

    print("\n🛠️ Enter your projects (type 'done' to stop):")
    projects = []
    while True:
        title = input("Project title: ")
        if title.lower() == "done":
            break
        desc = input("Description: ")
        projects.append({"title": title, "description": desc})

    print("\n💼 Enter your work experience (type 'done' to stop):")
    experience = []
    while True:
        title = input("Job Title: ")
        if title.lower() == "done":
            break
        company = input("Company: ")
        duration = input("Duration: ")
        experience.append({"title": title, "company": company, "duration": duration})

    resume = {
        "name": name,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "github": github,
        "objective": objective,
        "skills": skills,
        "education": education,
        "projects": projects,
        "experience": experience,
    }

    with open("resume.json", "w") as f:
        json.dump(resume, f, indent=4)

    generate_pdf(resume, "resume.pdf")
    print("\n✅ Resume generated successfully as resume.pdf!")

if __name__ == "__main__":
    main()
