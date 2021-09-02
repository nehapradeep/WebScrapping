# WebScrapping
Finding the top Restaurants in each City from the Zomato Website.
IMPLEMENTATION
● Used headers/agent because the request was timed out and asking for an agent. For this
first we need to fake the agent.
● Then the content is retrieved after accessing the website and dumped to a variable. The
dumped content then will be passed to the BeautifulSoup function in order to get only the
data with HTML/valid website tags that were used to develop the website.
● Now we have the details of the website and we need to extract the features that we require
for our analysis. So here we need the Restaurant’s Name, Restaurant’s Address and Type
of Cuisine. In order to start looking for these details, we would need to find the HTML
tags which store this information. It is clear from the HTML Tags that the information is
stored in a div tag with classes defined as the type of fonts used or the used formats.
● We have defined a DataFrame to collect the required information. Restaurant Name is
stored underclass – res_title zblack bold nowrap, Restaurant Address is stored underclass

– nowrap grey-text fontsize5 tupper and Cuisine type is stored under class – nowrap grey-
text.

● We will access this information one by one and store them into different DataFrame
columns. We will also have to use a few String functions here because the HTML data
uses \n to separate the data and cannot be stored into the DataFrame. So, to avoid any
errors – we can replace \n with ”(space).
● This is stored in a spreadsheet with attributes in each column.
● The result is an excel file attached to this document.
