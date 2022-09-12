import my_ARYA as a
talk= a.sptotext()
i=0
if "hello arya"in talk.lower():
    a.texttosp("Hello")
 
    while(i==0):
        t= a.sptotext()
        t1=t.lower()
        if "play" in t1:
            a.texttosp("OK")
            a.video(t1)
        if "exit" in t1:
            a.texttosp("OK")
            i=1
        if "google" in t1:
            a.texttosp("OK")
            a.google(t1)
            i=1
        if "time" in t1:
            a.texttosp("OK")
            a.time_tell()
        if "search" in t1:
            x,y= t1.split("search")
            a.wiki(y)
        if "joke" in t1:
            a.texttosp("OK")
            a.joke()
            