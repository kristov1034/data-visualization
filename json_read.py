"""Json file handling"""

import json
import datetime

def json_read(filename):
    """Function to read in Json files and convert sensor data
       returns measurement data from input file

    """
    with open(filename, 'r') as thefile:
        json_data = json.load(thefile)

    for k in json_data.keys():
        print k

    themeasurement = json_data["sensorData"]

    thetime = []
    thevalue = []

    for mpoint in themeasurement:
        print mpoint["time"]

        # convert unix time to human readable time (WTF: 1000?)
        tmptime = datetime.datetime.utcfromtimestamp(
            int(mpoint["time"]/1000)
        ).strftime('%Y-%m-%d %H:%M:%S')
        thetime.append(tmptime)
        thevalue.append(mpoint["value"])

    return (thetime, thevalue)
