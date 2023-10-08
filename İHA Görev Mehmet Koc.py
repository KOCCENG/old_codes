from dronekit import mavutil
from dronekit import connect,VehicleMode,Command
import time

iha=connect("127.0.0.1:14550",wait_ready=True)

def takeoff(irtifa):
    while iha.is_armable is not True:
        print("İHA arm edilebilir durumda değil")

    print("IHA arm edilebilir")

    iha.mode=VehicleMode("GUIDED")
    
    iha.armed=True

    while iha.armed is not True:
        print("İHA arm ediliyor...")
        time.sleep(0.5)
    print("İHA arm edildi")

    iha.simple_takeoff(irtifa)
    while iha.location.global_relative_frame.alt<irtifa*0.9:
        print("IHA hedefe yükseliyor")

def gorev_ekle():
    global komut
    komut=iha.commands

    time.sleep(1)

    #TAKEOFF    
    komut.add(Command(0, 0, 0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,0,0,0,0,0,0,20))

    #WAYPOINT
    komut.add(Command(0, 0, 0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,-35.36283857,149.16521763,20))
    
    komut.add(Command(0, 0, 0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_LOITER_TIME,0,0,15,0,0,0,-35.36283857,149.16521763,5))
    
    komut.add(Command(0, 0, 0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,0,0,0,0,0,0,20))

    komut.add(Command(0, 0, 0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,-35.36257291,149.16506115,20))

    komut.add(Command(0, 0, 0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_LOITER_TIME,0,0,15,0,0,0,-35.36257291,149.16506115,3))
    
    komut.add(Command(0, 0, 0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,0,0,0,0,0,0,20))

    komut.add(Command(0, 0, 0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,0,0,0,0,0,0,0,0,0))
    komut.upload()
    print("Komutlar yükleniyor...")

takeoff(10)
gorev_ekle()
komut.next=0
iha.mode=VehicleMode("AUTO")

    #while True:
       # next_waypoint=komut.next
        #print("Siradaki komut{next_waypoint}")
        #time.sleep(1)

       