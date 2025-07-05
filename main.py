prompt = "Enter a todo:"
todos = []
i =0
while i<5:
    user_text = input(prompt)
    todos.append(user_text)
    i = i + 1
# user_text = input(prompt)
print("todo's are: - ")
print(todos)