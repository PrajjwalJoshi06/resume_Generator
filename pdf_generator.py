# resume_builder/utils/pdf_generator.py

from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        if os.path.exists("profile.jpg"):
            self.image("profile.jpg", 160, 10, 30)
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Resume", ln=True, align="C")
        self.ln(10)

    def section_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)

    def section_body(self, content):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, content)
        self.ln()

def generate_pdf(data, filename):
    pdf = PDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, data['name'], ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Email: {data['email']} | Phone: {data['phone']}", ln=True)
    pdf.cell(0, 10, f"LinkedIn: {data['linkedin']}", ln=True)
    pdf.cell(0, 10, f"GitHub: {data['github']}", ln=True)
    pdf.ln(5)

    pdf.section_title("Objective")
    pdf.section_body(data['objective'])

    pdf.section_title("Skills")
    pdf.section_body(", ".join(data['skills']))

    pdf.section_title("Education")
    for edu in data['education']:
        pdf.section_body(f"{edu['degree']} from {edu['institution']} ({edu['year']})")

    pdf.section_title("Projects")
    for proj in data['projects']:
        pdf.section_body(f"{proj['title']} - {proj['description']}")

    pdf.section_title("Experience")
    for exp in data['experience']:
        pdf.section_body(f"{exp['title']} at {exp['company']} ({exp['duration']})")

    pdf.output(filename)
