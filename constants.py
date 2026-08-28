# Model Configuration
MODEL_PATH = "models/gemma2-9b--q4_k_m.gguf"
CONTEXT_SIZE = 8192


# Generation Parameters
GENERATION_PARAMS = {
    "temperature": 0.7,
    "top_p": 0.85,
    "top_k": 50,
    "repeat_penalty": 1.1,
    "max_tokens": 256
}