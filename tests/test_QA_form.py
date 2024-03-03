from selene import browser, by, have, command, be

from home_work.pages.registration_page import RegistrationPage
from home_work.resources import resource_path

def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    #WHEN
    registration_page.type_first_name("NewFirst name")
    registration_page.type_last_name("NewLast name")
    registration_page.type_email('example@mail.com')
    registration_page.select_gender()
    registration_page.type_phone_number('1023456789')

    registration_page.date_of_birth('1995', 'June', '18')
    registration_page.select_subject('English')
    registration_page.select_hobby('Sports')

    browser.element('#uploadPicture').set_value(resource_path('resources/photo_1.jpg'))

    registration_page.type_current_address('Russian Federation, Penza')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Noida')

    registration_page.submit()



    #THEN
    registration_page.modal_registration_text('Thanks for submitting the form')
    registration_page.should_registrated_user_contains().should(  #можно у класса написать @property и средние скобки не писать
                    have.texts(
                    'NewFirst name NewLast name',
                    'example@mail.com',
                    'Female',
                    '1023456789',
                    '18 June,1995',
                    'English',
                    'Sports',
                    'photo_1.jpg',
                    'Russian Federation, Penza',
                    'NCR Noida',)
    )
    registration_page.close_modal_win()