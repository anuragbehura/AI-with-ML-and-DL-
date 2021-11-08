import datetime
import speedtest 
from Speak import Say


def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def InternetDownSpeed():
    Say("..............Checking Downloading Speed..............")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    Say(f"The downloading speed is {correctDown} mb p s")

def InternetUpSpeed():
    Say("..............Checking Uploading Speed................")
    speed = speedtest.Speedtest()
    uploading = speed.upload()
    correctUp = int(uploading/800000)
    Say(f"The uploading speed is {correctUp} mb p s")

def NonInputExecution(query): 

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

    elif "downloading speed" in query:
        InternetDownSpeed()

    elif "uploading speed"in query:
        InternetUpSpeed()

        
def InputExecution(tag,query):

    if "wikipedia" in tag:
        query = str(query).replace("who is", "")
        query = str(query).replace("about", "")
        query = str(query).replace("what is", "")
        query = str(query).replace("wikipedia", "")
        import wikipedia
        result = wikipedia.summary(query)
        Say(f"According To Wikipedia : {result}")

    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search", "")
        import pywhatkit
        import wikipedia as googleScrap
        Say("This Is What I Found On The Web")
        pywhatkit.search(query)

        try:
            result = googleScrap.summary(query,2)
            Say(result)

        except:
            Say("No Speakable Data Available!")






