from .abstract_llm import AbstractLLM
from llama_cpp import Llama
from pathlib import Path
from constants import  CONTEXT_SIZE, MODEL_PATH, GENERATION_PARAMS

class LLMWrapper(AbstractLLM):
    def __init__ (self, llm_state):
        super().__init__(llm_state)
        
        self.model = self._load_model()
        
    def _load_model(self):
        """
        Load the LLaMA model using the provided model path and parameters.
        
        Returns:
            Llama: An instance of the LLaMA model.
        """
        model_path = Path(MODEL_PATH).absolute()
        if not model_path.exists():
            raise FileNotFoundError(f"Model not found: {model_path}")
            
            
        return Llama(
            model_path=str(model_path),
            n_ctx=CONTEXT_SIZE,
            n_gpu_layers=-1,
            n_threads=8,
            verbose=False
        )
    
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response based on the given prompt using the LLaMA model.
        
        Args:
            prompt (str): The input prompt for the LLM.
        
        Returns:
            str: The generated response from the LLM.
        """
        # Here you would implement the logic to generate a response using the LLaMA model
        # For example, you might call a method on self.model to generate text based on the prompt
        # This is a placeholder implementation and should be replaced with actual model inference code
        
        # Example (pseudo-code):
        # response = self.model.generate(prompt)
        # return response
        
        prompt = self.assemble_prompt(prompt)
        # Assuming the model has a method called 'generate' that takes a prompt and returns a
        # response. Replace this with the actual method you use to generate text.
        try:
            print(f"Generating response for prompt: {prompt}")
            responce = self.model.create_completion(
                prompt=prompt,
                **GENERATION_PARAMS
            )
            return responce["choices"][0]["text"]
        except Exception as e:
            print(f"Error generating response: {e}")
            return "An error occurred while generating the response."
        
        