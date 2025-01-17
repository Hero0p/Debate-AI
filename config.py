import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    OLLAMA_API_URL = 'http://localhost:5000' #11434
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Model configurations
    MODELS = {
        'pro_model': 'llama2',
        'con_model': 'llama2',
        'judge_model': 'llama2'
    }
    
    # Application configurations
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    
    # Rate limiting
    RATELIMIT_DEFAULT = "20/minute"
    RATELIMIT_STORAGE_URL = "memory://"
