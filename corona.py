from tkinter import *
import datetime
from datetime import datetime
from covid import Covid
from tkinter import messagebox
covid = Covid()


# necessary details
root = Tk()
root.title("Covid Tracker")
root.geometry("375x350")
root['background'] = "white"


# country search
country_name = StringVar()
country_entry = Entry(root, textvariable=country_name, width=45)
country_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S)


def country_name():
    # get the data by country name
    try:
        data = covid.get_status_by_country_name(country_entry.get())

        # Extracting Data
        country = data['country']
        confirmed = data['confirmed']
        active = data['active']
        deaths = data['deaths']
        recovered = data['recovered']
        date = data['last_update']
        last_update = datetime.fromtimestamp(date/1000)

        # Adding the received info into the screen
        lable_country.configure(text=country)
        lable_confirmed.configure(text=confirmed)
        lable_active.configure(text=active)
        lable_deaths.configure(text=deaths)
        lable_recovered.configure(text=recovered)
        lable_updatetime.configure(text=last_update)

        # if there is an error in the country name show Error Message
    except ValueError:
        messagebox.showerror("Error", "Country Not Found \n"
                             "Please enter valid Country name")
        country_entry.delete(0, END)


# Clear all button to clear all fields
def clear_all():
    country_entry.delete(0, END)
    lable_country.configure(text="...")
    lable_confirmed.configure(text='...')
    lable_active.configure(text='...')
    lable_deaths.configure(text='...')
    lable_recovered.configure(text='...')
    lable_updatetime.configure(text='...')
    country_entry.focus_set()


# Search Bar and Button
city_nameButton = Button(root, text="Search", command=country_name)
city_nameButton.grid(row=1, column=1, padx=5, stick=W+E+N+S)


# Country Name
countryHolder = Label(root, text="Country : ", width=0,
                      bg='white', font=('bold'))
countryHolder.place(x=65, y=65)


lable_country = Label(root, text="...", width=0,
                      bg='white', font=("bold", 15))
lable_country.place(x=135, y=63)


# Confirmed Cases
confirmHolder = Label(root, text="Confirmed : ", width=0,
                      bg='white', font=('bold'))
confirmHolder.place(x=65, y=89)
lable_confirmed = Label(root, text="...", width=0,
                        bg='white', font=("bold", 15))
lable_confirmed.place(x=155, y=87)


# Active Cases
activeHolder = Label(root, text="Active : ", width=0,
                     bg='white', font=('bold'))
activeHolder.place(x=65, y=113)
lable_active = Label(root, text="...", width=0,
                     bg='white', font=("bold", 15))
lable_active.place(x=135, y=111)


# Deaths
deathHolder = Label(root, text="Deaths : ", width=0,
                    bg='white', font=('bold'))
deathHolder.place(x=65, y=137)
lable_deaths = Label(root, text="...", width=0,
                     bg='white', font=("bold", 15))
lable_deaths.place(x=135, y=135)


# Recoverd
recoveredHolder = Label(root, text="Recovered : ", width=0,
                        bg='white', font=('bold'))
recoveredHolder.place(x=65, y=161)
lable_recovered = Label(root, text="...", width=0,
                        bg='white', font=("bold", 15))
lable_recovered.place(x=155, y=159)

# Last updated
dateHolder = Label(root, text="Last Updated : ", width=0,
                   bg='white', font=('bold'))
dateHolder.place(x=65, y=185)
lable_updatetime = Label(root, text="...", width=0,
                         bg='white', font=("bold", 15))
lable_updatetime.place(x=175, y=183)

# Clear Button
clearButton = Button(root, text="Clear", bg="red",
                     fg="black", command=clear_all, height=2, width=6)
clearButton.place(x=170, y=222)
root.mainloop()
