from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact('Contact to be modified'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='New first name', birthday='15', middlename='II')
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname
    contact.lastname = old_contacts[0].lastname
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact('Contact to be modified'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(middlename='II', birthday='15')
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname
    contact.lastname = old_contacts[0].lastname
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_birth_month(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact('Contact to be modified'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(birth_month='April')
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname
    contact.lastname = old_contacts[0].lastname
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_firstname_by_index(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact('Contact to be modified'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname='New Contact name', birthday='15', middlename='II')
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    contact.lastname = old_contacts[index].lastname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




