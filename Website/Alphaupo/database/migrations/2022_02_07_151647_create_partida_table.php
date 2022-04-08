<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePartidaTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('partida', function (Blueprint $table) {
            $table->id();
            $table->string('Black');
            $table->unsignedInteger('BlackElo');
            $table->date('Date');
            $table->string('ECO');
            $table->string('Game', 8192);
            $table->string('Event');
            $table->string('Result');
            $table->unsignedInteger('Round');
            $table->string('Site');
            $table->string('White');
            $table->unsignedInteger('WhiteElo');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('partida');
    }
}
