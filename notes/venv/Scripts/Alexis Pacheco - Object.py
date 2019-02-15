class Drone(object):
    def __init__(self, flying, charge_left=90):
        self.propellers = 4
        self.camera = True
        self.range_left = 2500
        self.flying = flying
        self.battery_left = charge_left
        self.storage_left = 512

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
            print("You lose signal and see a quick video of the drone falling.")
        if self.battery_left <= 25:
            print("Battery low, return to home")
        elif self.battery_left == 0:
            print("Annndd it's gone!")
        else:
            print("Your drone hovers and is at %s percent." % self.battery_left)

    def take_picture(self):
        if not self.camera:
            print("You are out of storage.")
            return
        if self.storage >= 0:
            print("Ready to take a picture.")
        else:
            print("You took a picture of a beautiful sunset.")

    def flip(self):
        if not self.battery_left:
