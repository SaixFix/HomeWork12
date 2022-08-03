from flask import Flask
from main.views import main_blueprint
from loader.views import loader_blueprint
import logging


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
#Файл для записи логов
logging.basicConfig(filename="log_search.txt", level=logging.INFO, encoding="utf-8")

if __name__ == "__main__":
    app.run()