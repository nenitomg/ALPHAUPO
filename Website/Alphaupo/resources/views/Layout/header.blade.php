  <!-- ======= Header ======= -->
  <header id="header" class="fixed-top ">
    <div class="container d-flex align-items-center">

      <h1 class="logo me-auto"><a href="{{ route('portada') }}">ALPHAUPO</a></h1>
      <!-- Uncomment below if you prefer to use an image logo -->
      <!-- <a href="index.html" class="logo me-auto"><img src="assets/img/logo.png" alt="" class="img-fluid"></a>-->

      <nav id="navbar" class="navbar">
        <ul>
          <li><a class="nav-link" href="{{ route('portada') }}">Home</a></li>
          <li><a class="nav-link" id="header-juega" href="{{ route('juega') }}">Juega</a></li>
          <li><a class="nav-link" id="header-basededatos" href="{{ route('basededatos') }}">Base de Datos</a></li>
        </ul>
        <i class="bi bi-list mobile-nav-toggle"></i>
      </nav><!-- .navbar -->

    </div>
  </header><!-- End Header -->