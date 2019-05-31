import datetime
from time import gmtime, strftime


class DatetimeBase():
    def __init__(self):
        date = datetime.datetime.now().strftime('%d')
        month = datetime.datetime.now().strftime('%m')
        monthfull = datetime.datetime.now().strftime('%B')
        yearsmall = datetime.datetime.now().strftime('%y')
        year = datetime.datetime.now().strftime('%Y')
        week = datetime.datetime.now().strftime('%W')
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        weekday =days[datetime.date.today().weekday()]
        weekdaynum = datetime.date.weekday(datetime.datetime.now())

        hour = datetime.datetime.now().strftime('%d')
        min = datetime.datetime.now().strftime('%d')
        sec = datetime.datetime.now().strftime('%d')
        ampm = datetime.datetime.now().strftime('%p')
        pass

    def get_current_date(self,format="default"):
        '''
            @returns : Get Current Date formatted

            @param:
                    # format = default : 2019-05-31 | YYYY-MM-DD
                    # format = 1 : 2019/05/31 | YYYY/MM/DD
                    # format = 2 : 2019_05_31 | YYYY_MM_DD
                    # format = 3 : 20190531 | YYYYMMDD
                    # format = 4 : 190531 | YYMMDD
                    # format = 5 : 31-05-19 | DD-MM-YY
                    # format = 6 : 31/05/19 | DD/MM/YY
                    # format = 7 : 31-05 | DD-MM
                    # format = 8 : 31/05 | DD/MM
                    # format = 9 : May 31,2019
                    # format = 10 : Fri,May 31,2019
                    # format = 11 : Friday,May 31,2019

        '''
        if format == "default":
            try:
                return datetime.date.today().__str__()
            except:
                try:
                    return strftime("%Y-%m-%d", gmtime())
                except:
                    try:
                        return datetime.datetime.now().strftime('%Y-%m-%d')
        elif format == 1:
            return datetime.datetime.now().strftime('%Y/%m/%d')
        elif format == 2:
            return datetime.datetime.now().strftime('%Y_%m_%d')
        elif format == 3:
            return datetime.datetime.now().strftime('%Y%m%d')
        elif format == 4:
            return datetime.datetime.now().strftime('%y%m%d')
        elif format == 5:
            return datetime.datetime.now().strftime('%d-%m-%y')
        elif format == 6:
            return datetime.datetime.now().strftime('%d/%m/%y')
        elif format == 7:
            return datetime.datetime.now().strftime('%d-%m')
        elif format == 8:
            return datetime.datetime.now().strftime('%d/%m')
        elif format == 9:
            return datetime.datetime.now().strftime('%B %d,%Y')
        elif format == 10:
            return datetime.datetime.now().strftime('%a,%B %d,%Y')
        elif format == 11:
            return datetime.datetime.now().strftime('%A,%B %d,%Y')
        else:
            raise ValueError("Mode Number doesn't exist")

    def get_current_time(self,mode=1):
        '''
            @returns : Current Time
        '''
        if mode == 1:
            return strftime("%H:%M:%S", gmtime())
        elif mode ==2:
            return datetime.datetime.now().strftime('%H:%M:%S')

    def get_current_datetime(self):
        '''
            @returns : Current Date & Time
        '''
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


 