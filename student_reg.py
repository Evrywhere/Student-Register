students = int(input("Please enter the amount of students registered."))
id_number = ""


with open('reg_form.txt', 'w')as reg_form:
    for i in range (0,students):
        id_number = (int(input("Please enter student ID numbers.")))
        id_number = id_number + 1
        with open('reg_form.txt', 'a') as file:
            file.write("Student ID numbers: \n" + (str(id_number)))
      

reg_form.close()
print ("Thank you, ID numbers saved to txt file reg_form")
