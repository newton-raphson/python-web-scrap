#simple code to scrap web
import requests
from bs4 import BeautifulSoup
import shutil
import pandas as pd
import numpy as np
import os
#file to read websites from
df = pd.read_excel(r'Electrical Engineering.xlsx',sheet_name='E')

for i in range (29):
    (x,y)=df.iloc[i]
    BASE=y
    filename=x+'.txt'
    folder_image='Electrical/'+x+'/'
    os.mkdir('Electrical/'+x)
    f=open('readme.txt', 'w') 
    val=0
    for j in range(1,10,1):
        string= str(j)
        URL = BASE+string
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="idAgentType")
       
        #print(soup.prettify())
        job_elements = soup.find_all("div", class_="bix-div-container")
        for job_element in job_elements:
            question = job_element.find("td", class_="bix-td-qtxt")
            optiontbl= job_element.find("table", class_="bix-tbl-options")
            answer = job_element.find("span", class_="jq-hdnakqb mx-bold")
            img_tags=job_element.find_all('img')
            for img in img_tags:
                n=str(val)
                img_url = img['src']
                r = requests.get('https://www.indiabix.com'+img_url)
                fname=folder_image+str(val)+".gif" 
                with open(fname, 'wb') as x:
                    x.write(r.content)
                val+=1
            #writer.writerow(question.text.strip())
            print(question.text.strip())
            f.write(question.text.strip())
            f.write('\n')
            print(optiontbl.text.strip())
            f.write(optiontbl.text.strip())
            f.write('\n')
            f.write('\n')
            f.write(answer.text.strip())
            f.write('\n')
            f.write('\n')
    shutil.move('readme.txt','Electrical/'+filename)