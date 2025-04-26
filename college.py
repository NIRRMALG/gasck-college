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
    return render_template('courses.html')

# Faculty List Page
@app.route('/faculty')
def faculty():
    faculty_list = [
        {'name': 'Dr. A. Kumar', 'slug': 'a_kumar', 'department': 'Computer Science'},
        {'name': 'Prof. B. Lakshmi', 'slug': 'b_lakshmi', 'department': 'Mathematics'},
        {'name': 'Dr. R.Gurumoorthy', 'slug': 'c_guru', 'department': 'English'},
        {'name': 'Dr. D. Meena', 'slug': 'd_meena', 'department': 'Tamil'},
    ]
    return render_template('faculty.html', faculty_list=faculty_list)

# Faculty Profile Page
@app.route('/faculty/<slug>')
def faculty_profile(slug):
    faculty_data = {
        'a_kumar': {
            'name': 'Dr. A. Kumar',
            'department': 'Computer Science',
            'qualification': 'Ph.D in Computer Science',
            'cabin': 'Room 101',
            'photo': 'faculty_photos/a_kumar.jpg'
        },
        'b_lakshmi': {
            'name': 'Prof. B. Lakshmi',
            'department': 'Mathematics',
            'qualification': 'M.Sc., M.Phil',
            'cabin': 'Room 102',
            'photo': 'faculty_photos/b_lakshmi.jpg'
        },
        'c_guru': {
            'name': 'Dr. R.Gurumoorthy',
            'department': 'English',
            'qualification': 'Ph.D in Computer Science,Mphil,MBA,MCA',
            'cabin': 'Room 103',
            'photo': 'faculty_photos/c_guru.jpg'
        },
        'd_meena': {
            'name': 'Dr. D. Meena',
            'department': 'Tamil',
            'qualification': 'Ph.D in Tamil',
            'cabin': 'Room 104',
            'photo': 'faculty_photos/d_meena.jpg'
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

# Step 1: Select a course
@app.route('/syllabus/select')
def select_course():
    return render_template('select_course.html')

# Step 2: After selecting course - show PDF links
@app.route('/syllabus/<course>')
def show_course_pdfs(course):
    pdf_links = {
        'BSc_Computer_Science': {
            'syllabus_pdf': url_for('static', filename='pdfs/BSc_CS_Syllabus.pdf'),
            'outcomes_pdf': url_for('static', filename='pdfs/BSc_CS_Outcomes.pdf')
        },
        'BA_Tamil': {
            'syllabus_pdf': url_for('static', filename='pdfs/BA_Tamil_Syllabus.pdf'),
            'outcomes_pdf': url_for('static', filename='pdfs/BA_Tamil_Outcomes.pdf')
        },
        'BA_English': {
            'syllabus_pdf': url_for('static', filename='pdfs/BA_English_Syllabus.pdf'),
            'outcomes_pdf': url_for('static', filename='pdfs/BA_English_Outcomes.pdf')
        },
        'BSc_Mathematics': {
            'syllabus_pdf': url_for('static', filename='pdfs/BSc_Math_Syllabus.pdf'),
            'outcomes_pdf': url_for('static', filename='pdfs/BSc_Math_Outcomes.pdf')
        },
        'Bcom': {
            'syllabus_pdf': url_for('static', filename='pdfs/BCom_Syllabus.pdf'),
            'outcomes_pdf': url_for('static', filename='pdfs/BCom_Outcomes.pdf')
        }
    }

    course_info = pdf_links.get(course)
    if not course_info:
        return "<h1>Course Not Found</h1>", 404

    return render_template('course_pdfs.html', course=course.replace('_', ' '), course_info=course_info)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
