from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, String, Text
import sqlalchemy, pymysql

from bs4 import BeautifulSoup
import requests
import pandas as pd

from utils.DateTimeUtil import DateTime
from Big import Big
from Power import Power

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/test")

# 設定請求參數
# start 為起始期數
# type 為樂通種類，1 大樂透，2 威力彩
# te 為是否包含特別好，1 包含，0 不包含
def setParam(start, type, te = 1):
    year = DateTime.getCurrentYear()

    return {
        "p1": start,
        "p2": str(year + 1) + "001",
        "te": te,
        "l": "0",
        "type": type
    }

# 取得資料格式
def getDataFormat():
    return {
        "TERM": [],
        "NUM1": [],
        "NUM2": [],
        "NUM3": [],
        "NUM4": [],
        "NUM5": [],
        "NUM6": [],
        "SPECIAL": []        
    }

# 取得資料表欄位格式
def getDataType():
    return {
        "TERM": String(6),
        "NUM1": Integer,
        "NUM2": Integer,
        "NUM3": Integer,
        "NUM4": Integer,
        "NUM5": Integer,
        "NUM6": Integer,
        "SPECIAL": Integer
    }

# 解析網頁原始碼，取得樂透期數、號碼等資訊
def getNums(content):
    data = getDataFormat()

    soup = BeautifulSoup(content, "lxml")
    trs = soup.find_all("tr", {"onmouseout" : "this.style.backgroundColor=''"})
    for tr in trs:
        term = tr.find("div", {"align" : "center"})
        nums = tr.select("td#h6")
        special = tr.select_one("td#h7")

        data["TERM"].append(term.text)
        data["NUM1"].append(nums[0].text)
        data["NUM2"].append(nums[1].text)
        data["NUM3"].append(nums[2].text)
        data["NUM4"].append(nums[3].text)
        data["NUM5"].append(nums[4].text)
        data["NUM6"].append(nums[5].text)
        data["SPECIAL"].append(special.text)
    return data

# 將資料儲存成EXCEL 格式至指定路徑
def saveCsv(fileRoute, data):
    pd.DataFrame(data).to_csv(fileRoute)

# 將資料儲存至資料表
def saveSql(tableName, data):
    dataType = getDataType()
    pd.DataFrame(data).to_sql(tableName, engine, if_exists = "replace", index = False, chunksize = 500, dtype = dataType)

def Spider(target):
    url = "http://9800.com.tw/trend.asp"
    res = requests.get(url, params = setParam(target.START_TERM, target.TYPE))

    result = getNums(res.text)
    saveCsv(target.CSV_FILE_ROUTE, result)
    saveSql(target.TABLE_NAME, result)

Spider(Big)
Spider(Power)