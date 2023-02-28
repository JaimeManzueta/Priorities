from tkinter import *

# defy the buttons 
def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height= listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height= listbox.size())

# the GUI
window = Tk()
window.title('Priorities')



# creating list 
listbox = Listbox(window, bg= 'white', font=('Arial',35),width= 12)
listbox.pack()

# the list
listbox.insert(1,"")
listbox.insert(2,"")
listbox.insert(3,"")

listbox.config(height= listbox.size())

# to type in 
entrybox = Entry(window)
entrybox.pack()
 
# buttons
delete_button = Button(window, text= 'delete',command= delete)
delete_button.pack()

add_button = Button(window, text= 'Add',command= add)
add_button.pack()

window.mainloop()



