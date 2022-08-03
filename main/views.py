from flask import Blueprint, request, render_template
from functions import get_posts_by_key
import logging


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    """
    Главная страница
    """
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    """
    Страница поиска, возвращает результат поиска
    """
    s = request.args['s']

    logging.info(f"Поиск по {s} запрошен")

    try:
        posts = get_posts_by_key(s)
    except:
        logging.error('файл не найден')
        return "Файл с постами не найден"
    return render_template('post_list.html', posts=posts, request=s)
