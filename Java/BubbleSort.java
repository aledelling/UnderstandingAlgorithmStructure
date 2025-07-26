public class BubbleSort {
    // English: Method to perform bubble sort on an array
    // Español: Método para realizar bubble sort en un array
    public static void bubbleSort(int[] array) {
        // English: Check if array is null or empty
        // Español: Verificar si el array es nulo o está vacío
        if (array == null || array.length == 0) {
            return;
        }
        // English: Get the length of the array
        // Español: Obtener la longitud del array
        int n = array.length;
        // English: Loop through the array
        // Español: Recorrer el array
        for (int i = 0; i < n - 1; i++) {
            // English: Compare and swap adjacent elements
            // Español: Comparar y cambiar elementos adyacentes
            for (int j = 0; j < n - i - 1; j++) {
                // English: If current element is greater, swap
                // Español: Si el elemento actual es mayor, cambiar
                if (array[j] > array[j + 1]) {
                    // English: Swap elements
                    // Español: Cambiar elementos
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }

    // English: Main method to test bubble sort
    // Español: Método principal para probar bubble sort
    public static void main(String[] args) {
        // English: Create an unsorted array
        // Español: Crear un array desordenado
        int[] array = {64, 34, 25, 12, 22, 11, 90};
        // English: Call bubble sort
        // Español: Llamar a bubble sort
        bubbleSort(array);
        // English: Print sorted array
        // Español: Imprimir array ordenado
        System.out.print("English: Sorted array: ");
        System.out.println("Español: Array ordenado: ");
        for (int num : array) {
            System.out.print(num + " ");
        }
    }
}