Alvaro Villanova Ahlroth            STEM Granada 2023
# Programacion:



## Historial de versiones:


#### Iteracion 4 (V0.40):

Durante esta semana pienso trabajar en:
  - Limpiar código y refactorizar.
  - Añadir requerimientos de los incrementos:
    a) Implementar plaza (_square_) al gotchi. Desde aquí se accede a los antiguos menus de tienda (_shop_) y jugar (_play_).
    b) Implementar los juegos de "Piedra, Papel o Tijera"(_RPS_) y "Ahorcado"(_Hangman_).
    c) ~~Implementar juego de Tres en Raya (tictactoe).~~ (TicTacToe no entrará en la version final.)
    

**0.41**:
  - Añadido Town Square al programa, esto ha involucrado dos partes; interfaz gráfica y funcionalidad. En el GFX, se ha añadido el ASCII art de la plaza (Original de Steven Maddison, año desconocido) como una función para alimentar la ya bastante reusada funcion _refreshCurrentScreenGFX_ (que usamos para refrescar la pantalla de acuerdo al menú que estemos explorando.). Por otro lado, en el lado funcional no han habido muchos cambios para conseguir el objetivo: Se ha creado y añadido la opción _square_ al arbol de acciones del _gameLoop_. Las opciones _play_ y _shop_ se han movido dentro de _square_.
  - RockPaperScissors: Añadido el juego (función _rockPaperScissors()_), se llama escribiendo el comando _play_ y luego _RPS_ desde la pantalla de plaza (_square_). El juego no tiene interfaz gráfica. **No está hecho a partir del codigo propuesto en EED, es codigo propio**.
  - Hangman: Añadido el juego (función _hangmanGame_) al menu _play_. El juego funciona bien, falta añadir los detalles de la recompensa de oro (ahora mismo se gana la suma generica de 100-200 al ganar un juego).

**0.42**:
  - Arreglado el tema de las recompensas tanto en _hangman_ como en _RPS_, en ningun momento se enunciaba cuanto se oro (_gold_) se ganaba tras cada juego. Ahora esto si ocurre. Añadida la formula para ganar dinero en _hangman_, que era un poco más complicada (victoryMultiplier*(_totalPoints_+_victoryPoints_)).

#### Iteracion 3 (V0.30):

Durante esta semana pienso trabajar en:
  - Implementar pantalla de inicio (donde se escoge el nombre del Gotchi)
  - Añadir requerimientos del incremento:
    a) Añadir edad al gotchi (y muerte al llegar a 99 iteraciones)
    b) Añadir oro al gotchi:
      - Va de 0 a 9999g
      - Se gana de 100 a 200 (aleatoriamente) al jugar.
      - Se puede gastar en la tienda comprando objetos.
    c) Mejorar pantalla info:
      - Ahora incluye mas estadisticas (edad, oro e inventario)
      - Interfaz/Pantalla de INFO mejorada.
    d) Añadir tienda:
      - Cada 9 iteraciones los objetos de la tienda cambian.
      - Los objetos solo se pueden comprar si NO se tienen y si se tiene suficiente DINERO.
      - La tienda tiene 3 objetos aleatorios de una lista:
            Pelota ⚾  -> 50G
            Gorra 🧢 -> 200G
            Patines ⛸️ -> 500
            Skate 🛹 -> 900
            Lápices 🖍️ -> 100
            Raqueta 🏸  -> 350
            Botas 👢 -> 400
            Saxofón 🎷 -> 1000
            Collar 📿 -> 250
            Cometa 🪁-> 150

- **0.31**:
  - Añadida la edad al gotchi (aunque todavia no puede morir). Añadida también una pantalla de GAME OVER para cuando el gotchi pueda morir (a los 99 años)
  - Implementada la pantalla de inicio con gráficas bonitas.
  - Implementado el oro y la tienda: Ya se gana oro aleatorio entre 100 y 200 despues de jugar. La tienda muestra objetos y valor y se aleatoriza cada 9 iteraciones. Todavía no se puede comprar (falta por implementar); tampoco han sido implementadas las limitaciones de compra (si no tienes dinero suficiente o si ya se tiene el objeto en el inventario).


