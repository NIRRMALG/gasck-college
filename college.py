from flask import Flask, render_template
import os

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('homepage.html')

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
def syllabus_topics(course, year):
    return f"<h1>{course.replace('_', ' ')} - {year.replace('_', ' ')}</h1><p>Here will be your syllabus topics!</p>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
