import datetime
date = datetime.datetime.now()
d = date.date()
date_str = (str)(d)
file = open(date_str,'a')
while True:
    name = input("Enter Coustomer's Name: ")
    no = input("Enter Mobile Number: ")
    gender = input("Enter Gender: ")
    vacc_dose = input("Enter Vaccination does with name: ")
    date_now = (str)(date)
    file.write(date_now)
    file.write("\n")
    file.write(f"\nName: {name} \n")
    file.write(f"Mobile Number: {no} \n")
    file.write(f"Gender : {gender} \n")
    file.write(f"Vaccination Name and Dose: {vacc_dose}\n")
    file.write(f"------------------------------------------------------------")
    again = input("Do u want to add more patients here \'y/n\': ").lower()
    if again == 'y':
        continue
    elif again == 'n':
        print("File Saved")
        file.close()
        break
    else:
        print("Invalid Input \n File Saved")
        file.close()
        break 
    

