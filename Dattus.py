from covid import Covid
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

covid = Covid(source="worldometers")


def indv():
    def search():
        cname = ctname.get()
        if cname == '':
            return messagebox.showerror('Error', 'Enter country name')
        else:
            data = covid.get_status_by_country_name(cname)
            sta = Toplevel()
            sta.geometry('300x300')
            sta.title('Status of ' + cname)
            Label(sta, text='Status', font='Proxima 12 bold').grid(row=1, column=2)
            Label(sta, text='Confirmed cases: ' + str(data['confirmed'])).grid(row=2, column=1)
            Label(sta, text='Active cases: ' + str(data['active'])).grid(row=3, column=1)
            Label(sta, text='Deaths: ' + str(data['deaths'])).grid(row=4, column=1)
            Label(sta, text='Recoveries: ' + str(data['recovered'])).grid(row=5, column=1)
            st.destroy()

    ctname = StringVar()
    st = Toplevel()
    st.geometry('400x100')
    st.title('Individual Status')
    Label(st, text='Specific Country Status', font='Proxima 12 bold').grid(row=1, column=2)
    Label(st, text='Enter country name:').grid(row=2, column=1)
    Entry(st, width=15, textvariable=ctname).grid(row=2, column=2)
    Button(st, text='Search', command=search).grid(row=2, column=3)


# main window
main = Tk()
style = ttk.Style(main)
style.theme_use('winnative')
p1 = PhotoImage(file='dattus.png')
main.iconphoto(False, p1)
bg = PhotoImage(file="dattusbg.png")
label1 = Label(main, image=bg)
label1.place(x=0, y=0)

main.geometry('845x543')
main.title('Dattus V1')
Label(main, text='This is Dattus. The Ultimate Country Status App for Covid-19', font='Proxima 12 bold').grid(row=1,
                                                                                                              column=1)
Label(main, text='Global Covid-19 Status', font='Proxima 12 bold').grid(row=3, column=1)
Label(main, text='COVID-19 Status in Countries', font='Proxima 12 bold').grid(row=11, column=1)
Label(main, text='Total confirmed cases: ' + str(covid.get_total_confirmed_cases())).grid(row=5, column=1)
Label(main, text='Total active cases: ' + str(covid.get_total_active_cases())).grid(row=6, column=1)
Label(main, text='Total deaths: ' + str(covid.get_total_deaths())).grid(row=7, column=1)
Label(main, text='Total recoveries: ' + str(covid.get_total_recovered())).grid(row=8, column=1)
Button(main, text='Get Specifc Country Status', command=indv).grid(row=13, column=1)
main.mainloop()
