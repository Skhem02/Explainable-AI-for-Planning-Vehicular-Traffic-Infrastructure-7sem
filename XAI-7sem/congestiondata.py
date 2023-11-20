import traci
import pandas as pd

sumo_cmd = ["sumo-gui", "-c", "osm.sumocfg"]
traci.start(sumo_cmd)

congestion_threshold = 0  # Set your congestion threshold here (in seconds)
edge_speeds = {edge_id: [] for edge_id in traci.edge.getIDList()}
congestion_data = []

for step in range(1500):
    veh_ids = traci.vehicle.getIDList()
    for veh_id in veh_ids:
        edge_id = traci.vehicle.getRoadID(veh_id)
        speed = traci.vehicle.getSpeed(veh_id)
        edge_speeds[edge_id].append(speed)

    traci.simulationStep()

for edge_id, speeds in edge_speeds.items():
    if speeds:
        avg_speed = sum(speeds) / len(speeds)
        congested_vehicles = traci.edge.getLastStepHaltingNumber(edge_id)
        congestion_duration = congested_vehicles * 0.001  # Assuming simulation time step is 0.1 seconds

        if congestion_duration >= congestion_threshold:
            congestion_data.append({'Edge ID': edge_id, 'Congestion Duration': congestion_duration, 'Average Speed': avg_speed})

if congestion_data:
    df = pd.DataFrame(congestion_data)
else:
    df = pd.DataFrame(columns=['Edge ID', 'Congestion Duration', 'Average Speed'])

df.to_excel('10buswal_data.xlsx', index=False)
