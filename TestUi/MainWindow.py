from tkinter import Tk, Menu, Menubutton

class MainWindow(object):
    
    def __init__(self, root):
        self.root = root
        self.ui = object()
        self.ui.script_menu = None;
        root.title("Main")
        self.init_menu()
        
    def init_menu(self):
        # create a toplevel menu
        menu_bar = Menu(self.root)
        
        # add file menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=None)
        file_menu.add_command(label="Save", command=None)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # add script menu
        script_menu = Menu(menu_bar, tearoff=0)
        self.ui.script_menu = script_menu
        menu_bar.add_cascaded(label="Scripts", menu=script_menu)
        script_menu.add_command(label="Run selected", command = None);
        
        # display the menu
        root.config(menu=menu_bar)

'''
        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

'''
'''  
    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)
'''

root = Tk()
main_gui = MainWindow(root)
root.mainloop()