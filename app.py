# app.py

from flask import Flask, render_template, request, jsonify
from main import ChatBot
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

bot = ChatBot()  # Initialize your ChatBot instance

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_input = request.form['user_input']
        response = bot.rag_chain.invoke(user_input)
        start_marker = "Answer: "
        start_index = response.find(start_marker) + len(start_marker)
        answer = response[start_index:].strip()
        print(f"Hello")
        # return jsonify({"response": response})
        return jsonify({"response": answer})
    except Exception as e:
        # Log the exception to debug
        print(f"Exception here: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
