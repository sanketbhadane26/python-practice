def get_marks():
    while True:
        try:
            marks = int(input("Enter student's marks: "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def get_name():
    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name

        print("Name cannot be empty.")