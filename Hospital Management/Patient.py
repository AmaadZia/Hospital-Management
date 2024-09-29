class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            postcode (string): postcode
        """
        self.__first_name = first_name  # Set to the parameter value
        self.__surname = surname          # Set to the parameter value
        self.__age = age                  # Set to the parameter value
        self.__mobile = mobile            # Set to the parameter value
        self.__postcode = postcode        # Set to the parameter value
        self.__symptoms = []              # Initialize with an empty list
        self.__doctor = 'None'            # Initialize doctor as 'None'

    def full_name(self):
        """Return the full name, which is first_name and surname."""
        return f"{self.__first_name} {self.__surname}"  # Correctly combines first name and surname

    def get_doctor(self):
        """Return the name of the linked doctor."""
        return self.__doctor

    def link(self, doctor):
        """Link a doctor to this patient.
        
        Args:
            doctor (string): the doctor's full name
        """
        self.__doctor = doctor

    def add_symptom(self, symptom):
        """Add a symptom to the patient's symptom list."""
        self.__symptoms.append(symptom)

    def print_symptoms(self):
        """Print all the symptoms."""
        return ', '.join(self.__symptoms)  # Join the list into a string for better display

    def __str__(self):
        """Return a formatted string representation of the patient."""
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
