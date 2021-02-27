def plural_form(value, form1, form2, form3):

    if(value % 10 == 1) and (value != 11):
        return (f'{value}{form1}')
    
    elif(value % 10 in range(2,5)) and (value not in range(12,15)):
        return (f'{value}{form2}')

    elif(value % 10 in range(5,9)) or (value in range(5,20)):
        return (f'{value}{form3}')

print (plural_form(92, ' яблоко', ' яблока', ' яблок'))
print (plural_form(7, ' студент', ' студента', ' студентов'))
