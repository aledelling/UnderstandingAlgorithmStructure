# English: Model containing the bubble sort algorithm
# Español: Modelo que contiene el algoritmo bubble sort
def bubble_sort(lst):
    # English: Check if list is None or empty
    # Español: Verificar si la lista es None o está vacía
    if lst is None or len(lst) == 0:
        return None
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