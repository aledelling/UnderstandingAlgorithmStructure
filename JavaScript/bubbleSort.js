// English: Function to perform bubble sort on an array
// Español: Función para realizar bubble sort en un array
function bubbleSort(array) {
    // English: Check if array is null or empty
    // Español: Verificar si el array es nulo o está vacío
    if (!array || array.length === 0) {
        return;
    }
    // English: Get the length of the array
    // Español: Obtener la longitud del array
    const n = array.length;
    // English: Loop through the array
    // Español: Recorrer el array
    for (let i = 0; i < n - 1; i++) {
        // English: Compare and swap adjacent elements
        // Español: Comparar y cambiar elementos adyacentes
        for (let j = 0; j < n - i - 1; j++) {
            // English: If current element is greater, swap
            // Español: Si el elemento actual es mayor, cambiar
            if (array[j] > array[j + 1]) {
                // English: Swap elements
                // Español: Cambiar elementos
                [array[j], array[j + 1]] = [array[j + 1], array[j]];
            }
        }
    }
    return array;
}

// English: Test bubble sort
// Español: Probar bubble sort
const testArray = [64, 34, 25, 12, 22, 11, 90];
// English: Call bubble sort
// Español: Llamar a bubble sort
const sortedArray = bubbleSort(testArray);
// English: Print sorted array
// Español: Imprimir array ordenado
console.log("English: Sorted array:", sortedArray);
console.log("Español: Array ordenado:", sortedArray);