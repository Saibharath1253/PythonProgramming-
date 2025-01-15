class Time:
    def _init_(self, hour, minute, second):
        self.__hour = hour  # Private attribute
        self.__minute = minute
        self.__second = second

    def _add_(self, other):
        total_seconds = self._second + other._second
        total_minutes = self._minute + other._minute + (total_seconds // 60)
        total_hours = self._hour + other._hour + (total_minutes // 60)

        seconds = total_seconds % 60
        minutes = total_minutes % 60
        hours = total_hours % 24  # Assume a 24-hour clock

        return Time(hours, minutes, seconds)

    def display(self):
        print(f"{self._hour:02}:{self.minute:02}:{self._second:02}")


hour1 = int(input("Enter hours for Time 1: "))
minute1 = int(input("Enter minutes for Time 1: "))
second1 = int(input("Enter seconds for Time 1: "))

hour2 = int(input("Enter hours for Time 2: "))
minute2 = int(input("Enter minutes for Time 2: "))
second2 = int(input("Enter seconds for Time 2: "))

time1 = Time(hour1, minute1, second1)
time2 = Time(hour2, minute2, second2)

time_sum = time1 + time2

print("\nSum of Times:")
time_sum.display()
