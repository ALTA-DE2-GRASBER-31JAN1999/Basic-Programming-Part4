def mean_median(array_input):
    n = len(array_input)
    sorted_array = sorted(array_input)
    
    if n % 2 == 0:
        mid1 = n // 2
        mid2 = mid1 - 1
        median = (sorted_array[mid1] + sorted_array[mid2]) / 2
    else:
        mid = n // 2
        median = sorted_array[mid]
    
    mean = sum(array_input) / n
    return (mean, median)

if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4])) # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5])) # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15])) # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50])) # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120])) # (49.0, 30)