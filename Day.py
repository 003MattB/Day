class Day(object):

    def __init__(self,date):
        self.__date = date
        self.__ranges = {'01' : 31,
                         '02' : 28,
                         '03' : 31,
                         '04' : 30,
                         '05' : 31,
                         '06' : 30,
                         '07' : 31,
                         '08' : 31,
                         '09' : 30,
                         '10' : 31,
                         '11' : 30,
                         '12' : 31}
        self.updateRanges()

    def __add__(self,num):
        ## TODO finish this
        year = int(self.__date[0:4])
        month = int(self.__date[5:7])
        day = int(self.__date[8:10])
        y2add = 0
        m2add = 0
        d2add = 0
        if self.isLeapYear():
            y2add = num // 366
            num %= 366
        else:
            y2add = num // 365
            num %= 365
        
        m2add = num // self.__ranges[self.__date[5:7]] 
        num %= self.__ranges[self.__date[5:7]]
        d2add = num

        year += y2add
        month += m2add
        day += d2add
        if day > self.__ranges[self.__date[5:7]]:
            month += 1
            day = day - self.__ranges[self.__date[5:7]]
        if month > 12:
            year += 1
            month = 1
        if month < 10:
            month = '0'+str(month)
        else:
            month = str(month)
        if day < 10:
            day = '0'+str(day)
        else:
            day = str(day)
        self.__date = str(year) + '-' + month + '-' + day
        self.updateRanges()
        return self

    ## TODO make a subtraction method


    def __eq__(self,other):
        return self.__date == other.getDate()

    def __lt__(self,other):
        if int(self.__date[0:4]) > int(other.getDate()[0:4]):
            return True
        elif int(self.__date[5:7]) > int(other.getDate()[5:7]):
            return True
        elif int(self.__date[8:10]) > int(other.getDate()[8:10]):
            return True
        
        return False

    def __lt__(self,other):
        if int(self.__date[0:4]) < int(other.getDate()[0:4]):
            return True
        elif int(self.__date[5:7]) < int(other.getDate()[5:7]):
            return True
        elif int(self.__date[8:10]) < int(other.getDate()[8:10]):
            return True
        
        return False


    def __lteq__(self,other):
        return self < other or self == other
    
                
    def isLastDayofMonth(self):
        month = self.__date[5:7]
        day = self.__date[8:10]
        return self.__ranges[month] == day


    def updateRanges(self):
        year = int(self.__date[0:4])
        #its a leap year
        if self.isLeapYear():
            self.__ranges['02'] = 29
        return


    def isLeapYear(self):
        year = int(self.__date[0:4])
        return year % 4 == 0


    def getDate(self):
        return self.__date


    def __str__(self):
        return self.__date + ' isLeapYear: ' + str(self.isLeapYear())
