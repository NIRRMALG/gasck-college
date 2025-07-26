from flask import Flask, render_template, url_for, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")


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

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    print(" User message:", user_message)

    perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")
    if not perplexity_api_key:
        return jsonify({"error": "Perplexity API key not configured."}), 500

    headers = {
        "Authorization": f"Bearer {perplexity_api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sonar-pro",  # or the correct model string
        "messages": [
            {
  "role": "system",
  "content": "You are a helpful and friendly chatbot for the GASCK college website. Please answer questions briefly and conversationally, without citations or overly detailed explanations."
}
,
            {"role": "user", "content": user_message}
        ],
        "max_tokens": 500,
        "temperature": 0.3
    }

    try:
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            json=payload,
            headers=headers
        )
        response.raise_for_status()
        data = response.json()
        reply = data['choices'][0]['message']['content']
        return jsonify({"reply": reply})

    except requests.exceptions.HTTPError as err:
        print("Perplexity API HTTP Error:", err)
        print("Response content:", response.text) 
        return jsonify({"error": f"HTTP Error: {err}, Details: {response.text}"}), 500

    except Exception as e:
        print("Perplexity API Error:", e)
        return jsonify({"error": str(e)}), 500





# ---------------- Run the App ----------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
