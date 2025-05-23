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
    courses = [
        'BSc_Computer_Science',
        'BSc_Mathematics',
        'BA_English',
        'BA_Tamil',
        'Bcom'
    ]
    return render_template('courses.html', courses=courses)

# Course PDFs Page
@app.route('/courses/<course>')
def course_pdfs(course):
    pdf_links = {
        'BSc_Computer_Science': {
            'syllabus_pdf': url_for('static', filename='Bsc Computer science.pdf'),
            'outcomes_pdf': url_for('static', filename='Cse learning.pdf')
        },
        'BSc_Mathematics': {
            'syllabus_pdf': url_for('static', filename='Bsc mathematics.pdf'),
            'outcomes_pdf': url_for('static', filename='Mathematics learning.pdf')
        },
        'BA_English': {
            'syllabus_pdf': url_for('static', filename='English.pdf'),
            'outcomes_pdf': url_for('static', filename='English learning.pdf')
        },
        'BA_Tamil': {
            'syllabus_pdf': url_for('static', filename='Tamil.pdf'),
            'outcomes_pdf': url_for('static', filename='Tamil Learning.pdf')
        },
        'Bcom': {
            'syllabus_pdf': url_for('static', filename='Bcom.pdf'),
            'outcomes_pdf': url_for('static', filename='Bcom learning.pdf')
        }
    }

    course_info = pdf_links.get(course)
    if not course_info:
        return "<h1>Course Not Found</h1>", 404

    return render_template('course_pdfs.html', course=course.replace('_', ' '), course_info=course_info)

# Faculty List Page
@app.route('/faculty')
def faculty():
    faculty_list = [
        {'name': 'Dr. A. Kumar', 'slug': 'a_kumar', 'department': 'English'},
        {'name': 'Prof. B. Lakshmi', 'slug': 'b_lakshmi', 'department': 'Mathematics'},
        {'name': 'Dr. R. Gurumoorthy', 'slug': 'c_guru', 'department': 'Computer Science'},
        {'name': 'Dr. F. Nisha Meena', 'slug': 'f_meena', 'department': 'Commerce'},
        {'name': 'Prof. D. Rajesh', 'slug': 'd_rajesh', 'department': 'Tamil'}
    ]
    return render_template('faculty.html', faculty_list=faculty_list)

# Faculty Profile Page
@app.route('/faculty/<slug>')
def faculty_profile(slug):
    faculty_data = {
        'a_kumar': {
            'name': 'Dr. A. Kumar',
            'department': 'English',
            'qualification': 'Ph.D in English Literature',
            'cabin': 'Room 101',
            'photo': url_for('static', filename='a_kumar.png')
        },
        'b_lakshmi': {
            'name': 'Prof. B. Lakshmi',
            'department': 'Mathematics',
            'qualification': 'M.Sc., M.Phil',
            'cabin': 'Room 102',
            'photo': url_for('static', filename='b_lakshmi.png')
        },
        'c_guru': {
            'name': 'Dr. R. Gurumoorthy',
            'department': 'Computer Science',
            'qualification': 'Ph.D, M.Phil, MBA, MCA',
            'cabin': 'Room 103',
            'photo': url_for('static', filename='c_guru.png')
        },
        'f_meena': {
            'name': 'Dr. F. Nisha Meena',
            'department': 'Commerce',
            'qualification': 'Ph.D in Commerce',
            'cabin': 'Room 104',
            'photo': url_for('static', filename='d_meena.png')
        },
        'd_rajesh': {
            'name': 'Prof. D. Rajesh',
            'department': 'Tamil',
            'qualification': 'Phd in Tamil Literature',
            'cabin': 'Room 105',
            'photo': url_for('static', filename='default_faculty.png')
        }
    }

    faculty = faculty_data.get(slug)
    if not faculty:
        return "<h1>Faculty Not Found</h1>", 404

    return render_template('faculty_profile.html', faculty=faculty)

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Academics Main Page
@app.route('/academics')
def academics():
    return render_template('academics.html')

# Scholarships Page (new)
@app.route('/scholarships')
def scholarships():
    return render_template('scholarships.html')
@app.route('/location')
def location():
    return render_template('location.html')

# Run the App
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
