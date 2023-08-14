import datetime

def get_current_date():
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        print("Today's date is " + current_date)

def get_current_day():
    current_day = datetime.date.today().strftime("%A")
    print("The day is " + current_day)

def get_current_time():
    CurrentTime = datetime.datetime.now().time().strftime('%H:%M:%S')
    print("The time is" + CurrentTime)
    


    
