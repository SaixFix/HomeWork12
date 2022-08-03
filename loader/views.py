from flask import Blueprint, request, render_template
from functions import write_user_data_in_json
from loader.utils import is_filename_allowed


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/upload')
def add_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/post', methods=['POST'])
def uploads_page():
    picture = request.files.get("picture")
    content = request.form.get('content')
    filename = picture.filename

    if not is_filename_allowed(filename):
        extension = filename.split(".")[-1]
        return f"Тип файлов {extension} не поддерживается"

    picture.save(f"./uploads/images/{filename}")
    post = write_user_data_in_json(f"/uploads/images/{filename}", content)
    return render_template('post_uploaded.html', post=post)


