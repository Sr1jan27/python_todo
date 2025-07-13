todos = []

while True:
    user_action = input("Type add or show or edit or complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter Todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            for item_number, item in enumerate(todos):
                # row = f"{item_number+1}->{item}"
                print(f"{item_number+1}->{item}")
        case 'edit':
            index = int(input("Tell us which item you want to edit :- "))
            if index> len(todos):
                print("Enter Correct position dude")
            else :
                todos[index-1] = input("Please enter the edited todo:- ")
        case 'complete':
            completed_ToDo = input("Which ToDo is complete?")
            todos.remove(completed_ToDo)
        case 'exit':
            break
        case whatever:
            print("Wrong Command dude!")

print('Bye!')