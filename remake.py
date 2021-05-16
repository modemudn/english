a0 = '''
|-----| 
|     | game over!
|     O
|    /|\\
|    / \\
|__
|__|
'''
a1 = '''
|-----| 
|     | 
|     O
|    
|    
|__
|__|
'''
a2 = '''
|-----| 
|     | 
|     O
|     |
|    
|__
|__|
'''
a3 = '''
|-----| 
|     | 
|     O
|    /|
|     
|__
|__|
'''
a4 = '''
|-----| 
|     |
|     O
|    /|\\
|    
|__
|__|
'''
a5 = '''
|-----| 
|     | 
|     O
|    /|\\
|    /
|__
|__|
'''
a6 = '''
|-----| 
|     | game over!
|     O
|    /|\\
|    / \\
|__
|__|
'''
target = 'football'
graphic = [a1,a2,a3,a4,a5,a6]
index_of_graphic=0
word = []
corrected = []
guessed =[]

for i in target:
    print('_',end=' ') 
print('( n =',len(target),')')


while True:
    
    x=input('Put a letter =')
    if x in guessed:
        print('duplicate character')
        continue
    
    if len(x)>1:
        print('too much guessing characters ')
        continue
    guessed.append(x)
    print(guessed)
    if x not in target :
    # not correct case
        print(graphic[index_of_graphic])
        index_of_graphic += 1
    if  index_of_graphic ==5 :
        break   
    #correct
    else :
        print('correct')
        corrected.append(x) 
        for i in target:
            if i in corrected:
                print(i,end=' ')
            else :
                print('_',end=' ')