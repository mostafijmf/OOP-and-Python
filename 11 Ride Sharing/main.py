from ride import Ride, RideSharing, RideRequest, RideMatching
from users import Driver, Ride
from vehicle import Bike, Car


stead_slow = RideSharing('Stead_slow')
fahim = Ride('Fahim', 'fahim@gmail.com', 871326545, 'Mirpur', 1000)
stead_slow.add_rider(fahim)
naim = Driver('Naim', 'naim@gmail.com', 78451254, 'Mirpur')
stead_slow.add_driver(naim)

fahim.request_ride(stead_slow, 'uttara', 'car')
naim.reach_destination(fahim.current_ride)

fahim.show_current_ride()
# print(stead_slow)