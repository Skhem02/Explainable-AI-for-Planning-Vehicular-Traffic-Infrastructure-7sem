import traci

sumo_cmd = ['sumo-gui', '-c', 'osm.sumocfg']

# Start SUMO and connect to it with Traci
traci.start(sumo_cmd)

# Simulation time step (in seconds)
sim_step = 10

total_congestion_duration = 0
congested_vehicle_count = 0
prev_congested = False
congested_start_time = 0

# Simulation loop
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

    # Get the number of vehicles that are currently congested for all edges
    edge_ids = traci.edge.getIDList()
    congested_vehicles = sum([traci.edge.getLastStepHaltingNumber(edge_id) for edge_id in edge_ids])

    if congested_vehicles > 0:
        if not prev_congested:
            congested_start_time = traci.simulation.getTime()
            prev_congested = True
        congested_vehicle_count += congested_vehicles * sim_step
    else:
        if prev_congested:
            total_congestion_duration += traci.simulation.getTime() - congested_start_time
            prev_congested = False

# Stop the simulation and Traci
traci.close()

print("Total congestion duration: ", total_congestion_duration, " seconds")
