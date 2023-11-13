import datetime
tagad = datetime.datetime.now()
stunda = tagad.hour
if 6 <= stunda < 12:
    print("Labrīt!")
elif 12 <= stunda < 18:
    print("Labdien!")
elif 18 <= stunda < 24:
    print("Labvakar")
else:
    print("Labrīt!") 