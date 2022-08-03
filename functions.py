import json


def get_list_from_json() -> list[dict]:
    """
    Читает из файла и возвращает список постов
    """
    with open('posts.json', 'r', encoding='utf-8') as file:
        list_posts = json.load(file)

        return list_posts


def write_user_data_in_json(pic: str, content: str):
    """
    Получаем данные с формы сайта и перезаписываем с ними json файл с постами
    """
    posts = get_list_from_json()
    new_post = {"pic": pic, "content": content}
    posts.append(new_post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)

    return new_post


def get_posts_by_key(key: str) -> list[dict]:
    """
    Получаем список постов по ключу, возвращаем список
    """
    list_posts = []

    for post in get_list_from_json():
        if key in post['content']:
            list_posts.append(post)

    return list_posts

