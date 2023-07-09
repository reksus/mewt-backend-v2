from typing import List
from pydantic import BaseSettings # pants: no-infer-dep
from dotenv import load_dotenv # pants: no-infer-dep
import os

# if pants cmd is run from the root dir
current_working_dir_path = os.path.join(os.getcwd())
path_to_env = "projects/mewt_backend/.env" 
dotenv_path = os.path.join(current_working_dir_path, path_to_env)
load_dotenv(dotenv_path)  


class Settings(BaseSettings):
    database_url: str = ""
    api_key: str = "default_key"
    API_PREFIX: str = "/api"
    ROUTE_PREFIX_V1: str = "/v1"
    JWT_TOKEN_PREFIX: str = "Authorization"
    ALLOWED_HOSTS: List[str] = ["*"]


settings = Settings()
