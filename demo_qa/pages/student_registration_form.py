from selene import be, command, have, by
from selene.support.shared import browser

from demo_qa.resources import resource_path
from demo_qa.users import user, user_interests


class StudentRegistrationForm:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def type_first_name(self, user):
        browser.element('#firstName').should(be.blank).type(user.first_name)
        return self

    def type_last_name(self, user):
        browser.element('#lastName').should(be.blank).type(user.last_name)
        return self

    def type_email(self, user):
        browser.element('#userEmail').should(be.blank).type(user.email)
        return self

    def select_gender(self):
        browser.element('[value="Female"]').perform(command.js.click)
        return self

    def type_phone_number(self, user):
        browser.element('#userNumber').should(be.blank).type(user.phone_number)
        return self

    def date_of_birth(self, user):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__month-select").click().element(by.text(user.month_of_birth)).click()
        browser.element(".react-datepicker__year-select").click().element(
            by.text(user.year_of_birth)).click()
        browser.element(f'.react-datepicker__day--0{user.date_of_birth}').click()
        return self

    def select_subject(self, user_interests):
        browser.element('#subjectsInput').type(user_interests.subject).press_enter()
        return self

    def select_hobby(self, user_interests):
        browser.element('[for=hobbies-checkbox-1]').click().should(have.text(user_interests.hobby))
        return self

    def upload_picture(self, user):
        browser.element('#uploadPicture').set_value(resource_path(user.photo))
        return self

    def type_current_address(self, user):
        browser.element('#currentAddress').should(be.blank).type(user.current_address)
        return self

    def fill_state(self, user):
        browser.element('#state').element('.css-19bqh2r').click()
        browser.element('#react-select-3-option-0').should(have.text(user.state)).click()
        return self

    def fill_city(self, user):
        browser.element('#city').element('.css-1wy0on6').click()
        browser.element('#react-select-4-option-2').should(have.text(user.city)).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def registration(self, user):
        (self
         .type_first_name(user)
         .type_last_name(user)
         .type_email(user)
         .select_gender()
         .type_phone_number(user)
         .date_of_birth(user)
         .select_subject(user_interests)
         .select_hobby(user_interests)
         .upload_picture(user)
         .type_current_address(user)
         .fill_state(user)
         .fill_city(user)
         .submit())
        return self

    def modal_registration_text(self):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        return self

    def should_registrated_user_contains(self, user, user_interests):
        return browser.element('.table').all('td').even.should(have.texts(f'{user.first_name} {user.last_name}'
                                                                          , user.email, user.gender,
                                                                          f'{user.phone_number}',
                                                                          f'{user.date_of_birth} {user.month_of_birth},{user.year_of_birth}',
                                                                          user_interests.subject, user_interests.hobby,
                                                                          user.photo, user.current_address,
                                                                          f'{user.state} {user.city}'))

    def close_modal_win(self):
        browser.element('#closeLargeModal').click()
        return self

    def modal_window_check(self, user, user_interests):
        (self
         .modal_registration_text()
         .should_registrated_user_contains(user, user_interests))
        self.close_modal_win()
        return self
