def bubble_sort(array):
    '''Bubble sort implementation that keeps track of the number of swaps that happen in the sort'''
    swaps = 0
    swaps_per_pass = 1
    
    for i in range(len(array)):
        if not swaps_per_pass:
            print(swaps)
            return     
        
        swaps_per_pass = 0
        for j in range(len(array)- i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j +1] = array[j+1], array[j]
                swaps += 1
                swaps_per_pass += 1
    
    return array, swaps
       