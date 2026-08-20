student={}
def check_status(code):
    match code:
        case 1:
            print("1. Add Student")
            name=input("Enter Student name : ")
            marks = int(input("Enter Students marks : "))
            student[name]=marks
        case 2:
            print("Search student")
            search_name=input("Enter student name to search : ")
            if search_name in student:
                print(f"Student found {search_name} marks = {student[search_name]}")
            else :
                print("Student not found")
        case 3:
            print("Update marks")
            u_name=input("Enter Student name : ")
            if u_name in student:
                update_marks=int(input("Enter Students new marks to update : "))
                student[u_name]=update_marks 
            else :
                print("Student not found")
            
            
        case 4:
            print("Delete student")
            d_name=input("Enter Student name to delete : ")
            if d_name in student:
                student.pop(d_name)
                print("Student deleted")
            else:
                print("Student not found")
        case 5:
            print("Display Students")
            for i in student.items():
                print(i)
        case 6:
            print("Exit")
            print("End of program")
            exit()


user_input = input("Do you want to start y/n? ")

while user_input == 'y':

    print("Menu")
    print("1 = Add Student")
    print("2 = Search student")
    print("3 = Update marks")
    print("4 = Delete student")
    print("5 = Display Students")
    print("6 = Exit")

    code = int(input("Enter your choice: "))

    check_status(code)

    user_input = input("Do you want to start again y/n? ")