# importing the requests library 
import requests 
  
# defining the api-endpoint  
API_ENDPOINT = "https://dataloggerserver.tk/logdata.php"
  
# your API key here 
API_KEY = "XXXXXXXXXXXXXXXXX"

# data to be sent to api 

"""data = {'api_dev_key':API_KEY, 
        'api_option':'paste', 
        'api_paste_code':source_code, 
        'api_paste_format':'python'} 
"""

header = {"Content-type": "application/json"} 
data = {"key":"(cRos+y1lxa2" , "logdate" : "2019-01-01","humidity" : 40 ,"temparature": 20 }
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, json = data , headers=header) 
  
# extracting response text  
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url) 
