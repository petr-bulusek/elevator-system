from ElevatorSystem import ElevatorSystem


def test_one_elevator_target_request():
    """
    1 elevator starting in 0
    person  goes 0 -> 2
    another goes 2 -> 0
    """
    num_elevators = 1 # elevator id == 0
    el_id         = 0
    lowest_floor  = 0
    highest_floor = 10
    es = ElevatorSystem(num_elevators, lowest_floor, highest_floor)
    es.target_floor_request(el_id, 2)
    es.step()
    assert es.get_floor_and_target(el_id) == (1, 2)
    es.step()
    assert es.get_floor_and_target(el_id) == (2, None)
    es.target_floor_request(el_id, 0)
    es.step()
    assert es.get_floor_and_target(el_id) == (1, 0)
    es.step()
    assert es.get_floor_and_target(el_id) == (0, None)
    print("test_one_elevator_target_request OK")


def test_one_elevator_pickup_request():
    """
    1 elevator starting in 0
    pickup_request 2, down
    """
    num_elevators = 1 # elevator id == 0
    el_id         = 0
    lowest_floor  = 0
    highest_floor = 10
    es = ElevatorSystem(num_elevators, lowest_floor, highest_floor)
    es.pickup_request(2, -1)
    es.step()
    assert es.get_floor_and_target(el_id) == (1, 2)
    es.step()
    assert es.get_floor_and_target(el_id) == (2, None)
    print("test_one_elevator_pickup_request OK")


