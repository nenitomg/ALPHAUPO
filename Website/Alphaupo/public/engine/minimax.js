/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */




function negativeRotateArray(arr) {
    var res = arr.slice();
    var tam = arr.length;

    for (var i = 0; i < tam; i++) {
        for (var j = 0; j < tam; j++) {
            res[i][tam - 1 - j] = arr[tam - 1 - i][j] * (-1);
        }
    }
    return res;
}



var wp = [
    [0., 0., 0., 0., 0., 0., 0., 0.],
    [5., 5., 5., 5., 5., 5., 5., 5.],
    [1., 1., 2., 3., 3., 2., 1., 1.],
    [0.5, 0.5, 1., 2.5, 2.5, 1., 0.5, 0.5],
    [0., 0., 0., 2., 2., 0., 0., 0.],
    [0.5, -0.5, -1., 0., 0., -1., -0.5, 0.5],
    [0.5, 1., 1., -2., -2., 1., 1., 0.5],
    [0., 0., 0., 0., 0., 0., 0., 0.]
];

var bp = this.negativeRotateArray(wp);

var wn = [
    [-5., -4., -3., -3., -3., -3., -4., -5.],
    [-4., -2., 0., 0., 0., 0., -2., -4.],
    [-3., 0., 1., 1.5, 1.5, 1., 0., -3.],
    [-3., 0.5, 1.5, 2., 2., 1.5, 0.5, -3.],
    [-3., 0., 1.5, 2., 2., 1.5, 0., -3.],
    [-3., 0.5, 1., 1.5, 1.5, 1., 0.5, -3.],
    [-4., -2., 0., 0.5, 0.5, 0., -2., -4.],
    [-5., -4., -3., -3., -3., -3., -4., -5.]
];

var bn = this.negativeRotateArray(wn);

var wb = [
    [-2., -1., -1., -1., -1., -1., -1., -2.],
    [-1., 0., 0., 0., 0., 0., 0., -1.],
    [-1., 0., 0.5, 1., 1., 0.5, 0., -1.],
    [-1., 0.5, 0.5, 1., 1., 0.5, 0.5, -1.],
    [-1., 0., 1., 1., 1., 1., 0., -1.],
    [-1., 1., 1., 1., 1., 1., 1., -1.],
    [-1., 0.5, 0., 0., 0., 0., 0.5, -1.],
    [-2., -1., -1., -1., -1., -1., -1., -2.]
];

var bb = this.negativeRotateArray(wb);

var wr = [
    [0., 0., 0., 0., 0., 0., 0., 0.],
    [0.5, 1., 1., 1., 1., 1., 1., 0.5],
    [-1., 0., 0.5, 1., 1., 0.5, 0., -0.5],
    [-1., 0.5, 0.5, 1., 1., 0.5, 0.5, -0.5],
    [-1., 0., 1., 1., 1., 1., 0., -0.5],
    [-1., 1., 1., 1., 1., 1., 1., -0.5],
    [-1., 0.5, 0., 0., 0., 0., 0.5, -0.5],
    [0., 0., 0., 0.5, 0.5, 0., 0., 0.]
];

var br = this.negativeRotateArray(wr);

var wq = [
    [-2, -1, -1, -0.5, -0.5, -1, -1, -2],
    [-1, 0., 0., 0., 0., 0., 0., -1],
    [-1, 0., 0.5, 0.5, 0.5, 0.5, 0., -1],
    [-0.5, 0., 0.5, 0.5, 0.5, 0.5, 0., -0.5],
    [0, 0., 0.5, 0.5, 0.5, 0.5, 0., -0.5],
    [-1, 0.5, 0.5, 0.5, 0.5, 0.5, 0., -1],
    [-1, 0., 0.5, 0., 0., 0., 0., -1],
    [-2, -1, -1, -0.5, -0.5, -1, -1, -2]
];

var bq = this.negativeRotateArray(wq);


var wk = [
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-2, -3, -3, -4, -4, -3, -3, -2],
    [-1., -2, -2, -2, -2, -2, -2, -1],
    [2, 2, 0., 0., 0., 0., 2, 2],
    [2, 3, 1, 0, 0, 1, 3, 2]
];

