# All beginnings are difficult. Starting is easy. Perseverance is an art
from tkinter import *

root = Tk()
f = open("credentials.txt", "rt")

l1 = Label(root, text = "This is a login/signup system").grid(row=0, column=0)

option = Label(root, text="Do you want to signup or login").grid(row=1, column=0)

x = Entry(root)
x.grid(row=2, column=0)

def loginsys():
    x1 = x.get()
    if x1 == "signup":
        root4 = Tk()
        print("signup system online")
        
        l1 = Label(root4, text = "username").grid(row= 0, column = 0)
        my_entry3 = Entry(root4)
        my_entry3.grid(row = 0, column = 1)

        l2 = Label(root4, text = "password").grid(row = 1, column = 0)
        my_entry4 = Entry(root4)
        my_entry4.grid(row = 1 , column = 1)
        
        
        global f
      
        def signup():
            f = open("credentials.txt", "a")
            f.writelines(str(my_entry3.get()) + "\n")
            f.writelines(str(my_entry4.get()) + "\n")
            print("signup complete")
            f.close()
        button2  = Button(root4, text = "submit", command =  signup).grid(row = 4, column=0)
        root4.mainloop()
        root.quit()
    

    if x1 == "login":
        root1 = Tk()
        print("login system online")
        word = f.read().split()

        l1 = Label(root1, text= "username").grid(row=0, column=0)
        my_entry = Entry(root1)
        my_entry.grid(row=0, column=1)


        l2 = Label(root1,text='password').grid(row=1, column=0)
        my_entry2= Entry(root1, show="*")
        my_entry2.grid(row=1,column=1)

        def retrieve():
            username = my_entry.get()
            password = my_entry2.get()
            if username and password in word:
                print("You are logged in")
                root1.quit()


                root2 = Tk()
                l3 = Label(root2, text="you're logged in")
                
                l3.pack()
                root2.mainloop()
            else:
                print("We could not find your credentials")
                root3 = Tk()
                
                l4 = Label(root3, text="We could not find your credentials.")

                l4.pack()
                root3.mainloop()
        button = Button(root1, text="submit", command=retrieve).grid(row=4, column=0)



button = Button(root, text="submit", command=loginsys).grid(row= 3, column= 1)
root.mainloop()
