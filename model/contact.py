from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, middlename=None, birthday=None, birth_month=None, id=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page=None,
                 all_mails_from_home_page=None, email=None, email2=None, email3=None, address=None):

        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.birthday = birthday
        self.birth_month = birth_month
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_mails_from_home_page = all_mails_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address = address

    def __repr__(self):
        return '%s:%s %s' % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize






