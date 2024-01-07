from fastapi import FastAPI
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# URL local: http://127.0.0.1:8000



# Carga de archivos: ----------------------------------------------------------------------------------------

# PlayTimeGenre:
df_playtimegenre_final = pd.read_csv(r"Archivos Producidos\Data para Endpoints\df_playtimegenre_final.csv")

# UserForGenre:
df_userforgenre_final = pd.read_csv(r"Archivos Producidos\Data para Endpoints\df_userforgenre_final.csv")

# UsersRecommend:
df_usersrecommend = pd.read_csv(r"Archivos Producidos\Data para Endpoints\df_usersrecommend.csv")

# UsersWorstDeveloper:
df_usersworstdeveloper = pd.read_csv(r"Archivos Producidos\Data para Endpoints\df_usersworstdeveloper.csv")

# sentiment_analysis:
df_sentiment_analysis = pd.read_csv(r"Archivos Producidos\Data para Endpoints\df_sentiment_analysis.csv")

# recomendacion_juego:
df_recom_game = pd.read_csv(r"Archivos Producidos\Data para Endpoints\df_recom_game.csv")

# recomendacion_usuario:
user_df = pd.read_csv(r"Archivos Producidos\Data para Endpoints\user_df.csv")
videogames_df = pd.read_csv(r"Archivos Producidos\Data para Endpoints\videogames_df.csv")
# también cargaremos la función "recomendacion_juego" que se usará en "recomendacion_usuario":
def recomendacion_juego(item_id):

    # Obtenemos la fila correspondiente al juego dado por "item_id":
    juego = df_recom_game[df_recom_game["item_id"] == item_id].iloc[:, 1:]

    # Excluímos el juego del DataFrame antes de calcular la similitud (evitamos que el modelo nos recomiende el mismo juego):
    df_sin_juego = df_recom_game[df_recom_game["item_id"] != item_id]

    # Calculamos la similitud de coseno entre el juego y todos los demás juegos:
    similitudes = cosine_similarity(juego, df_sin_juego.iloc[:, 1:])

    # Convertimos las similitudes en un DataFrame:
    similitudes_df = pd.DataFrame(similitudes.flatten(), columns=["similitud"])

    # Encontramos los 5 juegos más similares:
    juegos_similares = df_sin_juego.loc[similitudes_df.sort_values(
        by="similitud", ascending=False).index[:5], "item_id"]

    # Devolvemos el resultado final:
    return list(juegos_similares)

# -----------------------------------------------------------------------------------------------------------



@app.get("/")
def index():
    return "PROYECTO DE BASE DE DATOS DE STEAM, POR VALENTÍN AMAT"


@app.get("/PlayTimeGenre/")
def PlayTimeGenre(genero: str):

    # Verificamos si la variable introducida es una cadena de texto:
    if type(genero) != str: return f"El género '{genero}' no existe."
    else:

        # Capitalizamos la cadena de texto:
        genero = genero.strip().capitalize()
    
        # Comprobamos si el género existe en el DataFrame
        if genero not in df_playtimegenre_final["genre"].tolist():
            return f"El género '{genero}' no existe."
        
        # # Filtramos las filas para el género específico:
        df_genero = df_playtimegenre_final[df_playtimegenre_final["genre"] == genero]

        # En caso de que el género introducido no tenga horas de juego:
        if (df_genero["playtime"] == 0).any():
            return f"El género '{genero}' no posee horas jugadas."
        
        # En caso de que el género introducido si tenga horas de juego:
        else:

            # Hallamos el índice del registro con mayor cantidad de horas de juego:
            indice_max_playtime = df_genero["playtime"].idxmax()
            
            # Tomamos el año de dicho registro:
            año_max_playtime = df_genero.loc[indice_max_playtime]["release_year"]

            # Devolvemos la respuesta final:
            return {f"Año de lanzamiento con más horas jugadas para Género {genero}" : año_max_playtime}


@app.get("/userForGenre/")
def UserForGenre(genero: str):

    # Verificamos si la variable introducida es una cadena de texto:
    if type(genero) != str: return f"El género '{genero}' no existe."
    else:

        # Capitalizamos la cadena de texto:
        genero = genero.strip().capitalize()
    
        # Comprobamos si el género existe en el DataFrame:
        if genero not in df_userforgenre_final["genre"].tolist():
            return f"El género '{genero}' no existe o no tiene horas de juego."

        # En caso de que el género introducido si tenga horas de juego:
        else:

            # Filtramos por género, ordenamos con orden de años descendente:
            df_genero = df_userforgenre_final[df_userforgenre_final["genre"] == genero].sort_values(by="year", ascending=False)

            # Agrupamos haciendo suma de las horas jugadas según usuario:
            df_genero_grouped = df_genero.groupby(["user_id", "genre"], as_index=False)["playtime"].sum()

            # Hallamos el índice del mayor tiempo de juego:
            indice_max_playtime = df_genero_grouped["playtime"].idxmax()

            # Hallamos el usuario con dicho índice:
            user = df_genero_grouped.loc[indice_max_playtime]["user_id"]

            # Buscamos el historial de juego del usuario:
            historial = df_genero[df_genero["user_id"] == user]

            # Creamos la variable que utilizaremos como respuesta final:
            diccionario = {f"Usuario con más horas jugadas para Género {genero}" : user,
                        "Horas jugadas":[]}

            # Rellenamos esa variable:
            for index, row in historial.iterrows():
                diccionario["Horas jugadas"].append({"Año": row["year"], "Horas": row["playtime"]})

            # Devolvemos la respuesta final:
            return diccionario


