todos = []

while True:
    user_action = input("Type add or show or edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter Todo: ")
            todos.append(todo)
        case 'show':
            item_number = 1
            for item in todos:
                print(item_number, item)
                item_number+=1
        case 'edit':
            index = int(input("Tell us which item you want to edit :- "))
            if(index> len(todos)):
                print("Enter Correct position dude")
            else :
                todos[index-1] = input("Please enter the edited todo:- ")
        case 'exit':
            break
        case whatever:
            print("Wrong Command dude!")

print('Bye!')