He hecho un juego donde el jugador decide un nivel entre 1 y 4 para escojer un rango donde el ordenador escoje un numero random que el jugador tiene que adivinar. Si el jugador gana (porque hay un numero maximo de intentos por nivel), se puede registrar en la lista de los leaders llamada leader_booard.

Una vez que el jugador elige un rango, el jugador va poniendo un numero y recibiendo indicaciones de si el numero es mayor o menor que el numero propuesto. Para eso he definido una funcion play_game .
La funicon play game es donde ocurre el juego principal, donde el juego va diciendo si se tiene un numero mayor o menor al numero propuesto, y cuando el jugador gana, lo invita a poner su numbre en la lista. 

Para la leaderboard, he definido tres funciones : 
- load_leaderboard : para abrir un documento leaderboard.txt o crearlo si no existe.
- update leader_board : para que el nombre del jugador que gana se registre en el leaderboard y se ordone por un dicionario con el que tiene el menor numero de intentos arriba. luego aparece como print la lista de ganadores con el rank, el nombre y el numero de intentos
- save leaderboard : para que se guarde la lista en el documento en el ordenador

Para terminar he definido una funcion main que es la principal que coordina la ejecucion del juego, es el menu de usuario donde el jugador elige un nivel para jugar y se establece el rango del juego.

