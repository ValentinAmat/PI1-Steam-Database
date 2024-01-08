<h1 align="center">Proyecto MLOps: Steam Database</h1>
<p align="center">
  <img src="https://cdn.cloudflare.steamstatic.com/store/home/store_home_share.jpg" alt="Logo de Steam" width=auto height="400" style="border-radius: 10px;">
</p>
<p align="center">
  <img src="https://assets.soyhenry.com/logoOG.png" alt="Logo de Henry" width=200 height="auto" style="border-radius: 5px;">
</p>


<h3>Introducción:</h3>

Este proyecto consiste en crear una **API** que utiliza un modelo de recomendación para la plataforma de videojuegos "Steam". El objetivo es crear un sistema de recomendación de videojuegos para usuarios, basado en Machine Learning, y crear funciones que realicen consultas de interés para la empresa.  
**¿Qué es una API?** Es como el menú de un restaurante. Los clientes (aplicaciones o servicios) no necesitan conocer todos los detalles de cómo se preparan los platillos (funciones internas). En cambio, pueden hacer pedidos (llamadas a la API) utilizando el menú (conjunto de funciones y datos disponibles) y recibir los platillos (respuestas o resultados) sin necesidad de entrar a la cocina (conocer la implementación interna). La API actúa como un intermediario que facilita la interacción sin revelar todos los detalles internos.

**Herramientas utilizadas:** Python, Pandas, Scikit-Learn, FastAPI, Uvicorn, Render, Matplotlib, Seaborn, Plotly, WordCloud, TextBlob.


<h3>Pasos del proyecto:</h3>

**1. ETL**  
Realizamos un proceso de ETL (Extracción, Transformación y Carga) en el que extrajimos datos de diferentes fuentes, los transformamos según las necesidades del proyecto y los cargamos en un destino final para su análisis y uso posterior.  
Herramientas utilizadas: Python, Pandas, TextBlob.  
Archivos utilizados para la carga: steam_games.json.gz, australian_user_reviews.json, australian_users_items.json.  
Archivos producidos: games.csv, reviews.csv, text_reviews.csv, users.csv.

**2. EDA**  
Realizamos un EDA (Analisis Exploratorio de Datos) con el objetivo de obtener insights, identificar patrones, tendencias y relaciones, y así tomar decisiones fundamentadas en base a la información obtenida. Intentando asi obtener alguna pista para crear los modelos de ML.  
Herramientas utilizadas fueron: Pandas, Matplotlib, Seaborn, Plotly, WordCloud.

**3. Funciones**  
Creamos las funciones:

>PlayTimeGenre(genero): Devuelve año con mas horas jugadas para dicho género.

>UserForGenre(genero): Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

>UsersRecommend(año): Devuelve el top 3 de juegos más recomendados por usuarios para el año dado.

>UsersWorstDeveloper(año): Devuelve el top 3 de empresas desarrolladoras cuyos juegos tienen menos reseñas por usuarios para el año dado.

>sentiment_analysis(empresa desarrolladora): Devuelve una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados como positivos, neutrales o negativos, para la empresa desarrolladora.

Herramientas utilizadas: Python, Pandas.


**4. MLOps: Modelos de recomendación**  
Creamos los modelos de recomendación:

>recomendacion_juego(id del juego): Recibimos una lista con 5 IDs de juegos recomendados similares al ingresado.

>recomendacion_usuario(id del usuario): Recibimos una lista con 5 juegos recomendados para dicho usuario.

Herramientas utilizadas: Python, Pandas, cosine_similarity de Scikit-Learn.


**5. Deployment de la API**  
Utilizamos las librerias Uvicorn y FastApi para la creación de la API. Una vez que ya tenemos nuestra API local con las 5 funciones y 2 modelos de recomendación, la subimos a Render creando asi una página web donde tenemos nuestra API con sus consultas en la nube.


<h3>Datos de prueba:</h3>

Géneros: "Action", "Adventure", "Animation & Modeling", "Audio Production", "Casual", "Design & Illustration", "Early Access", "Education", "Free to Play", "Indie", "Massively Multiplayer", "Photo Editing", "RPG", "Racing", "Simulation", "Software Training", "Sports", "Strategy", "Utilities", "Video Production", "Web Publishing".

Empresas desarrolladoras: "Valve", "Stainless Games Ltd", "Outerlight Ltd.", "Epic Games, Inc.", "Introversion Software", "Facepunch Studios", "Trion Worlds", "Wild Shadow Studios".

IDs de usuarios: "76561197970982479", "Js41637", "Evcentric", "Riot-punch", "Doctr", "76561198315899135", "Arkplays7", "Fr0stedline".

IDs de juegos: 719920, 403030, 718290, 718150, 717130, 718290, 718150, 466770, 280680, 659710, 414720, 522040, 280930, 662390, 348810.

Años: cualquier año entre 2011 y 2016.

**!!!**  
Introducir los valores sin las comillas dobles.  
Algunos valores introducidos pueden dar error por la falta de datos disponibles.


<h3>Links:</h3>

Deploy de la API en Render: https://deploy-steam-database.onrender.com/docs#/

Video explicativo:


<h3>Contacto:</h3>

Linkedin: https://www.linkedin.com/in/valent%C3%ADn-amat-45b6b1252/

Mail: amatgil5@gmail.com