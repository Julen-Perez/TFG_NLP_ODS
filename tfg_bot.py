from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as soup  # HTML data structure
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import urllib.parse 
import re

class ODS_BOT():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


    def parser(self,page_url):
       

        
        uClient = urllib.request.urlopen(page_url)

        
        page_soup = soup(uClient.read(), "html.parser")
        uClient.close()
        containers = page_soup.findAll("div", {"class": "views-field views-field-field-body"})

        cleantext = soup(str(containers[0]),'html.parser').text

        return cleantext

    #https://www.corresponsables.com/actualidad/turismo?page=3&field_news_groups_tid=All&field_news_iso_tid=All&field_news_ods_tid=127&field_news_sectors_tid=All
   # https://www.corresponsables.com/actualidad/turismo?page=3&field_news_groups_tid=All&field_news_iso_tid=All&field_news_ods_tid=127&field_news_sectors_tid=All
    def obtener_enlaces(self,a):
       


        lista_ods= self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div[1]/form/div/div/div/div[4]/div/div/select')
        lista_ods.click()
        sleep(1)
        escoger_filtro_ods= self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div[1]/form/div/div/div/div[4]/div/div/select/option[{}]'.format(a+1))
        escoger_filtro_ods.click()
        sleep(2)

        aplicar= self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div[1]/form/div/div/div/div[8]/input')
        aplicar.click()
        sleep(2)
        i=15
     
        articulo=[]
        while True:
            try:        
                mostrar_mas= self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/ul/li/a')
                mostrar_mas.click()
                print(i)
                sleep(4)
                i+=15
            except Exception:
                print("Entramos Hermano")
                break

        for x in range(i):
            try:
                articulo.append(self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div[2]/div[{}]/div[2]/span/a'.format(x+1)).get_attribute("href"))
            except Exception:
                continue 
    
        
        print("salimos Hermano")
        print(articulo[len(articulo)-1])
        print(len(articulo))
        
        return articulo
bot = ODS_BOT()               
bot.driver.get('https://www.corresponsables.com/actualidad')
sleep(4)
filename="texts_prueba.csv"
j=1001;
with open(filename, "w", encoding="utf-8") as f:
    for c in range(17):
        
        enlaces=bot.obtener_enlaces(c+1)
        print("exito en obtener_enlaces!!!!!")
        textos=[]
       

        

        for enlace in enlaces:
            try: 
                sol=bot.parser(enlace).replace("\n", " ")
                f.write(str(j)+ ";;"+"ODS{}".format(c+1)+";;"+sol+"\n")
                j=j+1
            except Exception:
                continue
            
        print("exito ODS{}".format(c+1)) 