@app.get("/UsersRecommend/")
def UsersRecommend(año: int):

    # Corroboramos que el año introducido sea un número:
    if isinstance(año, int):
        
        # En caso de que el año no se encuentre en el DataFrame:
        if año not in df_usersrecommend["year"].tolist(): return f"{año} no se encuentra entre los años disponibles."

        # Caso contrario (ideal):
        else:

            # Filtramos por año:
            df_año = df_usersrecommend[df_usersrecommend["year"] == año].head(3)

            # Creamos la variable que utilizaremos como respuesta final:
            respuesta = [{"Puesto 1": None}, {"Puesto 2": None}, {"Puesto 3": None}]

            # Rellenamos esa variable:
            respuesta[0]["Puesto 1"] = df_año.iloc[0]["app_name"]
            respuesta[1]["Puesto 2"] = df_año.iloc[1]["app_name"]
            respuesta[2]["Puesto 3"] = df_año.iloc[2]["app_name"]

            # Devolvemos la respuesta final:
            return respuesta


    # En caso de que el año introducido no sea un número:
    else: return f"'{año}' no es un año válido."


@app.get("/UsersWorstDeveloper/")
def UsersWorstDeveloper(año: int):

    # Corroboramos que el año introducido sea un número:
    if isinstance(año, int):
        
        # En caso de que el año no se encuentre en el DataFrame:
        if año not in df_usersworstdeveloper["year"].tolist(): return f"{año} no se encuentra entre los años disponibles."

        # Caso contrario (ideal):
        else:

            # Filtramos por año:
            df_año = df_usersworstdeveloper[df_usersworstdeveloper["year"] == año].head(3)

            # Creamos la variable que utilizaremos como respuesta final:
            respuesta = [{"Puesto 1": None}, {"Puesto 2": None}, {"Puesto 3": None}]

            # Rellenamos esa variable:
            respuesta[0]["Puesto 1"] = df_año.iloc[0]["developer"]
            respuesta[1]["Puesto 2"] = df_año.iloc[1]["developer"]
            respuesta[2]["Puesto 3"] = df_año.iloc[2]["developer"]

            # Devolvemos la respuesta final:
            return respuesta


    # En caso de que el año introducido no sea un número:
    else: return f"'{año}' no es un año válido."


@app.get("/sentiment_analysis/")
def sentiment_analysis(developer: str):

    # Verificamos si la variable introducida es una cadena de texto:
    if type(developer) != str: return f"La empresa '{developer}' no existe."
    else:

        # Capitalizamos la cadena de texto:
        developer = developer.strip().title()
    
        # Comprobamos si la empresa desarrolladora existe en el DataFrame:
        if developer not in df_sentiment_analysis["developer"].tolist():
            return f"La empresa '{developer}' no existe o no tiene reseñas."

        # En caso de que la empresa introducida exista en el DataFrame:
        else:

            # Filtramos por empresa desarrolladora:
            df_developer = df_sentiment_analysis[df_sentiment_analysis["developer"] == developer]

            # Contamos los registros para cada caso:
            positive = len(df_developer[df_developer["sentiment_analysis"] == 2]) # Sentimientos positivos
            neutral = len(df_developer[df_developer["sentiment_analysis"] == 1]) # Sentimientos neutrales
            negative = len(df_developer[df_developer["sentiment_analysis"] == 0]) # Sentimientos negativos

            # Devolvemos la respuesta final:
            return {developer: [f"Negative = {negative}, Neutral = {neutral}, Positive = {positive}"]}


@app.get("/recomendacion_juego/")
def recomendacion_juego(item_id: int):

    # Obtenemos la fila correspondiente al juego dado por "item_id":
    juego = df_recom_game[df_recom_game["item_id"] == item_id].iloc[:, 1:]

    # Excluímos el juego del DataFrame antes de calcular la similitud (evitamos que el modelo nos recomiende el mismo juego):
    df_sin_juego = df_recom_game[df_recom_game["item_id"] != item_id]

    # Calculamos la similitud de coseno entre el juego y todos los demás juegos:
    similitudes = cosine_similarity(juego, df_sin_juego.iloc[:, 1:])

    # Convertimos las similitudes en un DataFrame:
    similitudes_df = pd.DataFrame(similitudes.flatten(), columns=["similitud"])

    # Encontramos los 5 juegos más similares:
    juegos_similares = df_sin_juego.loc[similitudes_df.sort_values(by="similitud", ascending=False).index[:5], "item_id"]

    # Devolvemos el resultado final:
    return list(juegos_similares)


@app.get("/recomendacion_usuario/")
def recomendacion_usuario(usuario: str):

    # Capitalizamos la variable usuario:
    usuario = usuario.strip().capitalize()


    # Obtenemos el "item_id" del juego que ha jugado el usuario:
    item_id = user_df[user_df["user_id"] == usuario]["item_id"].values[0]

    # Llamamos a la función anteriormente creada y creamos una lista con los nombres de los videojuegos en lugar de sus IDs:
    lista_ids = recomendacion_juego(item_id)
    lista_nombres = []
    for i in lista_ids:
        game_name = videogames_df[videogames_df["item_id"] == i]["app_name"].values[0]
        lista_nombres.append(game_name)

    # Devolvemos el resultado final:
    return lista_nombres