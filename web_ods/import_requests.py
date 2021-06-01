#!C:\Users\Julen\AppData\Local\Programs\Python\Python38\python.exe
import sys
import os
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
import urllib.request
from wordcloud import WordCloud
from bs4 import BeautifulSoup as soup
from requests.auth import HTTPBasicAuth 
import json

def retrieve_input(texto):
	cleantext= texto.replace("\n","")
	url="http://localhost:8585/classes"
	filename= {"text": "{}".format(cleantext)}
	response=requests.post(url,json=filename)
	return response.text


if __name__ =="__main__":
	f=open("texto.txt","r", encoding="utf8")
	print(retrieve_input(f.read()))	
