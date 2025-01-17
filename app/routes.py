from flask import Blueprint, render_template, request, jsonify
from app.models import DebateAI

main = Blueprint('main', __name__)
debate_ai = DebateAI()

@main.route('/')
def index():
    return render_template('index.html')

# @main.route('/analyze', methods=['POST'])
# def analyze():
#     topic = request.json['topic']
#     pros = debate_ai.get_pros(topic)
#     cons = debate_ai.get_cons(topic)
#     verdict = debate_ai.get_verdict(pros, cons)
    
#     return jsonify({
#         'pros': pros,
#         'cons': cons,
#         'verdict': verdict
#     })

@main.route('/analyze', methods=['POST'])
def analyze():
    try:
        topic = request.json.get('topic', '')
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400

        print(f"Received topic: {topic}")  # Log the received topic

        # Simulate Ollama or backend model calls
        pros = debate_ai.get_pros(topic)
        print(f"Pros: {pros}")  # Log pros

        cons = debate_ai.get_cons(topic)
        print(f"Cons: {cons}")  # Log cons

        verdict = debate_ai.get_verdict(pros, cons)
        print(f"Verdict: {verdict}")  # Log verdict

        return jsonify({
            'pros': pros,
            'cons': cons,
            'verdict': verdict
        })
    except Exception as e:
        print(f"Error: {e}")  # Log any error
        return jsonify({'error': str(e)}), 500
