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

        print(cleantext)

    #
    def obtener_enlaces(self,a):
    	self.driver.get('https://www.corresponsables.com/actualidad')
    	sleep(4)

    	lista_ods= self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div[1]/form/div/div/div/div[4]/div/div/select')
    	lista_ods.click()
    	sleep(1)
    	escoger_filtro_ods= self.driver.find_element_by_xpath('//*[@id="edit-field-news-ods-tid"]/option[{}]'.format(a+1))
    	escoger_filtro_ods.click()
    	sleep(2)

    	aplicar= self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div[1]/form/div/div/div/div[8]/input')
    	aplicar.click()

    	sleep(2)
    	mostrar_mas= self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/ul/li')
    	mostrar_mas.click()
    	sleep(3)
    	mostrar_mas= self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/ul/li')
    	mostrar_mas.click()
    	sleep(3)
    	articulo=[]
    	for i in range(45):
    		articulo.append(self.driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div[2]/div[{}]/div[2]/span/a'.format(i+1)).get_attribute("href"))
    	print(articulo[0])

    	return articulo
    	       
    	##articulo.click()


bot = ODS_BOT()
enlaces=bot.obtener_enlaces(3)
print("exito en obtener_enlaces!!!!!") 
bot.parser(enlaces[0])
print("exito en el parser!!!!") 
