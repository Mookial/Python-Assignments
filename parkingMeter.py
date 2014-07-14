class ParkingMeter:
    
    def __init__(self, maxTime, rate):
        "Sets maxTime and rate"
        self.time = 0 #Time left
        self.maxTime = maxTime #Max Time on meter
        self.rate = rate # Minutes per quarter increase
        print("Meter Created")
        print ("Current time on meter: ", self.time)
    
    def insert_quarter (self):
          if (self.time < self.maxTime):
              self.time += self.rate
              print ("Time remaining increased to ", self.time)
    
          else:
              print ("Max limit hit.")

    def get_time (self):
        print ("Test ", self.maxTime)         
        print ("Time Remaining: %d of %d minutes" % (self.time, self.maxTime))
