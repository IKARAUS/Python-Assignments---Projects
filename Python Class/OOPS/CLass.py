# self is key words which is refer current class property
class student:
    def all_student(self):
        student_list = []
        
        status = True
        while status:
            name = input("Enter student name: ")
            student_list.append(name)
            choice = input("Do you want to enter more name : press 'y' for yes and 'n' for no")
            if choice == 'n' or choice == 'no':
                status = False
                
s_obj = student
s_obj.all_student()