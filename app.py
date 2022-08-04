from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint
import logging


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

#регистрируем блюпринты вьюшек из loader и main папок
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
#Файл для записи логов
logging.basicConfig(filename="log_basic.txt", level=logging.INFO, encoding="utf-8")


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()