def insertionSort(data):
    for step in range(1, len(data)):
        key = data[step]
        j = step - 1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j = j - 1
        # Place key at after the element just smaller than it.
        data[j + 1] = key
data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)