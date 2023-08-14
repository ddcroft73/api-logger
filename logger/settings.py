from dataclasses import dataclass

@dataclass
class Settings():
    LOG_DIRECTORY: str = './logs'
    LOG_ARCHIVE_DIRECTORY: str = f"{LOG_DIRECTORY}/log-archives"
    DEFAULT_LOG_FILE: str = f"{LOG_DIRECTORY}/DEFAULT-app-logs.log"  

settings = Settings()    
