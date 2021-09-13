from tkinter import *
from tkinter import messagebox 
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

root=Tk()
root.geometry('450x300')
root.title("Digital Form")
root.configure(bg='blue')
label1=Label(root,text="Enter your email id: ",font=("ariel",11,"bold"),bg="blue",fg="white")
label1.place(x=20,y=50)
name_var=StringVar()
name=name_var.get()
entry1=Entry(root,width='30',textvariable = name_var, font=('calibre',9,'normal'),bg="white")
entry1.place(x=167,y=52)

label2=Label(root,text="Enter the password: ",font=("ariel",11,"bold"),bg="blue",fg="white")
label2.place(x=20,y=90)
name_var2=StringVar()
name2=name_var2.get()
entry2=Entry(root,width='30',show="*",textvariable = name_var2, font=('calibre',9,'normal'),bg="white")
entry2.place(x=167,y=92)

def signin():
    listener = sr.Recognizer()
    engine = pyttsx3.init()


    def talk(text):
        engine.say(text)
        engine.runAndWait()


    def get_info():
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source,timeout=7, phrase_time_limit=6)
        try:
            print("Recognizing...")
            info = listener.recognize_google(voice)
            print(info)
        except Exception as e:
            print(e)
            talk("Say that again please")
            return "None"
        return info.lower()

    def send_email(receiver, subject, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Make sure to give app access in your Google account
        server.login(entry1.get(), entry2.get())
        email = EmailMessage()
        email['From'] = '123@gmail.com'
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)


    email_list = {
        'rock': '02@yahoo.in',
        'ram': 'ram@yahoo.com'
    }

    def get_email_info():
        talk('To Whom you want to send email')
        name = get_info().lower()
        receiver = email_list[name]
        print(receiver)
        talk('What is the subject of your email?')
        subject = get_info()
        talk('Tell me the text in your email')
        message = get_info()
        send_email(receiver, subject, message)
        talk('Hey Mr.lazy. Your email is successfully sent')
        talk('Do you want to send more email?')
        send_more = get_info()
        if 'yes' in send_more:
            get_email_info()
        else:
            entry1.delete(0,END)
            entry2.delete(0,END)
            quit()
                
    get_email_info()

submit=Button(text="SIGN IN",fg='white',bg='lightgreen',font=('calibre',13,'bold'),width='10',command=signin)
submit.place(x=170,y=162)
root.mainloop()
