from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog

window = Tk()

#photo = PhotoImage(file='images.png')
#label= Label(window, text="HEllo World", 
#             font=('Ariel', 40, 'bold'),
#             fg='blue', 
 #            bg='black', 
  #           relief=RAISED, 
   #          bd=10,
    #         padx=10, pady=10,
     #        image=photo, 
      #       compound='bottom')
#label.pack()

#count = 0


#def click():
#    global count
#    count+=1
#    print(count)
#    print("You click this button")

#photo=PhotoImage(file='icon.png')

#button = Button (window, 
 #                text="Clik here",
  #              command=click,
   #             font=("Comic Sans",30),
    #            fg="blue",
     #           bg="black",
      #          activeforeground="blue",
       #         activebackground="black",
        #        state=ACTIVE,
         #       image=photo,
          #      compound=BOTTOM,
           #     )
#button.pack()

#Entry widget = Textbox that accepts a single line of user input

#def submit():
 #   username = entry.get()
  #  print('Hello' + username)
   # entry.config(state=DISABLED)
#def delete():
 #   entry.delete(0,END)

#def backspace():
 #   entry.delete(len(entry.get())-1, END)


#entry = Entry(window,
 #             font=('Ariel',50),
  #            fg='blue',
   #           bg='Black'

              #)
#entry.pack(side=RIGHT)
#entry.insert(0, "Quandale Dingle")


#submitbtn = Button(window,
 #                  text="submit",
  #                 command=submit)
#submitbtn.pack(side=LEFT)

#deletebtn = Button(window,
 #                  text="delete",
  #                 command=delete)
#deletebtn.pack(side=LEFT)

#backspacebtn = Button(window,
 #                  text="backspace",
  #                 command=backspace)
#backspacebtn.pack(side=LEFT)

#CHECKBUTTON
#def display():
 #   if(x.get()==1):
  #      print("You agree")
   # else:
    #    print("You dont agree")

#photo=PhotoImage(file='icon.png')
#x = BooleanVar()


#check_button = Checkbutton(window,
 #                          text="I agree to something",
  #                         variable=x,
   #                        onvalue="YES",
    #                       offvalue="NO",
     #                      command=display,
      #                     font=('Ariel',30),
       #                    fg='blue',
        ##                  activeforeground='blue',
          #                 padx=25,
           #                pady=10,
            #               image=photo,
             #              compound=LEFT,)
#check_button.pack()



#RADIOBUTTONS

#feelings =["alright", "no comment","sad"]

#def opinion():
 #   if(x.get()==0):
  #      print("GOOD ENJOY")
   # elif (x.get()==1):
    #    print("IT COULD BE WORSE")
    #else:
     #   print("SORRY TO HEAR THAT")    


#x = IntVar()


#alrightImage = PhotoImage(file='download.png')
#noComentImage = PhotoImage(file='no comment.png')
#sadImage = PhotoImage(file='sad2.png')

#feelingImages = [alrightImage,noComentImage,sadImage]


#for index in range(len(feelings)):
 #   radiobutton = Radiobutton(window,
  #                            text=feelings[index], #adds text to radio button
   #                           variable=x, #groups radio buttons together if they share the same index/value
    #                          value=index,
     #                         padx=25,
      #                        font=('Impact',50),
       #                       image=feelingImages[index],
        #                      compound=LEFT,
         #                     command=opinion)#assigns each radio button a different button
    
    #radiobutton.pack(anchor=W)
#SCALE
#def submit():
 #   print("The temperature is:" + str(scale.get())+ "degrees C")

#hotImage=PhotoImage(file='hot.png')
#hotlabel = Label(image=hotImage)
#hotlabel.pack()

#scale = Scale(window,
 #             from_=100, to=0,
  #            length=600,
   #           orient=HORIZONTAL,# thiss is orientation of scale
    #          font=('Consolas',20),
     #         tickinterval=10, #adds numberic indicators for 
              
              
  #            )
#scale.set(50)
#scale.pack()

#hotImage=PhotoImage(file='')
#hotlabel = Label(image=hotImage)
#hotlabel.pack()


#button = Button(window,
#                text="Sumbit",
#                command=submit)
#button.pack()

#LISTBOX
#def submit():
 #   food = []

  #  for index in listbox.curselection():
   #     food.insert(index, listbox.get(index))

    #print("You have orderd: ")

  #  for index in food:
   #     print(index)
   # print(listbox.get(listbox.curselection()))
    
#def add():
 #   listbox.insert(listbox.size(), entry_box.get())
  #  listbox.config(height=listbox.size())

#def delete():
 #      listbox.delete(index)

  #  listbox.config(height=listbox.size())


#listbox = Listbox(window,
 #                 bg='lightgrey',
  #                font=("Constantia",35),
   #               width=15,
    #              selectmode=MULTIPLE,

      #         )
#listbox.pack()

#listbox.insert(1,"pizza")
#listbox.insert(2,"soup")
#listbox.insert(3,"salad")
#listbox.insert(4,"garlic bread")
#listbox.insert(5,"pasta")
#listbox.insert(6,"bread")

#listbox.config(height=listbox.size())

#entry_box = Entry(window,)
#entry_box.pack()




#sumbit_button = Button(window,
 #                      text="submit",
  #                     command=submit,
   #                    )
#sumbit_button.pack()

#add_button = Button(window,
 #                   text="Add",                  command=add)
#add_button.pack()

#delete_button = Button(window,
 #                   text="Delete",
  #                  command=delete)
#delete_button.pack()

#def click():
    #messagebox.showinfo(title="THis is a messagebox",
    #                    message="THis is a practise run",)
    #messagebox.showwarning(title="WARNING",
    #                       message="YOU HAVE A VIRUS")
    #messagebox.showerror(title="THERE iS A ERROR",
    #                     message="SOMETHING IS NOT RIGHT")
    #messagebox.askokcancel(title="OK CNACEL", message="DO YOU WNAT TO CONTINUE")
    #messagebox.askretrycancel(title="DO YOU WANT TO RETRY", message="YOU RETRY ")
    #messagebox.askyesno(title="DO YOU WANT TO CONTINUE", message="ARE YOU SURE")
    #messagebox.askquestion(title="DO YOU WNAT TO CONTINUE", message="DO YOU LIKE PI")
    #messagebox.askyesnocancel(title="DO YOU WANT TO ", message="DO YOU LIKE YO CODE")

#button = Button(window,
 #                text="CLICK ME",
  #               command=click,)
#button.pack()
#COLOR CHOOSER
window.geometry("420x420")
 
#def click():
 #   color= colorchooser.askcolor()
  #  color_hex= color[1]
   # window.config(bg=color_hex)


#button = Button(text="Click me", command=click)
#button.pack()

#TEXT WIDGET?AREA

#def submit():
 #   input = text.get("1.0",END)
  #  print(input)

#text = Text(window, 
 #           bg="yellow",
  #          font=("Ink Free",25),
   #         height=8,
    #        width=20,
     #       padx=20,
      #      pady=20,
       #     fg="purple")
#text.pack()

#button  = Button(window, 
 #                text="SUMBIT",
  #                 command=submit)
#button.pack()

#FILE--DIALOG--HOW TO OPEN AND READ FILES

#def open_file():
 #   filepath=filedialog.askopenfilename()
  #  file = open(filepath,'r')
   # print(file.read())
    #file.close()

#button = Button(
 #               text="OPEN FILE", 
  #              command=open_file)
#button.pack()


#



















window.mainloop()