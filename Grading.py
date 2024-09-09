NAME  =  input ('ENTER YOUR NAME:')
NAME = NAME.upper()
marks = input ('ENTER YOUR MARKS:')
marks = float(marks)
if 0 < marks <= 100:

   if 75 <= marks :
    print('CONGRATULATION ' + NAME + ' your GRADE IS :' 'A' )
   elif 65 <= marks < 75 :
    print('CONGRATULATION ' + NAME + ' your GRADE IS :' 'B' )
   elif 55 <= marks < 65 :
    print('CONGRATULATION ' + NAME + ' your GRADE IS :' 'C')
   elif 35 <= marks < 55 :
    print('CONGRATULATION' + NAME + ' your GRADE IS :' 'S')
   else :
    print('CONGRATULATION' + NAME  + ' your GRADE IS :' 'W' )
else :
    print('Input valid mark!!!')
