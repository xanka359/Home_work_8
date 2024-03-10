import allure

from demo_qa.pages.student_registration_form import StudentRegistrationForm
from demo_qa.users import user, user_interests


def test_registration_user():
    registration_page = StudentRegistrationForm()

    with allure.step("Открыть форму регистрации"):
        registration_page.open()

    with allure.step("Заполнить форму регистрации"):
        registration_page.registration(user)

    with allure.step("Проверить корректность данных на форме регистрации"):
        registration_page.modal_window_check(user, user_interests)
