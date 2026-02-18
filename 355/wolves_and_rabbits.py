

# r = 1000
# w = 4

# rra = 1.2
# wra = 1.1

# rre = w*10
# wre = 0 if r / w < 10 else w*(r / w)

# for i in range(0, 20):
#     # print()
#     wre = (0 if (r/w) > 10 else w-r/w**2)
#     # print(wre)
#     r = r*rra - rre*w
#     w = w*wra - wre
    
#     print(r, w)
#     # exit()/




r = 1000
w = 6

rra = 200
wra = 1.1

rre = w*10
wre = 0 if r / w < 10 else w*(r / w)

for i in range(0, 20):
    # print()
    # print(wre)
    r = r+rra - rre*w
    w = w*wra
    
    print(round(r,2), round(w, 2))
    # exit()/


