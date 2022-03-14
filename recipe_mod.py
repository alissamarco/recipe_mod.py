import tkinter
from tkinter import *
from measurement_list import dry_ingredient_measures, wet_ingredient_measures, dry_ingredient_list, wet_ingredient_list
import os


recipe = tkinter.Tk()
recipe.title('Recipe')
recipe.geometry('720x520-8-200')
recipe['padx'] = 10
chosen_dry, chosen_wet = '', ''
#Radio Buttons for Original Unit Type
optionFrame = tkinter.LabelFrame(recipe, text='Original Unit Type')
optionFrame.grid(row=1, column=2)

converted_dry_amount, converted_wet_amount, dry_amount_of, wet_amount_of = 0, 0, 0, 0
rbValue1 = tkinter.StringVar()
rbValue1.set('Cups')

radio1 = tkinter.Radiobutton(optionFrame, text='Cups', value='Cups', variable=rbValue1)
radio2 = tkinter.Radiobutton(optionFrame, text='Grams', value='Grams', variable=rbValue1)
radio3 = tkinter.Radiobutton(optionFrame, text='Tablespoons', value='Tablespoons', variable=rbValue1)
radio1.grid(row=0, column=2, sticky='w')
radio2.grid(row=1, column=2, sticky='w')
radio3.grid(row=2, column=2, sticky='w')

#Radio Buttons for New Unit Type
optionFrame = tkinter.LabelFrame(recipe, text='New Unit Type')
optionFrame.grid(row=3, column=2)

rbValue2 = tkinter.StringVar()
rbValue2.set('Cups')

radio1 = tkinter.Radiobutton(optionFrame, text='Cups', value='Cups', variable=rbValue2)
radio2 = tkinter.Radiobutton(optionFrame, text='Grams', value='Grams', variable=rbValue2)
radio3 = tkinter.Radiobutton(optionFrame, text='Tablespoons', value='Tablespoons', variable=rbValue2)
radio1.grid(row=3, column=2, sticky='w')
radio2.grid(row=4, column=2, sticky='w')
radio3.grid(row=5, column=2, sticky='w')

new_type, old_type = '', ''
#Input line for wet_amount
wetamountLabel = tkinter.Label(recipe, text='Wet Ingredient Amount')
wetamountLabel.grid(row=5, column=2, sticky='s')
wet_amount = tkinter.Entry(recipe)
wet_amount_of = wet_amount.get()
wet_amount.grid(row=6, column=2, sticky='n')

#Input line for dry amounts
dryamountLabel = tkinter.Label(recipe, text='Dry Ingredient Amount')
dryamountLabel.grid(row=4, column=2, sticky='n')
dry_amount = tkinter.Entry(recipe)
dry_amount_of = dry_amount.get()
dry_amount.grid(row=5, column=2, sticky='n')

#Input Line for Dry Ingredients
dryFrame = tkinter.LabelFrame(recipe, text='Dry Ingredients')
dryFrame.grid(row=0, column=0)
dryLabel = tkinter.Label(recipe, text='Dry Ingredients')
dryLabel.grid(row=0, column=0)
dryIngredientList = tkinter.Listbox(recipe, exportselection=0)
dryIngredientList.grid(row=1, column=0, rowspan=2)
for item in dry_ingredient_list:
    dryIngredientList.insert(1, item)
listScroll = tkinter.Scrollbar(recipe, orient=tkinter.VERTICAL, command=dryIngredientList.yview)
listScroll.grid(row=2, column=1, rowspan=2)
# ingredientList['yscrollcommand'] = listScroll.set

#Input Line for Wet Ingredients
wetLabel = tkinter.Label(recipe, text='Wet Ingredients')
wetLabel.grid(row=4, column=0)
wetingredientList = tkinter.Listbox(recipe, exportselection=0)
wetingredientList.grid(row=5, column=0, rowspan=2)
for item in wet_ingredient_list:
    wetingredientList.insert(1,item)
listScroll = tkinter.Scrollbar(recipe, orient=tkinter.VERTICAL, command=wetingredientList.yview)
listScroll.grid(row=5, column=1, rowspan=2)
# ingredientList['yscrollcommand'] = listScroll.set


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
wet_result_entry = tkinter.StringVar()
wet_result = tkinter.Entry(recipe, textvariable=wet_result_entry)
wet_result.grid(row=1, column=3)

dry_result_entry = tkinter.StringVar()
dry_result = tkinter.Entry(recipe, textvariable=dry_result_entry)
dry_result.grid(row=2, column=3)

wet_new_entry = tkinter.StringVar()
wet_new = tkinter.Entry(recipe, textvariable=wet_new_entry)
wet_new.grid(row=3, column=3)

dry_new_entry = tkinter.StringVar()
dry_new = tkinter.Entry(recipe, textvariable=dry_new_entry)
dry_new.grid(row=4, column=3)

#Command Buttons
convertButton = tkinter.Button(recipe, text='Convert', command=chosen_ingredient)
cancelButton = tkinter.Button(recipe, text='Cancel', command=recipe.destroy)
convertButton.grid(row=6, column=3, sticky='se')
cancelButton.grid(row=6, column=4, sticky='sw')


recipe.mainloop()

print('Your chosen dry ingrendient is {}'.format(chosen_dry))
print('Your chosen wet ingredient is {}'.format(chosen_wet))
print('The wet ingredient amount you want to change is {}'.format(wet_amount_of))
print('The dry ingredient amount you want to change is {}'.format(dry_amount_of))
print('Your original unit type was {}'.format(old_type))
print('Your new unit type is {}'.format(new_type))

if chosen_dry in dry_ingredient_measures:
    print(dry_ingredient_measures[chosen_dry][0], 'Cup of', chosen_dry, 'is', dry_ingredient_measures[chosen_dry][1], 'Grams')
else:
    print("Your ingredient is not in the list")
if chosen_wet in wet_ingredient_measures:
    print(wet_ingredient_measures[chosen_wet][0], 'Cup of', chosen_wet, 'is' , wet_ingredient_measures[chosen_wet][1], 'Grams')
else:
    print("Your ingredient is not in the list")

#conversions - gram/gram etc gram/tablespoon tbsp/gram tbsp/cup cup/tbsp cup/gram gram/cup

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
print(dry_amount_of, old_type, 'is', round(converted_dry_amount, 4), new_type, 'of', chosen_dry)


if old_type == new_type:
    converted_wet_amount = float(wet_amount_of)
elif old_type == 'Grams' and new_type == 'Cups':
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
print(wet_amount_of,old_type, 'is', round(converted_wet_amount, 4), new_type, 'of', chosen_wet)

