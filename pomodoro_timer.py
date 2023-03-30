#cls version of pomodoro(first attempt)/ NerdCademy yt vid
#March 30th, 2023
import time
import os


#turns minutes to seconds
def convert(t):
    t = t * 60
    return t

#starts a countdown from the input 
def countdown(t, label):
    while (t):

        min, sec = divmod(t, 60)
        print(f"{label}: {min:02d} : {sec:02d}", end = "\r")
        time.sleep(1)

        t -= 1


#uses the convert function to turn the input into seconds and then starts a countdown 
def pomodoro(work, rest):
 r = convert(rest)
 w = convert(work)
 countdown(w, "Work")
 #clears the screen 
 os.system("clear || cls")
 countdown(r, "rest")
 os.system("clear || cls")


#asking for user input
work = int(input("Enter work time(min): "))
rest = int(input("Enter rest time(min): "))

#lastly, we call the function
pomodoro(work, rest)