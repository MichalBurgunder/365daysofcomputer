# WOLVES AND RABBITS

# This very basic simulation demonstrates certain problems of simulating certain processes in the real world. 


# 1. Reducing animal numbers below zero
# By creating a straighforward simulation of wolves eating rabbits and rabbits multiplying, the problem of having a number reduced to below zero shows that a simulation is faulty.

# r = 1000 # number of rabbits 
# w = 6 # number of wolves

# rra = 200
# wra = 1.1

# rre = w*10
# wre = 0 if r / w < 10 else w*(r / w)

# for i in range(0, 20):
#     # print()
#     # print(wre)
#     r = r+rra - rre*w
#     w = w*wra
    
#     print(round(r,2), round(w, 2))



# 2. Achieving Semistable State 
# When we assume that wolf and rabbit populations always have a certain amout of them in the world, then each can multiply again to accomodate the other species. When we assume that there are always 2000 rabbits around that the wolves cannot eat (e.g. they hide very well) and 59 wolves that do not die (because they have other food sources) we can simualte a stable state, where both species can coexist. 

r = 1000 # number of rabbits 
w = 4 # number of wolves
always_r = 2000 # always existing rabbits
wolves_r = 100 # always existing wolves

rra = 1.2 # rate at which rabbits multiply
wra = 1.1 # rate at which wolves multiply

rre = w*10
wre = 0 if r / w < 10 else w*(r / w)

for i in range(0, 20):
    wre = (0 if (r/w) > 10 else w-r/w**2)

    r = r*rra - rre*w
    w = w*wra - wre

    print(r + always_r, w + wolves_r)

