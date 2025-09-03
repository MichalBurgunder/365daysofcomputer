import matplotlib.pyplot as plt
import random
import math

def bensons_standard(numbers):
    # numbers = 5582
    
    full_string = "".join([str(i) for i in range(0, numbers)])

    full_counts = [full_string.count(str(i)) for i in range(1, 10)] # + [full_string.count(str("0"))]
    print(full_counts)
    xs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    plt.bar(xs, full_counts, color='red')

    plt.xlabel('digit')
    plt.ylabel('counts')
    plt.title('counts per digit full range')

    plt.show()


def bensons_random(numbers):
    # numbers = 5582
    
    full_string = "".join([str(math.floor(random.random()*numbers)) for i in range(0, numbers)])

    full_counts = [full_string.count(str(i)) for i in range(1, 10)] # + [full_string.count(str("0"))]
    
    print(full_counts)
    xs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    plt.bar(xs, full_counts, color='red')

    plt.xlabel('digit')
    plt.ylabel('counts')
    plt.title('counts per digit by random numbers')

    plt.show()
    
    
numbers = 3962
bensons_standard(numbers)
bensons_random(numbers)