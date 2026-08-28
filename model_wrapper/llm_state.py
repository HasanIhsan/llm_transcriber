class LLMSTATE:
    def __init__(self):
        self.enabled = True
        self.generation_params = {
            "temperature": 0.7,
            "top_p": 0.85,
            "top_k": 50,
            "repeat_penalty": 1.1
        }
        
    