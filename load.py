import pandas as pd
from math import e
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

def load_data(movies_list):
    df = pre_process(movies_list)
    create_csv(df)
    dataframe = read_csv()
    send_data(dataframe)

def pre_process(movies_list):
    df = pd.DataFrame.from_dict(movies_list)
    df[['id','vote_count','vote_average','popularity']] = df[['id','vote_count','vote_average','popularity']].fillna(0)
    df[['original_language','title']] = df[['original_language','title']].fillna("Nulo")
    df['release_date'] = df['release_date'].fillna(value=pd.to_datetime('1/1/2015'))
    df['release_date'] = pd.to_datetime(df['release_date'])

    return df

def create_csv(df):
    df_columns = [ 'id', 'title', 'release_date','vote_count','vote_average','popularity', 'original_language']
    try:
        df[df_columns].to_csv('tmdb_movies1.csv', index=False)
    except:
        print("Arquivo já existe, por favor excluir antigo")

def read_csv():
    try:
        dataframe = pd.read_csv("tmdb_movies1.csv")
    except:
        print("Erro na leitura do arquivo")
    
    return dataframe

    
def send_data(dataframe):
    host = os.getenv('HOST')
    database = os.getenv('DATABASE')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')

    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    cur = conn.cursor()

    for index,row in dataframe.iterrows():
        try:
            cur.execute("SELECT * FROM filmes WHERE id = %s", [dataframe['id'][index].tolist()])
            db_id_in_database = cur.fetchone()
        except:
            db_id_in_database = None
        
        if db_id_in_database is None and dataframe['id'][index] != 0:
            try:
                query = "INSERT INTO filmes (id, title, release_date, vote_count, vote_average, popularity, original_language) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                records = (
                    dataframe['id'][index].tolist(),
                    dataframe['title'][index],
                    dataframe['release_date'][index],
                    dataframe['vote_count'][index].tolist(),
                    dataframe['vote_average'][index],
                    dataframe['popularity'][index],
                    dataframe['original_language'][index]
                )
                cur.execute(query, records)
                conn.commit()
                print(f"Inserido registro com ID {dataframe['id'][index]}")
            except Exception as e:
                print("Erro ao inserir registro: ", e)
        else:
            print("O filme já está no banco de dados")
