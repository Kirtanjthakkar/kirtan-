from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

converter = Tk()
converter.title("Currency Converter")
converter.geometry("800x500")
#converter.configure(bg='black')

image=Image.open("C:\\Users\\DELL\\Documents\\2nd Year\\Python Programming(2 year)\\pythonProject2\\Currency_Converter.png")
resize_image=image.resize((800,500))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img
label1.grid()


OPTIONS = {
    "Australian Dollar":49.10,
    "Brazilian Real":17.30,
    "British Pound":90.92,
    "Chinese Yuan":10.29,
    "Euro":87.85,
    "HongKong Dollar":8.83,
    "Indonesian Rupiah":0.004864,
    "Japanese Yen":0.628,
    "Pakistani Rupee":0.49,
    "SriLankan Rupee":0.39,
    "Swiss Franc":69.62,
    "Us Dollar":75.04
        }

def ok():
    try:
        price = rupees.get()
        answer = variable1.get()
        DICT = OPTIONS.get(answer,None)
        converted = float(DICT)*float(price)
        result.delete(1.0,END)
        result.insert(INSERT,"Value of ",INSERT,answer,INSERT," in INR",INSERT," : ",INSERT,converted)
    except:
        messagebox.showerror("Empty Fields","Please select an option!")


frame1 = Frame(converter, relief= RIDGE,bd=10, bg = "#b8d8be")    
frame1.grid(row=0, column=0,padx=5,pady=5)
appName = Label(frame1,text="INDIAN CURRENCY CONVERTER",font=("Cambria",25,"bold","underline"),fg="dark red",bg='#b8d8be')
appName.grid(row=0, column=0, columnspan= 3,padx=5,pady=5)


india = Label(frame1,text="ENTER YOUR AMOUNT:",font=("Cambria",12,"bold"),fg="#01303f",bg='#b8d8be')
india.grid(row=2, column=0,padx=5,pady=10)

rupees = Entry(frame1,font=("Cambria",15),fg='black',bg='white')
rupees.grid(row=2, column=1,padx=10,pady=10)

choice = Label(frame1,text="CONVERT YOUR CURRENCY TO INR:",font=("Cambria",12,"bold"),fg="#01303f",bg='#b8d8be')
choice.grid(row=3, column=0,padx=5,pady=5)

variable1 = StringVar(converter)
variable1.set("Please Select a Currency")
option = OptionMenu(frame1,variable1,*OPTIONS)
option.grid(row=3, column=1,padx=10,pady=5)

button = Button(frame1,text="CONVERT",fg="white",font=("Cambria",16),bg="#0f403f",command=ok)
button.grid(row=4, column=0,padx=5,pady=5, columnspan= 2)

result = Text(frame1)
result.configure(height=2,width=35,font=("Cambria",15,"bold"),bd=5)
result.grid(row=5, column=0,padx=5,pady=5, columnspan= 2)



converter.mainloop()