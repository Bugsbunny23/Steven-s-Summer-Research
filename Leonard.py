#Good evening Leonardo 

#I create a list of colors.
colors = ['red', 'orange', 'green']

#I create another list called count
counts = ['red' , 'yellow', 'blue', 'green', 'orange', 'yellow', 'black', 'white']

#for i in counts means that each value in count is assign to the variable i.
#For example, the first the list runs, i is assign the value red(i = 'red').
#The next time the list runs, i is assign the value yellow(i = 'yellow').
for i in counts:

    #for j in colors means that each value in colors is assign to the variable j.
    #For example, the first the list runs j is assign the value red(j = 'red').
    #The next time the list runs j is assign the value of orange(j = 'orange').

    for j in colors:

        #if the value of i('red) is equal to the value of j('red') remove that item from the list.
        if i == j:
            #the remove method removes that value past into the parameters.(parameters means the value inside the parentheses)
            colors.remove(j)
            print('The color that was remove from the list was:' + j)
            
#please contact me if you have further questions.
