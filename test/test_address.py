def test_address_on_home_page(app):
    # we will do the test for one contact so we write index 0 = [0]
    contact_from_home_page = app.contact.get_contact_list()[0]
    # now we will get contact info from edit page with index 0 as well
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_lastname_on_home_page(app):
    # we will do the test for one contact so we write index 0 = [0]
    contact_from_home_page = app.contact.get_contact_list()[0]
    # now we will get contact info from edit page with index 0 as well
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def test_firstname_on_home_page(app):
    # we will do the test for one contact so we write index 0 = [0]
    contact_from_home_page = app.contact.get_contact_list()[0]
    # now we will get contact info from edit page with index 0 as well
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname






