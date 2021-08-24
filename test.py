from tkinter import *

f = open("credentials.txt", "rt")
word = f.read().split()

root = Tk()

l1 = Label(root, text= "username").grid(row=0, column=0)
my_entry = Entry(root)
my_entry.grid(row=0, column=1)


l2 = Label(root,text='password').grid(row=1, column=0)
my_entry2= Entry(root, show="*")
my_entry2.grid(row=1,column=1)

def retrieve():
    username = my_entry.get()
    password = my_entry2.get()
    if username and password in word:
        print("You are logged in")
        root.quit()


        root1 = Tk()
        l3 = Label(root1, text="you're logged in")
        
        l3.pack()
        root1.mainloop()
    else:
        print("We could not find your credentials")
        root2 = Tk()
        
        l4 = Label(root2, text="We could not find your credentials.")

        l4.pack()
        root2.mainloop()


button = Button(root, text="submit", command=retrieve).grid(row=4, column=0)
root.mainloop()