var bk = negativeRotateArray(wk);








function minimax(board, depth) {
    if (depth === 0 || board.is_checkmate() || board.is_stalemate()) {
        return [this.fitness(board), null];
    } else {
        var toMove = board.toMove;
        var moves = board.getLegalMoves(board.toMove);

        //Maximizamos las blancas
        if (toMove === 0) {
            var bestScore = -9999999999;
            var bestMove = false;

            for (var i = 0; i < moves.length; i++) {
                board.makeMove(moves[i]);
                var res = minimax(board, depth - 1);
                board.revertLastMove(false);

                if (res[0] > bestScore) {
                    bestScore = res[0];
                    bestMove = moves[i];
                }
            }
            return [bestScore, bestMove];
        } else {
            var bestScore = 9999999999;
            var bestMove = false;

            for (var i = 0; i < moves.length; i++) {
                board.makeMove(moves[i]);
                var res = minimax(board, depth - 1);
                board.revertLastMove(false);

                if (res[0] < bestScore) {
                    bestScore = res[0];
                    bestMove = moves[i];
                }
            }
            return [bestScore, bestMove];
        }

    }

}




function minimaxAlphaBetaPruning(board, depth, alpha, beta) {
    if (depth === 0 || board.is_checkmate() || board.is_stalemate()) {
        return [this.fitness(board), null];
    } else {
        var toMove = board.toMove;
        var moves = board.getLegalMoves(board.toMove);

        //Maximizamos las blancas
        if (toMove === 0) {
            var bestMove = false;

            for (var i = 0; i < moves.length; i++) {
                board.makeMove(moves[i]);
                var res = minimaxAlphaBetaPruning(board, depth - 1, alpha, beta);
                board.revertLastMove(false);

                if (res[0] > alpha) {
                    bestMove = moves[i];
                    alpha = res[0];

                    if (alpha >= beta) {
                        break;
                    }
                }
            }
            return [alpha, bestMove];
        } else {
            var bestMove = false;

            for (var i = 0; i < moves.length; i++) {
                board.makeMove(moves[i]);
                var res = minimaxAlphaBetaPruning(board, depth - 1, alpha, beta);
                board.revertLastMove(false);

                if (res[0] < beta) {
                    bestMove = moves[i];
                    beta = res[0];

                    if (beta <= alpha) {
                        break;
                    }
                }
            }
            return [beta, bestMove];
        }

    }

}



function fitness(board) {
    var res = board.material_value();

    if (board.is_checkmate()) {
        if (board.toMove === 1) {
            return 999999;
        } else {
            return -999999;
        }
    }


    for (var i = 0; i < board.pieces.length; i++) {
        var pc = board.pieces[i];
        if (pc.name === "wp") {
            res += wp[pc.pos[0]][pc.pos[1]];
        } else if (pc.name === "bp") {
            res += bp[pc.pos[0]][pc.pos[1]];
        } else if (pc.name === "wn") {
            res += wn[pc.pos[0]][pc.pos[1]];
        } else if (pc.name === "bn") {
            res += bn[pc.pos[0]][pc.pos[1]];
        } else if (pc.name === "wb") {
            res += wb[pc.pos[0]][pc.pos[1]];
        } else if (pc.name === "bb") {
            res += bb[pc.pos[0]][pc.pos[1]];
        } else if (pc.name === "wr") {
            res += wr[pc.pos[0]][pc.pos[1]];
        } else if (pc.name === "br") {
            res += br[pc.pos[0]][pc.pos[1]];
        } else if (pc.name === "wq") {
            res += wq[pc.pos[0]][pc.pos[1]];
        } else if (pc.name === "bq") {
            res += bq[pc.pos[0]][pc.pos[1]];
        } else if (pc.name === "wk") {
            res += wk[pc.pos[0]][pc.pos[1]];
        } else if (pc.name === "bk") {
            res += bk[pc.pos[0]][pc.pos[1]];
        }
    }

    return res;

}