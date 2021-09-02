
#importing modules
import requests
from bs4 import BeautifulSoup
import pandas as pd


#url for getting the top restaurants of a city
city = input('Enter your city name : ')
url = 'https://www.zomato.com/'+city+'/top-restaurants'

#using a user aget to grant permission to use Zomato data
header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 RuxitSynthetic/1.0 v1221676329 t5600449317816442356 smf=0'}

#accessing the url
response = requests.get(url,headers=header)
html = response.text

#getting html content of that url
soup = BeautifulSoup(html,'html.parser')
print(soup.title.text,'\n')

# scraping raw data and storing it in a array
top_rest = soup.find_all('div',class_="bke1zw-0 cMipmx")
arr = []

#getting all restaurtant data
for tr in top_rest:
	rsts = tr.find_all('div',class_="bke1zw-1")
	for i in rsts:
		name = i.select('a',class_='sc-muxYx sc-euitrJ hIVRVA')
		for k in name:
			arr.append(k.text)
	break


#rearranging restaurant data in a single list
data = []
temp = [arr[0]]
for i in arr[1:]:
	if i.replace('.','',1).isdigit():
		data.append(temp)
		temp = [i]
	else:
		temp.append(i)


#storing different attributes in 4 lists
restaurants = []
address = []
cuisine = []
ratings = []
for lst in data:
	ratings.append(lst[0])
	restaurants.append(lst[1])
	address.append(lst[2])
	cuisine.append(','.join(lst[3:]))

#storing the scraped data in a csv file and printing it 
header = ['Restaurant','Address','Cuisine','Rating']
indices = [i for i in range(1,len(restaurants)+1)]
all_rests = zip(restaurants,address,cuisine,ratings)
df = pd.DataFrame(list(all_rests),index=indices,columns=header)
df.to_csv('Top restaurants in '+city+'.csv')
print(df)

