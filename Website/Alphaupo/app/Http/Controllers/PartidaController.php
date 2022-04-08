<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\partida;
use DB;

class PartidaController extends Controller
{
    public function index(){
        $partidas = partida::simplePaginate(50);
        return view('basededatos')->with('partidas', $partidas);
    }

    public function getNextDatabaseMove($game){

        echo json_encode(DB::select("
            SELECT LEFT(SUBSTRING(Game,LENGTH('%".$game."%')), InStr(SUBSTRING(Game,LENGTH('%".$game."%')),' ') - 1) as n_move, count(*) as number FROM `partida`
            WHERE Game LIKE '%".$game."%'
            GROUP BY n_move
            ORDER BY number DESC LIMIT 3;
        "));
    }

}
