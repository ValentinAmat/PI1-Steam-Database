<h1 align="center">Proyecto MLOps: Steam Database</h1>
<p align="center">
  <img src="https://cdn.cloudflare.steamstatic.com/store/home/store_home_share.jpg" alt="Logo de Steam" width=auto height="400" style="border-radius: 10px;">
</p>
<p align="center">
  <img src="data:image/png;base64,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" alt="Logo de Henry" width=200 height="auto" style="border-radius: 5px;">
</p>


<h3>Introducción:</h3>

Este proyecto consiste en crear una **API** que utiliza un modelo de recomendación para la plataforma de videojuegos "Steam". El objetivo es crear un sistema de recomendación de videojuegos para usuarios, basado en Machine Learning, y crear funciones que realicen consultas de interés para la empresa.  
**¿Qué es una API?** Es como el menú de un restaurante. Los clientes (aplicaciones o servicios) no necesitan conocer todos los detalles de cómo se preparan los platillos (funciones internas). En cambio, pueden hacer pedidos (llamadas a la API) utilizando el menú (conjunto de funciones y datos disponibles) y recibir los platillos (respuestas o resultados) sin necesidad de entrar a la cocina (conocer la implementación interna). La API actúa como un intermediario que facilita la interacción sin revelar todos los detalles internos.

**Herramientas utilizadas:** Python, Pandas, Scikit-Learn, FastAPI, Uvicorn, Render, Matplotlib, Seaborn, Plotly, WordCloud.


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

Deploy de la API en Render: https://deploy-steam-database.onrender.com

Video explicativo:


<h3>Contacto:</h3>

Linkedin: https://www.linkedin.com/in/valent%C3%ADn-amat-45b6b1252/

Mail: amatgil5@gmail.com