from typing import NamedTuple
from collections.abc import Iterator
from faker import Faker


class User(NamedTuple):
    name: str
    email: str

    def __str__(self):
        return f"{self.name} {self.email}"

    __repr__ = __str__


faker = Faker()


def generate_user() -> User:
    return User(name=faker.first_name(), email=faker.free_email())


def generate_users(amount: int=100) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()


def create_text() -> Faker:
    return faker.text().replace(". ", ".\n")
