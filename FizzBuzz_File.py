def FizzBuzz(start, finish):
    outlist = []
    for i in range(start,finish+1):
        if i%15 == 0:
            outlist.append('fizzbuzz')
        elif i%5 == 0:
            outlist.append('buzz')
        elif i%3 == 0:
            outlist.append('fizz')
        else:
            outlist.append(i)
    return(outlist)
