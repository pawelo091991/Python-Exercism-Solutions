class Clock:
    def __init__(self, hour, minute):
        minutes = (hour * 60 + minute) % 1440
        self.hour = minutes // 60
        self.minute =  (minutes - self.hour*60)
        

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour}".zfill(2) + ":" + f"{self.minute}".zfill(2)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour+minutes // 60, self.minute + minutes % 60)

    def __sub__(self, minutes):
        return Clock(self.hour-minutes // 60, self.minute - minutes % 60)
