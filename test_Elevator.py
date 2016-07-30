from Elevator import Elevator

def test_elevator_movement():
    elevator_id = 0
    current_floor = 0
    el = Elevator(elevator_id, current_floor)
    assert el.get_current_floor() == 0

    el.set_target_floor(5)
    assert el.get_target_floor() == 5
    assert el.get_direction() == 1

    el.step()
    assert el.get_current_floor() == 1
    el.step()
    el.step()
    assert el.get_current_floor() == 3
    el.step()
    el.step()
    assert el.get_current_floor() == 5
    print("test_elevator_movement OK")


def test_matches_pickup_request():
    elevator_id = 0
    current_floor = 4
    el = Elevator(elevator_id, current_floor)
    # target_floor is None
    directionUp = 1
    directionDown = -1

    floor = 2
    assert el.matches_request(floor, directionUp)

    floor = 5
    assert el.matches_request(floor, directionDown)
    

    el.set_target_floor(10)

    floor = 4
    assert not el.matches_request(floor, directionUp)

    floor = 8
    assert el.matches_request(floor, directionUp)

    floor = 2
    assert not el.matches_request(floor, directionUp)

    floor = 5
    assert not el.matches_request(floor, directionDown)

    floor = 9
    assert not el.matches_request(floor, directionDown)
    print("test_matches_pickup_request OK")