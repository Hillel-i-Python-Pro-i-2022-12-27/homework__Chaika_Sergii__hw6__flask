from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

from application.files_example.avare_value_file import average_value_from_csv
from application.files_example.create_text_fine import create_txt_file
from application.files_example.generators import generate_users
from application.files_example.number_of_astronauts import number_of_astronaut
from application.files_example.read_text_file import read_text_file
from application.files_example.request_end_download import get_requests_data, \
    get_download_file


app = Flask(__name__)


@app.route('/')
def home_work_6():
    return """
    <html>
        <head>
            <title>Home work 6 Flask</title>
        </head>
        <body>
            <h1>Home work 6</h1>
            <a href=/users target="_blank">Task 1 - List of users. </a><br>
            <a href=/read_file class="page-to" target="_blank">Task 2 - Reading file. </a><br>
            <a href=/astronauts class="page-to" target="_blank">Task 3 - List of astronauts. </a><br>
            <a href=/mean class="page-to" target="_blank"> Task 4 - Average value.</a><br>
        </body>
    </html>
    """


@app.route('/users')
@use_args({"amount": fields.Int(missing=10)}, location="query")
def generate_users_web(args) -> str:
    amount = args["amount"]
    users = generate_users(amount=amount)
    output = "".join(
        f"<li>" f"<span>{User.name}</span>" f"<span> - </span>" f"<span>{User.email}</span>" f"</li>" for User in users
    )
    return f"""
    <html>
        <head>
            <title>Generate users</title>
        </head>
        <body>
            <h2>Users:</h2>
            <ol>{output}</ol>
        </body>
    </html>
    """


@app.route("/read_file")
def read_file_txt() -> str:
    create_txt_file(name_file="fake_text")
    read_file = read_text_file(name_file="fake_text")
    return f"""
    <html>
        <head>
            <title>Fake txt file</title>
        </head>
        <body>
            <h2>Text file fake_text.txt:</h2>
            <p>{read_file}</p>
        </body>
    </html>
    """


@app.route("/astronauts")
def get_info_astronauts() -> str:
    get_requests_data(url="http://api.open-notify.org/astros.json")
    info_astronauts = number_of_astronaut(name_file="output")
    return f"""
    <html>
        <head>
            <title>List of astronauts</title>
        </head>
        <body>
            <h2>List of astronauts:</h2>
            <span>{info_astronauts}</span>
        </body>
    </html>
    """


@app.route("/mean")
def mean() -> str:
    url = "https://drive.google.com/uc?export=download&id=1yM0a4CSf0iuAGOGEljdb7qcWyz82RBxl"
    get_download_file(url)
    average_value = average_value_from_csv(name_file="output")
    return f"""
    <html>
        <head>
            <title>Average value</title>
        </head>
        <body>
            <h2>Data after processing csv-file:</h2>
            <span>{average_value}</span>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run()
