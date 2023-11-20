import sys
import xml.etree.ElementTree as ET

def decrease_bus_increase_passenger(trips_file):
    tree = ET.parse(trips_file)
    root = tree.getroot()

    # Iterate over each trip
    for trip in root.iter('trip'):
        trip_type = trip.attrib['type']

        # Check if the trip is a bus
        if 'bus_bus' in trip_type:
            # Decrease the number of buses
            trip.set('type', 'veh_passenger')
            trip.set('id', trip.get('id') + "_passenger")
            trip.set('depart', str(float(trip.get('depart')) + 1))  # Delay the departure for passenger vehicles

            # Increase the number of passenger vehicles (8 for each bus)
            for i in range(8):
                passenger_trip = ET.SubElement(root, 'trip')
                passenger_trip.set('id', f"{trip.get('id')}_passenger{i}")
                passenger_trip.set('depart', str(float(trip.get('depart'))))
                passenger_trip.set('from', trip.get('from'))
                passenger_trip.set('to', trip.get('to'))
                passenger_trip.set('type', 'veh_passenger')

            # Remove the original bus trip
            root.remove(trip)

    # Save the modified XML to a new file
    output_file = trips_file.replace('.xml', '_modified.xml')
    tree.write(output_file)
    print(f"Modified trips saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python modify_trips.py <trips_file.xml>")
        sys.exit(1)

    trips_file = sys.argv[1]
    decrease_bus_increase_passenger(trips_file)
