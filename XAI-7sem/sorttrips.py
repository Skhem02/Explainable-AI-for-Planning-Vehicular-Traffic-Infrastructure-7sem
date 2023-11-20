import xml.etree.ElementTree as ET

# Function to arrange vehicle trips in ascending order of depart time
def arrange_trips_by_depart_time(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Get all trip elements and sort them by depart time
    trips = root.findall(".//trip")
    sorted_trips = sorted(trips, key=lambda x: float(x.attrib["depart"]))

    # Create a new root element and add the sorted trips to it
    sorted_root = ET.Element(root.tag, root.attrib)
    for trip in sorted_trips:
        sorted_root.append(trip)

    # Write the sorted trips to the output file
    sorted_tree = ET.ElementTree(sorted_root)
    sorted_tree.write(output_file)

# Modify the trips file
input_file = "tenbus.xml"
output_file = "tenbus.trips.xml"
arrange_trips_by_depart_time(input_file, output_file)
print(f"Sorted trips file generated: {output_file}")
