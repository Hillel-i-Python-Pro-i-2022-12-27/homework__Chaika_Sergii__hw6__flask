from homework__Chaika_Sergii__hw6__flask.application.config.path import FILES_INPUT_PATH
from homework__Chaika_Sergii__hw6__flask.application.files_example.generators import create_text
from homework__Chaika_Sergii__hw6__flask.application.logging.loggers import get_core_logger


def create_txt_file(name_file: str = None) -> None:
    logger = get_core_logger()
    path_to_file = FILES_INPUT_PATH.joinpath(f"{name_file}.txt")
    with open(path_to_file, mode="w") as file:
        file.write(f"{create_text()}")
    logger.info(f"Path to file: {path_to_file}")
