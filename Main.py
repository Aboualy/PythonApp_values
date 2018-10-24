arr =[3,5,7,8,9,1,3]
def count_prev_curr_next(ls):
    values =  [(current,
                ls[idx - 1] if idx >= 1 else None,
                #ls[idx - 2] if idx > 1 else None,
                ls[idx + 1] if idx < len(ls) - 1 else None) for idx, current in enumerate(ls)]
    return values

#print(count_prev_curr(arr))
def getVal(arr):
    values = count_prev_curr_next(arr)
    curr=[]
    prev=[]
    #bprev=[]
    next_val=[]
    for i in values:
        curr.append(i[0])
        prev.append(i[1])
        #bprev.append(i[2])
        next_val.append(i[2])
    return curr, prev,next_val
output = getVal(arr)
print("Current values", output[0], "\nPrevious valeus:", output[1] , "\nNext values", output[2])
