import threading
import time


class CarBrands:
    def __init__(self, file_path="car_brands.txt"):
        self.file_path = file_path
        self.car_brands = []
        self.load_car_brands()
        self.start_update_thread()

    def load_car_brands(self):
        with open(self.file_path, "r") as file:
            self.car_brands = [line.strip() for line in file]

    def update_car_brands(self):
        while True:
            self.load_car_brands()
            print("Updated car brands:", self.car_brands)
            time.sleep(120)

    def start_update_thread(self):
        update_thread = threading.Thread(target=self.update_car_brands)
        update_thread.daemon = True
        update_thread.start()

    def get_car_brands(self):
        return self.car_brands
