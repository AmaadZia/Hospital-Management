class Doctor:
    """A class that deals with Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor's speciality
        """
        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    def full_name(self):
        """Return the full name of the doctor."""
        return f"{self.__first_name} {self.__surname}"  # Correctly combines first name and surname

    def get_first_name(self):
        """Return the first name of the doctor."""
        return self.__first_name

    def set_first_name(self, new_first_name):
        """Set a new first name for the doctor."""
        self.__first_name = new_first_name

    def get_surname(self):
        """Return the surname of the doctor."""
        return self.__surname

    def set_surname(self, new_surname):
        """Set a new surname for the doctor."""
        self.__surname = new_surname

    def get_speciality(self):
        """Return the speciality of the doctor."""
        return self.__speciality  # Fixed to return the correct attribute

    def set_speciality(self, new_speciality):
        """Set a new speciality for the doctor."""
        self.__speciality = new_speciality

    def add_patient(self, patient):
        """Add a patient to the doctor's patient list."""
        self.__patients.append(patient)

    def __str__(self):
        """Return a formatted string representation of the doctor."""
        return f'{self.full_name():^30}|{self.__speciality:^15}'

