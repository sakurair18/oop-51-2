# О(1) - Константное время
#Алгоритм работает за фиксированное время независимо от размера входных данных

lst = [1,2,3,4,5,6,7,8,9]
def get_element_by_index(lst, index):
    return lst[index]

#print(get_element_by_index(lst=lst, index=4))


#0(log n) - Логарифмическое время
#Часто встречается в алгоритмах, использующих деление входных данных на части (напрмер, бинарный поиск)

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid -1 
            
        
    return -1

#print(binary_search(lst, 9))



#O(n) - линейное время
#Алгоритм проходит по всем входным данным один раз


def find_element(lst, target):
    
    for i in lst:
        print(i)
        if i == target:
            return True
        
    return False

#print(find_element(lst, 10))



lst3 = [9, 2, 5, 1, 5, 2, 8, 7, 45]

#print(lst.sort())
#print(lst3)



def bubble_sort(lst):
    n = len(lst)
    print("for 1", range(n))
    for i in range(n):
        print(i)
        print("for 2--", range(n - i -1))
        for j in range(n - i - 1):
            print('for 3 ----' +j)
            if lst[j] > lst[j + 1]:
                print(f"{lst[j]} ----- {lst[j + 1]}")
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                print(f"lists------{lst}")
                
bubble_sort(lst=lst3)
print(lst3)