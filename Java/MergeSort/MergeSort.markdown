# Understanding Merge Sort Algorithm

This document explains the Merge Sort algorithm at a B1 English level, with Spanish translations in a two-column format for clarity.

## Merge Sort Algorithm

| **English (B1)** | **Spanish Translation** |
|------------------|-------------------------|
| **What is Merge Sort?**<br>Merge Sort is an algorithm that sorts a list by dividing it into smaller parts, sorting each part, and then joining them to make a sorted list. It uses a divide-and-conquer method.<br>- **Input**: A list of unsorted numbers.<br>- **Processing**: Split, sort, and combine using recursion.<br>- **Output**: A sorted list of numbers.<br>- **Data Structure**: List or array.<br>- **Error Handling**: Check if the list is empty or valid.<br>- **Termination**: Stops when all parts are merged.<br>Merge Sort is fast and good for big lists but needs extra space. | **¿Qué es Merge Sort?**<br>Merge Sort es un algoritmo que ordena una lista dividiéndola en partes más pequeñas, ordenando cada parte y luego uniéndolas para crear una lista ordenada. Usa un método de dividir y conquistar.<br>- **Entrada**: Una lista de números desordenados.<br>- **Procesamiento**: Dividir, ordenar y combinar usando recursión.<br>- **Salida**: Una lista de números ordenada.<br>- **Estructura de datos**: Lista o array.<br>- **Manejo de errores**: Verificar si la lista está vacía o es válida.<br>- **Terminación**: Para cuando todas las partes están combinadas.<br>Merge Sort es rápido y bueno para listas grandes, pero necesita espacio extra. |
| **How Merge Sort Works**<br>1. **Divide**: Split the list into two equal halves.<br>2. **Recurse**: Keep splitting each half until each part has one element (already sorted).<br>3. **Merge**: Combine the small parts by comparing elements and placing them in order.<br>4. **Repeat**: Continue merging until the whole list is sorted.<br>5. **Finish**: The list is fully sorted.<br>Example: For `[64, 34, 25, 12]`:<br>- Split: `[64, 34]` and `[25, 12]`.<br>- Split again: `[64]`, `[34]`, `[25]`, `[12]`.<br>- Merge: `[34, 64]` and `[12, 25]`.<br>- Final merge: `[12, 25, 34, 64]`. | **Cómo funciona Merge Sort**<br>1. **Dividir**: Dividir la lista en dos mitades iguales.<br>2. **Recursión**: Seguir dividiendo cada mitad hasta que cada parte tenga un elemento (ya ordenado).<br>3. **Combinar**: Unir las partes pequeñas comparando elementos y colocándolos en orden.<br>4. **Repetir**: Continuar combinando hasta que toda la lista esté ordenada.<br>5. **Finalizar**: La lista está completamente ordenada.<br>Ejemplo: Para `[64, 34, 25, 12]`:<br>- Dividir: `[64, 34]` y `[25, 12]`.<br>- Dividir otra vez: `[64]`, `[34]`, `[25]`, `[12]`.<br>- Combinar: `[34, 64]` y `[12, 25]`.<br>- Combinación final: `[12, 25, 34, 64]`. |
| **Key Characteristics**<br>- **Efficient**: Works well for big lists.<br>- **Stable**: Keeps the order of equal elements.<br>- **Extra Space**: Needs extra memory to hold split lists.<br>- **Time**: Fast, works in O(n log n) time, where n is the list size.<br>- **Use**: Good for large data or when stability is needed.<br>- **Control Structures**: Uses recursion and loops for merging. | **Características clave**<br>- **Eficiente**: Funciona bien para listas grandes.<br>- **Estable**: Mantiene el orden de elementos iguales.<br>- **Espacio extra**: Necesita memoria adicional para las listas divididas.<br>- **Tiempo**: Rápido, funciona en tiempo O(n log n), donde n es el tamaño de la lista.<br>- **Uso**: Bueno para datos grandes o cuando se necesita estabilidad.<br>- **Estructuras de control**: Usa recursión y bucles para combinar. |
| **Why is it Called Merge Sort?**<br>It’s called Merge Sort because it focuses on merging smaller sorted lists into a bigger sorted list. The “merge” step is the key part of the algorithm. | **¿Por qué se llama Merge Sort?**<br>Se llama Merge Sort porque se centra en combinar listas pequeñas ordenadas en una lista grande ordenada. El paso de “combinar” es la parte clave del algoritmo. |
| **Conclusion**<br>Merge Sort is an efficient way to sort a list using a divide-and-conquer method. It’s great for big data and stable sorting but needs extra space. It helps learn about recursion and algorithm design. | **Conclusión**<br>Merge Sort es una forma eficiente de ordenar una lista usando un método de dividir y conquistar. Es ideal para datos grandes y ordenamiento estable, pero necesita espacio extra. Ayuda a aprender sobre recursión y diseño de algoritmos. |

## How to Convert to PDF

To convert this Markdown file to a PDF:
1. **Use an Online Converter**:
   - Copy the content into a tool like [Dillinger](https://dillinger.io) or [Typora](https://typora.io).
   - Export as PDF (e.g., File > Export > PDF).
2. **Use Pandoc**:
   - Install Pandoc (https://pandoc.org).
   - Save the content as `README.md`.
   - Run: `pandoc README.md -o output.pdf --pdf-engine=pdflatex`.
3. **Use a Word Processor**:
   - Copy the content into Microsoft Word or Google Docs.
   - Format with two columns if desired (Layout > Columns > Two).
   - Save as PDF (File > Save As > PDF).
4. **Use VS Code**:
   - Install the Markdown Preview Enhanced extension.
   - Open `README.md` in VS Code.
   - Use the extension to export as PDF.

If you need help with conversion or want additional content (e.g., code examples), let me know!