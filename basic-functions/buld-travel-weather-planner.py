distance_mi = 0
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False

if distance_mi:
    if distance_mi <= 1 and is_raining == False:
        print(True)
    elif distance_mi > 1 and distance_mi <= 6 and is_raining and has_bike == False:
        print(False)
    elif distance_mi > 1 and distance_mi <= 6 and has_bike and is_raining == False:
        print(True)
    elif distance_mi > 6 and has_ride_share_app:
        print(True)
    elif distance_mi > 6 and has_car:
        print(True)
    else:
        print(False)
else:
    print(False)