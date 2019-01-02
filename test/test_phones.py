def test_phones_on_home_page(app):
    # we will do the test for one contact so we write index 0 = [0]
    contact_from_home_page = app.contact.get_contact_list()[0]
    # now we will get contact info from edit page with index 0 as well
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.homephone == contact_from_edit_page.homephone
    assert contact_from_home_page.workphone == contact_from_edit_page.workphone
    assert contact_from_home_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_home_page.secondaryphone == contact_from_edit_page.secondaryphone

