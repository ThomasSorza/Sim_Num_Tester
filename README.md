# README - Proyecto Software de Pruebas Estadísticas

Este README proporciona una visión general del software desarrollado en Python 3.0.11 que ofrece una variedad de pruebas estadísticas. El software utiliza PyQt para crear una interfaz gráfica de usuario (GUI) con 5 pestañas diferentes: Prueba de Medias, Prueba de Varianzas, Prueba de H², Prueba de KS y Prueba de Pocket. A continuación, se describen las principales funcionalidades y pasos para su uso.

## Requisitos del Sistema
- Python 3.0.11 instalado en su sistema.
- Las bibliotecas Scicy , PyQt y Matplotlib deben estar instaladas. Puede instalarlas usando `pip`.

## Ejecución del Software
Para ejecutar el software, simplemente ejecute el archivo ejecutable proporcionado. A continuación, se describen las funcionalidades disponibles en la interfaz.

## Interfaz de Usuario
El software consta de una ventana principal con 5 pestañas accesibles haciendo clic en los tabs correspondientes: Prueba de Medias, Prueba de Varianzas, Prueba de H², Prueba de KS y Prueba de Pocket. Cada pestaña contiene características comunes, como estado de la prueba, valor de chi², errores, valores KS, frecuencias, medias, varianzas, mínimos y máximos, intervalos o campos de texto para realizar la prueba específica.

En la parte inferior de la pantalla, encontrará un botón "Load File" que abre un widget para seleccionar un archivo. Una vez seleccionado el archivo, se mostrará un mensaje que indica "Archivo cargado correctamente" junto con la ruta del archivo seleccionado.

## Realización de Pruebas
Después de cargar el archivo, puede hacer clic en cada una de las pestañas y luego en el botón "Hacer Prueba". Esto mostrará el estado de la prueba y todas sus características específicas en la pestaña seleccionada. Además, tendrá acceso a todas las gráficas generadas.

## Prueba de Medias
Hacer click en el boton hacer prueba.

## Prueba de Varianzas
Hacer click en el boton hacer prueba.

## Prueba de chi²
Para la prueba de chi², es necesario ingresar un valor mínimo y un valor máximo. Ambos valores deben ingresarse juntos. Si ingresa solo un valor (por ejemplo, un valor A sin un valor B), se generará un error. Del mismo modo, si ingresa un valor B sin un valor A, también se generará un error. Asegúrese de ingresar ambos valores o ninguno para evitar errores.

## Prueba KS
Insertar intervalos o se utilizaran los valores por defecto.

## Prueba de Poker
Hacer click en el boton hacer prueba.

## Gráficas
Para visualizar las gráficas generadas por las pruebas estadísticas, se abrirá una ventana emergente de Matplotlib. Puede interactuar con estas gráficas y explorar los resultados en detalle.

¡Disfrute utilizando esta herramienta de pruebas estadísticas para numeros pseudaleatorios!
