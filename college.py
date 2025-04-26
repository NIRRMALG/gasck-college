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

# Courses
@app.route('/courses')
def courses():
    return render_template('course.html')

# Faculty Page
@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Academics Main Page
@app.route('/academics')
def academics():
    return render_template('academics.html')

# Step 1: Select a course
@app.route('/syllabus/select')
def select_course():
    return render_template('select_course.html')

# Step 2: After course selected, show PDFs
@app.route('/syllabus/<course>')
def course_pdfs(course):
    # Mapping course names to the actual PDF filenames
    pdf_files = {
        'BSc_Computer_Science': {
            'syllabus': 'BSc_COMPUTERSCIENCE_syllabus.pdf',
            'learning_outcomes': 'B.Sc_ComputerScience_learningoutcomes.pdf'
        },
        'BSc_Mathematics': {
            'syllabus': 'BSc_MATHEMATICS_syllabus.pdf',
            'learning_outcomes': 'B.Sc_Mathematics_learningoutcomes.pdf'
        },
        'BA_English': {
            'syllabus': 'BA_ENGLISH_syllabus.pdf',
            'learning_outcomes': 'BA_ENGLISH_learningoutcomes.pdf'
        },
        'BA_Tamil': {
            'syllabus': 'BA_TAMIL_syllabus.pdf',
            'learning_outcomes': 'BA_TAMIL_learningoutcomes.pdf'
        },
        'Bcom': {
            'syllabus': 'BCOM_syllabus.pdf',
            'learning_outcomes': 'BCOM_learningoutcomes.pdf'
        }
    }

    files = pdf_files.get(course)
    if not files:
        return "<h1>Course not found!</h1>"

    return render_template('course_pdfs.html', course=course.replace('_', ' '), files=files)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
