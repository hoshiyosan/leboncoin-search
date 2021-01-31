from flask_cors import CORS
from .database import AnounceDatabase

# web server addons
cors = CORS()

# database addons
anounces_db = AnounceDatabase()
