import weather_data as wd
from datetime import date, timedelta
import matplotlib.pyplot as plt


class HourlyForecast:
    def __init__(self, cn, dt):
        self.city_name = cn
        self.date = dt
        self.bar_pl = None
        plt.clf()


    def get_data(self, city_name, dt):
        coordinates = wd.get_city_coordinates(city_name)
        json_data = wd.get_json_data(coordinates, 'hourly')
        hourly_forecast = wd.get_hourly_forecast(dt, json_data)
        return hourly_forecast

    def make_bar_plot(self, hours, temps):
        self.bar_pl = plt.subplot()
        self.bar_pl.bar.xticks(temps, rotation='vertical')
        self.bar_pl.bar.show()

    def make_bar_plot_horizontal(self, hours, temps):
        self.bar_pl = plt.subplot()
        self.bar_pl.barh(hours, temps)
        self.bar_pl.set_title(self.city_name+" at "+str(self.date))
        self.bar_pl.set_xlabel('Temperature')
        self.bar_pl.set_ylabel('Hour')
        self.bar_pl.set_visible(True)
        plt.show()

    def split_dictionary(self, dict):
        temps = []
        hours = []
        for pair in dict:
            temps.append(pair['temp'])
            hours.append(pair['date'][11:])

        return temps, hours

    def create_bar_plot(self, plot_kind='normal'):
        json_data = self.get_data(self.city_name, self.date)
        temps, hours = self.split_dictionary(json_data)
        if plot_kind == 'horizontal':
            self.make_bar_plot_horizontal(hours, temps)
        else:
            self.make_bar_plot(hours, temps)


def main():
    pass


if __name__ == '__main__':
    main()