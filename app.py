from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from pypdf import PdfReader

# Initialize Flask app
app = Flask(__name__)

# Configure API key for the Generative Model
genai.configure(api_key="AIzaSyCqpRCumeh9oQxSXbD5QHQDfSkO-9XlKww")

# Route for the home page to upload resume
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded resume and job description
        resume_file = request.files['resume']
        job_desc = request.form.get('job_description')

        # Read the resume PDF and extract text
        reader = PdfReader(resume_file)
        page = reader.pages[0]
        resume_text = page.extract_text()

        # Create the prompt for the model
        prompt = f"""
        Below is a text that might contain a resume and a job description. If the text contains a resume and job description, update the resume to align with the job description by making only necessary changes. Return **only the updated parts of the resume**. If no changes are needed, respond with "No changes needed." If the provided content does not contain a resume or job description, respond with "Not a resume" or "Not a job description" accordingly.
        Resume:
        {resume_text}
        Job Description:
        {job_desc}
        """

        # Generate response from the model
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")
        response = model.generate_content(prompt)
        updated_parts = response._result.candidates[0].content.parts[0].text.strip()

        # Render the template with the updated resume parts
        return render_template('index.html', updated_resume_parts=updated_parts)

    # If it's a GET request, just render the empty form
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
