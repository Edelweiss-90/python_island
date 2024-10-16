#todo: Модифицировать программу таким образом чтобы она выводила
#  приветствие "Hello", которое до этого записано в файл text.txt
#  через метод write()

with open("text.txt", "w+") as file:
    file.write("Hello")
    file.seek(0)
    print(file.read())
