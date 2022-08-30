import pandas as pd
import re
import requests
from time import sleep
from tqdm import tqdm
from googletrans import Translator
from time import sleep

# CÓDIGO PARA ACHAR ESTABELECIMENTOS USANDO A API GOOGLE TEXT SEARCH (PLACES)

DF = pd.DataFrame(columns=['place_id','place_nome','tag','place_logradouro','nome_municipio','place_latitude','place_longitude'])
#address = 'EST PRESIDENTE JUSCELINO KUBITSCHEK DE OLIVEIRA 4414 - JARDIM ALBERTINA - GUARULHOS/SP CEP: 07252-000'


#-----------------------------------
# FIND PLACE (que é o location bias)
#-----------------------------------

type_location_return = ['pharmacy|drugstore|store|point_of_interest|establishment']

#type_location_return = ['supermarket|store|point_of_interest|establishment']

# lista de alguns latxlong da cidade de São José dos Campos

lista_lat_longs = [('-23.219840','-45.891566'),('-23.187207','-45.866376'),('-23.242072','-45.884798'),('-23.192660','-45.916026'),('-23.199913','-45.941625'),('-23.182165','-45.950534'),('-23.203169','-45.956188'),('-23.268154','-45.895449'),('-23.141791','-45.782441'),('-23.173162','-45.780787')]

# url com os dados para consultar com base nos parâmetros "type_location_return" e "lista_lat_longs"

radius = '5000'
query = 'padaria'
url_text_search = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={location_lat}%2C{location_long}&radius={radius}&type={type_location_return}&key={key}'


# loop de pesquisa - para cada par de latxlong faremos uma pesquisa que retornará 20 locais, que serão tratados e incluídos em um dataframe



for lat_long in lista_lat_longs:
    lat = lat_long[0]
    long = lat_long[1]

    url_text_search = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={lat}%2C{long}&radius={radius}&type={type_location_return}&key={key}'

    dado_ = requests.get(url_text_search)
    sleep(3)
    dado__ = dado_.json()
    dados = dado__['results']


    for local in dados:
        sleep(0.2)
        PLACE_ID = local['place_id']
        NOME = local['name']                              # place_nome
        TYPE = local['types']
        END = local['formatted_address']
        ENDERECO = re.sub(',','',END.replace('Brazil','')).strip()          # place_logradouro
        try:
            MUNICIPIO = re.sub('-','',ENDERECO.split(',')[1].replace('State of São Paulo','')).strip()                                  # nome_municipio
        except:
            MUNICIPIO = 'São José dos Campos'
        LATITUDE = local['geometry']['location']['lat']   # place_latitude
        LONGITUDE = local['geometry']['location']['lng']  #  place_longitude
        
        
        DF2 = pd.DataFrame([[PLACE_ID,NOME,TYPE,ENDERECO,MUNICIPIO,LATITUDE,LONGITUDE]],columns=['place_id','place_nome','tag','place_logradouro','nome_municipio','place_latitude','place_longitude'])
        print(f'##############################\n{PLACE_ID}\n{NOME}\n{ENDERECO}\n{MUNICIPIO}\n{LATITUDE}\n{LONGITUDE}\n##############################')
        
        # salvar no dataframe inicial
        
        DF = pd.concat([DF,DF2])

DF.to_excel('I:/Comum/Diversos/Otavio/projeto_estagio_producao/extracao_google/extrair_find_place/extraction_text_search_padaria.xlsx',index=False,encoding='utf-8')
