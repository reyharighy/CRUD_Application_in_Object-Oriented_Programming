"""This is a source-code of CRUD Application with Object-Oriented Programming Paradigm"""

import csv

# This is a section to load patient's record
with open(file='records-oop.csv', mode='r', encoding='utf-8') as load_file:
    patients_list = []
    reader = csv.DictReader(load_file)
    for row in reader:
        row['id_number'] = int(row['id_number'])
        row['birth_date'] = list([
            int(row['birth_date'].split()[0][1:-1]),
            int(row['birth_date'].split()[1][0:-1]),
            int(row['birth_date'].split()[2][0:-1]),
        ])
        patients_list.append(row)

class Initialize:
    """This is a section to initialize the program"""

    def __init__(self):
        """This is a section to instantiate necessary attributes"""
        self.user_name = username_input

    def dictionary(self, name: str, **kwargs: dict):
        """This is a method to get necessary dictionary"""
        if kwargs:
            if kwargs['kwargs']['entry']:
                kwargs = kwargs['kwargs']['entry']
                dict_list = {
                    'num_section':{
                        'Identification Number':[len(str(kwargs)) == 16,'16'],
                        'Phone Number':[len(str(kwargs)) >= 10 and len(str(kwargs)) <= 11,'11-12'],
                        'Year of Birth':[len(str(kwargs)) == 4,'4']
                    }
                }
        else:
            dict_list =  {
                'section':{
                    'main page':4,
                    'gender':3,
                    'month':13,
                    'confirmation':3,
                    'search page':5,
                    'modifier':4,
                    'update':8
                },
                'month':{
                    1:'January',
                    2:'February',
                    3:'March',
                    4:'April',
                    5:'May',
                    6:'June',
                    7:'July',
                    8:'August',
                    9:'September',
                    10:'October',
                    11:'November',
                    12:'December'
                },
                'prompt':{
                    'id_number':'identification number',
                    'name':'name',
                    'phone_number':'phone number'
                },
                'gender':{
                    1:'Male',
                    2:'Female'
                },
                'field':{
                    1:'id_number',
                    2:'name',
                    3:'birth_place',
                    4:'birth_date',
                    5:'gender',
                    6:'phone_number'
                }
            }
        return dict_list.setdefault(name)

    def option_entry_handler(self, name: str):
        """This is a method to handle incorrect option number input"""
        dictionary = self.dictionary(name='section')
        try:
            entry = int(input('\n'+'Please enter option number: '))
            if entry in list(range(1,dictionary.setdefault(name))):
                return entry
            print('\n'+'Error: Option number is invalid')
        except ValueError:
            print('\n'+'Error: Option input only accepts numerics')
        return None

    def alpha_entry_handler(self, name: str):
        """This is a method to handle incorrect alphabets input"""
        while True:
            entry = input('\n'+f"Patient's {name}: ").strip().title()
            if ''.join(entry.split()).isalpha():
                return entry
            print('\n'+f'Error: {name} only accepts alphabets')

    def num_entry_handler(self, name: str):
        """This is a method to handle incorrect numeric input"""
        while True:
            try:
                entry = int(input('\n'+f"Patient's {name}: "))
                dictionary = self.dictionary(name='num_section',kwargs={'entry':entry})
                if dictionary[name][0]:
                    if name == 'Phone Number':
                        return '0'+str(entry)
                    return entry
                print('\n'+f'Error: {name} must be {dictionary[name][1]} numerics')
            except ValueError:
                print('\n'+f'Error: {name} only accepts numerics')

    def main_page(self):
        """This is a section to start main page"""
        while True:
            terminate = False
            print(
                '\n'+" PATIENT'S PERSONAL RECORDS ".center(150,'=')+'\n\n'+
                f'Welcome, {self.user_name}!'.center(150,' ')+'\n\n'+
                'Please input an option number below for the next session page'+'\n'+
                "  1. Create a New Patient's Record"+'\n'+
                "  2. Search a Patient's Record"+'\n'+
                '  3. Exit'
            )
            mp_input = self.option_entry_handler(name='main page')

            # This is a section to create new patient's record
            if mp_input == 1:
                self.create_page()

            # This is a section to access recorded database
            elif mp_input == 2:
                self.search_page()

            # This is a section whether to terminate the program
            elif mp_input == 3:
                terminate = self.exit_page(terminate=terminate)

            # This is to save patient's record and terminate the program
            if terminate:
                with open(file='records-oop.csv', mode='w', encoding='utf-8') as save_file:
                    writer = csv.DictWriter(
                        f=save_file,
                        fieldnames=[
                            'id_number',
                            'name',
                            'birth_place',
                            'birth_date',
                            'gender',
                            'phone_number'
                        ]
                    )
                    writer.writeheader()
                    writer.writerows(patients_list)
                print('\n'+'Message: Program successfully terminated')
                break

    def create_page(self):
        """This is a section to start create page"""
        while True:
            print(
                '\n'+"Are you sure to create a new patient's record?"+'\n'+
                '  1. Yes'+'\n'+
                '  2. No'
            )
            confirm = self.option_entry_handler(name='confirmation')
            if confirm:
                if confirm == 1:
                    print('\n'+' CREATE A NEW PATIENT RECORD '.center(150,'=')+'\n\n'+
                          'Please fill out the following information below')
                    new_record = self.Create()
                    new_record.saving_confirmation()
                else:
                    print('\n'+'Message: Back to Main Page')
                break

    def search_page(self):
        """This is a section to search a patient's record"""
        while True:
            print(
                '\n'+" PATIENT'S RECORDED DATABASE ".center(150,'=')+'\n\n'+
                "Please input an option number below to search a patient's record by"+'\n'+
                '  1. Search by Identification Number'+'\n'+
                '  2. Search by Name'+'\n'+
                '  3. Search by Phone Number'+'\n'+
                '  4. Back to Main Page'
            )
            sp_input = self.option_entry_handler(name='search page')
            if sp_input:
                if sp_input == 1:
                    id_number = self.num_entry_handler(name='Identification Number')
                    self.Search().filtered_by(on_keys='id_number',value=id_number)
                elif sp_input == 2:
                    name = self.alpha_entry_handler(name='Name')
                    self.Search().filtered_by(on_keys='name',value=name)
                elif sp_input == 3:
                    phone = self.num_entry_handler(name='Phone Number')
                    self.Search().filtered_by(on_keys='phone_number',value=phone)
                elif sp_input == 4:
                    print('\n'+'Message: Back to Main Page')
                    break

    def exit_page(self, terminate: bool):
        """This is a section to start exit confirmation page"""
        while True:
            print(
                '\n'+"Are you sure to exit from the program?"+'\n'+
                '  1. Yes'+'\n'+
                '  2. No'
            )
            confirm = self.option_entry_handler(name='confirmation')
            if confirm:
                if confirm == 1:
                    terminate = True
                elif confirm == 2:
                    print('\n'+'Message: Back to Main Page')
                break
        return terminate

    def birth_date_entry(self):
        """This is a method to input patient's birth date
        included error exception for the input to be correctly output"""

        # Get necessary dictionary for the next process
        dictionary = self.dictionary(name='month')

        # Input patient's year of birth
        year = self.num_entry_handler(name='Year of Birth')

        # Input patient's month of birth
        while True:
            print(
                '\n'+"Please input an option number below for patient's month of birth"+'\n'+
                '  1. January       7. July'+'\n'+
                '  2. February      8. August'+'\n'+
                '  3. March         9. September'+'\n'+
                '  4. April        10. October'+'\n'+
                '  5. May          11. November'+'\n'+
                '  6. June         12. December'
            )
            month = self.option_entry_handler(name='month')
            if month:
                break

        # Input patient's day of birth
        while True:
            try:
                day = int(input('\n'+"Patient's Day of Birth : "))
                if month in [4,6,9,11]:
                    if day <= 30:
                        break
                    print(
                        '\n'+f'Error: {dictionary.setdefault(month)}'+
                        ' only has 30 days'
                    )
                elif month in [1,3,5,7,8,10,12]:
                    if day <= 31:
                        break
                    print(
                        '\n'+f'Error: {dictionary.setdefault(month)}'+
                        ' only has 31 days'
                    )
                else:
                    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
                        if day <= 29:
                            break
                        print(
                            '\n'+f'Error: {dictionary.setdefault(month)}'+
                            ' only has 29 days'
                        )
                    else:
                        if day <= 28:
                            break
                        print(
                            '\n'+f'Error: {dictionary.setdefault(month)}'+
                            ' only has 28 days'
                        )
            except ValueError:
                print('\n'+'Error: Day of Birth only accepts numerics')
        return [day, month, year]

    def gender_entry(self):
        """This is a method to input patient's gender
        included error exception for the input to be correctly output"""

        # Get necessary dictionary for the next process
        dictionary = self.dictionary(name='gender')
        while True:
            print(
                '\n'+"Please input an option number below for patient's gender"+'\n'+
                '  1. Male'+'\n'
                '  2. Female'
            )
            gender = self.option_entry_handler(name='gender')
            if gender:
                return dictionary.setdefault(gender)

    class Create:
        """This is a section to create a new patient's record"""

        def __init__(self):
            """This is a section to instantiate necessary attributes"""
            self.id_number = self.check_duplicate()
            self.name = Initialize().alpha_entry_handler(name='Name')
            self.birth_place = Initialize().alpha_entry_handler(name='Place of Birth')
            self.birth_date = Initialize().birth_date_entry()
            self.gender = Initialize().gender_entry()
            self.phone = Initialize().num_entry_handler(name='Phone Number')

        def saving_confirmation(self):
            """This is a confirm section to store the new patient's record"""

            # Get necessary dictionary for the next process
            dictionary = Initialize().dictionary(name='month')
            while True:
                print(
                    '\n'+' NEW PATIENT RECORD '.center(150,'=')+'\n\n'+
                    f'  ID number\t  :  {self.id_number}'+'\n'+
                    f'  Name\t\t  :  {self.name}'+'\n'+
                    f'  Place of birth  :  {self.birth_place}'+'\n'+
                    '  Date of birth\t  :  '+
                    f'{dictionary.setdefault(self.birth_date[1])} '+
                    f'{self.birth_date[0]}, {self.birth_date[2]}'+'\n'+
                    f'  Gender\t  :  {self.gender}'+'\n'+
                    f'  Phone number\t  :  {self.phone}'+'\n'+
                    '\n'+"Will the new patient's record above created?"+'\n'+
                    '  1. Yes'+'\n'+
                    '  2. No'
                )
                confirm = Initialize().option_entry_handler(name='confirmation')
                if confirm:
                    if confirm == 1:
                        patient_new = {
                            'id_number':self.id_number,
                            'name':self.name,
                            'birth_place':self.birth_place,
                            'birth_date':self.birth_date,
                            'gender':self.gender,
                            'phone_number':self.phone
                        }
                        patients_list.append(patient_new)
                        print('\n'+"Message: The new patient's record successfully created")
                    elif confirm == 2:
                        print('\n'+"Message: The new patient's record not created")
                    break

        def check_duplicate(self):
            """This is a section to handle identification number duplicates"""
            while True:
                id_number = Initialize().num_entry_handler(name='Identification Number')
                for each in patients_list:
                    if id_number == each['id_number']:
                        print(
                            '\n'+
                            f'Error: Identification number of "{id_number}" is already existent'
                        )
                        break
                else:
                    return id_number

    class Search:
        """This is a section to search a patient's record"""

        def __init__(self):
            """This is a section to instantiate necessary attributes"""
            self.show_list = []

        def filtered_by(self, on_keys: str, value):
            """This is a section to search by identification number"""

            # Iterate all patient's record and get all intended search results
            for i in patients_list:
                if value == i.setdefault(on_keys):
                    self.show_list.append(i)

            # apply tabular template to show the search results
            print(
                '\n'+''.center(150,'=')+'\n'
                '|'+'No'.center(4,' ')+
                '|'+'Identification Number'.center(25,' ')+
                '|'+'Name'.center(40,' ')+
                '|'+'Place of Birth'.center(24,' ')+
                '|'+'Date of Birth'.center(23,' ')+
                '|'+'Gender'.center(10,' ')+
                '|'+'Phone Number'.center(16,' ')+'|\n'+
                ''.center(150,'=')
            )
            if len(self.show_list) != 0:
                for i, items in enumerate(self.show_list):
                    dictionary = Initialize().dictionary(name='month')
                    print(
                        '|'+str(i+1).center(4,' ')+
                        '|'+str(items['id_number']).center(25,' ')+
                        '|'+items['name'].center(40,' ')+
                        '|'+items['birth_place'].center(24,' ')+
                        '|'+(
                        f' {dictionary.setdefault(items["birth_date"][1])} '+
                        str(items['birth_date'][0])+', '+
                        str(items['birth_date'][2])
                        ).center(23,' ')+
                        '|'+items['gender'].center(10,' ')+
                        '|'+items['phone_number'].center(16,' ')+'|'
                    )
            else:
                dictionary = Initialize().dictionary(name="prompt")
                text = (
                    f'The patient with {dictionary.setdefault(on_keys)} of '+
                    f'"{value}" '+'is not found in our system'
                )
                print(
                    '|'+''.center(148,' ')+'|\n|'+text.center(148,' ')+'|\n'+
                    '|'+'Back to Search Page'.center(148,' ')+'|\n'+
                    '|'+''.center(148,' ')+'|'
                )
            print(''.center(150,'='))

            # if the search results exist, select a patient's record based-on index number
            if self.show_list:
                while True:
                    try:
                        idx = int(input('\n'+'Please input the index number: '))
                        if idx <= len(self.show_list) and idx != 0:
                            selected = self.show_list[idx-1]
                            print(
                                ' PATIENT RECORD '.center(150,'=')+'\n\n'+
                                f'  ID number\t  :  {selected["id_number"]}'+'\n'+
                                f'  Name\t\t  :  {selected["name"]}'+'\n'+
                                f'  Place of birth  :  {selected["birth_place"]}'+'\n'+
                                '  Date of birth\t  :  '+
                                f'{dictionary.setdefault(selected["birth_date"][1])} '+
                                f'{selected["birth_date"][0]}, {selected["birth_date"][2]}'+'\n'+
                                f'  Gender\t  :  {selected["gender"]}'+'\n'+
                                f'  Phone number\t  :  {selected["phone_number"]}'
                            )
                            self.modifier(result=selected)
                            break
                        print('\n'+'Error: Index number is invalid')
                    except ValueError:
                        print('\n'+'Error: Index number only accepts numeric')

        def modifier(self, result: dict):
            """This is a section to modify search-intended patient's record"""
            while True:
                print(
                    '\n'+"Please input option number below for modifying the intended record"+'\n'+
                    "  1. Update the patient's record"+'\n'+
                    "  2. Delete the patient's record"+'\n'+
                    '  3. Back to Search Page'
                )
                mod_input = Initialize().option_entry_handler(name='modifier')
                if mod_input:
                    if mod_input == 1:
                        self.update(data_input=result)
                    elif mod_input == 2:
                        self.delete(data_input=result)
                    else:
                        print('\n'+'Message: Back to Search Page')
                    break

        def delete(self, data_input: dict):
            """This is a section to delete a patient's record"""
            while True:
                print(
                    '\n'+"Are you sure to delete the patient's record?"+'\n'+
                    '  1. Yes'+'\n'+
                    '  2. No'
                )
                confirm = Initialize().option_entry_handler(name='confirmation')
                if confirm:
                    if confirm == 1:
                        patients_list.remove(data_input)
                        print('\n'+"Message: The patient's record succesfully deleted")
                    else:
                        print('\n'+"Message: The patient's record not deleted")
                    break

        def update(self, data_input: dict):
            """This is a section to update a patient's record"""
            dictionary = Initialize().dictionary(name='field')
            while True:
                print(
                    '\n'+'Which information would you like to update?'+'\n'+
                    '  1. Identification Number'+'\n'+
                    '  2. Name'+'\n'+
                    '  3. Place of Birth'+'\n'+
                    '  4. Date of Birth'+'\n'+
                    '  5. Gender'+'\n'+
                    '  6. Phone Number'+'\n'+
                    '  7. Back to Search Page'
                )
                up_input = Initialize().option_entry_handler(name='update')
                if up_input:
                    if up_input != 7:
                        field = dictionary.setdefault(up_input)
                        if up_input == 1:
                            replacer = Initialize().num_entry_handler(name='Identification Number')
                        elif up_input == 2:
                            replacer = Initialize().alpha_entry_handler(name='Name')
                        elif up_input == 3:
                            replacer = Initialize().alpha_entry_handler(name='Place of Birth')
                        elif up_input == 4:
                            replacer = Initialize().birth_date_entry()
                        elif up_input == 5:
                            replacer = Initialize().gender_entry()
                        elif up_input == 6:
                            replacer = Initialize().num_entry_handler(name='Phone Number')
                        self.updating_confirmation(
                            new_data=replacer,
                            old_data=data_input,
                            on_keys=field
                        )
                    else:
                        print('\n'+'Message: Back to Search Page')
                    break

        def updating_confirmation(self, new_data, old_data: dict, on_keys: str):
            """This is a section to confirm the patient's record alteration"""
            while True:
                print(
                    '\n'+'Are you sure to alter the information?'+'\n'+
                    '  1. Yes'+'\n'+
                    '  2. No'
                )
                confirm = Initialize().option_entry_handler(name='confirmation')
                if confirm:
                    if confirm == 1:
                        old_data[on_keys] = new_data
                        print('\n'+"Message: The patient's record succesfully updated")
                    else:
                        print('\n'+"Message: The patient's record not updated")
                    break

# This is a section you need to input your credentials
print('\n'+'Please input your credentials')
username_input = input('Username: ')
password_input = input('Password: ')

# This is a section to initialize the program
Initialize().main_page()
