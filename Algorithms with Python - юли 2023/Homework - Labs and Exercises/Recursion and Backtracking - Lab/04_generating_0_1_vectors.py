n = int(input())

vector = [None] * n

def gen01(idx, vector):
    if idx >= len(vector): 
        print(*vector, sep='')
        return
    
    for num in range(2):
        vector[idx] = num
        gen01(idx + 1, vector)

gen01(0, vector)