import datetime
from dataclasses import dataclass
@dataclass
class User:
    first_name: str
    last_name: str
    date_of_birth: int
    month_of_birth: str
    year_of_birth: str
    photo:str
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

user = User(first_name='NewFirst name', last_name='NewLast name', date_of_birth= 18, month_of_birth= 'June',
            year_of_birth= '1995', photo= 'photo_1.jpg', email='example@mail.com', gender='Female', phone_number=1023456789,
            current_address='Russian Federation, Penza', city='Noida', state='NCR')

user_interests = User.UserInterests(subject = 'English', hobby = 'Sports')
