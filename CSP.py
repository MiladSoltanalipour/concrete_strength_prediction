#!/usr/bin/env python
# coding: utf-8

# # window configurations

# In[6]:


import tkinter as tk
import math as math
import datetime
import textwrap
import webbrowser

from tkinter import *
from tkcalendar import *
from tkinter import messagebox

root = tk.Tk()

root.title ('Concrete strength prediction')

def cofficienthelp():
    newwindow = tk.Toplevel(root)
    newwindow.title('Coefficients')
    newwindow.geometry( '560x150' )
    newwindow.resizable ( False,False )
    description_coefficient = """The cofficient depends on the type of cement:\n
    0.20, for cement of strength Classes CEM 42.5 R, CEM 52.5 N and CEM 52.5 R (Class R).\n
    0.25, for cement of strength Classes CEM 32.5 R, CEM 42.5 N (Class N).\n
    0.38, for cement of strength Classes CEM 32.5 N (Class S).\n"""
    label9 = tk.Label (newwindow, text = description_coefficient, justify = LEFT, anchor="e")
    label9.place(x = 10, y = 10)
    
def aboutprogram():
    newwindow = tk.Toplevel(root)
    newwindow.title('About')
    newwindow.geometry( '250x110' )
    newwindow.resizable ( False,False )
    
    label11 = tk.Label (newwindow, text = 'Created by Milad Soltanalipour', justify = LEFT)
    label11.place(x = 20, y = 20)
    
    label11 = tk.Label (newwindow, text = 'PhD Candidate @ UPC', justify = LEFT)
    label11.place(x = 20, y = 40)
    
    Googlescholar = tk.Label(newwindow, text = 'Google Scholar', fg='blue', cursor='hand2')
    Googlescholar.place(x = 20, y = 60)
    Googlescholar.bind('<Button-1>', lambda e: webbrowser.open_new('https://scholar.google.es/citations?user=fXrKLYYAAAAJ&hl=en'))

    linkedin = tk.Label(newwindow, text = 'LinkedIn', fg='blue', cursor='hand2')
    linkedin.place(x = 120, y = 60)
    linkedin.bind('<Button-1>', lambda e: webbrowser.open_new('https://www.linkedin.com/in/soltanalipour/'))
    
    linkedin = tk.Label(newwindow, text = 'ORCID', fg='blue', cursor='hand2')
    linkedin.place(x = 180, y = 60)
    linkedin.bind('<Button-1>', lambda e: webbrowser.open_new('https://orcid.org/0000-0002-4908-4546'))
    
my_menu = Menu(root)

def_font_1 = tk.font.nametofont("TkDefaultFont")
def_font_2 = tk.font.nametofont("TkTextFont")
def_font_3 = tk.font.nametofont("TkFixedFont")
def_font_1.config(size=10)
def_font_2.config(size=10)
def_font_3.config(size=10)

file_menu = Menu(my_menu)
my_menu.add_cascade( label = "File", menu = file_menu, command = aboutprogram )
file_menu.add_command( label = "About", command = aboutprogram )
file_menu.add_command( label = "Exit", command = root.quit )

root.configure ( background = '#D5D8DC', menu = my_menu)
root.geometry ( '600x290' )
root.resizable ( False,False )

color = '#EAECEE'
colorframe = '#EAECEE'
colorback = '#D5D8DC'

frame1 = Frame(root, bd = 5, bg = colorframe, height = 200, width = 180)
frame1.place( x = 20, y = 20 )

frame2 = Frame(root, bd = 5, bg = colorframe, height = 200, width = 180)
frame2.place( x = 210, y = 20 )

frame3 = Frame(root, bd = 5, bg = colorframe, height = 200, width = 180)
frame3.place( x = 400, y = 20 )

frame4 = Frame(root, bd = 5, bg = colorback, height = 50, width = 560)
frame4.place( x = 20, y = 230 )

description_about = """This program is based on Eurocode-2 Design of Concrete Structures - Part 1-1: General rules and rules for buildings, Clause 3.1.2 part (6)."""
    
