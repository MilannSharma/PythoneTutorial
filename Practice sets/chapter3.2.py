letter = ''' 
         Dear <|Name|> ,
         You are selcted
         <|Date|>

        '''
name = input("Enter name : ")
name = name.title()

day = input("Enter day (dd): ")
month = input("Enter month (mm): ")
year = input("Enter year (yyyy): ")
date = (day) , (month) ,(year)
date = '/'.join(date)

# or ->
#date = day + '/' + month + '/' + year


letter = letter.replace("<|Name|>", name).replace("<|Date|>", date) # called chaining 

print(letter)



