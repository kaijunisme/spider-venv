from pathlib import Path
from fake_useragent import UserAgent
import requests, random, time

from utils.DateTimeUtil import DateTime
from Candlestick import Candlestick
from Volume import Volume
from ForeignInvestors import ForeignInvestors

ua = UserAgent()
headers = {"user-agent": ua.random}

baseUrl = "https://www.twse.com.tw"
nowDate = DateTime.getCurrentDate()
endMonth = DateTime.getNextMonth(nowDate)
thisMonth = DateTime.getLastMonth(endMonth)

# 建立資料夾
def createFolder(fileRoute):
    # 判斷目標資料夾是否存在，不存在則建立資料夾
    path = Path(fileRoute)
    if not path.exists():
        path.mkdir(parents = True)

def pauseSpider():
    time.sleep(random.randrange(3, 10))

# 下載檔案
def downloadFile(fileRoute, url):
    res = requests.get(url, headers = headers)

    # 判斷檔案大小，若有內容則執行下載
    if len(res.content) != 2:
        print("download: " + fileRoute)
        with open(fileRoute, "wb") as file:
            file.write(res.content)

# 開、高、低、收歷史紀錄下載
def CandlestickHistory():
    createFolder(Candlestick.FILE_ROUTE)

    # 設定起始日期
    targetMonth = DateTime.getDate(Candlestick.YEAR, Candlestick.MONTH, 1)
    while endMonth != targetMonth:
        # 設定檔案名稱及路徑
        fileRoute = Candlestick.FILE_ROUTE + "/" + targetMonth + ".csv"

        # 若檔案不存在或目標日期為當月日期，執行下載
        if (not Path(fileRoute).exists()) or (targetMonth == thisMonth):
            url = baseUrl + Candlestick.URL + targetMonth
            downloadFile(fileRoute, url)

            pauseSpider()
        
        targetMonth = DateTime.getNextMonth(targetMonth)

# 成交量歷史紀錄下載
def VolumeHistory():
    createFolder(Volume.FILE_ROUTE)

    # 設定起始日期
    targetMonth = DateTime.getDate(Volume.YEAR, Volume.MONTH, 1)
    while endMonth != targetMonth:
        # 設定檔案名稱及路徑
        fileRoute = Volume.FILE_ROUTE + "/" + targetMonth + ".csv"

        # 若檔案不存在或目標日期為當月日期，執行下載
        if (not Path(fileRoute).exists()) or (targetMonth == thisMonth):
            url = baseUrl + Volume.URL + targetMonth
            downloadFile(fileRoute, url)

            pauseSpider()
        
        targetMonth = DateTime.getNextMonth(targetMonth)

# 三大法人交易歷史紀錄下載
def ForeignInvestorsHistory():
    createFolder(ForeignInvestors.FILE_ROUTE)

    # 設定起始日期
    targetDate = DateTime.getDate(ForeignInvestors.YEAR, ForeignInvestors.MONTH, ForeignInvestors.DAY)
    tomorrow = DateTime.getNextDate(nowDate)
    while tomorrow != targetDate:
        # 設定檔案名稱及路徑
        fileRoute = ForeignInvestors.FILE_ROUTE + "/" + targetDate + ".csv"
        
        # 若檔案不存在或目標日期為當月日期，執行下載
        if not Path(fileRoute).exists():
            url = baseUrl + ForeignInvestors.URL + targetDate
            downloadFile(fileRoute, url)
            
            pauseSpider()
        
        targetDate = DateTime.getNextDate(targetDate)

CandlestickHistory()
VolumeHistory()
ForeignInvestorsHistory()