f = open("myfile_3.txt", "a")

status = True
while status:
    name = input("Enter Student Name: ")
    f.write("\n "+name)
    choice = input("do you want to add more student press 'y' for yes: ")
    if choice == 'y':
        status = True
    else:
        status = False

f.close()