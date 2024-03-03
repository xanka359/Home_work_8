from selene import browser, by, be, have, command

from home_work.resources import resource_path


class RegistrationPage:
    def __init__(self):
        self.last_name = browser.element('#lastName')
        self.first_name = browser.element('#firstName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('[value="Female"]')
        self.p_number = browser.element('#userNumber')
        self.current_address = browser.element('#currentAddress')
        self.city = browser.element('#city')
        self.state = browser.element('#state')

    def open(self):
        browser.open('/')

    def type_first_name(self, f_name):
        self.first_name.should(be.blank).type(f_name)

    def type_last_name(self, l_name):
        self.last_name.should(be.blank).type(l_name)

    def type_email(self, email):
        self.email.should(be.blank).type(email)

    def select_gender(self):
        self.gender.perform(command.js.click)
        return self

    def type_phone_number(self, ph_number):
        self.p_number.should(be.blank).type(ph_number)

    def date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__month-select").click().element(by.text(month)).click()
        browser.element(".react-datepicker__year-select").click().element(
            by.text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def select_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def select_hobby(self, hobby):
        browser.element('[for=hobbies-checkbox-1]').click().should(have.text(hobby))

    def upload_picture(self, path):
        browser.element('#uploadPicture').set_value(resource_path(path))
        return self

    def type_current_address(self, address):
        self.current_address.should(be.blank).type(address)

    def fill_state(self, state):
        self.state.element('.css-19bqh2r').click()
        browser.element('#react-select-3-option-0').should(have.text(state)).click()

    def fill_city(self, city):
        self.city.element('.css-1wy0on6').click()
        browser.element('#react-select-4-option-2').should(have.text(city)).click()

    def submit(self):
        browser.element('#submit').click()
        return self

    def modal_registration_text(self, pop_up_text):
        browser.element('#example-modal-sizes-title-lg').should(have.text(pop_up_text))

    def should_registrated_user_contains(self):
        return browser.element('.table').all('td').even

    def close_modal_win(self):
        browser.element('#closeLargeModal').click()
        return self
