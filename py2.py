num = list(map(int, input("Enter numbers : ").split()))
import numpy
import statistics

def Average(lst):
    return sum(lst) / len(lst)
print("Minimum : " + str(min(num)))
print("Maximum : " + str(max(num)))
print("Average : " + str(Average(num)))
print("Standard Deviation : " + str(statistics.stdev(num)))
print("Vartiance : " + str(numpy.var(num)))


print("NAME AND ID :: DHRUV DIGVIJAYSINH 20CE117")