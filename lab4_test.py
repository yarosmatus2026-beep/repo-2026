try_status = True
song_name = input("Введіть назву пісні: ")
song_singername = input("Введіть виконавця пісні: ")
while try_status:
    try:
        song_duration = float(input("Введіть тривалість пісні у секундах(числом): "))
        try_status = False
        song_viewquantity = int(input("Введіть кількість переглядів пісні(числом): "))
        try_status = False
    except ValueError:
        try_status = True

class Clip:
    platf = "Youtube"
    version = 1
    def __init__(self, songname="", singername="", duration=0, viewquantity=0):
        self.__songname = songname
        self.__singername = singername
        self.__duration = duration
        self.__viewquantity = viewquantity
    def __str__(self):
        return f"кліп {self.__songname} виконавця {self.__singername}, тривалістю {self.__duration} секунд з {self.__viewquantity} переглядів"
    def display_info(self):
        print(f"кліп {self.__songname} виконавця {self.__singername}, тривалістю {self.__duration} секунд з {self.__viewquantity} переглядів")
    def __repr__(self):
        return f"Clip('{self.__songname}', '{self.__singername}', '{self.__duration}', '{self.__viewquantity}')"
    def __eq__(self, other):
        if isinstance(other, Clip):
            return self.__songname == other.__songname and self.__singername == other.__singername
    def __del__(self):
        print(f"кліп {self.__songname} видалено")
    def get_songname(self):
        return self.__songname
    def get_singername(self):
        return self.__singername
    def get_duration(self):
        return self.__duration
    def get_viewquantity(self):
        return self.__viewquantity
    
    def __add__(self, other):
        if isinstance(other, Clip):
            return Clip(self.__songname, self.__singername, self.__duration, self.__viewquantity + other.viewquantity)
clip = Clip(song_name, song_singername, song_duration, song_viewquantity)
clip.get_songname()
clip.get_singername()
clip.get_duration()
clip.get_viewquantity()
clip.display_info()
print(repr(clip))
def main():
    clip1 = Clip("gem", "ken", 5, 18)
    clip2 = Clip("gaz", "tuck", 12, 30)
    clip3 = Clip("chick", "muck", 14)
    clip1.display_info()
    clip2.display_info()
    clip3.display_info()
    print(clip1+clip2)
if __name__ == "__main__":
    main()