from tkinter import *
import requests


def add_car(self):
    class_instance = Appliction()
    class_instance.car_handler()
    response = requests.get('http://localhost:5000/cars/')
    cars = response.json()

    for car in cars:
        line = f'{car["car"]} {car["model"]}{car["year"]}\n'
        self.car_list.insert(END, line)

def edit_car():
    return
def remove_car():
    return
def add_customer():
    return
def edit_customer():
    return
def remove_customer():
    return

class Appliction(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.btn_car = Button(self, text='Manage car',
                              command=self.car_handler,
                              width= 20)
        self.btn_car.pack()

        self.btn_customer = Button(self, text= 'Manage customer',
                                   command='',
                                    width= 20)
        self.btn_customer.pack()

        self.btn_customer_to_car = Button(self, text='Assign car to customer', command='', width= 20)
        self.btn_customer_to_car.pack()


    def car_handler(self):
        carWindow = Toplevel()

        car_text = StringVar()
        car_label = Label(carWindow, text='Car', font=('bold', 14))
        car_label.grid(row=0, column=0, sticky=W)
        car_entry = Entry(carWindow, textvariable=car_text)
        car_entry.grid(row=0, column=1)

        model_text = StringVar()
        model_label = Label(carWindow, text='Model', font=('bold', 14))
        model_label.grid(row=1, column=0, sticky=W)
        model_entry = Entry(carWindow, textvariable=model_text)
        model_entry.grid(row=1, column=1)

        year_text = StringVar()
        year_label = Label(carWindow, text='Year', font=('bold', 14))
        year_label.grid(row=2, column=0, sticky=W)
        year_entry = Entry(carWindow, textvariable=year_text)
        year_entry.grid(row=2, column=1)

        #Create list
        car_list = Text(carWindow, height=8, width = 50)
        car_list.grid(row=3, column=0, columnspan=5, rowspan=6, pady=20, padx=20)


        #Buttons
        add_btn = Button(carWindow, text= 'Add car', width= 12, command= add_car)
        add_btn.grid(row=0, column=4, pady=20)
        edit_btn = Button(carWindow, text= 'Edit car', width= 12, command= edit_car)
        edit_btn.grid(row=1, column=4, pady=20)
        remove_btn = Button(carWindow, text= 'Remove car', width= 12, command= remove_car)
        remove_btn.grid(row=2, column=4, pady=20)

        carWindow.title('Manage Car')
        carWindow.geometry('500x400+500+300')
        carWindow.configure(bg='brown')



def main():

    # Create the Tkinter main application top level object (often called root)
    root = Tk()

    # Set size and position of the window
    root.title('Car App')
    root.geometry('400x200+500+300')
    root.configure(bg='brown')

    # Add widgets here

    # Add window
    app = Appliction(master=root)
   # app.configure_menu()

    # Run the main loop
    app.mainloop()



if __name__ == '__main__':
    main()