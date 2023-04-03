from homework__Chaika_Sergii__hw6__flask.application.config.path import FILES_INPUT_PATH
from homework__Chaika_Sergii__hw6__flask.application.logging.loggers import get_core_logger


def read_text_file(name_file: str = None) -> None:
    logger = get_core_logger()
    path_to_file = FILES_INPUT_PATH.joinpath(f"{name_file}.txt")
    logger.info(f"Path to file: file://{path_to_file}")
    file_text = path_to_file.read_text()
    return f"{file_text}"


if __name__ == "__main__":
    read_text_file()
