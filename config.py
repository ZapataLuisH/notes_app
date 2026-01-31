DB_FILE_PATH = os.path.join(os.path.dirname(__file__), "notes.sqlite")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

class Config: