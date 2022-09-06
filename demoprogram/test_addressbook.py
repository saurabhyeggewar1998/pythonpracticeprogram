from main import Addressbook,Contact


class TestAddressBook:
    def test_add_contact(self):
        addressbook = Addressbook()
        people_dict = {"first_name": "Saurabh", "last_name": "James", "address": "ldsldlld", "email": "abc",
                        "phone_number": 7057114002}
        contact = Contact(**people_dict)
        assert len(addressbook._people_dict) == 0
        addressbook.add_contacts(contact)
        assert len(addressbook._people_dict) == 1
    def test_edit_contact(self):
        addressbook1 = Addressbook()
        contact_dict = {"first_name":"Saurabh","last_name":"James","address":"ldsldlld","email": "abc","phone_number":7057114002}
        contact = Contact(**contact_dict)
        assert contact.first_name == "Saurabh"
        addressbook1.edit(contact.first_name, contact.last_name, contact.address, contact.email, contact.phone)
        contact.last_name = "rose"
        assert contact.last_name == "rose"
    def test_remove_contact(self):
        addressbook = Addressbook()
        contact_dict = {"first_name": "Saurabh", "last_name": "James", "address": "ldsldlld", "email": "abc",
                       "phone_number": 7057114002}
        contact = Contact(**contact_dict)
        assert contact.first_name == "Saurabh"
        addressbook.remove_contact(contact)












