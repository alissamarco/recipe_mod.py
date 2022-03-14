import tkinter
from tkinter import *
from measurement_list import dry_ingredient_measures, wet_ingredient_measures, dry_ingredient_list, wet_ingredient_list
import os

recipe = tkinter.Tk()
recipe.title('Recipe')
recipe.geometry('620x400-8-200')
recipe['padx'] = 12
#Frames
listbox_frame = tkinter.Frame(recipe, width=240, height=680)
listbox_frame.grid(row=0, column=0, rowspan=7, padx=12, pady=12)
middle_frame = tkinter.Frame(recipe, width=240, height=680)
middle_frame.grid(row=0, column=1, rowspan=6)
result_frame = tkinter.Frame(recipe, width=240, height=680)
result_frame.grid(row=0, column=2, rowspan=6)

chosen_dry, chosen_wet = '', ''
#Radio Buttons for Original Unit Type
optionFrame = tkinter.LabelFrame(middle_frame, text='Original Unit Type', font=('Georgia', 12, 'bold'))
optionFrame.grid(row=0, pady=10)

converted_dry_amount, converted_wet_amount, dry_amount_of, wet_amount_of = 0, 0, 0, 0
rbValue1 = tkinter.StringVar()
rbValue1.set('Cups')

radio1 = tkinter.Radiobutton(optionFrame, text='Cups', font=('Georgia', 12), value='Cups', variable=rbValue1)
radio2 = tkinter.Radiobutton(optionFrame, text='Grams',font=('Georgia', 12), value='Grams', variable=rbValue1)
radio3 = tkinter.Radiobutton(optionFrame, text='Tablespoons', font=('Georgia', 12), value='Tablespoons', variable=rbValue1)
radio1.grid(row=0, sticky='w')
radio2.grid(row=1, sticky='w')
radio3.grid(row=2,  sticky='w')

#Radio Buttons for New Unit Type
optionFrame = tkinter.LabelFrame(middle_frame, text='New Unit Type', font=('Georgia', 12, 'bold'))
optionFrame.grid(row=1, pady=10)

rbValue2 = tkinter.StringVar()
rbValue2.set('Cups')

radio1 = tkinter.Radiobutton(optionFrame, text='Cups', font=('Georgia', 12), value='Cups', variable=rbValue2)
radio2 = tkinter.Radiobutton(optionFrame, text='Grams', font=('Georgia', 12), value='Grams', variable=rbValue2)
radio3 = tkinter.Radiobutton(optionFrame, text='Tablespoons', font=('Georgia', 12),  value='Tablespoons', variable=rbValue2)
radio1.grid(row=3,sticky='w')
radio2.grid(row=4,  sticky='w')
radio3.grid(row=5,  sticky='w')

new_type, old_type = '', ''
#Input line for wet_amount
wetamountLabel = tkinter.Label(middle_frame, text='Wet Ingredient Amount', font=('Georgia', 12, 'bold'))
wetamountLabel.grid(row=2, sticky='s', pady=1)
wet_amount = tkinter.Entry(middle_frame, font=('Georgia', 12))
wet_amount_of = wet_amount.get()
wet_amount.grid(row=3,sticky='n', pady=1)

#Input line for dry amounts
dryamountLabel = tkinter.Label(middle_frame, text='Dry Ingredient Amount', font=('Georgia', 12, 'bold'))
dryamountLabel.grid(row=4, sticky='s', pady=1)
dry_amount = tkinter.Entry(middle_frame, font=('Georgia', 12))
dry_amount_of = dry_amount.get()
dry_amount.grid(row=5,  sticky='n', pady=1-0)

#Listbox for Dry Ingredients
dryLabel = tkinter.Label(listbox_frame, text='Dry Ingredients', font=('Georgia', 12, 'bold'))
dryLabel.grid(row=0, column=0)
dryIngredientList = tkinter.Listbox(listbox_frame, exportselection=0, font=('Georgia', 12))
dryIngredientList.grid(row=1, column=0, rowspan=2)
for item in dry_ingredient_list:
    dryIngredientList.insert(1, item)
listScroll = tkinter.Scrollbar(listbox_frame, orient=tkinter.VERTICAL, command=dryIngredientList.yview)
listScroll.grid(row=2, column=1, rowspan=2)
# ingredientList['yscrollcommand'] = listScroll.set

#Listbox for Wet Ingredients
wetLabel = tkinter.Label(listbox_frame, text='Wet Ingredients', font=('Georgia', 12, 'bold'))
wetLabel.grid(row=4, column=0)
wetingredientList = tkinter.Listbox(listbox_frame, exportselection=0, font=('Georgia', 12))
wetingredientList.grid(row=5, column=0, rowspan=2)
for item in wet_ingredient_list:
    wetingredientList.insert(1,item)
listScroll = tkinter.Scrollbar(listbox_frame, orient=tkinter.VERTICAL, command=wetingredientList.yview)
listScroll.grid(row=5, column=1, rowspan=2)

