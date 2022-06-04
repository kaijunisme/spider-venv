from datetime import datetime, timedelta
import calendar

class DateTime:
    DATE_PATTERN_1 = "%Y%m%d"
    DATE_PATTERN_2 = "%Y/%m/%d"
    DATE_PATTERN_3 = "%Y-%m-%d"

    DATETIME_PATTERN_1 = "%Y%m%d %H:%M:%S"
    DATETIME_PATTERN_2 = "%Y/%m/%d %H:%M:%S"
    DATETIME_PATTERN_3 = "%Y-%m-%d %H:%M:%S"

    def __init__(self) -> None:
        pass

    # 取得今天日期
    def getCurrentDate(pattern = DATE_PATTERN_1):
        return datetime.now().strftime(pattern)
    
    # 取得今年民國年
    def getCurrentYear():
        return datetime.now().year - 1911

    # 根據參數取得對應日期字串
    def getDate(year, month, day, pattern = DATE_PATTERN_1):
        return datetime(year, month, day).strftime(pattern)

    # 取得後x 天日期，預設為1 天
    def getNextDate(source, pattern = DATE_PATTERN_1, num = 1):
        # string to datetime
        sourceDate = datetime.strptime(source, pattern)
        nextDate = sourceDate + timedelta(days = num)

        # datetime to string
        return nextDate.strftime(pattern)

    # 取得前x 天日期，預設為一天
    def getLastDate(source, pattern = DATE_PATTERN_1, num = 1):
        # string to datetime
        sourceDate = datetime.strptime(source, pattern)
        lastDate = sourceDate - timedelta(days = num)
        
        # datetime to string
        return lastDate.strftime(pattern)

    # 取得下個月第一天日期
    def getNextMonth(source, pattern = DATE_PATTERN_1):
        # string to datetime
        sourceDate = datetime.strptime(source, pattern)

        # 取得當月第一天是星期幾，以及當月天數
        week, endDay = calendar.monthrange(sourceDate.year, sourceDate.month)
        sourceEndDate = sourceDate.replace(day = endDay)
        nextMonth = sourceEndDate + timedelta(days = 1)
        return nextMonth.strftime(pattern)
    
    # 取得上個月第一天日期
    def getLastMonth(source, pattern = DATE_PATTERN_1):
        # string to datetime
        sourceDate = datetime.strptime(source, pattern)

        sourceStartDate = sourceDate.replace(day = 1)
        lastMonth = sourceStartDate - timedelta(days = 1)
        return lastMonth.replace(day = 1).strftime(pattern)

# currentDate = DateTime.getCurrentDate(DateTime.DATE_PATTERN_2)
# print(currentDate)

# print(DateTime.getDate(1999, 1, 1, DateTime.DATE_PATTERN_2))

# print(DateTime.getNextDate(currentDate, DateTime.DATE_PATTERN_2))
# print(DateTime.getLastDate(currentDate, DateTime.DATE_PATTERN_2))

# print(DateTime.getNextMonth(currentDate, DateTime.DATE_PATTERN_2))
# print(DateTime.getLastMonth(currentDate, DateTime.DATE_PATTERN_2))