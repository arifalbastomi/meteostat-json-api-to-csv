import requests
import csv
from csv import writer
import os
import time
from multiprocessing.pool import ThreadPool

#lattitude and longitude setting
lat="0.783609"
lon="103.770675"

key="7a180b2290msh9eab950c4de629dp14cfe2jsn7b7f4211b274"
host="meteostat.p.rapidapi.com"

start = time.time()

def monthSetting(month):
    if month == 1:
        return 31
    elif month == 2:
        return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31

def requestdData(end_date):
    splitter= end_date.split("-")
    start_date=splitter[0]+"-"+splitter[1]+"-01"
    url = "https://meteostat.p.rapidapi.com/point/hourly"

    querystring = {"lat":lat,"lon":lon,"start":start_date,"end":end_date,"alt":"113","tz":"Asia/Singapore"}

    headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': host
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(files)
    if os.path.isfile('data.csv'):
        if os.stat("data.csv").st_size == 0:
            createCsv(response,"createnew")
        else:
            createCsv(response,"addData")
    else:
        createCsv(response,"createnew")

def createCsv(response,type):
    files=response.json()
    if type=="createnew":
        c = csv.writer(open("data.csv","w"),lineterminator='\n')
        c.writerow(['time','temp','dwpt','rhum','prcp','snow','wdir','wspd','wpgt','pres','tsun','coco'])
        for item in files['data']:
            c.writerow([item['time'],item['temp'],item['dwpt'],item['rhum'],item['prcp'],item['snow'],item['wdir'],item['wspd'],item['wpgt'],item['pres'],item['tsun'],item['coco']])
    else:
        with open("data.csv", 'a') as write_obj:
            csv_writer = writer(write_obj)
            for item in files['data']:
                   csv_writer.writerow([item['time'],item['temp'],item['dwpt'],item['rhum'],item['prcp'],item['snow'],item['wdir'],item['wspd'],item['wpgt'],item['pres'],item['tsun'],item['coco']])
  

def downloadData(start,end,year):
    print("Please wait download data......")
    end_date=''
    temp_date=[]
    if start <= 12 and end <=12:
        if end > start:
            for i in range(start,end+1):
                end_date=str(year)+"-"+str(i).zfill(2)+"-"+str(monthSetting(i)).zfill(2)
                temp_date.append(end_date)
            #change threadpool with (2) thread
            results = ThreadPool(2).imap_unordered(requestdData, temp_date)
            for r in results:
                print("download data...")
        else:
            print("end month must bigger then start month")
    else:
        print("Please Input valid data (month)")

#sending data from januari (1) to june(6) year 2021
downloadData(1,6,2021)
end = time.time()
print("proccess time: ",end - start)