label10 = tk.Label (root, text = description_about, justify = LEFT, wraplength = 540, bg = colorback)
label10.place(x = 20, y = 235)


# # labels

# In[7]:


x1 = 30
x2 = x1+130+60
x3 = x2+130+60

x10 = x1+80
x11 = x2+80
x12 = x3+70

y1 = 40
y2 = y1+40
y3 = y2+35
y4 = y3+35
y5 = y4+35

y10 = y3+35+30

lsrt_unit = 350
lsrt_command = 35
entryloc = 270

title1 = tk.Label (root, text='Input', bg = color )
title1.place(x = x1, y = y1)

label1 = tk.Label (root, text='f_cm [MPa]', bg = color )
label1.place(x = x1, y = y2)

label1 = tk.Label (root, text='Casting date', bg = color )
label1.place(x = x1, y = y3)

label3 = tk.Label (root, text='Testing date', bg = color )
label3.place(x = x1, y = y4)

title2 = tk.Label (root, text='Date for prediction', bg = color )
title2.place(x = x2, y = y1)

label4 = tk.Label (root, text='Predict date', bg = color )
label4.place(x = x2, y = y2)

title3 = tk.Label (root, text='Output', bg = color )
title3.place(x = x3, y = y1)

label5 = tk.Label (root, text='f_cm [MPa]', bg = color )
label5.place(x = x3, y = y2)

label6 = tk.Label (root, text='Coefficient', bg = color )
label6.place(x = x1, y = y5)


# # functionality

# In[8]:


def predict(f_cm_now,casting_day,testing_day,coefficient,predict_day):
    
    f_cm_now_float = float (f_cm_now)
    casting_day_format = datetime.datetime.strptime(casting_day,'%m/%d/%Y')
    testing_day_format = datetime.datetime.strptime(testing_day,'%m/%d/%Y')
    coefficient_float = float (coefficient)
    predict_day_format = datetime.datetime.strptime(predict_day,'%m/%d/%Y')
    
    days1 = testing_day_format - casting_day_format
    days = days1.days
        
    f_cm_28 = (f_cm_now_float) / ( math.exp ( coefficient_float * ( 1 - math.sqrt(28/days) ) ) )
    f_cm_28_float = float (f_cm_28)

    days_day1 = predict_day_format - casting_day_format
    days_day = days_day1.days
    
    f_cm_day = f_cm_28_float * ( math.exp ( coefficient_float * ( 1 - math.sqrt(28/days_day) ) ) )
    f_cm_day_float = float (f_cm_day)
                      
    label7['text'] = "%1.2f" % (f_cm_day)

buttonE = tk.Button (root, text= 'Check', bd=0, bg = '#00FF00', width=10, height=1, command = lambda: predict( f_cm_now.get(), casting_day.get(), testing_day.get(), coefficient.get(), predict_day.get()) )
buttonE.place(x = x12-25, y = y4+5)

label7 = tk.Label (root, bg = '#00FF00', width = 10)
label7.place(x = x12, y = y2)

buttonC = tk.Button (root, text= '?', bd=0, bg = '#00FFFF', width = 2, height = 1, command = cofficienthelp)
buttonC.place(x = x10+58, y = y5)


# # inputs

# In[9]:


f_cm_now = tk.Entry (root, width=11)
f_cm_now.place(x = x10, y = y2)

casting_day = DateEntry (root, width=9, date_pattern = 'MM/DD/YYYY')
casting_day.place(x = x10, y = y3)

testing_day = DateEntry (root, width=9, date_pattern = 'MM/DD/YYYY')
testing_day.place(x = x10, y = y4)

coefficient = tk.Entry (root, width=6)
coefficient.place(x = x10, y = y5)

predict_day = DateEntry (root, width=9, date_pattern = 'MM/DD/YYYY')
predict_day.place(x = x11, y = y2)


# # end of the program

# In[10]:


root.mainloop()

