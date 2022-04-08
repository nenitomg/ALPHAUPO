<head>
    <title>ALPHAUPO</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!--JQUERY-->
    <script src="{{asset('lib/Jquery/jquery-3.6.0.min.js')}}"></script>

    <!--BOOTSTRAP-->
    <link href="{{ asset('lib/Bootstrap5/bootstrap.css') }}" rel="stylesheet">
    <script src="{{ asset('lib/Bootstrap5/bootstrap.bundle.js')}}"></script>

    <!--BOARD STYLES-->
    <link href="css/board.css" rel="stylesheet">

    @extends('Layout.linksPortada')
</head>
<body>
    @extends('Layout.header')
<div id="contenido2">
    <h1 id="titulo-basededatos">BASE DE DATOS</h1>
    <table id="tabla-de-partidas" class="table table-light table-striped">
        <thead class="table-dark">
            <tr>
                <th scope="col">Black</th>
                <th scope="col">White</th>
                <th scope="col">Event</th>
                <th scope="col">Date</th>
                <th scope="col">Round</th>
                <th scope="col">Result</th>
                <th scope="col">Site</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
            @foreach($partidas as $partida)
            <tr>
                <td>{{ $partida->Black}}</td>
                <td>{{ $partida->White }}</td>
                <td>{{ $partida->Event }}</td>
                <td>{{ $partida->Date }}</td>
                <td>{{ $partida->Round }}</td>
                <td>{{ $partida->Result }}</td>
                <td>{{ $partida->Site }}</td>
                <td><button class="btn btn-primary" onclick="reviewGame({{$partida->id}})">Analizar</button></td>
                <input id="{{$partida->id}}" style="display:none;" value="{{$partida->Game}}"/>
            </tr>
            @endforeach
        </tbody>
        
    </table>
    <div id="links-tabla-partidas">
        {{ $partidas->links() }}
    </div>
