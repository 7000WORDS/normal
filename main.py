# All beginnings are difficult. Starting is easy. Perseverance is an art

print("This is a login/signup system")
x = input("Do you want to signup or login: ")
if x == "signup":
    print("ok")
    username = input("create a username: ")
    password = input("create a password: ")
    f = open("credentials.txt", "a")
    f.writelines(username + "\n")
    f.writelines(password + "\n")
    f.close()



if x == "login":
    print("ok")
    username = input("enter your username: ")
    password = input("enter your password: ")
    f = open("credentials.txt", "rt")
    word = f.read().split()
    if username in word and password in word:
        print("you are logged in")
    else:
        print("Your credentials could not be found.")
