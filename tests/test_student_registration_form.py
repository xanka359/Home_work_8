import allure

from demo_qa.pages.student_registration_form import StudentRegistrationForm
from demo_qa.users import user, user_interests


def test_registrated_user():
    registration_page = StudentRegistrationForm()

    registration_page.open()
    registration_page.registration(user)
    registration_page.modal_window_check(user, user_interests)
