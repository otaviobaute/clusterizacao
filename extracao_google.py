import pandas as pd
import os
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
import re
import random
import pyautogui
import requests

#-------------------------------------------------
# teste função
def ajuste(PLACE_ID,DAY,ENDERECO,MUNICIPIO,NOME,TAG,PLACE_LATITUDE,PLACE_LONGITUDE,PLACE_NOME,list):
    return_frame = pd.DataFrame(columns=['place_id','day','0hs','1hs','2hs','3hs','4hs','5hs','6hs','7hs','8hs','9hs','10hs','11hs','12hs','13hs','14hs','15hs','16hs','17hs','18hs','19hs','20hs','21hs','22hs','23hs','place_nome','tag','place_logradouro','nome_municipio','place_latitude','place_longitude'])
    PLACE_ID = PLACE_ID
    DAY = DAY
    nova_lista_hora_fluxo = []
    lista_horas = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    for hora in lista_horas:
        valor_hora1 = ''
        valor_hora2 = ''
        for valor in lista_hora_fluxo:
            if hora in valor:
                #print(f'HORA: {hora} / FLUXO: {valor[1]}')
                valor_hora1 = valor[1]
            else:
                valor_hora2 = '0'

        if valor_hora1 != '':
            nova_lista_hora_fluxo.append(valor_hora1)
        else:
            nova_lista_hora_fluxo.append(valor_hora2)
        #print(f'HORA: {hora} / FLUXO: {valor[1]}')
    C = nova_lista_hora_fluxo
    return_frame2 = pd.DataFrame({'place_id':PLACE_ID,'day':DAY,'0hs':C[0],'1hs':C[1],'2hs':C[2],'3hs':C[3],'4hs':C[4],'5hs':C[5],'6hs':C[6],'7hs':C[7],'8hs':C[8],'9hs':C[9],'10hs':C[10],'11hs':C[11],'12hs':C[12],'13hs':C[13],'14hs':C[14],'15hs':C[15],'16hs':C[16],'17hs':C[17],'18hs':C[18],'19hs':C[19],'20hs':C[20],'21hs':C[21],'22hs':C[22],'23hs':C[23],'place_nome':NOME,'tag':TAG,'place_logradouro':ENDERECO,'nome_municipio':MUNICIPIO,'place_latitude':PLACE_LATITUDE,'place_longitude':PLACE_LONGITUDE},index=[0])
    return_frame = pd.concat([return_frame,return_frame2],ignore_index=True)

    #return(PLACE_ID,DAY,nova_lista_hora_fluxo)
    return(return_frame)
#-------------------------------------------------

dados_busca = pd.read_csv('I:/Comum/Diversos/Otavio/projeto_estagio_producao/dados_kognita/POI_BR_2021-6-23-18-31.csv', delimiter='\t',encoding='utf-8',usecols=['place_id','nome_municipio_10','munic','tag','place_latitude','place_longitude','place_logradouro','place_nome']).query('nome_municipio_10 == "sao_jose_dos_campos" & tag  == ["drogaria","farmacia","hipermercado","hortifruti","hospital","dentista","consultorio","clinica medica","clinica","banco","mercado","odontologia","padaria","posto","restaurante","supermercado"]')
dados_busca = dados_busca.query('tag  == ["drogaria","farmacia","hipermercado","hortifruti","banco","mercado","padaria","posto","restaurante","supermercado"]')
#dados_busca = query[['nome_municipio_10','munic','tag','place_latitude','place_longitude','place_logradouro','place_nome']]
URL = 'https://www.google.com.br/search?q=AVENIDA+DOS+AUTONOMISTAS+1768&ei=djMFY9anKNyj1sQPlbaXoA8&ved=0ahUKEwjWupXk4d35AhXckZUCHRXbBfQQ4dUDCA4&uact=5&oq=AVENIDA+DOS+AUTONOMISTAS+1768&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDICCCYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWSgQIQRgASgQIRhgAUABYAGD6AmgAcAF4AIABc4gBc5IBAzAuMZgBAKABAqABAcABAQ&sclient=gws-wiz&safe=active&ssui=on'

frame = pd.DataFrame(columns=['place_id','day','0hs','1hs','2hs','3hs','4hs','5hs','6hs','7hs','8hs','9hs','10hs','11hs','12hs','13hs','14hs','15hs','16hs','17hs','18hs','19hs','20hs','21hs','22hs','23hs','place_nome','tag','place_logradouro','nome_municipio','place_latitude','place_longitude']) #,'nome_municipio_10','codigo_uf','tag','place_bairro','place_business_type','place_latitude','place_longitude','place_logradouro','place_nome'


navegador = webdriver.Chrome('I:/Comum/Diversos/Otavio/Scrapping Concorrentes/Associadas/chromedriver.exe')
sleep(15)
navegador.get(URL)
sleep(3)
#pyautogui.scroll(+3000)

