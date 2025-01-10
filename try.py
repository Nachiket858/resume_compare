import google.generativeai as genai
genai.configure(api_key="AIzaSyCqpRCumeh9oQxSXbD5QHQDfSkO-9XlKww")

from pypdf import PdfReader
reader = PdfReader("profile.pdf")
number_of_pages = len(reader.pages)
# print(number_of_pages)
page = reader.pages[0]
text = page.extract_text()
# print(text)
escription= """We are looking for a talented and motivated DevOps Engineer to join our growing team. As a DevOps Engineer, you will be responsible for automating and streamlining the development, deployment, and operational processes for our applications. You will work closely with development teams to ensure seamless integration, continuous delivery, and system reliability.
Key Responsibilities:
CI/CD Pipeline Management: Design, implement, and manage continuous integration and continuous deployment pipelines to ensure fast and reliable delivery of software.
Infrastructure Automation: Automate provisioning, configuration management, and monitoring of infrastructure using tools like Terraform, Ansible, or CloudFormation.
Cloud Management: Manage and deploy applications on cloud platforms such as AWS, Azure, or Google Cloud. Ensure high availability, scalability, and security of the infrastructure.
Containerization & Orchestration: Utilize Docker for containerization and Kubernetes for container orchestration to deploy applications in a scalable and efficient manner.
Monitoring & Logging: Set up monitoring and logging tools (e.g., Prometheus, Grafana, ELK Stack) to track application performance, uptime, and system health.
Collaboration & Support: Work closely with development, QA, and IT operations teams to ensure smooth communication, integration, and issue resolution.
Security Best Practices: Implement security policies for infrastructure, applications, and databases to safeguard against potential threats.
Required Skills & Qualifications:
Bachelor’s degree in Computer Science, Engineering, or a related field (or equivalent work experience).
3+ years of experience in DevOps, system administration, or cloud engineering.
Proficiency in cloud platforms (AWS, Azure, GCP) and services.
Experience with containerization technologies like Docker and Kubernetes.
Strong knowledge of CI/CD tools such as Jenkins, GitLab CI, or CircleCI.
Familiarity with Infrastructure as Code (IaC) tools like Terraform or Ansible.
Solid understanding of version control systems, particularly Git.
Experience in automating repetitive tasks using scripting languages such as Python, Bash, or Ruby.
Strong problem-solving skills, attention to detail, and the ability to troubleshoot complex issues.
Excellent communication and collaboration skills.
Preferred Skills:
Experience with serverless architectures.
Knowledge of microservices architecture.
Familiarity with monitoring tools like Prometheus, Grafana, or ELK stack.
Certifications in cloud platforms (AWS Certified DevOps Engineer, Azure DevOps Engineer, etc.).
What We Offer:
A collaborative and innovative work environment.
Competitive salary and benefits package.
Opportunities for career growth and professional development.
Flexible work hours and the possibility of remote work"""

model = genai.GenerativeModel(model_name="gemini-1.5-pro")
# prompt = (f"{text} this is my resume how can i improve that to apply post for devops position change accordigly do not tell what to do just chage it only if want some information ask me ")
prompt = f"""
Below is a resume and a job description. Update the resume to align with the job description by making only necessary changes. Return **only the updated parts of the resume**. If no changes are needed, respond with "No changes needed."

Resume:
{text}

Job Description:
{escription}
"""
# prompt = "ask me one question 2"
response = model.generate_content(prompt)
print(response._result.candidates[0].content.parts[0].text)