- **0.32** Añadido lo fuerte del incremento: 
  - Tienda: Los objetos ya se pueden comprar de la tienda. Esto conlleva a un numero de comprobaciones (revisa si el gotchi no tiene ya el objeto pedido, si el gotchi tiene suficiente dinero y tambien si el gotchi tiene suficiente espacio en su inventario, 8 casillas en mi caso.
  - Una vez los objetos son comprados, la cantidad relevante de oro es restado de la estadistica de oro del gotchi y el objeto añadido al inventario. El inventario se puede ver en la pantalla de INFO. Administrar el inventario ha resultado un pequeño reto puesto que en mi inventario no se añaden objetos a una lista vacia: en vez, el inventario "vacio" realmente esta "lleno" de strings de 8 caracteres de espacio ("        ") que van siendo sustituidos por los objetos comprados. El razonamiento detrás de esto es para mantener las proporciones graficas de la interfaz iguales (Como siempre, la interfaz lo complica todo). Por este mismo motivo, todos los objetos tienen 8 caracteres ("⚾Ball  ","🧢Hat   ","⛸️ Skates",etc...).
  - Muerte: El gotchi ya puede morir. Se añade una comprobacion al final de gameLoop que si timeIteration%100==0 (Si llegamos a 100 iteraciones temporales) gameLoop cambia a FALSE y por lo tanto termina el loop de juego. A esto le sigue una pantalla de "game over" que termina el programa.





#### Iteracion 2 (12/11 al 21/11 - V0.20):


Durante esta semana pretendo trabajar en:
 - Cambiarle el nombre del loop "gameIsOn" a "gameLoop" :P 
 - Arreglar el spaggheti que tengo con los sprites tanto de gotchi, como de la caca, como de la futura calavera
 - Definir una seccion del codigo para valores iniciales de las estadisticas de un gotchi.
 - Anadir a funcion takeAction las acciones "ver info" y "curar" (info/heal). Tener en cuenta interacciones con otros stats.
 - Plantear pantalla de estadisticas y otras alternativas al mainScreenGFX (quizas cuando muera, la pantalla de inicio, etc...)
 - gfx: Linea de "Enfermo/Sano"(sick/healthy) debajo de Hungry/Happy/Poo.
 - gfx: Crear menu de seleccion de accion. Ahora tenemos 5 acciones.
 - Sobre Nombre/Peso:
   - ! Ambas estadisticas se mostraran al pulsar "ver info".
   - Modificar codigo existente "escoger nombre" para que solo pueda tener 5 caracteres (antes no tenia limitacion).
   - Al nacer, gotchi pesa 1KG, hasta 99KG (e implementar a funcion "normaliseStats")
   - Al comer "comida" peso +1, dulce +2 (Pero NO puede comer dulce si ENFERMO)
   - Al jugar peso -1 (Pero NO puede jugar si ENFERMO)
 - Sobre curar/enfermedad:
   - Si llega a 3 cacas, gotchi enferma.
   - Accion "Curar" solo funciona si hay 0 cacas presentes.
   - La enfermedad no permite comer dulces/jugar
   - gfx: anadir calavera en unicode a mainScreenGFX

- **0.23**:
  Arreglados un monton de problemas relacionados con la estructura del mainLoop:
    - Funcionamiento mainLoop: Anteriormente todo el arbol de acciones ocurria a través de una función llamada ¨takeAction¨ y esto era sub-optimo. Esta decision, aparte de ocultar el arbol de acciones y hacerlo más complicado de entender, también complicaba el cambio entre diferentes pantallas de la interfaz grafica (pantalla de inicio, pantalla principal, pantalla de estadisticas, etc...). Esto iba a ser un problema cuando más adelante se vayan a implementar nuevas pantallas (pantalla de la tienda, pantalla del inventario, pantalla de game over, etc...). Esto se ha solucionado usando una variable llamada "currentScreenGFX" que, dependiendo de que opción escogemos previamente (¨info¨,¨shop¨, etc...) es modificada para mostrar una nueva pantalla de menu basada en nuestra elección.
    - Funcionamiento normalizacion de estadisticas: Anteriormente, al final de cada "turno" se normalizaban todas las estadísticas por encima/debajo del limite estipulado. Esto se hacia a través de una función llamada "normaliseStats". Esto también era sub-optimo porque la función hacía una comprobación de TODAS las estadisticas disponibles. Esto ha sido mejorado añadiendo esa normalización a cada acción independientemente (feedGotchi,playGotchi,cleanGotchi, etc...), de esta manera solo se normalizan las estadísticas pertinentes y nos ahorra un montón de comprobaciones cada turno.

- **0.22**:
  Implementadas todas las funcionalidades importantes que faltaban en este incremento:
    - Enfermedad: Esta funcionalidad se ha anadido al final de la funcion timeIteration (al final del turno).Si hay 3 cacas, el gotchi enferma. Tambien, mientras este enfermo gotchi no podra jugar ni comer dulces. Para curar al gotchi no deberan de haber presentes ninguna caca.
    - Peso: Creada una nueva estadistica llamada ¨weight¨. Esta se inicializa en 1 con un maximo de 99 y es afectada por ¨meal¨ (+1) y por "candy" (+2)

- **0.21**:
    - Corregido un problema con el sprite de calavera cuando el gotchi enferma: el sprite de calavera se encontraba ANTES de la funcion que la refrescaba, por lo tanto la calavera no se actualizaba a tiempo, sino en la siguiente iteracion temporal. Inverti el orden de la funcion y dicha variable para arreglarlo.
    - Añadidos a la funcion takeAction (que procesa toda la toma de acciones) las opciones ¨cure¨ e ¨info¨. Cura hace lo que debe bajo las condiciones correctas (el gotchi ha de estar enfermo y no han de haber cacas). Info muestra un nuevo menu con las estadisticas principales.
    - Modificado el menu de seleccion de accion para incluir ¨cure¨ e ¨info¨.
    - Añadida la estadistica peso (valor inicial 1) y añadida a la funcion de normalizacion de estadisticas.

- **0.20**: 
    - Corregidas las acciones auxiliares "wrongChoice" (que muestra la frase "decision incorrecta" cuando se tome una eleccion incorrecta) y "gottaClean" (que muestra la frase "hay cacas" cuando tomar decision sea incompatible por presencia de cacas). Ambas acciones estaban presentes en la lista "actions" que han sido pasadas a la nueva lista "auxActions".
    - Añadidos los elementos gráficos (NO FUNCIONALES) relacionados con enfermedad (una calavera encima del gotchi y las frases ¨Gotchi is sick!¨,¨Gotchi is healthy!¨) para esto he creado nuevas listas ¨sicknessState¨(muestra estado actual)¨sicknessSprites¨(muestra los sprites de calavera) y ¨sicknessStatus¨ (muestra en mainScreenGFX las frases healthy/sick mencionadas antes).
    - Quitado el nombre del gotchi de pantalla; ya que esto estara presente en la pantalla de INFO que sera anadida posteriormente.

#### Iteracion 1 (30/10 al 11/11 - V0.10):


Esta iteración es el comienzo del proyecto: He comenzado programando el juego.
Realmente el código base estaría ya completado. Futuras iteraciones incluirán mejoras de funcionalidades, abrillantado y demás.


- **V0.14**: Corregidas las estadísticas máximas de 5/5/5 a 4/4/6. Añadida una función para normalizar valores cuando se pasen o queden por debajo de esos rangos. Añadido un salto-de-linea(multiplicado por 100) a la función refreshMainScreenGFX para dar la impresión de “refresco de pantalla”.

- **V0.13**: Añadida la funcionalidad para nombrar a tu Gotchi (e implementación en la interfaz gráfica del usuario)

- **V0.12**: Añadida la función de iteración de tiempo y función de toma de acciones básicas (comer, jugar, limpiar cacas). Retocada la interfaz gráfica y añadida una caca detrás del Gotchi (cuando contador de cacas igual o mayor a 1)

- **V0.11**: Añadido devlog al propio proyecto y empezado a utilizar notas explicativas a cada “commit”. Convertido el pseudo-código del gameLoop a código real. Implementadas las estadísticas de hambre, felicidad y cacas.

- **V0.10**: Escrito una aproximación del gameLoop inicial en pseudocódigo. Embocetada la interfaz gráfica y declaradas algunas variables y listas que van a ser utilizadas.



#### Iteracion 4 (V0.40):
