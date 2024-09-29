# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    The main function to be run when the program starts.
    """

    # Initialising the actors
    admin = Admin('admin', '123', 'B1 1AB')  # username is 'admin', password is '123'
    doctors = [
        Doctor('John', 'Smith', 'Internal Med.'),
        Doctor('Jone', 'Smith', 'Pediatrics'),
        Doctor('Jone', 'Carlos', 'Cardiology')
    ]
    patients = [
        Patient('Sara', 'Smith', 20, '07012345678', 'B1 234'),
        Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB'),
        Patient('David', 'Smith', 15, '07123456789', 'C1 ABC')
    ]
    discharged_patients = []

    # Keep trying to login until the login details are correct
    while True:
        if admin.login():
            running = True  # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # Print the menu
        print('Choose the operation:')
        print(' 1 - Register/View/Update/Delete doctor')
        print(' 2 - Discharge patients')
        print(' 3 - View discharged patients')
        print(' 4 - Assign doctor to a patient')
        print(' 5 - Update admin details')
        print(' 6 - Quit')

        # Get the option
        op = input('Option: ')

        if op == '1':
            # 1 - Register/View/Update/Delete doctor
            admin.doctor_management(doctors)

        elif op == '2':
            # 2 - Discharge patients
            admin.view_patient(patients)  # Show current patients before discharging
            while True:
                discharge_option = input('Do you want to discharge a patient (Y/N): ').lower()
                if discharge_option in ['yes', 'y']:
                    admin.discharge(patients, discharged_patients)  # Pass both lists for discharging
                elif discharge_option in ['no', 'n']:
                    break
                else:
                    print('Please answer with yes or no.')

        elif op == '3':
            # 3 - View discharged patients
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4 - Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5 - Update admin details
            admin.update_details()

        elif op == '6':
            # 6 - Quit
            print("System is now being exited.\nGoodbye!")
            running = False  # Exit the loop to quit

        else:
            # The user did not enter an option that exists in the menu
            print('Invalid option. Try again.')

if __name__ == '__main__':
    main()
