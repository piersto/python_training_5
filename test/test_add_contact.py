# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    # string will be chosen from letters, digits and 10 spaces -- ' '*10
    symbols = string.ascii_letters + \
              string.digits + string.punctuation + ' '*5
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname='', middlename='', lastname='')] + [
    # will generate random string that starts with word 'Name' or 'Header etc and + some more random symbols
    Contact(firstname=random_string('First name ', (10)), middlename=random_string('Middlename ', (5)),
            lastname=random_string('Lastname', (7)))
                for i in range(5)
    ]


@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new_contact_page()
    app.contact.fill_in_contact_form(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


"""def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new_contact_page()
    app.contact.fill_in_contact_form(Contact(firstname='', middlename='', lastname=''))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)"""
