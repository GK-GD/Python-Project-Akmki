class Student:
    def __init__(self, student_SerialNumber, first_name, last_name, phone_number, register_number):
        self.student_SerialNumber = student_SerialNumber
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.register_number = register_number

class StudentManager:
    last_student_id = 0

    def __init__(self):
        self.students = []

    def get_next_student_id(self):
        StudentManager.last_student_id += 1
        return StudentManager.last_student_id

    def view_students(self, students=None):
        if students is None:
            students = self.students

        print("{:<10} {:<15} {:<15} {:<15} {:<15}".format("Serial", "Last Name", "First Name", "Phone", "ID"))
        for index, student in enumerate(students, start=1):
            print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(
                index, student.last_name, student.first_name, student.phone_number, student.register_number))
    
    def search_student(self, search_field, search_value):
        matching_students = []
        for student in self.students:
            if search_field == 1 and search_value.lower() in student.last_name.lower():
                matching_students.append(student)
            elif search_field == 2 and search_value.lower() in student.first_name.lower():
                matching_students.append(student)
            elif search_field == 3 and search_value in student.phone_number:
                matching_students.append(student)
            elif search_field == 4 and search_value in student.register_number:
                matching_students.append(student)

        return matching_students

    def register_student(self):
        while True:
            first_name = input("Enter student first name: ")
            if not (first_name.isalpha() and len(first_name) <= 15):
                print("Invalid input: First name must contain only alphabetic characters and be less than or equal to 15 characters.")
                continue

            last_name = input("Enter student last name: ")
            if not (last_name.isalpha() and len(last_name) <= 15):
                print("Invalid input: Last name must contain only alphabetic characters and be less than or equal to 15 characters.")
                continue

            phone_number = input("Enter student phone number: ")
            if not (phone_number.isdigit() and len(phone_number) == 10):
                print("Invalid input: Phone number must contain exactly 10 digits and no non-numeric characters.")
                continue

            register_number = self.get_next_student_id()

            new_student = Student(register_number, first_name, last_name, phone_number, str(register_number))
            self.students.append(new_student)
            print("Student registered successfully. Assigned Student ID:", register_number)
            break


    def delete_student(self):
        self.view_students() 

        while True:
            student_index = input("Enter the serial number of the student to delete (0 to cancel): ")

            try:
                student_index = int(student_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if student_index == 0:
                print("Deletion canceled.")
                return False

            if not (0 < student_index <= len(self.students)):
                print("Invalid input for student index. Please enter a valid serial number or 0 to cancel.")
                continue

            break

        deleted_student = self.students.pop(student_index - 1)
        print("Student deleted successfully.")
        return True

    def print_students_to_file(self):
        with open("students.txt", "w") as file:
            file.write("{:<10} {:<15} {:<15} {:<15} {:<15}\n".format(
                "Serial", "Last Name", "First Name", "Phone", "ID"))
            for index, student in enumerate(self.students, start=1):
                file.write("{:<10} {:<15} {:<15} {:<15} {:<15}\n".format(
                    index, student.last_name, student.first_name, student.phone_number, student.register_number))
                
def main():
    student_manager = StudentManager()

    while True:
        print("\nOptions:")
        print("1. View Students")
        print("2. Search Student")
        print("3. Register Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if not choice.isdigit() or int(choice) not in range(1, 6):
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        choice = int(choice)

        if choice == 1:
            try:
                with open("students.txt", "r") as file:
                    lines = file.readlines()
                    if lines:
                        print("Contents of students.txt:")
                        for line in lines:
                            print(line.strip())
                    else:
                        print("No students found in students.txt.")
            except FileNotFoundError:
                print("No students found in students.txt.")

        elif choice == 2:
            print("Search by:")
            print("1. Last Name")
            print("2. First Name")
            print("3. Phone Number")
            print("4. ID Number")
            search_field = input("Choose a search field (1-4): ")

            if not search_field.isdigit() or int(search_field) not in range(1, 5):
                print("Invalid input for search field. Please enter a number between 1 and 4.")
                continue

            search_field = int(search_field)

            search_value = input("Enter value to search: ")
            matching_students = student_manager.search_student(search_field, search_value)

            if matching_students:
                print("Matching students:")
                student_manager.view_students(matching_students)
            else:
                print("No matching students found.")
        elif choice == 3:
            student_manager.register_student()
            student_manager.print_students_to_file()
        elif choice == 4:
            while True:
                deletion_success = student_manager.delete_student()
                student_manager.print_students_to_file()
                if deletion_success:
                    continue_deletion = input("Do you want to delete another student? (yes/no): ")
                    if continue_deletion.lower() != "yes":
                        break

        elif choice == 5:
            print("Exiting the program. Goodbye!")
            input("Press Enter to exit...")
            break
if __name__ == "__main__":
    main()