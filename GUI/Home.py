# imported all function from custom Tkinter
from customtkinter import * 
import fileOpen as file 
import NewMain as music 

# default mode settings
set_appearance_mode('system')
set_default_color_theme('blue')

# background color 
bac = 'white'
# root window
root = CTk()
root.title('Music Recommender system')
root.iconbitmap(r'D:\Projects\Major Project I v2\GUI\ICON\apple-music.ico')
root.resizable(0,0)
root.attributes('-alpha',0.9)
root.configure(fg_color = bac)
root.geometry('350x600')

# Home frame
homeFrame = CTkFrame(root,fg_color='light grey')
homeFrame.pack(fill=BOTH)

# question head frame
quesheadFrame = CTkFrame(root,fg_color=bac)
quesheadFrame.pack()

# to show question 
questionFrame = CTkFrame(root,fg_color=bac)
questionFrame.pack(pady=40)

# SubmitFrame 
submitFrame = CTkFrame(root,width=350,height=550,bg_color=bac,fg_color=bac)
# homeFrame.config(bg = bac)
# homeFrame.configure(bg_color= bac)
submitFrame.pack(fill=BOTH,expand= False)



# font family 
fontFamily = 'Work Sans'

# text color = 
textColor = 'black'

# Home window which is going to be the most essential part of teh UI
def HomeWindow() :
    # for clearing main window after click on button 
    def remove() :
        # questionHeadline.forget()
        # question.forget()
        # yesRadiob.forget()
        # noRadiob.forget()
        # submit.forget()
        quesheadFrame.forget()
        questionFrame.forget()
        submitFrame.forget()
    # events after clicking the submit button 
    def nextWindow() :
        print(ans.get())
        # getting mood from the dataset
        mood = file.getMood(ques[1],ans.get())
        print(mood)
        # clearing home window
        remove()
        homeFrame = CTkFrame(root,fg_color=bac)
        homeFrame.pack()
        # showing text suggested songs
        ansheadline = CTkLabel(homeFrame,text='Suggested Songs',font=(fontFamily,18),fg_color=bac,text_color=textColor)
        ansheadline.pack(pady=20)
        # finding music 
        song =music.__init__(mood)
        # print(song)
        # getting songs and storing it in list
        songlist = song[0]
        # decide number of songs to show
        numberOfSongs = 2*song[1]
        # another frame to show songs
        listBoxFrame = CTkFrame(root,width=300,height=600,fg_color=bac)
        listBoxFrame.pack(padx=10,pady=10,fill=None,expand= False)
        # list box to store sogns
        listbox = CTkTextbox(listBoxFrame,height=40*9,width=35*9,fg_color=bac,font=(fontFamily,15,'italic'),text_color=textColor,border_width=0)
        listbox.pack(pady=10,fill= 'both',expand=True) 
        
        
        # insert value in listbox 
        x = 1
        print(type(x))
        for i in songlist :
            if x <= numberOfSongs :
                # listbox.insert(END,("    "+i+" Link : "+songlist[i]))
                listbox.insert(END,("    "+i))
                x+=1
                listbox.insert(END,'\n')
                listbox.insert(END,'\n')
            else :
                break
            x+=1
        listbox.configure(state=DISABLED)
    # end of nextwindow
        
    
    # find QUestion 
    ques = file.getQuestion()
    
    # text at home window
    CTkLabel(homeFrame,text='Music Recommeder System',text_color='Dark red',font=('San Sarif',22,'bold')).pack(padx=10,pady=25,anchor='center')
    questionHeadline = CTkLabel(quesheadFrame,text='Feedback',font=(fontFamily,20,'bold'),fg_color=bac,text_color=textColor)
    questionHeadline.pack(padx =10,pady=10,expand = True)
    print(len(ques[0]))
    # height of textbox
    if len(ques[0]) < 80 :
        theight = len(ques[0])+len(ques[0])/4
    else :
        theight = len(ques[0])-len(ques[0])/4
    question=CTkTextbox(questionFrame,text_color=textColor,fg_color=bac,width=35*9,height=theight,font=(fontFamily,16),border_width=0)
    question.pack(padx=10,pady=10,expand = True)
    question.insert(END,ques[0])
    # question.insert(END,'\n')
    question.configure(state = DISABLED)
    
    # variable
    ans = IntVar()
    # radio button to select yes or no
    # yes button
    yesRadiob = CTkRadioButton(questionFrame,text='Yes',fg_color='dark red',font=(fontFamily,14),text_color=textColor,variable=ans,value=1)
    yesRadiob.pack(padx=15,pady=5,anchor= SW,expand=False)
    # no button
    noRadiob = CTkRadioButton(questionFrame,text='No',fg_color='dark red',font=(fontFamily,14),text_color=textColor,variable=ans,value=2)
    noRadiob.pack(padx=15,pady=5,anchor= SW,expand=False)
    
    submit = CTkButton(submitFrame,text='Submit',command=nextWindow,font=(fontFamily,14),text_color='white',fg_color='dark red',width=100,height=30)
    submit.pack(pady=20)

HomeWindow()
# finally initailize to start
root.mainloop()