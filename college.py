# Flask App (college.py)

from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('homepage.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Courses Page
@app.route('/courses')
def courses():
    return render_template('courses.html')  # now correct spelling

# Faculty Page
@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Academics Page
@app.route('/academics')
def academics():
    return render_template('academics.html')

# Step 1: Select a course (now opens PDFs)
@app.route('/syllabus/select/<course>')
def select_course(course):
    syllabus_files = {
        'BSc_Computer_Science': ('BSc_COMPUTERSCIENCE_syllabus.pdf', 'B.Sc_ComputerScience_learningoutcomes.pdf'),
        'BA_Tamil': ('BA_TAMIL_syllabus.pdf', 'BA_TAMIL_learningoutcomes.pdf'),
        'BA_English': ('BA_ENGLISH_syllabus.pdf', 'BA_ENGLISH_learningoutcomes.pdf'),
        'BSc_Mathematics': ('BSc_MATHEMATICS_syllabus.pdf', 'B.Sc_Mathematics_learningoutcomes.pdf'),
        'BCom': ('BCOM_syllabus.pdf', 'BCOM_learningoutcomes.pdf')
    }

    syllabus_pdf, learning_outcomes_pdf = syllabus_files.get(course, (None, None))

    if syllabus_pdf and learning_outcomes_pdf:
        syllabus_url = url_for('static', filename=syllabus_pdf)
        learning_url = url_for('static', filename=learning_outcomes_pdf)
        return render_template('show_pdfs.html', course=course.replace('_', ' '),
                               syllabus_url=syllabus_url, learning_url=learning_url)
    else:
        return "<h1>Course not found!</h1>"

# Running the server
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
