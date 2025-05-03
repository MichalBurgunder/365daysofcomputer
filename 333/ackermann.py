

def A(x, y):
    if x == 0:
        return y + 1
    if y == 0:
        return A(x-1,1)
    return A(x-1, A(x,y-1))

# for x in range(0,5):
#     for y in range(0,3):
#         print(A(x,y))
print(A(4,0))