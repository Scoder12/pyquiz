import ast

def ask():
    mode = input("1 for import, 2 for make: ")
    if mode == "1":
        quiz()
    elif mode == "2":
        name = input("Filename: ")
        questions = input("Questions (dictionary): ")
        make(name, questions)
    else:
        print("Invalid input.")
        mode = input("1 for import, 2 for make ")

def make(filename, qlist):
    filename = filename + ".qli"
    f = open(filename, "w+")
    f.write(str(qlist))
    f.close()
    f = open(filename, "r")
    print(ast.literal_eval(f.read())["qone"])

def encrypt():
  pass
