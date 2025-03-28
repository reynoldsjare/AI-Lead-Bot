from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from openai import OpenAI
import os
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin


# Load environment variables
load_dotenv()

#Set CoRS to allow cross-origin requests
app = Flask(__name__)
CORS(app)
# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leads.db'
db = SQLAlchemy(app)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Database model
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    conversation = db.Column(db.Text)

@app.route('/')
def home():
    return render_template('index.html')

# Chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    try:
        # Use the new client.chat.completions.create() method
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-4o" if you have access
            messages=[
                {
                    "role": "system",
                    "content": "You are a website visitor assistant on a home goods website. Collect emails and answer questions."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            max_tokens=150
        )

        bot_reply = completion.choices[0].message.content

        # Save email if detected (simple example)
        if '@' in user_message and '.' in user_message:
            new_lead = Lead(email=user_message, conversation=bot_reply)
            db.session.add(new_lead)
            db.session.commit()

        return jsonify({"text": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5000)