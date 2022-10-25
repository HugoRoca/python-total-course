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
panel_cost = Frame(panel_left, bd=1, relief=FLAT, bg='azure4', padx=50)
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
list_food = ['chicken', 'Fish', 'Salmon', 'Kelab', 'Pizza', 'KFC', 'Chaufa', 'eggs', 'hotdog', 'ramen', 'cachanga']
list_drink = ['Wine', 'Ron', 'Juice', 'Water', 'Bear', 'Bear Pilsen', 'soda', 'chicha', 'evian', 'inka cola', 'coca']
list_dessert = ['ice', 'fruit', 'flan', 'mousse', 'cake', 'chocolate', 'brownies', 'arroz con leche', 'humita', 'wawa', 'pan']
count = 0
variables_food = []
food_box = []
food_text:list = []

for food in list_food:
    variables_food.append('')
    variables_food[count] = IntVar()
    foodChk = Checkbutton(panel_food, text=food.title(), font=('Dosis', 14, 'bold'),
                          onvalue=1, offvalue=0, variable=variables_food[count])
    foodChk.grid(row=count, column=0, sticky=W)

    food_box.append('')
    food_text.append('')
    food_text[count] = StringVar()
    food_text[count].set('0')
    food_box[count] = Entry(panel_food, width=6, font=('Dosis', 14, 'bold'), bd=1, state=DISABLED, textvariable=food_text[count])
    food_box[count].grid(row=count, column=1, sticky=W)
    count += 1

count = 0
variables_drink = []
drink_box = []
drink_text:list = []

for drink in list_drink:
    variables_drink.append('')
    variables_drink[count] = IntVar()
    drinkChk = Checkbutton(panel_drink, text=drink.title(), font=('Dosis', 14, 'bold'),
                          onvalue=1, offvalue=0, variable=variables_drink[count])
    drinkChk.grid(row=count, column=0, sticky=W)

    drink_box.append('')
    drink_text.append('')
    drink_text[count] = StringVar()
    drink_text[count].set('0')
    drink_box[count] = Entry(panel_drink, width=6, font=('Dosis', 14, 'bold'), bd=1, state=DISABLED, textvariable=drink_text[count])
    drink_box[count].grid(row=count, column=1, sticky=W)
    count += 1

count = 0
variables_dessert = []
dessert_box = []
dessert_text:list = []

for dessert in list_dessert:
    variables_dessert.append('')
    variables_dessert[count] = IntVar()
    dessertChk = Checkbutton(panel_dessert, text=dessert.title(), font=('Dosis', 14, 'bold'),
                          onvalue=1, offvalue=0, variable=variables_dessert[count])
    dessertChk.grid(row=count, column=0, sticky=W)

    dessert_box.append('')
    dessert_text.append('')
    dessert_text[count] = StringVar()
    dessert_text[count].set('0')
    dessert_box[count] = Entry(panel_dessert, width=6, font=('Dosis', 14, 'bold'), bd=1, state=DISABLED, textvariable=dessert_text[count])
    dessert_box[count].grid(row=count, column=1, sticky=W)
    count += 1
# tags
tag_title = Label(panel_superior, text='Restaurant app', fg='azure4',
                  font=('Dosis', 58), bg='burlywood', width=27)
tag_title.grid(row=0, column=0)

# tags cost
tag_cost_food = Label(panel_cost, text='Food Cost', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
tag_cost_food.grid(row=0, column=0)

var_cost_food = StringVar()
text_cost_food = Entry(panel_cost, font=('Dosis', 12, 'bold'), width=10, bd=1, state='readonly', textvariable=var_cost_food)
text_cost_food.grid(row=0, column=1, padx=41)

tag_cost_drink = Label(panel_cost, text='drink Cost', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
tag_cost_drink.grid(row=1, column=0)

var_cost_drink = StringVar()
text_cost_drink = Entry(panel_cost, font=('Dosis', 12, 'bold'), width=10, bd=1, state='readonly', textvariable=var_cost_drink)
text_cost_drink.grid(row=1, column=1, padx=41)

tag_cost_dessert = Label(panel_cost, text='dessert Cost', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
tag_cost_dessert.grid(row=2, column=0)

var_cost_dessert = StringVar()
text_cost_dessert = Entry(panel_cost, font=('Dosis', 12, 'bold'), width=10, bd=1, state='readonly', textvariable=var_cost_dessert)
text_cost_dessert.grid(row=2, column=1, padx=41)

tag_cost_subtotal = Label(panel_cost, text='subtotal Cost', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
tag_cost_subtotal.grid(row=0, column=2)

var_cost_subtotal = StringVar()
text_cost_subtotal = Entry(panel_cost, font=('Dosis', 12, 'bold'), width=10, bd=1, state='readonly', textvariable=var_cost_subtotal)
text_cost_subtotal.grid(row=0, column=3, padx=41)

tag_cost_taxes = Label(panel_cost, text='taxes Cost', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
tag_cost_taxes.grid(row=1, column=2)

var_cost_taxes = StringVar()
text_cost_taxes = Entry(panel_cost, font=('Dosis', 12, 'bold'), width=10, bd=1, state='readonly', textvariable=var_cost_taxes)
text_cost_taxes.grid(row=1, column=3, padx=41)

tag_cost_total = Label(panel_cost, text='total Cost', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
tag_cost_total.grid(row=2, column=2)

var_cost_total = StringVar()
text_cost_total = Entry(panel_cost, font=('Dosis', 12, 'bold'), width=10, bd=1, state='readonly', textvariable=var_cost_total)
text_cost_total.grid(row=2, column=3, padx=41)

# buttons
buttons = ['Total', 'Ticket', 'Save', 'Reset']
columns = 0
for i in buttons:
    i = Button(panel_buttons, text=i.title(), font=('Dosis', 14, 'bold'), fg='white', bg='azure4', bd=1, width=9)
    i.grid(row=0, column=columns)
    columns += 1

# avoid resize
app.resizable(False, False)

# Avoid that screen close
app.mainloop()
