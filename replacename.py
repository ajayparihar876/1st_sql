letter=''' DEAR <|NAME|>,
you are selected!
'''
name = input("enter your name \t")
letter = letter.replace("<|NAME|>", name)
print(letter)
