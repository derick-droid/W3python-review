import sys

# reading the file


def reading_file(name):
    content = []
    ifile = open(name, "r")
    file_read = ifile.readline()
    for item in file_read:
        new_list = []
        line = line[:-1].split(" ")
        new_list.append((" ".join(line[:-1])))
        new_list.append(line[-1])
        content.append(new_list)
    ifile.close()
    return content

# ask the user to provide alist for updating


def menu():
    print("\nMenu: \n0 to Exit\n1 to search entries\n3 to delete an entry\n4 to print entries\n")
    choice = int(input("please choose the option: "))
    return choice

# code helping to print all the entries


def entries(phonelist):
    print("\nNAME\t\t\t\tphone number ")

    for user_information in phonelist:
        print("{:<32}{:s}".format(user_information[0],user_information[1]))

#      to add content to the phone txt file


def writefile(filename, phonebook):
    print(phonebook)
    ifile = open(filename, "w")

    for user_info in phonebook:
        ifile.write(" ".join(user_info) + "\n")
        ifile.close()

#  to ask for name search


def search(phonebook):
    name = input("Enter name: ")
    for item in phonebook:
        if item[0] == name:
            print("\nName: ", item[0])
            print("phone: ", item[1])
            break

        else:
            print("\n name not found")

#  to delete


def delete(phonebook):
    name = input("Enter name: ")
    for item in phonebook:
        if item[0] == name:
            phonebook.remove(item)

# add function


def add(phonebook):
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    phonebook.append([name, number])


# the implementation function

def implement():
    phonebook = reading_file("phone.txt")

    while True:
        user_choice = menu()
        if user_choice == 0:
            writefile("phne.txt", phonebook)
            sys.exit()

        elif user_choice == 1:
            search(phonebook)
        elif user_choice == 2:
            add(phonebook)
        elif user_choice == 3:
            delete(phonebook)

        elif user_choice == 4:
            print(entries(phonebook))


if __name__ == "__implement__":
    implement()

