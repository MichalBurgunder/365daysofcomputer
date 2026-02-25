# BENSONS LAW DEMONSTRATION
import matplotlib.pyplot as plt
import random
import math

# when arranging the digits of all numbers up to a particular value, we get a reduction of digits as the digits get bigger
def bensons_standard(numbers):
    full_string = "".join([str(i) for i in range(0, numbers)])

    full_counts = [full_string.count(str(i)) for i in range(1, 10)]
    # print(full_counts)

    xs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    plt.bar(xs, full_counts, color='red')

    plt.xlabel('digit')
    plt.ylabel('counts')
    plt.title('counts per digit full range')

    plt.show()


# when we take random numbers up to a particular value, we get a a similar distribution, which is what is found in the real world
def bensons_random(numbers):
    full_string = "".join([str(math.floor(random.random()*numbers)) for i in range(0, numbers)])

    full_counts = [full_string.count(str(i)) for i in range(1, 10)]
    # print(full_counts)
    
    xs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    plt.bar(xs, full_counts, color='red')

    plt.xlabel('digit')
    plt.ylabel('counts')
    plt.title('counts per digit by random numbers')

    plt.show()
    
    
numbers = 3962
bensons_standard(numbers)
bensons_random(numbers)