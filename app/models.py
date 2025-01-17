import ollama

class DebateAI:
    def __init__(self):
        self.pro_model = ollama.Client()
        self.con_model = ollama.Client()
        self.judge_model = ollama.Client()
    
    def get_pros(self, topic):
        prompt = f"Analyze only the positive aspects of: {topic}. List clear 5 arguments."
        response = self.pro_model.chat(model='llama2', messages=[
            {'role': 'user', 'content': prompt}
        ])
        return response['message']['content']
    
    def get_cons(self, topic):
        prompt = f"Analyze only the negative aspects of: {topic}. List clear 5 arguments."
        response = self.con_model.chat(model='llama2', messages=[
            {'role': 'user', 'content': prompt}
        ])
        return response['message']['content']
    
    def get_verdict(self, pros, cons):
        prompt = f"Compare these arguments:\nPros:{pros}\nCons:{cons}\nWhich side presents stronger arguments? Score out of 100."
        response = self.judge_model.chat(model='llama2', messages=[
            {'role': 'user', 'content': prompt}
        ])
        return response['message']['content']
