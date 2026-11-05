import datetime
from dataclasses import dataclass
from faker import Faker


@dataclass
class RegisterUserData:
    first_name: str
    last_name: str
    birth_date: datetime.date
    email: str
    company: str
    password: str
    country: str


def generate_user_registration_data():
    f = Faker("en_US")

    return RegisterUserData(
        first_name=f.first_name_female(),
        last_name = f.last_name(),
        birth_date = f.date_of_birth(),
        email = f.free_email(),
        company = f.company(),
        password = f.password(),
        country = f.country()
    )

@dataclass
class UserAddressData:
    country: str
    state: str
    city: str
    street: str
    zipcode: str
    phone: str


def generate_address_data():
    f = Faker()

    return UserAddressData(
        country = "United States of America",
        state = f.state(),
        city = f.city(),
        street = f.address(),
        zipcode= f.postalcode(),
        phone = f.phone_number()
    )