# free4talk_users_scraper
## Video Demo: <https://www.youtube.com/watch?v=ymAksmngeQU>


### scrap users data from [free4talk.com](https://www.free4talk.com/) 

### the scraped data will be stored in data.csv file

## data that will be scraped 
- User Name 
- User Id
- Number of Friends
- Number of Followers
- Number of people that the user follows

### Note: 
- #### Tthis is an interactive website, however i didn't use any third party libs like scrapy and so on , 
- #### I just used the requests package and pure python code to parse the json data retuned from the server  


## project files structure

- #### free4talk_scraper.Py file: this includes the source code for the scraper 
##### in this file I have implemented three classes first one is
- JsonRequest: for making the http request and it will return data received as in json format
- ParsedData: for parsing and extracting the targeted data ( it takes json_data as an arg which is returned by JsonRequest)
 - SaveAsCsv: this class is for saving the extracted data into a csv file it takes file as an arg so you can chose the name of the csv file that the data will be stored in  
#### test_free4talk_scraper.py file: this includes the test code for the scraper i used Pytest for testing 
- ##### test_JsonRequest: for testing the JsonRequest class 
- ##### test_ParsedData: for testing ParsedData class 
- ##### test_SaveAsCsv for testing the SaveAsCsv class 

#### data.csv an example of the generated csv file there are three functions in this file 
