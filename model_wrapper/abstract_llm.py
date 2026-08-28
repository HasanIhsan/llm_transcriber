from abc import ABC, abstractmethod

class AbstractLLM(ABC):
    def __init__(self, llm_state):
        super().__init__()
        
        self.llm_state = llm_state
        
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response based on the given prompt.
        
        Args:
            prompt (str): The input prompt for the LLM.
        
        Returns:
            str: The generated response from the LLM.
        """
        pass
    

    def assemble_prompt(self, user_input: str) -> str:
        """
        Assemble the final prompt to be sent to the LLM based on the user input.
        
        Args:
            user_input (str): The input provided by the user.
        
        Returns:
            str: The assembled prompt for the LLM.
        """
        # You can customize this method to format the prompt as needed
        base_prompt = f"You are a helpful assistant. Please respond to the following input:\n{user_input}"
        
        return f"{base_prompt}"
    
    
    
    