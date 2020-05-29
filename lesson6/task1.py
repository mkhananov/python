class TrafficLight:
    __color = {"red": 7, "yellow": 2, "green": 7}

    def running(self):
        import time
        while True:
            for el in self.__color:
                print(el)
                for sec in range(self.__color.get(el)):
                    print(".", end="")
                    time.sleep(1)
                print()


t = TrafficLight()
t.running()