</div>



            <!-- Modal -->
        <div class="modal fade" id="analizar-partidas" tabindex="-1" role="dialog" aria-labelledby="analizar-partidasLabel" aria-hidden="true">
            <div id="modal-dialog-analisis" class="modal-dialog" role="document">
                <div id="modal-content-analisis" class="modal-content">
                    <div id="modal-header-analisis" class="modal-header">
                        <h5 class="modal-title" id="analizar-partidasLabel">Análisis</h5>
                        <button type="button" class="btn-close btn-close-white" aria-label="Close" onclick="closeModalGamesTable()"></button>
                    </div>
                    <div class="modal-body">
                            <div id="game-content">
                                <div id="game-board">
                                    <table id="tablero">
                                        <tbody>
                                            <tr>
                                                <td id="0_0" onclick="printMovesFor(0,0);" class="w_square"></td>
                                                <td id="0_1" onclick="printMovesFor(0,1);" class="b_square"></td>
                                                <td id="0_2" onclick="printMovesFor(0,2);" class="w_square"></td>
                                                <td id="0_3" onclick="printMovesFor(0,3);" class="b_square"></td>
                                                <td id="0_4" onclick="printMovesFor(0,4);" class="w_square"></td>
                                                <td id="0_5" onclick="printMovesFor(0,5);" class="b_square"></td>
                                                <td id="0_6" onclick="printMovesFor(0,6);" class="w_square"></td>
                                                <td id="0_7" onclick="printMovesFor(0,7);" class="b_square"></td>
                                            </tr>
                                            <tr>
                                                <td id="1_0" onclick="printMovesFor(1,0);" class="b_square"></td>
                                                <td id="1_1" onclick="printMovesFor(1,1);" class="w_square"></td>
                                                <td id="1_2" onclick="printMovesFor(1,2);" class="b_square"></td>
                                                <td id="1_3" onclick="printMovesFor(1,3);" class="w_square"></td>
                                                <td id="1_4" onclick="printMovesFor(1,4);" class="b_square"></td>
                                                <td id="1_5" onclick="printMovesFor(1,5);" class="w_square"></td>
                                                <td id="1_6" onclick="printMovesFor(1,6);" class="b_square"></td>
                                                <td id="1_7" onclick="printMovesFor(1,7);" class="w_square"></td>
                                            </tr>
                                            <tr>
                                                <td id="2_0" class="w_square" onclick="updateBoardHTML(2,0);"></td>
                                                <td id="2_1" class="b_square" onclick="updateBoardHTML(2,1);"></td>
                                                <td id="2_2" class="w_square" onclick="updateBoardHTML(2,2);"></td>
                                                <td id="2_3" class="b_square" onclick="updateBoardHTML(2,3);"></td>
                                                <td id="2_4" class="w_square" onclick="updateBoardHTML(2,4);"></td>
                                                <td id="2_5" class="b_square" onclick="updateBoardHTML(2,5);"></td>
                                                <td id="2_6" class="w_square" onclick="updateBoardHTML(2,6);"></td>
                                                <td id="2_7" class="b_square" onclick="updateBoardHTML(2,7);"></td>
                                            </tr>
                                            <tr>
                                                <td id="3_0" class="b_square" onclick="updateBoardHTML(3,0);"></td>
                                                <td id="3_1" class="w_square" onclick="updateBoardHTML(3,1);"></td>
                                                <td id="3_2" class="b_square" onclick="updateBoardHTML(3,2);"></td>
                                                <td id="3_3" class="w_square" onclick="updateBoardHTML(3,3);"></td>
                                                <td id="3_4" class="b_square" onclick="updateBoardHTML(3,4);"></td>
                                                <td id="3_5" class="w_square" onclick="updateBoardHTML(3,5);"></td>
                                                <td id="3_6" class="b_square" onclick="updateBoardHTML(3,6);"></td>
                                                <td id="3_7" class="w_square" onclick="updateBoardHTML(3,7);"></td>
                                            </tr>
                                            <tr>
                                                <td id="4_0" class="w_square" onclick="updateBoardHTML(4,0);"></td>
                                                <td id="4_1" class="b_square" onclick="updateBoardHTML(4,1);"></td>
                                                <td id="4_2" class="w_square" onclick="updateBoardHTML(4,2);"></td>
                                                <td id="4_3" class="b_square" onclick="updateBoardHTML(4,3);"></td>
                                                <td id="4_4" class="w_square" onclick="updateBoardHTML(4,4);"></td>
                                                <td id="4_5" class="b_square" onclick="updateBoardHTML(4,5);"></td>
                                                <td id="4_6" class="w_square" onclick="updateBoardHTML(4,6);"></td>
                                                <td id="4_7" class="b_square" onclick="updateBoardHTML(4,7);"></td>
                                            </tr>
                                            <tr>
                                                <td id="5_0" class="b_square" onclick="updateBoardHTML(5,0);"></td>
                                                <td id="5_1" class="w_square" onclick="updateBoardHTML(5,1);"></td>
                                                <td id="5_2" class="b_square" onclick="updateBoardHTML(5,2);"></td>
                                                <td id="5_3" class="w_square" onclick="updateBoardHTML(5,3);"></td>
                                                <td id="5_4" class="b_square" onclick="updateBoardHTML(5,4);"></td>
                                                <td id="5_5" class="w_square" onclick="updateBoardHTML(5,5);"></td>
                                                <td id="5_6" class="b_square" onclick="updateBoardHTML(5,6);"></td>
                                                <td id="5_7" class="w_square" onclick="updateBoardHTML(5,7);"></td>
                                            </tr>
                                            <tr>
                                                <td id="6_0" onclick="printMovesFor(6,0);" class="w_square"></td>
                                                <td id="6_1" onclick="printMovesFor(6,1);" class="b_square"></td>
                                                <td id="6_2" onclick="printMovesFor(6,2);" class="w_square"></td>
                                                <td id="6_3" onclick="printMovesFor(6,3);" class="b_square"></td>
                                                <td id="6_4" onclick="printMovesFor(6,4);" class="w_square"></td>
                                                <td id="6_5" onclick="printMovesFor(6,5);" class="b_square"></td>
                                                <td id="6_6" onclick="printMovesFor(6,6);" class="w_square"></td>
                                                <td id="6_7" onclick="printMovesFor(6,7);" class="b_square"></td>
                                            </tr>
                                            <tr>
                                                <td id="7_0" onclick="printMovesFor(7,0);" class="b_square"></td>
                                                <td id="7_1" onclick="printMovesFor(7,1);" class="w_square"></td>
                                                <td id="7_2" onclick="printMovesFor(7,2);" class="b_square"></td>
                                                <td id="7_3" onclick="printMovesFor(7,3);" class="w_square"></td>
                                                <td id="7_4" onclick="printMovesFor(7,4);" class="b_square"></td>
                                                <td id="7_5" onclick="printMovesFor(7,5);" class="w_square"></td>
                                                <td id="7_6" onclick="printMovesFor(7,6);" class="b_square"></td>
                                                <td id="7_7" onclick="printMovesFor(7,7);" class="w_square"></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                <div id="botones-game-content">
                    
                                    <div id="botones-adelante-atras">
                                        <button id="boton-ir-atras" class="btn btn-outline-dark" onclick="revertMove()"><</button>
                                        <button id="boton-ir-adelante" class="btn btn-outline-dark" onclick="goForwardMove()">></button>
                                    </div>
                                </div>
                                <p id="Pensando"></p>
                            </div>

                        <div id="next-moves"></div>
                    </div>
                </div>
            </div>

            

        </div>



    @extends('Layout.footer')


    <script src="engine/Alphaupo.js"></script>
    <script src="js/basededatos.js"></script>
    <script>
        $(document).ready(function() {
            $('#header-basededatos').addClass('active');
        });
    </script>

</body>