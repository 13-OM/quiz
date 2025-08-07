from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Sample questions
sample_questions = {
    "math": [
        "What is 7 + 8?",
        "Solve: 12 × 4",
        "What is the square root of 81?",
        "What is 25% of 200?",
        "Solve: (5 + 3) × 2",
        "What is 100 ÷ 4?"
    ],
    "science": [
        "What planet is known as the Red Planet?",
        "Define photosynthesis.",
        "What is H2O?",
        "Name the force that keeps us on the ground.",
        "What gas do plants release during photosynthesis?",
        "What organ pumps blood in the human body?"
    ],
    "english": [
        "What is a noun?",
        "Define a verb.",
        "What is the plural of 'mouse'?",
        "What is a synonym for 'happy'?",
        "Use 'although' in a sentence.",
        "Identify the adjective: 'The sky is blue.'"
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    subject = request.form['subject']
    level = request.form['level']

    questions = random.sample(sample_questions[subject], 3)

    return f"""
        <body style='font-family:Poppins; padding:2rem; background:#f4f4f4;'>
            <h2>Hello, {name}!</h2>
            <p>Here are your <strong>{subject.title()}</strong> questions for Grade {level}:</p>
            <ul>
                {''.join(f'<li>{q}</li>' for q in questions)}
            </ul>
            <br>
            <a href="/" style="color:#3f51b5; text-decoration:underline;">Go back</a>
        </body>
    """

if __name__ == '__main__':
    app.run(debug=True)