# Dry Ingredient Get
def chosen_ingredient():
    global chosen_wet, chosen_dry, wet_amount_of, dry_amount_of, old_type, new_type
    chosen_wet = wetingredientList.get(ANCHOR)
    chosen_dry = dryIngredientList.get(ANCHOR)
    wet_amount_of = wet_amount.get()
    dry_amount_of = dry_amount.get()
    old_type = rbValue1.get()
    new_type = rbValue2.get()
    dry_result_entry.set(str(chosen_dry) + ' ' + str(dry_amount_of) + ' ' + str(old_type))
    wet_result_entry.set(str(chosen_wet) + ' ' + str(wet_amount_of) + ' ' + str(old_type))

    if old_type == 'Grams' and new_type == 'Cups':
        converted_wet_amount = float(wet_amount_of) / wet_ingredient_measures[chosen_wet][1]
    elif old_type == 'Cups' and new_type == 'Grams':
        converted_wet_amount = float(wet_amount_of) * wet_ingredient_measures[chosen_wet][1]
    elif old_type == 'Tablespoons' and new_type == 'Cups':
        converted_wet_amount = float(wet_amount_of) / 16
    elif old_type == 'Cups' and new_type == 'Tablespoons':
        converted_wet_amount = float(wet_amount_of) * 16
    elif old_type == 'Grams' and new_type == 'Tablespoons':
        converted_wet_amount = float(wet_amount_of) / wet_ingredient_measures[chosen_wet][1] * 16
    elif old_type == 'Tablespoons' and new_type == 'Grams':
        converted_wet_amount = float(wet_amount_of) / 16 * wet_ingredient_measures[chosen_wet][1]
    wet_new_entry.set(str(chosen_wet) + ' ' + str(round(converted_wet_amount, 4)) + ' ' + str(new_type))

    if old_type == new_type:
        converted_dry_amount = float(dry_amount_of)
    elif old_type == 'Grams' and new_type == 'Cups':
        converted_dry_amount = float(dry_amount_of) / dry_ingredient_measures[chosen_dry][1]
    elif old_type == 'Cups' and new_type == 'Grams':
        converted_dry_amount = float(dry_amount_of) * dry_ingredient_measures[chosen_dry][1]
    elif old_type == 'Tablespoons' and new_type == 'Cups':
        converted_dry_amount = float(dry_amount_of) / 16
    elif old_type == 'Cups' and new_type == 'Tablespoons':
        converted_dry_amount = float(dry_amount_of) * 16
    elif old_type == 'Grams' and new_type == 'Tablespoons':
        converted_dry_amount = float(dry_amount_of) / dry_ingredient_measures[chosen_dry][1] * 16
    elif old_type == 'Tablespoons' and new_type == 'Grams':
        converted_dry_amount = float(dry_amount_of) / 16 * dry_ingredient_measures[chosen_dry][1]
    dry_new_entry.set(str(chosen_dry) + ' ' + str(round(converted_dry_amount, 4)) + ' ' + str(new_type))


#Result Window
wet_start_label = tkinter.Label(result_frame,text='Current Wet Ingredient Amount', font=('Georgia', 12, 'bold'))
wet_start_label.grid(row=0, sticky = 's', pady=10)
wet_result_entry = tkinter.StringVar()
wet_result = tkinter.Entry(result_frame, textvariable=wet_result_entry, font=('Georgia', 12, 'bold'))
wet_result.grid(row=1, sticky='n', pady=10)

dry_start_label = tkinter.Label(result_frame,text='Current Dry Ingredient Amount', font=('Georgia', 12, 'bold'))
dry_start_label.grid(row=2, sticky='s', pady=10)
dry_result_entry = tkinter.StringVar()
dry_result = tkinter.Entry(result_frame, textvariable=dry_result_entry, font=('Georgia', 12, 'bold'))
dry_result.grid(row=3, pady=10)

wet_result_label = tkinter.Label(result_frame,text='Converted Wet Ingredient Amount', font=('Georgia', 12, 'bold'))
wet_result_label.grid(row=4, pady=10)
wet_new_entry = tkinter.StringVar()
wet_new = tkinter.Entry(result_frame, textvariable=wet_new_entry, font=('Georgia', 12, 'bold'))
wet_new.grid(row=5, pady=10)

dry_result_label = tkinter.Label(result_frame, text='Converted Dry Ingredient Amount', font=('Georgia', 12, 'bold'))
dry_result_label.grid(row=6, pady=10)
dry_new_entry = tkinter.StringVar()
dry_new = tkinter.Entry(result_frame, textvariable=dry_new_entry, font=('Georgia', 12, 'bold'))
dry_new.grid(row=7, pady=10)

#Command Buttons
convertButton = tkinter.Button(result_frame, text='Convert', font=('Georgia', 12), command=chosen_ingredient)
cancelButton = tkinter.Button(result_frame, text='Cancel', font=('Georgia', 12),  command=recipe.destroy)
convertButton.grid(row=8, column=0, sticky='s')
cancelButton.grid(row=8, column=0, sticky='se')


recipe.mainloop()
