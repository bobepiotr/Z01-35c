import tkinter as tk
from tkinter import Label, Entry, Button, PhotoImage, Frame
import datetime
from datetime import date
import weather_data as wd
import hourly_window as hw

class Interface:
    root = tk.Tk()
    city_name: Entry

    def __init__(self):
        self.create_interface()
        self.act_city_name = "Warsaw"

    def get_act_city_name(self):
        if self.city_name.get() != "":
            return self.city_name
        else:
            return "Warsaw"

    def create_interface(self):
        week_days = ["Mon", "Tue", "Wen", "Thu", 'Fri', "Sat", "Sun"]
        title_frame = Frame(self.root)
        title_frame.grid(row=0, column=0, columnspan=3)

        prompt_label = Label(title_frame, text='Enter city name: ', font=('Arial', 12), padx=30)
        prompt_label.grid(row=0, column=0)

        self.city_name = Entry(title_frame, font=('Arial', 12), width=35)
        self.city_name.grid(row=0, column=1)

        button = Button(title_frame, text='Search', font=('Arial', 12),
                        command=lambda: self.display_weather_conditions_for_n_days(3))
        button.grid(row=0, column=2)

        today_button = Button(self.root, text='Today', font=('Arial', 12), width=25,
                              command=lambda: self.create_bar_plot(self.get_act_city_name(), date.today(), 'horizontal'))
        today_button.grid(row=1, column=0)

        tomorrow = date.today() + datetime.timedelta(days=1)
        tomorrow_button = Button(self.root, text=str(tomorrow) + " " + week_days[tomorrow.weekday()],
                              font=('Arial', 12), width=25, command=lambda:
                                    self.create_bar_plot(self.get_act_city_name(), tomorrow, 'horizontal'))
        tomorrow_button.grid(row=1, column=1)

        third_day = date.today() + datetime.timedelta(days=2)
        tomorrow_button = Button(self.root, text=str(third_day) + " " + week_days[third_day.weekday()],
                                 font=('Arial', 12), width=25, command=lambda: self.create_bar_plot(self.get_act_city_name(), third_day, 'horizontal'))
        tomorrow_button.grid(row=1, column=2)

        tk.mainloop()

    def get_weather_conditions_for_n_days(self, how_many_days):
        location_name = self.city_name.get()
        location_coordinates = (52.2319581, 21.0067249) #Warsaw is default city

        if location_name != "":
            location_coordinates = wd.get_city_coordinates(location_name)

        json_weather_data = wd.get_json_data(location_coordinates, 'daily')
        conditions = wd.get_weather_conditions_for_n_days(how_many_days, json_weather_data)
        return conditions

    def display_weather_data(self, column_index, conditions):
        icon_name = str(conditions['icon'])
        icon = PhotoImage(file='./icons/' + icon_name + '.png')
        icon_label = Label(self.root, image=icon)
        icon_label.image = icon
        icon_label.grid(row=4, column=column_index)

        Label(self.root, text=str(conditions['desc'])).grid(row=5, column=column_index)

        frame = Frame(self.root, width=30)
        frame.grid(row=6, column=column_index)

        icon = PhotoImage(file='./icons/drops.png')
        icon_label = Label(frame, image=icon)
        icon_label.image = icon
        icon_label.pack(side='left')
        Label(frame, text=str(conditions['humidity']) + '%', font=('Arial', 11)).pack(side='left')

    def display_current_weather_conditions(self, current_conditions):
        Label(self.root, text='act_temp: ' + str(current_conditions['temp']) + ' °C',
              font=('Arial', 11)).grid(row=2, column=0)
        Label(self.root, text='min_temp: ' + str(current_conditions['feels_like']) + ' °C',
              font=('Arial', 11)).grid(row=3, column=0)

        self.display_weather_data(0, current_conditions)

    def display_weather_conditions_for_n_days(self, how_many_days):
        conds = self.get_weather_conditions_for_n_days(how_many_days)

        self.display_current_weather_conditions(conds[0])

        for i in range(1, len(conds)):
            Label(self.root, text='temp_min: ' + str(conds[i]['temp_min'])+' °C',
                  font=('Arial', 11)).grid(row=2, column=i)
            Label(self.root, text='temp_max: ' + str(conds[i]['temp_max'])+' °C',
                  font=('Arial', 11)).grid(row=3, column=i)

            self.display_weather_data(i, conds[i])

    def create_bar_plot(self, city_name, date, type):
        window = hw.HourlyForecast(city_name, date)
        window.create_bar_plot(type)

def main():
    window = Interface()


if __name__ == "__main__":
    main()