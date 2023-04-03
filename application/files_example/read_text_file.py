from application.config.path import FILES_INPUT_PATH
from application.logging.loggers import get_core_logger


def read_text_file(name_file: str = None):
    logger = get_core_logger()
    path_to_file = FILES_INPUT_PATH.joinpath(f"{name_file}.txt")
    logger.info(f"Path to file: file://{path_to_file}")
    file_text = path_to_file.read_text()
    return f"{file_text}"


if __name__ == "__main__":
    read_text_file()
