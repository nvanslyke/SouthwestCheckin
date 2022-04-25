from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from tkinter import *
import sys

root = Tk()
root.title("Check in Bot")
root.geometry("600x300")


large_font = ('Verdana',20)
Button_font = ('verdana', 50)
driver = webdriver.Chrome()
driver.get('https://www.southwest.com/')
time.sleep(1)


def firstfinds():
    check = driver.find_element_by_id('TabbedArea_4-tab-4')
    check.click()

firstfinds()

def main():

    newWindow = Toplevel(root)
    newWindow.geometry("400x100")
    newWindow.title("countdown")
    countdownLabel = Label(newWindow, text="", font = large_font)
    killButton = Button(newWindow, text="KILL", command=kill)


    
    now = datetime.now()
    cur = now.hour * 60 * 60 + now.minute * 60 + now.second  
   
    hourint = int(hourBox.get())
   
    minint = int(minBox.get())
    eta = (hourint * 60 * 60) + minint * 60
    
    seconds_sleep = (eta - cur) 
    xy = seconds_sleep
    
    for i in range(0, seconds_sleep):
    
        print("Starting in " + str(xy) + " Seconds")
        countdownLabel.configure(text="Starting in " + str(xy) + " Seconds")
        countdownLabel.pack()
        killButton.pack()
        newWindow.update()

        time.sleep(1)
        xy -= 1
    
    
    confNum = driver.find_element_by_id('LandingAirReservationSearchForm_confirmationNumber_check-in')
    confNum.send_keys(confBox.get())
    print("Confirmation Number Has Been Added")
    print()
    firstN = driver.find_element_by_id('LandingAirReservationSearchForm_passengerFirstName_check-in')
    firstN.send_keys(firstBox.get())
    print("First Name Has Been Added")
    print()
    
    lastN = driver.find_element_by_id('LandingAirReservationSearchForm_passengerLastName_check-in')
    lastN.send_keys(lastBox.get())
    print("Last Name Has Been Added")
    print()

    check1 = driver.find_element_by_id('LandingAirReservationSearchForm_submit-button_check-in')
    check1.click()

    check2 = driver.find_element_by_id('form-mixin--submit-button')
    check1.click()

def kill():
    sys.exit()

def GotoName():
    
    conflab.pack_forget()
    confBox.pack_forget()
    NextButton.pack_forget()
    global firstlab
    firstlab = Label(root, text = "First Name")
    firstlab.pack()
    global firstBox
    firstBox = Entry(root,font=large_font)
    firstBox.pack()
    global  lastlab
    lastlab = Label(root, text = "Last Name")
    lastlab.pack()
    global lastBox
    lastBox = Entry(root,font=large_font)
    lastBox.pack()
    global NextButton2
    NextButton2 = Button(root,font=Button_font,text = "Next", command = GoToTime,activebackground='#00ff00')
    NextButton2.pack()


def GoToTime():
    
    firstlab.pack_forget()
    firstBox.pack_forget()
    lastlab.pack_forget()
    lastBox.pack_forget()
    NextButton2.pack_forget()

    hourlab = Label(root, text = "Hour Of Reservation")
    hourlab.pack()

    global hourBox
    hourBox = Entry(root,font=large_font)
    hourBox.pack()

    minLab = Label(root, text = "Minute of Reservation")
    minLab.pack()

    global minBox
    minBox = Entry(root,font=large_font)
    minBox.pack()

    GoButton = Button(root,font=Button_font,text = "START", command = main,activebackground='#00ff00')
    GoButton.pack()




conflab = Label(root, text ="Confirmation Number")
conflab.pack()
confBox = Entry(root,font=large_font)
confBox.pack()
NextButton = Button(root, font=Button_font, text = "Next", command = GotoName,activebackground='#00ff00')
NextButton.pack()










root.mainloop()





