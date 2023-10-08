from pymavlink import mavutil,mavwp

address="udpin.localhost:14551"
vehicle=mavutil.mavlink_connection(address, baud=57600,autoreconnect=True)
vehicle.wait_heartbeat()
print("Bağlanti Başarili")

wp=mavwp.MAVWPLoader()


def anlik_irtifa():
    message=vehicle.recv_match(type="GLOBAL_POSITION_INT", blocking=True)
    alt=message.relative_alt
    alt=alt/1000
    return alt
def takeoff(alt):
    vehicle.mav.command_long_send(vehicle.target_system,vehicle.target_component,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,0,0,0,0,0,alt)
    while True:
        current_alt=anlik_irtifa()
        if current_alt < alt:
            print(f"Anlik irtifa {current_alt}")
        elif current_alt >= alt:
            print("istenilen irtifaya ulaşildi.")
            break

def add_mission(seq,lat,lon,alt):
    frame=mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT
    wp.add(mavutil.mavlink.MAVLink_mission_item_message(vehicle.target_system,vehicle.target_component,
    seq,
    frame,
    mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,lat,lon,alt))

    vehicle.waypoint_clear_all_send()
    vehicle.waypoint_count_send(wp.count())

    for i in range (wp.count()):
        msg= vehicle.recv_match(type=["MISSION_REQUEST"], blocking=True)
        vehicle.mav.send(wp.wp(msg.seq))
        print("Sending waypoint {0}".format(msg.seq))

vehicle.set_mode("GUIDED")
vehicle.arducopter_arm()
takeoff(10)
add_mission(0,-35.36318990, 149.16529030,25)
add_mission(1,-35.36326430, 149.16522730,35)
add_mission(2,-35.36318550, 149.16514810,40)
add_mission(3,-35.36308820, 149.16517760,20)
add_mission(4,-35.36302150, 149.16521250,10)

vehicle.set_mode("AUTO")