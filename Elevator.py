class Elevator(object):
    """represents one elevator

    movement instructions (setTargetFloor) are made by class ElevatorSystem

    members:
    elevator_id : >= 0
    current_floor : in interval [lowest_floor, highest_floor]
    running_direction : [0, -1, +1], 0 means not moving
    target_floor : floor currently running to"""

    def __init__(self, elevator_id: int, current_floor: int):
        self.elevator_id = elevator_id
        self.current_floor = current_floor
        self.running_direction = 0
        self.target_floor = None


    def status(self):
        """prints status of elevator"""

        print(self.__repr__())


    def __repr__(self):
        return "id: {}, current floor: {}, running: {}, target floor: {}" \
        .format(self.elevator_id, self.current_floor, self.running_direction, self.target_floor)


    def set_target_floor(self, target_floor: int):
        """sets target floor and running_direction will be changed accordingly"""

        self.target_floor = target_floor
        if self.target_floor is not None:
            self.running_direction = 1 if (self.target_floor > self.current_floor) else -1
        else:
            self.running_direction = 0


    def get_current_floor(self):
        return self.current_floor


    def get_target_floor(self):
        return self.target_floor


    def get_direction(self):
        return self.running_direction


    def matches_request(self, pickup_floor: int, direction: [-1, 1]) -> bool:
        """returns True if elevator is free or runs through pickup request floor with right direction"""

        if self.target_floor is None:
            return True

        if direction == self.running_direction:
            if direction > 0 and pickup_floor > self.current_floor:
                return True
            if direction < 0 and pickup_floor < self.current_floor:
                return True
        return False


    def is_coming_to(self, pickup_floor: int) -> bool:
        """ returns True if elevator is coming in direction of pickup request floor"""

        if pickup_floor < self.current_floor and self.running_direction < 0:
            return True
        if pickup_floor > self.current_floor and self.running_direction > 0:
            return True
        return False


    def step(self):
        """discrete move of elevator - 0, -1 or +1 floors"""
        self.current_floor += self.running_direction


    def hard_set_current_floor(self, current_floor: int):
        """for testing"""
        self.current_floor = current_floor
