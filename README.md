# elevator-system

**`class ElevatorSystem`**

In constructor you provide number of elevators (e.g. 4) and lowest and highest floor index (e.g. -2 and 10)

Example: 
`es = ElevatorSystem(4, -2, 10)`

elevators get ids 0, ... , number of elevators - 1

public interface:

* **def hard_set(self, elevator_id: int, current_floor: int, target_floor=None):**
  - for testing, for setting elevators to their init positions, you can also set target and elevator will move there
* **def status(self)**
  - Querying the state of the elevators (what floor are they on and where they are going),
* **def get_floor_and_target(self, elevator_id: int) -> (int, int):**
  - receiving an update about the status of an elevator, returns (current floor, target floor) as tuple
* **def pickup_request(self, pickup_floor: int, direction: [-1, 1]):**
  - receiving a pickup request
* **def target_floor_request(self, elevator_id: int, target_floor: int):**
  - recieving request from inside of elevator
* **def step(self)**
  - time-stepping the simulation, it's descrete simulation, elevators are moving 0, +1 or -1 floor in each step


 ### Improvement of FCFS (first-come, first-served) order for one elevator - calling of method target_floor_request
 if one elevator gets request to go 1, 10, 2, 9, FCFS would not be good
 if the elevator is currently in some floor x and goes to y and receives request of floor z
 than z is put in the queue in front if z is between x and y, so that elevator stops in z and person can exit
 else the request is put at the end, for that linked list deque from collections is used and this logic is implemented in
 method target_floor_request
 
 ### Handling pickup requests
 pickup requests are registered and in each step processed, they are turned into target_floor_requests
 because with target_floor_requests we tell the elevators where to go
 we try to find the nearest elevators from free elevators and elevators going through pick up floor with same direction as request
 if we find suitable nearest, we give him target_floor_request
 if we don't find any
 we find nearest elevator coming in direction to pickup floor and making target_floor_request to this elevator
 else the request stays in the queue and will be processed in further steps
 at leaste some elevator will be free or comming in direction to the pickup request
 
 ### Tests
 For testing pytest is used
 Some simple tests are in `test_Elevator.py` and `test_ElevatorSystem.py` files
 You can run them with `run_tests.py`
 
