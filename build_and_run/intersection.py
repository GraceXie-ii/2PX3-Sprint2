
from trafficSimulator import *
import numpy as np


class Intersection:
    def __init__(self):
        self.sim = Simulation()
        lane_space = 3.5
        intersection_size = 24
        island_width = 2
        length = 100


#---------------------------------------------------------------Variables----------------------------------------------------------------------------#
        self.vehicle_rate = 15
        self.v = 17
        self.speed_variance = 0
        self.self_driving_vehicle_proportion = 0.6 #number between 0 and 1, 0 means no self driving vehicles, 1 means entirely self driving vehicles
        if self.self_driving_vehicle_proportion == 1:
            self.v = self.v * 1.5

        self.sim.create_segment((112, -1.75), (12, 1.75)) #Segment 0
        self.sim.create_quadratic_bezier_curve((12, 1.75), (1.75, -1.75), (1.75, -12)) #Segment 1
        
    
    def get_sim(self):
        return self.sim