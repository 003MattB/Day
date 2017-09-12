class Day(object):

    def __init__(self,date):
        self.__date = date
        #ranges represents the days in each month
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
        #if its a leap year '02' (Feb) will be changed to 29
        self.__updateRanges()

    def addOne(self):
        #increments self by 1 day
        year = int(self.__date[0:4])
        month = int(self.__date[5:7])
        day = int(self.__date[8:10])
        day += 1
        if day > self.__ranges["{0:0>2}".format(month)]:
            month += 1
            if month > 12:
                year += 1
                month = 1
            day = 1
        #stringify and add a leading zero if month or day < 10
        if month < 10:
            month = "{0:0>2}".format(month)
        else:
            month = str(month)
        if day < 10:
            day = "{0:0>2}".format(day)
        else:
            day = str(day)

        self.__date = str(year) + '-' + month + '-' + day
        self.__updateRanges()
        return self

    def __add__(self,num):
        #intended to increment "self" by "num" days and return a new object
        assert num >= 0
        new = Day(self.getDate())
        while num > 0:
            new.addOne()
            num -= 1
        return new
            
        

    ## TODO make a subtraction method

    def __eq__(self,other):
        return self.__date == other.getDate()

    def __gt__(self,other):
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


    def __le__(self,other):
        return self < other or self == other
    
                
    def isLastDayofMonth(self):
        month = self.__date[5:7]
        day = self.__date[8:10]
        return self.__ranges[month] == day


    def __updateRanges(self):
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


if __name__ == "__main__":
    today = Day("2017-09-11")
    print(today)
