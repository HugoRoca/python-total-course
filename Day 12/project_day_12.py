from tkinter import *

# Init tkinter
app = Tk()

# custom
# height nd with
app.geometry('1200x630+0+0')
# title
app.title('Restaurant app')
# background
app.config(bg='burlywood')

# panel
panel_superior = Frame(app, bd=1, relief=FLAT)
panel_left = Frame(app, bd=1, relief=FLAT)
panel_cost = Frame(panel_left, bd=1, relief=FLAT)
panel_food = LabelFrame(panel_left, text='Food', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, bg='azure4')
panel_drink = LabelFrame(panel_left, text='Drink', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, bg='azure4')
panel_dessert = LabelFrame(panel_left, text='Dessert', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, bg='azure4')
panel_right = Frame(app, bd=1, relief=FLAT)
panel_calculator = Frame(panel_right, bd=1, relief=FLAT, bg='burlywood')
panel_ticket = Frame(panel_right, bd=1, relief=FLAT, bg='burlywood')
panel_buttons = Frame(panel_right, bd=1, relief=FLAT, bg='burlywood')

panel_superior.pack(side=TOP)
panel_left.pack(side=LEFT)
panel_cost.pack(side=BOTTOM)
panel_food.pack(side=LEFT)
panel_drink.pack(side=LEFT)
panel_dessert.pack(side=LEFT)
panel_right.pack(side=RIGHT)
panel_calculator.pack()
panel_ticket.pack()
panel_buttons.pack()

# list products
list_food = ['chicken', 'Fish', 'Salmon', 'Kelab', 'Pizza', 'KFC', 'Chaufa rice', 'eggs', 'hotdog', 'ramen', 'cachanga']
list_drink = ['Wine', 'Ron', 'Juice', 'Water', 'Bear', 'Bear Pilsen', 'soda', 'chicha', 'evian', 'inka cola', 'coca cola']
list_dessert = ['ice', 'fruit', 'flan', 'mousse', 'cake', 'chocolate cake', 'brownies', 'arroz con leche', 'humita', 'wawa', 'pan']
count = 0
variables_food = []

for food in list_food:
    variables_food.append('')
    variables_food[count] = IntVar()
    foodChk = Checkbutton(panel_food, text=food.title(), font=('Dosis', 19, 'bold'),
                          onvalue=1, offvalue=0, variable=variables_food[count])
    foodChk.grid(row=count, column=0, sticky=W)
    count += 1

count = 0
variables_drink = []

for drink in list_drink:
    variables_drink.append('')
    variables_drink[count] = IntVar()
    drinkChk = Checkbutton(panel_drink, text=drink.title(), font=('Dosis', 19, 'bold'),
                          onvalue=1, offvalue=0, variable=variables_drink[count])
    drinkChk.grid(row=count, column=0, sticky=W)
    count += 1

count = 0
variables_dessert = []

for dessert in list_dessert:
    variables_dessert.append('')
    variables_dessert[count] = IntVar()
    dessertChk = Checkbutton(panel_dessert, text=dessert.title(), font=('Dosis', 19, 'bold'),
                          onvalue=1, offvalue=0, variable=variables_dessert[count])
    dessertChk.grid(row=count, column=0, sticky=W)
    count += 1
# tags
tag_title = Label(panel_superior, text='Restaurant app', fg='azure4',
                  font=('Dosis', 58), bg='burlywood', width=27)
tag_title.grid(row=0, column=0)

# avoid resize
app.resizable(False, False)

# Avoid that screen close
app.mainloop()
