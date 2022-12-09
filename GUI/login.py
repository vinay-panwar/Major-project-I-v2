# Importing the module
from customtkinter import * 

# defualt setting
set_appearance_mode('system')
set_default_color_theme('blue')

# defining root window
root = CTk()
root.configure(fg_color = 'white',anchor = 'center')
root.geometry("350x600")
root.attributes('-alpha',0.9)
root.title('Music Recommender system')
root.iconbitmap(r'D:\Projects\Major Project I v2\GUI\ICON\apple-music.ico')
root.resizable(0,0)

def login() :
    user = userName.get()
    passw = password.get()
    print(user+"\n"+passw)
    print('test')


# homeFrame
homeFrame = CTkFrame(root,fg_color='light grey')
homeFrame.pack(fill = BOTH)

# login window 
MainFrame = CTkFrame(root,fg_color='white')
MainFrame.pack(padx=20,pady=20,anchor='center')

# Music recommendersystem 
CTkLabel(homeFrame,text='Music Recommeder System',text_color='Dark red',font=('San Sarif',22,'bold')).pack(padx=10,pady=25,anchor='center')
# Text on the root window
MainText = CTkLabel(MainFrame, text='Login',font=('Sans Sarif',24),anchor='center');
MainText.pack(padx=50,pady=12)

# Enter usernamae
userName = CTkEntry(MainFrame,placeholder_text='user-name')
userName.pack(padx=10,pady=20)
# Enter password
password = CTkEntry(MainFrame,placeholder_text='password',show='*')
password.pack(padx=10,pady=20)

clickB = CTkButton(MainFrame,text='Click',fg_color='dark red',command=login)
clickB.pack(padx=10,pady=10,anchor= 'center')

checkbox = CTkCheckBox(MainFrame,text='Remember me',fg_color='dark red')
checkbox.pack(padx=10,pady=10)

root.mainloop()