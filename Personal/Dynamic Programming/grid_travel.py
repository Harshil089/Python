# def gridTravel(m,n):
#     if(m==1 and n==1):
#         return 1
#     if(m==0 or n==0):
#         return 0
#     return gridTravel(m-1,n)+gridTravel(m,n-1)

def gridTravel(m,n,memo={}):
    if (m,n) in memo:
        return memo[(m,n)]
    if (n,m) in memo:
        return memo[(n,m)]

    if(m==1 and n==1):
        return 1
    if(m==0 or n==0):
        return 0
    memo[(m,n)]= gridTravel(m-1,n,memo)+gridTravel(m,n-1,memo)
    return memo[(m,n)]


m=18
n=18
print(f"The number of options to travel for grid of size {m,n} is {gridTravel(m,n)}")
