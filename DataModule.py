
# coding: utf-8

# In[2]:



# coding: utf-8

# 我看见你了
# 走开


# In[20]:




import CoinDataDictonary
import urllib.request, json 
import time
def GETCOIN():
    with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=0") as url:
        data = json.loads(url.read().decode())
        return data
def GET_NAME_ID(count, data):
    data_part = data[count]
    Currency_name = data_part['name']
    return Currency_name
def GET_PERCENT(count, data):
    data_part = data[count]
    Currency_percent = data_part['percent_change_1h']
    return Currency_percent
def DATABASE_ID(getname):
    if CoinDataDictonary.CoinDictonary.get(getname) != None:
        Currency_database_number = CoinDataDictonary.CoinDictonary[getname]
        return Currency_database_number
def GET_DATA_ARRAY():
    Main_data=GETCOIN()
    Percent_array = [0.0]*1495
    Percent_array[0]='0.'+str(int(time.time()))
    for i in range(0,len(Main_data)):
        Name = GET_NAME_ID(i, Main_data)
        Percent = GET_PERCENT(i, Main_data)
        Database_id = DATABASE_ID(Name)
        if Database_id != None:
            if Percent == None:
                Percent_array[int(Database_id)] = 0.0
            else:
                Percent_array[int(Database_id)] = Percent
    return Percent_array
