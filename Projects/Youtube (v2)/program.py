from tkinter import *
from PIL import ImageTk, Image
from tkinter import PhotoImage

window = Tk()
window.geometry("820x620")
window.title("First program")

icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
window.config(background="lightgrey")

title_frame = Frame(window)
title_frame.pack(side="top", fill="x")
menu = Button(title_frame, text="menu").grid(row=0, column=0, padx=10)

title = Label(title_frame, text="Youtube", font=('Ariel', 15, 'bold'))
title.grid(row=0, column=1,padx=20, pady=5)

search_bar = Text(title_frame, width=50, height=1)
search_bar.grid(row=0, column=2, padx=10, pady=10)
search_icon = Button(title_frame, text="🔍",height=1).grid(row=0, column=3)

user_icon = Button(title_frame, text="T",height=1).grid(row=0, column=4, padx=25)

side_frame= Frame(window)
side_frame.pack(side="left", fill="y", pady=20)
option1 = Button(side_frame, text="🏚").grid(row=0, column=0, pady=10)
option1_label = Label(side_frame, text="Home", font=('Ariel', 10, 'bold'))
option1_label.grid(row=1, column=0, pady=5)

option2 = Button(side_frame, text="⚡").grid(row=3, column=0, pady=10 )
option2_label = Label(side_frame, text="Shorts", font=('Ariel', 10, 'bold'))
option2_label.grid(row=4, column=0, pady=5)

option3 = Button(side_frame, text="👍").grid(row=5, column=0, pady=10)
option3_label = Label(side_frame, text="Subscribe", font=('Ariel', 10, 'bold'))
option3_label.grid(row=6, column=0, pady=5)

option4 = Button(side_frame, text="👤").grid(row=7, column=0, pady=10)
option4_label = Label(side_frame, text="You", font=('Ariel', 10, 'bold'))
option4_label.grid(row=8, column=0, pady=5)

option5 = Button(side_frame, text="⇲").grid(row=9, column=0, pady=10)
option5_label = Label(side_frame, text="Download",font=('Ariel', 10, 'bold'))
option5_label.grid(row=10, column=0, pady=5)

Video_frame = Frame(window, bg="lightgrey")
Video_frame.pack(side="top", pady=20, fill="both", padx=25)

Video1 = Text(Video_frame, width=30, height=5).grid(row=0, column=0, sticky="w")
Video1_label = Label(Video_frame, text="This is a video", font=('Ariel', 5,'bold')).grid(row=1, column=0, pady=5)

Video2 = Text(Video_frame, width=30, height=5).grid(row=0, column=1, sticky="w", padx=10)
Video2_label = Label(Video_frame, text="This is a video", font=('Ariel', 5,'bold')).grid(row=1, column=1, pady=5)

Video3 = Text(Video_frame, width=30, height=5).grid(row=0, column=2, sticky="w", padx=5)
Video3_label = Label(Video_frame, text="This is a video", font=('Ariel', 5,'bold')).grid(row=1, column=2, pady=5)

Video4 = Text(Video_frame, width=30, height=5).grid(row=2, column=0, sticky="w")
Video4_label = Label(Video_frame, text="This is a video", font=('Ariel', 5,'bold')).grid(row=3, column=0, pady=5)

Video5 = Text(Video_frame, width=30, height=5).grid(row=2, column=1, sticky="w", padx=10,)
Video5_label = Label(Video_frame, text="This is a video", font=('Ariel', 5,'bold')).grid(row=3, column=1, pady=5)

Video6 = Text(Video_frame, width=30, height=5).grid(row=4, column=2, sticky="w", padx=10, pady=5)
Video6_label = Label(Video_frame, text="This is a video", font=('Ariel', 5,'bold')).grid(row=5, column=2)

video7 = Text(Video_frame, width=30, height=5).grid(row=4, column=0, sticky="w")
Video7_label = Label(Video_frame, text="This is a video", font=('Ariel', 5,'bold')).grid(row=5, column=0, pady=5)

Video8 = Text(Video_frame, width=30, height=5).grid(row=4, column=1, sticky="w", padx=10,)
Video8_label = Label(Video_frame, text="This is a video", font=('Ariel', 5,'bold')).grid(row=5, column=1, pady=5)

video9 = Text(Video_frame, width=30, height=5).grid(row=4, column=2, sticky="w", padx=10, pady=5)
Video9_label = Label(Video_frame, text="This is a video", font=('Ariel', 5,'bold')).grid(row=5, column=2)

AD_label = Label(Video_frame, text="This is a AD", font=('Ariel', 10,'bold'), width=40, height=10).grid(row=6, columnspan=3, sticky="w")




window.mainloop()