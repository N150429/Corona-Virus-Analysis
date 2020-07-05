#						Realtime analysis on corona virus

# Visit pyGuru on youtube

# importing modules
import requests
import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import csv
from twilio.rest import Client
# requesting data from website
url = 'https://www.worldometers.info/coronavirus/'
r = requests.get(url)

# parsing it to beautiful soup
data = r.text
soup = BeautifulSoup(data,'html.parser')

# Printing basic data
print(soup.title.text)
print()
live_data = soup.find_all('div',id='maincounter-wrap')
for i in live_data:
	print(i.text)

print()
print('Analysis based on individual countries')
print()

# Extracting table data
table_body = soup.find('tbody')
table_rows = table_body.find_all('tr')

countries = []
total_cases = []
new_cases = []
total_deaths = []
for tr in table_rows:
	td = tr.find_all('td')    
	countries.append(td[1].text)
	total_cases.append(td[2].text)
	new_cases.append(td[3].text)
	total_deaths.append(td[4].text)

countries = countries[8:]
total_cases = total_cases[8:]
new_cases  =new_cases[8:]
total_deaths = total_deaths[8:]
#print(countries)
#print(total_cases)
#print(new_cases)
#print(total_deaths)
indices = [i for i in range(1,len(countries)+1)]
print(indices)
headers = ['Countries','Total Cases','Todays Cases','Total Deaths']
df = pd.DataFrame(list(zip(countries,total_cases,new_cases,total_deaths)),index=indices,columns=headers)

print(df)

# Saving it to csv file
df.to_csv('corona-virus-cases.csv')

#read csv file
with open('corona-virus-cases.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[1]=="India":
            text = str("Covid-19 cases in India \nCountry:"+row[1]+"\n Cases:"+row[2]+"\nActive Cases:"+row[3]+"\n Deaths:"+row[4])
            #text = {"Country":row[1],"Cases":row[2],"Deaths":row[4]}
#print(text)

account_sid = 'AC413f25369c98cf2a6bc383e23747e847' 
auth_token = '91a037578c8192c976e8458a3cc9f03c' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=text,      
                              to='whatsapp:+919553649202' 
                          )
# plotting a graph
y_pos = np.arange(len(countries[:10]))
total_cases  =total_cases[:10]
countries = countries[:10]
plt.bar(y_pos,total_cases[::-1],align='center',alpha=0.6,color="red")
plt.xticks(y_pos,countries[::-1],rotation=60)
plt.ylabel('Total cases')
plt.title('Persons affected by Corona virus')
plt.savefig('Corona-analysis.png',dpi=600)
plt.show()




