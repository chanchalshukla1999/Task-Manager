import datetime

# (user data function) which take data from signup function and make a text file to save user data
def user_information(User_name,Pass_word):
    name = input("Enter your name:")
    address = input("Enter your address:")
    age = input("Enter your age:")
    User_name_ = User_name+"task.txt" 
    f = open(User_name_,"a")
    f.write(Pass_word)
    f.write("\nName:")
    f.write(name)
    f.write("\n")
    f.write("Address:")

    f.write(address)
    f.write("\n")
    f.write(age)
    f.write("\n")
    f.close()

def signup():
    print("Kindly enter the username which you wanna access your account:")
    username = input("Enter Your Username: ")
    password = input("Enter your password: ")
    user_information(username,password)
    print("Mam kindly proceed towards log in -->")
    login()


def login():
    print("Kindly Enter Your Username:")
    user_ln = input("Enter here:")

    pass_ln = (input("Enter your password: "))+ "\n"
    try:

        user_ln = user_ln+"task.txt"
        f_ = open(user_ln,"r")

        k = f_.readlines(0)[0]
        f_.close()

        if pass_ln ==k:
            print("1--To view your data \n2--To add task \n3--Update task \n4--view task status")
            a = input()

            if a == '1':
                view_data(user_ln)
            elif a == '2':
                # add task
                task_information(user_ln)
            elif a == '3':
                task_update(user_ln)
            elif a == '4':
                task_update_viewer(user_ln)
            else:
                print("Wrong input ! Bhen")
        else:
            print("Sir/Mam your Password and username is wrong")
            login()
    except Exception as e:
        print(e)
        login()

def view_data(username):
    ff = open(username,"r")
    print(ff.read())
    ff.close()

def task_information(username):
    print("Sir enter n.o of task you want to ADD -->")
    j =int(input())
    f1 = open(username,"a")

    for i in range(1,j+1):
        task = input("Enter the task:")
        target = input("Enter the target:")
        pp = "Task" +str(i)+" :"
        qq = "Target"+str(i)+" :"

        f1.write(pp)
        f1.write(task)
        f1.write("\n")
        f1.write(qq)
        f1.write(target)
        f1.write("\n")
        
        print("Do you want to stop type YES otherwise enter:")
        s = input()
        if s =="YES":
            break
    f1.close()


def task_update(username):
    username = username+ "task.txt"
    print("Kindly enter the task which are completed:")

    task_completed = input()
    print("Enter the task which are still not started by you")

    task_not_started = input()
    print("Enter task which are you doing:")

    task_ongoing = input()
    fw = open(username,"a")
    Dt = str(datetime.datetime.now())

    fw.write(Dt)
    fw.write("\n")
    fw.write("COMPLETED TASK \n")
    fw.write(task_completed)
    fw.write("\n")
    fw.write("ONGOING TASK \n")
    fw.write(task_ongoing)
    fw.write("\n")
    fw.write("NOT YET STARTED \n")
    fw.write(task_not_started)
    fw.write("\n")

def task_update_viewer(username):
    username = username+"task.txt"
    o = open(username,"r")
    print(o.read())
    o.close()

if __name__ == "__main__":
    print("WELCOME CHANCHAL SHUKLA'S TASK MANAGER:")
    print("MAM ARE YOU NEW TO THIS SOFTWARE")
    a = int(input("Type 1 if new otherwise press 0 ::"))

    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("YOU HAVE PROVIDED WRONG INPUT!")









    


