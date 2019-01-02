import re


def test_mails_on_home_page(app):
    # we will do the test for one contact so we write index 0 = [0]
    contact_from_home_page = app.contact.get_contact_list()[0]
    # now we will get contact info from edit page with index 0 as well
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_mails_from_home_page == merge_mails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_mails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
