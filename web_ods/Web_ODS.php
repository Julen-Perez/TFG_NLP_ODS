	<!DOCTYPE html>
	<html>
	<head>
		<title>Mi Página</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
	</head>
	<body>
	<header id="primario">
	<div class="contenedor">
		<h1>Modelo de Tópicos basado en los Objetivos de desarrollo sostenible
		</h1>
	</div>

	</header>
	<nav id="navbar">
	<div class="contenedor">
		<ul>
			<li><a href="#">HOME</a></li>
			<li><a href="#">ABOUT</a></li>
			<li><a href="#">CONTACT US</a></li>
		</ul>
	</div>

	</nav>
	<section id="showcase">
		´<div class="contenedor">
			

		</div>
	</section>
	<div class="contenedor2">
	<section id="main">
		<h1>BIENVENIDO</h1>
		<p>Este proyecto pretende ayudar a 
		Se basa en tecnologías de Inteligencia Artificial y Machine Learning para crear un modelo de tópicos y poder reconocer tokens represetnatativos de cada ODS.
		<br>
		Ponga el texto a clasificar en el recuadro inferior destinado a ello y pulse enviar, el modelo de tópicos hará el resto y le devolverá una lista de tópicos ordenados de mas a menos representativos.
		<br>
		La respuesta incluye una lista con todos los ODS que son representativos en el texto, el campo id marca el grado de relevancia, siendo el id=0 el mas relevante, incluye también una lista de las palabras o "tokens" mas relevantes para cada ODS.</p>
	
	</section>
	<aside id="sidebar">
		
	</aside>
	</div>
	<div class="contenedor3">
	<section id="main">
		<h1>¡PRUÉBELO!</h1>
		<form action="Web_ODS.php" method="get">
 <textarea rows="5" cols="60" name="texto_a_clasificar" placeholder="Introducir texto"></textarea>

    <input type="submit">
</form>
<br>
<?php 
file_put_contents("texto.txt", $_GET["texto_a_clasificar"]);
echo utf8_encode(exec("import_requests.py"));


?> 
	</section>
	
	</div>
	<footer id= "pie">
	<p> <b>Developed by Julen Pérez Álvarez, 
		in colaboration with Oscar Corcho and Carlos Badenes-Olmedo
		</b></p>
		
		<p><b>Copyright &copy;2021 SDGs Topic Model Classifier</b></p>
	</footer>
	</body>
	</html>