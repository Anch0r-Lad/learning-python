def spam():
    global eggs
    eggs ='spam'#this is the global

def bacon():
    return 'crispy bacon' # this is a local

def ham():
    print(eggs) #this is the global

eggs = 42 # this is the global
eggs = bacon()
print(eggs)
