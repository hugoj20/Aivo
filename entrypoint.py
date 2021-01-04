from os.path import join, dirname
from os import environ
from dotenv import load_dotenv
from app import create_app

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

settings_module = environ.get('APP_SETTINGS_MODULE')
app = create_app(settings_module)