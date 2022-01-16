from tkinter import *
#from PIL import Imagetk

root = Tk()
root.title('CruzChecks')
root.geometry("800x700")
root.resizable(False,False)

#background image##
backgroundimage=PhotoImage(file="cruzhacks01.png")
backgroundimagelabel=Label(root, image=backgroundimage)
backgroundimagelabel.place(x=0, y=0)


# frame on for options##
canvas=Canvas(width=600,height=700, bg='#e5e5e5')
img = PhotoImage(file='cruzChecklogo.png')
my_img = canvas.create_image(305,120, anchor='n', image=img)


canvas.place(x=105,y=30)


#user Entries
label0 = Label(root, text='Input or Update Your Medical Records',font="bold 20")
label0.place(x=180,y=50)

label1 = Label(root, text='Full Name', bg='#99ccff')
label1.place(x=206,y=130)
entry1=Entry(root)
entry1.place(x=206,y=160)

label2 = Label(canvas, text='SSN', bg='#99ccff')
label2.place(x=400,y=100)
entry2 = Entry(canvas)
entry2.place(x=400, y=130)

label3 = Label(canvas, text='Address', bg='#99ccff')
label3.place(x=100,y=200)
entry3 = Entry(canvas)
entry3.place(x=100, y=230)

label4 = Label(canvas, text='Date of Birth', bg='#99ccff')
label4.place(x=400,y=200)
entry4 = Entry(canvas)
entry4.place(x=400, y=230)

label5 = Label(canvas, text='Phone Number', bg='#99ccff')
label5.place(x=100,y=300)
entry5 = Entry(canvas)
entry5.place(x=100, y=330)

label6 = Label(canvas, text='Insurance Provider', bg='#99ccff')
label6.place(x=400,y=300)
entry6 = Entry(canvas)
entry6.place(x=400, y=330)

label7 = Label(canvas, text='Insurance Number', bg='#99ccff')
label7.place(x=100,y=400)
entry7 = Entry(canvas)
entry7.place(x=100, y=430)

label8 = Label(canvas, text='Medical Conditions', bg='#99ccff')
label8.place(x=400, y=400)
entry8 = Entry(canvas)
entry8.place(x=400, y=430)



def show_medical_list():
    medical_list = {'name':entry1.get(),'SSN':entry2.get(),'Address':entry3.get()
    ,'Date of Birth':entry4.get(),'Phone Number':entry5.get(),'Insurance Provider':entry6.get()
    ,'Insurance Number':entry7.get(),'Medical Conditions':entry8.get()}
    print(medical_list)


#button for submitting###
button = Button(root, text="Submit", command=show_medical_list)
button.place(x=390,y=500)




root.mainloop()