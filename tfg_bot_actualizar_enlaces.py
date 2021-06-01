
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as soup  # HTML data structure
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import urllib.parse 
import re
from datetime import datetime

class ODS_BOT_ACTUALIZAR_ENLACES():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


    def parser(self,page_url): 
        uClient = urllib.request.urlopen(page_url)
        page_soup = soup(uClient.read(), "html.parser")
        uClient.close()
        containers = page_soup.findAll("div", {"class": "views-field views-field-field-body"})
        cleantext = soup(str(containers[0]),'html.parser').text
        return cleantext

  
    def actualizar_enlaces(self,a,fecha_ultima_actualizacion):
        lista_ods= self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div[1]/form/div/div/div/div[4]/div/div/select')
        lista_ods.click()
        sleep(1)
        escoger_filtro_ods= self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div[1]/form/div/div/div/div[4]/div/div/select/option[{}]'.format(a+1))
        escoger_filtro_ods.click()
        sleep(2)
        aplicar= self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div[1]/form/div/div/div/div[8]/input')
        aplicar.click()
        sleep(2)
        i=0
        articulo=[]
        while True:
            if i!=0 and i%15==0:
                mostrar_mas= self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/ul/li/a')
                mostrar_mas.click()
                sleep(4)
            stri= bot.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div[2]/div[{}]/div[3]/span'.format(i+1)).text
            fecha_noticia = datetime.strptime(stri, '%d/%m/%Y').date()
            if fecha_ultima_actualizacion<fecha_noticia:
                try:
                    articulo.append(self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div[2]/div[{}]/div[2]/span/a'.format(i+1)).get_attribute("href"))
                    i+=1
                except Exception:
                    i+=1
                    continue     
            else:
                break
        return articulo


bot = ODS_BOT_ACTUALIZAR_ENLACES()               
bot.driver.get('https://www.corresponsables.com/actualidad')
sleep(4)
filename="texts_tests.csv"
j=11058;
p=11058;
fecha_ultima_actualizacion=datetime.strptime('16/04/2021', '%d/%m/%Y').date()
numero_enlaces=[]
with open(filename, "w", encoding="utf-8") as f:
    for c in range(17):
        enlaces=bot.actualizar_enlaces(c+1,fecha_ultima_actualizacion)
        numero_enlaces.append(len(enlaces))

        for enlace in enlaces:
            try: 
                sol=bot.parser(enlace).replace("\n", " ")
                f.write(str(j)+ ";;"+"ODS{}".format(c+1)+";;"+sol+"\n")
                j=j+1
            except Exception:
                numero_enlaces[c]-=1
                continue
        print("Añadidos {} ".format(numero_enlaces[c])+"enlaces para la ODS {}".format(c+1))
    f.close()
    print("Añadidos un total de: {}".format(j-p))
exit()