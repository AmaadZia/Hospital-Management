from Doctor import Doctor

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """
        self.__username = username
        self.__password = password
        self.__address =  address


    def view(self, a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')


    def login(self):
        """
        A method that handles admin login
        Raises:
            Exception: If the username and password don't match.
        Returns:
            bool: True if login is successful, otherwise False
        """
        print("-----Login-----")
        # Get the details of the admin
        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if self.__username == username and self.__password == password:
            return True
        else:
            print("Incorrect username or password.")
            return False
        

    def find_index(self, index, doctors):
        """
        Checks if a given index is valid within the range of doctors list
        Args:
            index (int): Index of the doctor
            doctors (list): List of doctors
        Returns:
            bool: True if valid, False otherwise
        """
        if index in range(0, len(doctors)):
            return True
        else:
            return False
            
    def get_doctor_details(self):
        """
        Get the details needed to add a doctor
        Returns:
            tuple: first name, surname and speciality of the doctor
        """
        first_name = input('Enter the first name: ')
        surname = input('Enter the surname: ')
        speciality = input('Enter the speciality: ')
        
        return first_name, surname, speciality
        

    def doctor_management(self, doctors):
        """
        A method that handles registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Doctor Management-----")
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
        op = input('Input: ')

        # Register
        if op == '1':
            print("-----Register-----")
            first_name, surname, speciality = self.get_doctor_details()

            # Check if the doctor already exists
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Doctor already exists.')
                    return  # Exit if doctor exists

            new_doctor = Doctor(first_name, surname, speciality)
            doctors.append(new_doctor)
            print('Doctor registered successfully.')
            self.view(doctors)

        # View Doctors
        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)
        
        # Update Doctor
        elif op == '3':
            print("-----Update Doctor-----")
            self.view(doctors)
            try:
                index = int(input('Enter the ID of the doctor: ')) - 1
                if self.find_index(index, doctors):
                    doctor = doctors[index]
                    
                    # Update Menu
                    print('Choose the field to update:')
                    print(' 1 - First name')
                    print(' 2 - Surname')
                    print(' 3 - Speciality')
                    op = int(input('Input: '))

                    if op == 1:
                        first_name = input('Enter the new first name: ')
                        doctor.set_first_name(first_name)

                    elif op == 2:
                        surname = input('Enter the new surname: ')
                        doctor.set_surname(surname)

                    elif op == 3:
                        speciality = input('Enter the new speciality: ')
                        doctor.set_speciality(speciality)

                    print('Doctor details updated.')
                else:
                    print("Doctor not found.")
            except ValueError:
                print('Invalid ID entered.')

        # Delete Doctor
        elif op == '4':
            print("-----Delete Doctor-----")
            self.view(doctors)
            try:
                index = int(input('Enter the ID of the doctor to delete: ')) - 1
                if self.find_index(index, doctors):
                    doctors.pop(index)
                    print('Doctor deleted successfully.')
                    self.view(doctors)
                else:
                    print('Doctor not found.')
            except ValueError:
                print('Invalid ID entered.')

        else:
            print('Invalid operation chosen. Check your input!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)
        

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")
        self.view(patients)

        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
            if patient_index not in range(len(patients)):
                print('The patient ID entered was not found.')
                return

            print("-----Doctors-----")
            self.view(doctors)

            doctor_index = int(input('Please enter the doctor ID: ')) - 1
            if self.find_index(doctor_index, doctors):
                doctor = doctors[doctor_index]
                patient = patients[patient_index]
                doctor.add_patient(patient)  # Link patient to doctor
                print('Doctor assigned to the patient.')
            else:
                print('The doctor ID entered was not found.')

        except ValueError:
            print('Invalid ID entered.')


    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        self.view(patients)

        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
            if patient_index in range(len(patients)):
                discharged_patient = patients.pop(patient_index)
                discharged_patients.append(discharged_patient)
                print(f"Patient {discharged_patient} has been discharged.")
            else:
                print('Invalid patient ID.')

        except ValueError:
            print('Invalid input. Please enter a valid number.')


    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharged Patients-----")
        self.view(discharged_patients)


    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """
        print('Choose the field to update:')
        print(' 1 - Username')
        print(' 2 - Password')
        print(' 3 - Address')
        op = int(input('Input: '))

        if op == 1:
            username = input('Enter the new username: ')
            if username == input('Enter the new username again: '):
                self.__username = username
                print('Username updated successfully.')

        elif op == 2:
            password = input('Enter the new password: ')
            if password == input('Enter the new password again: '):
                self.__password = password
                print('Password updated successfully.')

        elif op == 3:
            address = input('Enter the new address: ')
            if address == input('Enter the new address again: '):
                self.__address = address
                print('Address updated successfully.')

        else:
            print("Invalid input.")


