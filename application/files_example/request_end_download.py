import json
import urllib.request
import requests

from homework__Chaika_Sergii__hw6__flask.application.config.path import FILES_OUTPUT_PATH
from homework__Chaika_Sergii__hw6__flask.application.logging.loggers import get_core_logger


def get_requests_data(url: str = None) -> None:
    logger = get_core_logger()
    path = FILES_OUTPUT_PATH.joinpath("output.json")
    with requests.Session() as session:
        response = session.get(url)
        logger.info(f"{response}")
        response_json = response.json()
        path.write_text(json.dumps(response_json, indent=2))
        logger.info(f"Path to file: {path}")


def get_download_file(url: str = None) -> None:
    logger = get_core_logger()
    path_to_file = FILES_OUTPUT_PATH.joinpath("output.csv")
    downloaded_file = urllib.request.urlopen(url).read()
    with open(path_to_file, "wb") as file:
        file.write(downloaded_file)
        logger.info(f"Path to file: {path_to_file}")
