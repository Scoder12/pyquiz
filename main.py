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
    numqs = 1
    filename = input("Filename to write: ")
    questions = [{}]
    name = input("What shall be the name of your quiz? ")
    questions[0] = {"name":name}
    i = 0
    while i < numqs:
        q = input("Enter a question: ") + " "
        a = input("Enter the answer to the question: \n" + q)
        questions.append({"q":q, "a":a})
        print(questions)
        again = input("Another question? (y/n): ")
        if again == "y":
            numqs = numqs + 1
            #print(numqs)
        elif again == "n":
            #print(questions[0]["numqs"])
            questions[0]["numqs"] = numqs
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
    err1 = False
    err2 = False
    while True:
        filename = input("Enter filename (before .qli): ")
        filename = filename + ".qli"
        try:
            questions = pickle.load(open(filename, "rb"))
        except IOError:
            print('An error occured trying to read the file. \nCheck the name and try again.  Remember, just type name before .qli. ErrorNo1\n')
            err1 = True
        except EOFError:
            print("\nFile does not contain valid quiz data.  ErrorNo2\n")
            err1 = True
        if err1 == False:
            try:
                questions = pickle.load(open(filename, "rb"))
            except EOFError:
                print("\nFile exists but does not contain valid quiz data.  ErrorNo3\n")
                err2 = True
            try:
               name = questions[0]["name"]
            except IndexError:
                print("\nFile exists, but doesn't contain valid quiz data.  ErrorNo4\n")
                err2 = True
            except UnboundLocalError:
                print("\nFile exists, but doesn't contain valid quiz data.  ErrorNo5\n")
                err2 = True
            if err2 == False:
                return filename

def quiz():
    filename = ""
    while True:
        filename = get_filename()
        if filename == "err":
            filename = get_filename()
        else:
            break
    print("Loading quiz from ", filename, "...")
    questions = pickle.load(open(filename, "rb"))
    numqs = questions[0]["numqs"]
    score = 0
    for i in range(numqs):
        l = i + 1
        ans = input(questions[l]["q"])
        if ans == questions[l]["a"]:
            print("\nCorrect! +1 points. ", (numqs - l), " questions remaining.  ")
            print("l is ", l, "and numqs is ", numqs)
            score = score + 1
        else:
            print("\nSorry, Incorrect! The correct answer was " + questions[l]["a"], "\nThere are ", (numqs - l), " questions remaining.  ")
    print("Congratulations! Your quiz is done. You scored ", score, "/", numqs)
    nhund = 100 / numqs
    print("(" + str(round(score * nhund, 1)) + "%)")
    print("Thanks for using py-quiz to administer " + questions[0]["name"], " =) ")



