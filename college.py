from flask import Flask, render_template
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

# Step 2: Select a year after choosing course
@app.route('/syllabus/<course>')
def select_year(course):
    return render_template('year.html', course=course)

# Step 3: Show syllabus topics for selected course and year
@app.route('/syllabus/<course>/<year>')
def show_syllabus(course, year):
    syllabus = {
        'BSc_Computer_Science': {
            '1st_year': ['Introduction to Programming', 'Basic Mathematics', 'Fundamentals of Computer Systems','Introduction to Web Development'],
            '2nd_year': ['Advanced Programming', 'Operating Systems', 'Data Structures and Algorithms','Database Management Systems','Computer Networks'],
            '3rd_year': ['Software Engineering', 'System Software','Python Programming','Mobile Application Development','Electives', 'Project Work']
        },
        'BA_Tamil': {
            '1st_year': ['Tamil Literature I', 'History of Tamil Language'],
            '2nd_year': ['Tamil Literature II', 'Modern Tamil Poetry'],
            '3rd_year': ['Tamil Novel', 'Tamil Journalism']
        },
        'BA_English': {
            '1st_year': ['English Literature I', 'Introduction to Literary Forms'],
            '2nd_year': ['English Literature II', 'Modern English Drama'],
            '3rd_year': ['Shakespeare Studies', 'Contemporary Literature']
        },
        'BSc_Mathematics': {
            '1st_year': ['Differential Calculus and Trigonometry', 'Algebra and Trigonometry'],
            '2nd_year': ['Differential Equations', 'Vector Calculus'],
            '3rd_year': ['Real Analysis', 'Complex Analysis']
        },
        'Bcom':{
            '1st_year': ['Calcu', 'Algebr and Trigoetry'],
            '2nd_year': ['Differtial Equatns', 'Veor Calculus'],
            '3rd_year': ['Real Anysis', 'Comex Analysis']
        }
    }

    subjects = syllabus.get(course, {}).get(year, [])
    return render_template('show_syllabus.html', course=course.replace('_', ' '), year=year.replace('_', ' '), subjects=subjects)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
