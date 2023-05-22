# get teacher names from command line, store it to an array, search by user input

teacher_names = []


def add_teacher_name():
    name = input("Enter teacher's name : ")
    teacher_names.append(name)
    if name in teacher_names:
        print("added successfully!")
    else:
        print("unexpected error!")
    return


def search_names():
    searched_name = input("Enter the name : ")
    if searched_name in teacher_names:
        index = teacher_names.index(searched_name)
        found_name = teacher_names[index]
        print(f"name found at block {index}")
    else:
        print("name not found")
    return


if __name__ == "__main__":
    end_program = False
    while not end_program:
        print("Enter your choice :")
        print("    1. add a teacher name")
        print("    2. search through existing teachers")
        print("    3. exit")
        choice = int(input())

        if choice == 1:
            add_teacher_name()
        elif choice == 2:
            search_names()
        elif choice == 3:
            end_program = True
        else:
            print("invalid input!")
