from collections import deque
from Elevator import Elevator


class ElevatorSystem(object):
    """represents system of up to 16 elevators
    going from lowest_floor to highest_floor (set highest_floor > lowest_floor)
    num_elevators should be >= 1
    lowest_floor : int
    highest_floor : int
    floors are indexed : lowest_floor, lowest_floor+1, ..., highest_floor-1, highest_floor"""

    def __init__(self, num_elevators: int, lowest_floor: int, highest_floor: int):
        assert highest_floor > lowest_floor, "Please set highest_floor > lowest_floor"

        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.elevators = []
        self.elevator_queues = {} # key is id of elevator

        default_floor = lowest_floor
        for elevator_id in range(num_elevators):
            elevator = Elevator(elevator_id, default_floor)
            self.elevators.append(elevator)
            self.elevator_queues[elevator_id] = deque() # FIFO

        self.pickup_requests = deque() # tupels (pickup_floor, target_floor)


    def hard_set(self, elevator_id: int, current_floor: int, target_floor=None):
        """for testing"""
        self.elevators[elevator_id].hard_set_current_floor(current_floor)
        self.elevators[elevator_id].set_target_floor(target_floor)


    def status(self):
        """prints status of elevators"""
        for elevator in self.elevators:
            elevator.status()


    def get_floor_and_target(self, elevator_id: int) -> (int, int):
        """returns info about elevator, current floor and target floor
        target floor can be None"""
        assert 0 <= elevator_id <= len(self.elevators)-1, "elevator_id out of range"
        elevator = self.elevators[elevator_id]
        floor = elevator.get_current_floor()
        target_floor = elevator.get_target_floor()
        return floor, target_floor


    def pickup_request(self, pickup_floor: int, direction: [-1, 1]):
        """request by human on floor
        pickup_floor : floor with request
        direction: -1 : down, +1 up"""

        self.pickup_requests.append((pickup_floor, direction))


    def target_floor_request(self, elevator_id: int, target_floor: int):
        """request coming from persons in particular elevator
        target_floor has to be in interval [lowest_floor, highest_floor]"""

        assert target_floor >= self.lowest_floor
        assert target_floor <= self.highest_floor

        elevator = self.elevators[elevator_id]
        current_floor = elevator.get_current_floor()
        current_target_floor = elevator.get_target_floor()

        if current_target_floor is not None:
            if current_floor < target_floor < current_target_floor:
                self.elevator_queues[elevator_id].appendleft(target_floor)
        else:
            self.elevator_queues[elevator_id].append(target_floor)


    def step(self):
        """steps all elevators, if elevator fullfills target request, request is removed"""
        self.__schedule_elevators()
        for elevator_id, elevator in enumerate(self.elevators):
            elevator.step()

            if elevator.get_current_floor() == elevator.get_target_floor():
                self.elevator_queues[elevator_id].popleft() # request fulfilled
                self.elevators[elevator_id].set_target_floor(None)


    def __process_pickup_requests(self):
        """transforms pickup requests into target floor requests
        by finding suitable elevator and sending him to pickup floor"""        
        to_remove = []
        for pickup_floor, direction in self.pickup_requests:
            possible_elevators = []

            for elevator in self.elevators:
                if elevator.matches_request(pickup_floor, direction):
                    possible_elevators.append(elevator)

            if len(possible_elevators) > 0:
                elevator_id = self.__find_nearest_elevator_id(possible_elevators, pickup_floor)
                self.target_floor_request(elevator_id, pickup_floor)
                to_remove.append((pickup_floor, direction))
            else:
                comming_elevators = []
                for elevator in self.elevators:
                    if elevator.is_coming_to(pickup_floor):
                        comming_elevators.append(elevator)

                if len(comming_elevators) > 0:
                    elevator_id = self.__find_nearest_elevator_id(possible_elevators)
                    self.target_floor_request(elevator_id, pickup_floor)
                    to_remove.append((pickup_floor, direction))

        for item in to_remove:
            self.pickup_requests.remove(item)


    def __find_nearest_elevator_id(self, possible_elevators: list, pickup_floor: int):
        nearest_el = min(possible_elevators, key=lambda el: abs(el.get_current_floor() - pickup_floor))
        return nearest_el.elevator_id


    def __schedule_elevators(self):
        """in this method, following pairs are decided: elevator_id -> target_floor
        in other words where to send each elevator"""
        self.__process_pickup_requests()

        for elevator_id, elevator in enumerate(self.elevators):
            if len(self.elevator_queues[elevator_id]) > 0:
                first_in_queu = self.elevator_queues[elevator_id][0]
                elevator.set_target_floor(first_in_queu)
