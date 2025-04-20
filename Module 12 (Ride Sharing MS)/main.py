from ride import Ride,RideMatching,RideRequest,RideSharing
from vehicle import Car,Bike
from user import Driver,Rider

niye_jao = RideSharing('Niye jao')
rahim = Rider('rahim uddin','rahim@gmail.com',13213,'Mohakhali',1200)
niye_jao.add_rider(rahim)

kolimuddin = Driver('koli uddin','kolim@gmail.com',3213213,'Gulshan')
niye_jao.add_driver(kolimuddin)

rahim.request_ride(niye_jao,'uttara','car')

kolimuddin.reach_destination(rahim.current_ride)
rahim.show_current_ride()
