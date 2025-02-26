

def selection_sort(numbers):
    num = len(numbers)
    for i in range(num):
        min_number = i
        for j in range(i + 1, num):
            if numbers[j] < numbers[min_number]:
                min_number = j
        target = numbers[i]    
        numbers[i] = numbers[min_number]   
        numbers[min_number] = target
        
        
list = [4, 11, 2, 82, 18, 1, 23, 25]
selection_sort(list)
print(list)