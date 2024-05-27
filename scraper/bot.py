
import mechanize
from bs4 import BeautifulSoup
import pandas as pd
import re 
import datetime
import os
from scraper.parsing import MyBeautifulSoup
from scraper.file import FileCreation





class Stocks():

    def __init__(self,base_url,login,password,base_url1):

       
        self.BASE_URL = base_url
        self.LOGIN = login
        self.PASSWORD = password
        self.BASE_URL1 = base_url1
        
    

    def scrape_website(self):
         
        br = mechanize.Browser()

        try:
            br.open(self.BASE_URL) 
         
          
            
            for form in br.forms():
                if form.attrs.get("class") == "card card-small margin-0":
                    br.form = form
                  
                    br["username"] = self.LOGIN
                 
                    br["password"] = self.PASSWORD
                
                    response = br.submit()
          
            
                    if response.geturl() != self.BASE_URL:
                
                        #print("Login successful!")
                        br.open(self.BASE_URL1)
                        # print("Navigated to:", url1)            
 
                        #br.follow_link(url_regex=r'\?limit=50&page=1')
                        html = br.response().read()
                        return html
        finally:
            br.close

    
    def apply_parsing(self):

        parsing = MyBeautifulSoup(self.scrape_website())
        self.column = parsing.parse_columns()
        self.data = parsing.parse_data()
       

    def file(self):

        file = FileCreation()
        file.stock_file_creation(self.data,self.column)
        file.save_to_csv(file.df,file.name)

    def daily_file(self,file_path):

        file = FileCreation()
        dataframe = file.daily_file_creation(file_path=file_path)
        print('first time data saved') if dataframe.size == 0 else file.save_to_csv(dataframe,file.file_name)
            
      
            
            

    


   







