import datetime
from dataclasses import dataclass
@dataclass
class User:
    first_name: str
    last_name: str
    date_of_birth: int
    month_of_birth: str
    year_of_birth: str
    email: str
    gender: str
    phone_number: int
    current_address: str
    city: str
    state: str

    @dataclass
    class UserInterests:
        subject: str
        hobby: str
