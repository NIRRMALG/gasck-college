from flask import Flask, render_template, url_for, request, jsonify
from flask_cors import CORS
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

# ---------- College Website Routes (unchanged) ----------
@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

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

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/academics')
def academics():
    return render_template('academics.html')

@app.route('/scholarships')
def scholarships():
    return render_template('scholarships.html')

@app.route('/location')
def location():
    return render_template('location.html')


# ---------------- ✅ Chatbot Route Using OpenAI ----------------
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant for a college website called GASCK. You provide information about the college and can answer general questions too."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- Run the App ----------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
