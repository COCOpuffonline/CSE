class Drone(object):
    def __init__(self, flying, charge_left=90):
        self.propellers = 4
        self.camera = 1
        self.range_left = 2500
        self.flying = flying
        self.battery_left = charge_left

    def charge(self, time):
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100

    def flying(self, range_left):
        if not self.range_left:
            print("Oh look a beautiful lake...")
            print("And it's GONE!")
            return
        battery_loss_per_minute = 3
        if self.battery_left <= 25:
            print("The drone is returning to home.")
            return
        self.battery_left -= range_left * battery_loss_per_minute
        if self.battery_left < 0:
            self.battery_left = 0
