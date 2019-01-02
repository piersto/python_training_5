from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def submit_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def fill_in_contact_form(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        self.specify_drop_downs(contact)
        self.submit_contact_form()
        self.app.return_on_home_page()
        self.contact_cache = None

    def specify_drop_downs(self, contact):
        wd = self.app.wd
        self.select_in_drop_down('bday', contact.birthday)
        self.select_in_drop_down('bmonth', contact.birth_month)

    def select_in_drop_down(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('middlename', contact.middlename)
        self.change_field_value('lastname', contact.lastname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        # click modification button
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # specify new data
        self.fill_contact_form(new_contact_data)
        self.specify_drop_downs(new_contact_data)
        # click update button
        wd.find_element_by_name("update").click()
        # return to home page
        self.app.return_on_home_page()
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        # specify new data
        self.fill_contact_form(new_contact_data)
        self.specify_drop_downs(new_contact_data)
        # click update button
        wd.find_element_by_name("update").click()
        # return to home page
        self.app.return_on_home_page()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_css_selector("img[alt=\"Edit\"]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name('td')
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_name("selected[]").get_attribute('value')
                all_phones = cells[5].text
                all_mails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(firstname=firstname,
                                                  lastname=lastname,
                                                  id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_mails_from_home_page=all_mails,
                                                  address=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        secondaryphone = wd.find_element_by_name('phone2').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3,
                       address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search('H: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        secondaryphone = re.search('P: (.*)', text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)




