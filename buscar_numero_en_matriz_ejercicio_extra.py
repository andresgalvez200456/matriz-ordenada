def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
 
global count  
count = 0
def ordenamiento(target, array):
    count = 0

    if(array[0] != target): 
        middleIndex = (len(array) - 1)//2
    
    
    if(array[0] == target):
        print(" ") 
        print("el numero") 
        print( target) 
        print ("existe")
        count = 1
        return True

    if(count == 0):        
        if(array[middleIndex] <= target):
            print(" ")   
            print("elementos de la lista menores a 7 que borrar")
            for i in range(middleIndex + 1):
                #elimino todos los valores antes que 7
                print(array[0]) #1,4,7
                array.pop(0)
            print("nueva lista")        
            print(array)
            print(" ")    

        else:
            print("elementos de la lista mayores a 14 que borrar")
            # es 14 mayor a 13 ? entonces borro desde el 14 hasta los mayores
            if(middleIndex == target):
                print(" ") 
                print("el numero" + target + "existe")
                return True
            
    
            if(array[middleIndex] >= target):
                for i in range(middleIndex +1):
                    #elimino todos los valores despues de 14
                    print(array[middleIndex]) #1,4,7
                    array.pop(middleIndex)
            print("nueva lista")        
            print(array)
    



if __name__ == '__main__':
    """""
    data = [1, 7, 4, 1, 10, 9, -2]
    print("Unsorted Array")
    print(data)
 
    size = len(data)
 
    quickSort(data, 0, size - 1)
 
    print('Sorted Array in Ascending Order:')
    print(data)
   """"" 

    

    a1 = [1, 4, 7, 11, 15]
    a2 = [2, 5, 8, 11, 19]
    a3 = [3, 6, 9, 16, 22]
    a4 = [10,13,14,17, 24]
    a5 = [18,21,23,26,30]


    a =[a1,
        a2 ,
        a3,
        a4,
        a5]


    #print("mitad :")
    #print (a1[middleIndex])        
        # es 7    menor a 13 ?
    
    ordenamiento(13,a1)
    ordenamiento(13,a2)
    ordenamiento(13,a3)
    ordenamiento(13,a4)
    ordenamiento(13,a5)

    ordenamiento(13,a1)
    ordenamiento(13,a2)
    ordenamiento(13,a3)
    ordenamiento(13,a4)
    ordenamiento(13,a4)
    