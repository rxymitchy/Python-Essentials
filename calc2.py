class Calculator:
    def __init__(self):
        input_lists = []
        input_lists = input("Enter a list element separated by space: ")
        user_list = input_lists.split()

        cleaned_list = []
        for num in user_list:
            cleaned_list.append(int(num))

        self.ilist = cleaned_list

    def add(self):
        add = sum(self.ilist)

        return add

    def sub(self):
        sub = self.ilist[0]
        for numbers in range(1, len(self.ilist)):
            print(sub)
            sub -= self.ilist[numbers]
            print(sub)

        return sub

    def multiply(self):
        times = self.ilist[0]
        for numbers in range(1, len(self.ilist)):
            times *= self.ilist[numbers]

        return times

    def divide(self):
        div = self.ilist[0]
        for numbers in range(1, len(self.ilist)):
            if self.ilist[numbers] != 0:
                div /= self.ilist[numbers]

        return div


def menu():
    operator_menu = ('1. Add \n2. Sub \n3. Multiply \n4. Divide \n5.Quit')
    print(operator_menu)


while True:
    menu()
    choice = int(input('Please select one of the following : '))

    if choice == 5:
        exit()

    try:
        obj = Calculator()
    except ValueError:
        print("Insert numbers only")
        break
    except Exception:
        print("Something else went wrong")
        break

    if choice == 1:
        print("Result: ", obj.add())

    elif choice == 2:
        print("Result: ", obj.sub())

    elif choice == 3:
        print("Result: ", obj.multiply())

    elif choice == 4:
        print("Result: ", obj.divide())

    else:
        print('Invalid option')
