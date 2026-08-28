from constants import *
from model_wrapper.llm_wrapper import LLMWrapper
from model_wrapper.llm_state import LLMSTATE

class model_transcriber:
    def __init__(self):
        self.llm_state = LLMSTATE()
        self.llm_wrapper = LLMWrapper(self.llm_state)

        #initialze llm first
        self.llm = LLMWrapper(self.llm_state)
        
    
    def process_input(self, user_input: str) -> str:
        """
        Process the user input and generate a response using the LLM.
        
        Args:
            user_input (str): The input provided by the user.   """

        #generate response using the LLM
        response = self.llm.generate_response(user_input)
        return response
    
    def run(self):
        print("Welcome to the LLM Transcriber!")
        while True:
            user_input = input("Enter your input (or type 'exit' to quit): ")
           
           
            if user_input.lower() == 'exit':
                print("Exiting the LLM Transcriber. Goodbye!")
                break
            else:
                response = self.process_input(user_input)
                print(f"LLM Response: {response}")
            
            #response = self.process_input(user_input)
            #print(f"LLM Response: {response}")
    
if __name__ == "__main__":
    # Your main code logic here
    print("This is the main entry point of the program.")
    llm_bot = model_transcriber()
    llm_bot.run()