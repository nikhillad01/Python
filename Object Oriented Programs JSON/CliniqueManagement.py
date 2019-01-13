from JSON import OOPS_Utility
cliniqueManagement_obj = OOPS_Utility.CliniqueManagement()

if __name__ == '__main__':


    patient_file=cliniqueManagement_obj.read_Json_file_of_Patient()
    appointment_file=cliniqueManagement_obj.readJsonfileofAppoinment()
    cliniqueManagement_obj.getUserInput()