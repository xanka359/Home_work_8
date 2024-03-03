from home_work.pages.high_level_registration_page import HighLevelRegistrationPage
from home_work.users import User

user = User(first_name='NewFirst name', last_name='NewLast name', date_of_birth=18, month_of_birth='June',
            year_of_birth='1995', email='example@mail.com', gender='Female', phone_number=1023456789,
            current_address='Russian Federation, Penza', city='Noida', state='NCR')

user_interests = User.UserInterests(subject='English', hobby='Sports')


def test_registrated_user():
    registration_page = HighLevelRegistrationPage()

    registration_page.open()
    #THEN
    registration_page.type_first_name(user.first_name)
    registration_page.type_last_name(user.last_name)

    registration_page.type_email(user.email)
    registration_page.select_gender()
    registration_page.type_phone_number(user.phone_number)

    registration_page.date_of_birth(user.year_of_birth, user.month_of_birth, user.date_of_birth)
    registration_page.select_subject(user_interests.subject)
    registration_page.select_hobby(user_interests.hobby)

    registration_page.upload_picture('resources/photo_1.jpg')

    registration_page.type_current_address(user.current_address)
    registration_page.fill_state(user.state)
    registration_page.fill_city(user.city)

    registration_page.submit()
    #WHEN
    registration_page.modal_registration_text('Thanks for submitting the form')
    registration_page.should_registrated_user_contains(f'{user.first_name} {user.last_name}', user.email,
                                                       user.gender, f'{user.phone_number}',
                                                       f'{user.date_of_birth} {user.month_of_birth},{user.year_of_birth}',
                                                       user_interests.subject, user_interests.hobby,
                                                       'photo_1.jpg', user.current_address, f'{user.state} {user.city}'
                                                       )
    registration_page.close_modal_win()
