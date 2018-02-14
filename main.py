import pickle

def ask():
    mode = input("1 for import, 2 for make: ")
    if mode == "1":
        quiz()
    elif mode == "2":
        make()
    else:
        print("Invalid input.")
        mode = input("1 for import, 2 for make ")

def make():
    filename = input("Filename to write: ")
    questions = {}
    name = input("What shall be the name of your quiz? ")
    numqs = 1
    i = 0
    while i < numqs:
        q = input("enter a question: ") + " "
        a = input("enter the answer to the question: \n" + q)
        questions[numqs] = [q, a]
        print(questions)
        again = input("Another question? (y/n): ")
        if again == "y":
            numqs = numqs + 1
            #print(numqs)
        elif again == "n":
            questions["info"] = [name, numqs]
            break
        else:
            print("Invalid input. ")
            again = input("Another question? (y/n): ")
    print(questions)
    filename = filename + ".qli"
    pickle.dump( questions, open(filename, "wb+") )
    print("Quiz written successfully to ", filename, " which you can now import and quiz yourself.  ")

def encrypt():
  pass

def get_filename():
    filename = input("Enter filename (before .qli): ")
    filename = filename + ".qli"
    try:
        pickle.load(open(filename, "rb"))
    except IOError:
        print('An error occured trying to read the file. \nCheck the name and try again.  Remember, just type name before .qli. \n')
        return "err"
    
    return filename

def quiz():
    #filename = input("Enter filename (before .qli): ")
    filename = get_filename()
    if filename == "err":
        get_filename()
    questions = pickle.load(open(filename, "rb"))
    #print(questions["info"][0])
    print(questions)
