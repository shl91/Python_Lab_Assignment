from simple_chatbot import latest_news
from simple_chatbot import temp_and_weather
from simple_chatbot import date_and_time
from simple_chatbot import greetings


asDateKeywords = ['date', 'day']
asTimeKeywords = ['time', 'clock']
asNewsKeywords = ['news', 'headlines']
asTemperatureKeywords = ['temperature','hot','cold']
asWeatherKeywords = ['weather']
asExitKeywords = ['leave','exit','thank']

def mapper(tasks):

    if any(keyword in tasks for keyword in asDateKeywords):
        date_and_time.get_current_date()
        date_and_time.get_current_day()

    elif any(keyword in tasks for keyword in asTimeKeywords):
        date_and_time.get_current_time()
    
    elif any(keyword in tasks for keyword in asNewsKeywords):
        latest_news.get_latest_news()

    elif any(keyword in tasks for keyword in asTemperatureKeywords):
        temp_and_weather.provide_temperature()

    elif any(keyword in tasks for keyword in asWeatherKeywords):
        temp_and_weather.provide_weather()
    
    elif any(keyword in tasks for keyword in asExitKeywords):
        greetings.farewellText()
        exit()

    else:
        print('Gita:I do not understand the task.')