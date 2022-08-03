import logging


def is_filename_allowed(filename):

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True

    logging.info(f"неверный формат файла")
    return False