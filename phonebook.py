class Phonebook:

    """ This is a phonebook which permits adding, deleting, checking if the phonebook is empty and printing out all contents of the phonebook """


    def __init__(self):
        """ Initializes the phonebok and a dictionary to the the records """
        self.phonebook = {}
        # this is s a counter for given a key to a no  named number or 
        # numbers with None name
        self.counter = 0
        print("New dictionary created\nmemory alloted")
    

    def add_contact(self, name=None, number=None):
        """ Adds contact to phonebook 
        :params name: name of contact
        :params number: number of contact """
        # there shouldn"t be a name without a number
        # there can be a number without a name
        # but name shouldn"t have a value of None, give it an it value
        # there shouldn"t be duplicate of names or numbers, as there 
        # shouldn"t be a duplicate key and values (you can"t have two people using the same number)
        if name in self.phonebook.keys() or number in self.phonebook.values():
            print("Name or number already exist")
        elif name != None and number != None:
            self.phonebook.setdefault(name, number)
        elif name == None and number != None:
            name = self.counter
            self.phonebook.setdefault(name, number)
            # if name is not give, a int value is given to it as a counter
            self.counter += 1
        else:
            print("Name and number, only number is needed to add to phonebook")
        

    def update_contact(self, name=None, number = None):
        """ Updates contact's name when name and (new) number is given
        :params name: name of contact
        :params number: number of contact """
        if name in self.phonebook.keys():
            self.phonebook[name] = number
        else:
            print("Give name or number, that exists, to update contact in phonebook")


    def is_empty_contact(self):
        """ Checks if the phonebook is empty 
        :return bool: True if phonebook is empty, else False """
        return self.phonebook == {}
        

    def loop_name_contact(self, name):
        """ Loops through phonebook and prints key and value whose key matches name 
        :params name: name of contact """
        for namekey, numbervalue in self.phonebook.items():
                if namekey == name:
                    print(namekey, ":", numbervalue)


    def print_contact(self, name=None, number=None):
        """ Prints out the name and number of contact 
        :params name: name of contact
        :params number: number of contact """
        if name in self.phonebook.keys():
            self.loop_name_contact(name)
        elif name == None and number in self.phonebook.values():
            name = self.get_name_contact(number)
            self.loop_name_contact(name)
        else:
            print("Give name or number, that exists, to view contact from phonebook")


    def print_all_contact(self):
        """ Prints out all the contents of the phonebook """
        if self.is_empty_contact():
            print('Contact is empty')
        else:
            for name in self.phonebook.keys():
                self.loop_name_contact(name)


    def get_name_contact(self, number=None):
        """Returns the name of contact if number exist.
        :params number: number of the contact
        :return key: name"""
        # change the numbers (values) to a list and find it's index
        # use the index index to find the value
        numberlist = list(self.phonebook.values())
        if number in numberlist:
            numberindex = numberlist.index(number)
            namelist = list(self.phonebook.keys())
            key = namelist.index(numberindex)
            return key


    def delete_contact(self, name=None, number=None):
        """ Deletes contact from the phonebook 
        :params name: name of contact
        :params number: number of contact """
        # deleting contact if name is given and exists
        # checking if it exists is in phonebook is similar to ckecking if 
        # it is given and exists
        if name in self.phonebook.keys():
            del self.phonebook[name]
        elif name == None and number in self.phonebook.values():
            # deleting contact if number (value) is given instead and exists
            # find the index (key or name) of number (value)
            name = self.get_name_contact(number)
            del self.phonebook[name]
        else:
            print("Give name or number, that exists, to delete from phonebook")
        

    def delete_all_contact(self):
        """ Deletes all contacts from phonebook """
        self.phonebook.clear()


# test cases

pb = Phonebook()
# testing add
add = pb.add_contact
add(name = 'Lucy Adolfimov', number = "331-021-220")
add(name = 'George Martin', number = None)
add(name = None, number = '000-263-341')
add(name = None, number = None)

pb.print_all_contact()

# testing update
update = pb.update_contact
update(name = 'Lucy Adolfimov', number = "000-021-000")
update(name = 'George Martin', number = None)
update(name = None, number = '000-263-341')
update(name = None, number = None)

pb.print_all_contact()

# testing delete
delete = pb.delete_contact
delete(name = 'Lucy Adolfimov', number = "000-021-000")
delete(name = 'George Martin', number = None)
delete(name = None, number = '000-263-341')
delete(name = None, number = None)

pb.print_all_contact()

# testing is_empty
print(pb.is_empty_contact())

# testing print conatact
p_c = pb.print_contact
p_c(name = 'Lucy Adolfimov', number = "000-021-000")
p_c(name = 'George Martin', number = None)
p_c(name = None, number = '000-263-341')
p_c(name = None, number = None)

# testing delete_all_contact
pb.delete_all_contact()
pb.print_all_contact()
