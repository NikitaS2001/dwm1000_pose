import rospy

from dwm1000_msgs.msg import BeaconDataArray
from sensor_msgs.msg import Range


def callback(data):
    global msg_pub, pub0, pub1, pub2, pub3

    msg_pub = Range()

    msg_pub.header.stamp = rospy.Time().now()
    msg_pub.range = data.beacons[0].dist

    pub0.publish(msg_pub)

    msg_pub.header.stamp = rospy.Time().now()
    msg_pub.range = data.beacons[1].dist

    pub1.publish(msg_pub)

    msg_pub.header.stamp = rospy.Time().now()
    msg_pub.range = data.beacons[2].dist

    pub2.publish(msg_pub)

    msg_pub.header.stamp = rospy.Time().now()
    msg_pub.range = data.beacons[3].dist

    pub3.publish(msg_pub)


def main():
    global msg_pub, pub0, pub1, pub2, pub3
    pub0 = rospy.Publisher("dwm1000/beacon_range0", Range, queue_size=10)
    pub1 = rospy.Publisher("dwm1000/beacon_range1", Range, queue_size=10)
    pub2 = rospy.Publisher("dwm1000/beacon_range2", Range, queue_size=10)
    pub3 = rospy.Publisher("dwm1000/beacon_range3", Range, queue_size=10)

    rospy.init_node("pub_range_beacon", anonymous=True)

    while not rospy.is_shutdown():

        rospy.Subscriber("dwm1000/beacon_data", BeaconDataArray, callback)
        rospy.spin()


if __name__ == "__main__":
    main()