for end in range(60,250):#len(dados_busca)):

    sleep(random.randint(2,5))
    navegador.find_element_by_xpath('//html/body/div/div[2]/form/div[1]/div/div[2]/div/div[2]/input').click()
    #pyautogui.moveTo(790,280)
    #pyautogui.click()
    sleep(0.5)
    navegador.find_element_by_xpath('//html/body/div/div[2]/form/div[1]/div/div[2]/div/div[2]/input').clear()
    sleep(0.5)
    navegador.find_element_by_xpath('//html/body/div/div[2]/form/div[1]/div/div[2]/div/div[2]/input').click()
    #pyautogui.press('backspace',200,0.001)
    #pyautogui.press('delete',200,0.001)
    

    PLACE_ID = dados_busca.iloc[end,1]
    ENDERECO = dados_busca.iloc[end,6] #6
    MUNICIPIO = 'Sao Jose dos Campos' #dados_busca.iloc[end,0]
    NOME = dados_busca.iloc[end,7] #7
    TAG = dados_busca.iloc[end,2]
    PLACE_LATITUDE = dados_busca.iloc[end,4]
    PLACE_LONGITUDE = dados_busca.iloc[end,5]
    PLACE_NOME = dados_busca.iloc[end,7]

    print(f'Pesquisando \n{NOME} \n{ENDERECO} \n{MUNICIPIO}')


    # digitar expressão que vamos pesquisar

    sleep(1)
    pyautogui.write(f'{ENDERECO} {MUNICIPIO} {NOME}')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)

    lista_dias = ['segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','sábado','domingo']
    for y in lista_dias:
        DAY = y
        lista_hora_fluxo = []
        sleep(0.3)
        #a = navegador.find_element_by_link_text('qua.')
        try:
            navegador.find_element_by_xpath(f"//div[@aria-label='{y}']").click()
        except:
            continue
        sleep(1.5)
        conteudo = navegador.page_source
        soup = bs(conteudo,'html.parser')
        flow_box = soup.find_all('div', {'class':'wYzX9b'})

        # verifica se o dia da semana não foi encontrado
        # se o dia não tiver fluxo ele preenche com 0 cada horário

        if len(flow_box) == 0:
            print(f'não encontrei o dia :{y}')
            teste = pd.DataFrame([[f'{PLACE_ID}',f'{DAY}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'-','-','-','-','-','-']],columns=['place_id','day','0hs','1hs','2hs','3hs','4hs','5hs','6hs','7hs','8hs','9hs','10hs','11hs','12hs','13hs','14hs','15hs','16hs','17hs','18hs','19hs','20hs','21hs','22hs','23hs','place_nome','tag','place_logradouro','nome_municipio','place_latitude','place_longitude'])
            frame = pd.concat([frame,teste],ignore_index=True)
            continue

        lista_hora_fluxo.append((PLACE_ID,f'{y}'))
        sleep(1)
        for x in range(len(flow_box)):

            # pegar dados da página

            #conteudo = navegador.page_source
            #soup = bs(conteudo,'html.parser')
            #flow_box = soup.find_all('div', {'class':'wYzX9b'})
            sleep(0.2)
            #soup2 = bs(str(flow_box), 'html.parser')
            hora = soup.find_all('div', {'class':'wYzX9b'})
            fluxo = soup.find_all('div', {'class':'cwiwob'})
            sleep(0.2)

            hr = str(hora[x])
            fl = str(fluxo[x])
            # pegar valor de hora

            inicio_hr = hr.find('aria-label=')+12
            fim_hr = hr.find('class="wYzX9b"')-2
            HORA = hr[inicio_hr:fim_hr-3]

            # pegar valor de fluxo

            inicio_fl = fl.find('height:')+7
            fim_fl = fl.find('px;')
            FLUXO = fl[inicio_fl:fim_fl]
            #print(f'HORA: {HORA} / FLUXO: {FLUXO}')

            # inserir na lista de pois

            lista_hora_fluxo.append((HORA,FLUXO))

            # ajustar dados da lista_hora_fluxo

            teste = ajuste(PLACE_ID,DAY,ENDERECO,MUNICIPIO,NOME,TAG,PLACE_LATITUDE,PLACE_LONGITUDE,PLACE_NOME,lista_hora_fluxo)

        frame = pd.concat([frame,teste],ignore_index=True)
        #frame2 = pd.DataFrame(teste, columns=['place_id','day','0hs','1hs','2hs','3hs','4hs','5hs','6hs','7hs','8hs','9hs','10hs','11hs','12hs','13hs','14hs','15hs','16hs','17hs','18hs','19hs','20hs','21hs','22hs','23hs'])
        print('Pesquisa concluída')
    #except:
        #print('Erro na pesquisa')
        #lista_erros.insert(-1,PLACE_ID)


# converter as colunas para string ou integer e exportar para excel


frame['place_id'] = frame['place_id'].astype(str)

frame[['0hs','1hs','2hs','3hs','4hs','5hs','6hs','7hs','8hs','9hs','10hs','11hs','12hs','13hs','14hs','15hs','16hs','17hs','18hs','19hs','20hs','21hs','22hs','23hs']] = frame[['0hs','1hs','2hs','3hs','4hs','5hs','6hs','7hs','8hs','9hs','10hs','11hs','12hs','13hs','14hs','15hs','16hs','17hs','18hs','19hs','20hs','21hs','22hs','23hs']].astype(int)

frame.to_excel(f'I:/Comum/Diversos/Otavio/projeto_estagio_producao/extracao_google/extraction_0_250.xlsx',index=False)
