# English: Function to perform bubble sort on a list
# Español: Función para realizar bubble sort en una lista
def bubble_sort(lst):
    # English: Check if list is None or empty
    # Español: Verificar si la lista es None o está vacía
    if lst is None or len(lst) == 0:
        return
    # English: Get the length of the list
    # Español: Obtener la longitud de la lista
    n = len(lst)
    # English: Loop through the list
    # Español: Recorrer la lista
    for i in range(n - 1):
        # English: Compare and swap adjacent elements
        # Español: Comparar y cambiar elementos adyacentes
        for j in range(n - i - 1):
            # English: If current element is greater, swap
            # Español: Si el elemento actual es mayor, cambiar
            if lst[j] > lst[j + 1]:
                # English: Swap elements
                # Español: Cambiar elementos
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# English: Test bubble sort
# Español: Probar bubble sort
if __name__ == "__main__":
    # English: Create an unsorted list
    # Español: Crear una lista desordenada
    test_list = [64, 34, 25, 12, 22, 11, 90]
    # English: Call bubble sort
    # Español: Llamar a bubble sort
    sorted_list = bubble_sort(test_list)
    # English: Print sorted list
    # Español: Imprimir lista ordenada
    print("English: Sorted list:", sorted_list)
    print("Español: Lista ordenada:", sorted_list)