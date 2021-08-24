# All beginnings are difficult. Starting is easy. Perseverance is an art
from tkinter import *

root = Tk()

l1 = Label(root, text = "This is a login/signup system").grid(row=0, column=0)


option = Label(root, text="Do you want to signup or login").grid(row=1, column=0)


x = Entry(root)
x.grid(row=2, column=0)




def retrieve():
    x1 = x.get()
    if x1 == "signup":
        print("ok")
        username = input("create a username: ")
        password = input("create a password: ")
        f = open("credentials.txt", "a")
        f.writelines(username + "\n")
        f.writelines(password + "\n")
        f.close()


    if x1 == "login":
        print("ok")
        username = input("enter your username: ")
        password = input("enter your password: ")
        f = open("credentials.txt", "rt")
        word = f.read().split()
        if username in word and password in word:
            print("you are logged in")
        else:
            print("Your credentials could not be found.")


button = Button(root, text="submit", command=retrieve).grid(row= 3, column= 1)
root.mainloop()