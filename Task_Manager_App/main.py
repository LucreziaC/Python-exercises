#from functions import get_todos, write_todo
import functions
import time

now= time.strftime("%b %d, %Y %h:%M:S")
print("It is", now)

prompt = "type add,show, edit, complete or exit: "

while True:
    user_action = input(prompt).strip()

    # match user_action.strip():

    if user_action.startswith("add"):
        
        todo = user_action[4:]
        todos= functions.get_todos()
        todos.append(todo + "\n")
        functions.write_todo(todos)



    elif user_action.startswith("show"):

        todos= functions.get_todos()
     

        # new_todos= [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            # print(index, '-', item)
            row = f"{index+1}-{item.strip('\n')}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            todos= functions.get_todos()
                
            new_todo = input("Insert the new todo to replace: ")

            todos[number] = new_todo + "\n"

            functions.write_todo(todos)


            for index, item in enumerate(todos):
                # print(index, '-', item)
                row = f"{index+1}-{item.strip('\n')}"
                print(row)
                
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            todos= functions.get_todos()

            for index, item in enumerate(todos):
                # print(index, '-', item)
                row = f"{index+1}-{item.strip('\n')}"
                print(row)

            number = user_action[9:]
            todo_to_remove = todos[int(number) - 1]
            todos.pop(int(number) - 1)

            functions.write_todo(todos)


            print(
                "/n"
                + f"Todo {todo_to_remove.strip('\n')} was removed from the list. This is the new list: "
            )

            for index, item in enumerate(todos):
                # print(index, '-', item)
                row = f"{index+1}-{item.strip('\n')}"
                print(row)
        except IndexError:
            print("There is no tiem with that number")

    elif user_action.startswith("exit"):
        break

    else:
        print("command not valid")

print("Bye!")



