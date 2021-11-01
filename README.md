# ALPHAUPO
Alphaupo es un motor de ajedrez que intenta imitar la inteligencia humana con varias implementaciones.

Contiene una demo para minimax y minimax con alphabeta en el fichero que se encuentra en Game -> Engine -> main.py.

Organización:

  Database maker:
  Contiene un script que carga la base de datos con los archivos pgn que se le pasen.

  Game:
  En esta carpeta va la implementación del juego y los motores de ajedrez.

  Game -> Game:
  Contiene los archivos de la implementación del juego base.

  Game -> Engine:
  Contiene los archivos de los motores de ajedrez.

  Game -> Engine -> Games:
  Contiene las partidas exportadas desde el motor en formato pgn.

  Game -> Engine -> MiniMax:
  Contiene los archivos de la implementación con el algoritmo de minimax.
