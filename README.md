# Explainable AI for Planning Vehicular Traffic Infrastructure

## Project Overview

This project, developed during the 7th semester of the Bachelor of Technology program in Computer Science & Engineering at NIT Meghalaya, aims to address traffic congestion issues in Shillong City through the implementation of Explainable AI for Planning Vehicular Traffic Infrastructure.

## Contents

- [Introduction](#introduction)
- [Workflow](#workflow)
- [Methodology](#methodology)
- [Application](#application)
- [Results](#results)
- [Conclusion](#conclusion)
- [How to Use](#how-to-use)
- [Contributors](#contributors)

## Introduction

Traffic congestion in Shillong City has become a significant issue, especially during peak hours. This project explores different scenarios to understand and address the challenges posed by traffic congestion.

## Workflow

The workflow includes tools and technologies used, simulation steps, and the creation of necessary files for SUMO.

## Methodology

1. **Data Collection**: Comprehensive data on schools, traffic patterns, and congestion-related information were collected.

2. **Scenario Generation and Simulation**: Realistic scenarios were generated and simulated using SUMO (Simulation of Urban Mobility) with customized enhancements.

3. **Congestion Identification**: Congested road segments were identified using advanced visualization techniques and quantitative metrics.

4. **Dijkstra Model Application**: The Dijkstra algorithm was employed for routing vehicles through the network, optimizing travel time.

5. **Scenario Comparison**: Different scenarios, including 10% and 50% buses, were simulated, and their impacts on congestion and average speed were compared.

## Application

Two scenarios were considered: one with 10% buses and another with 50%. The simulation provides insights into traffic patterns, average speeds, and congestion durations.

## Results

After the simulation of two scenarios:
- The average speed on roads is higher with 50% buses than with 10% buses.
- The congestion duration on roads is improved by 39% with 50% buses than with 10% buses.

After the simulation of two scenarios with the Model simulated scenarios:
- The average speed on roads is higher with 50% buses with the Model than with 50% buses.
- The congestion duration on roads is improved by 8% with 50% buses with the Model than with 50% buses.
  
Hence, the total congestion on roads is improved by 45% by using 50% Buses with the Model than by using 10% Buses.

## Conclusion

Two scenario-based visualizations of traffic congestion for Shillong city were successfully simulated. The project concludes that using 50% buses, coupled with the Dijkstra algorithm, results in a 45% improvement in total congestion on roads compared to using 10% buses.

## How to Use

1. **Run Simulation:**
   - Open the SUMO simulation with the `osm.sumocfg` file.
   - Use the network file and route file as the main input.

2. **Generate Congestion Data:**
   - Execute the "Congestion Data Program" with the route file to generate data.

3. **Calculate Congestion Time:**
   - Run the "Congestion Time Program" with the route file to calculate congestion time.

4. **Algorithm Performance:**
   - Execute the "Algorithm Program" to check the algorithm's performance.
   - Ensure all files are in the same folder.

## References

•	https://www.researchgate.net/publication/224793504_SUMO_Simulation_of_Urban_MObility_An_open-source_traffic_simulation
•	https://sumo.dlr.de/docs/sumo-gui.html#showing_routes_and_route-related_information
•	https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#stops_and_waypoints
•	https://sumo.dlr.de/docs/sumo-gui.html#configuration_files
•	https://sumo.dlr.de/docs/sumo-gui.html#gui-settings_files
•	https://gis.stackexchange.com/questions/16986/steps-to-creating-a-geotiff
•	https://sumo.dlr.de/docs/sumo-gui.html#edgelane_visualisation_settings
•	https://sumo.dlr.de/docs/Tools/Emissions.html#emissionsmap
•	https://josm.openstreetmap.de/doc/
•	https://docs.python.org/fr/3.6/
•	https://sumo.dlr.de/docs/TraCI.html
•	https://pandas.pydata.org/docs/
•	https://sumo.dlr.de/docs/Netedit/index.html
•	https://www.researchgate.net/publication/338790110_A_SUMO_Based_Simulation_Framework_for_Intelligent_Traffic_Management_System
•	https://sumo.dlr.de/docs/Simulation/Routing.html

## Contributors

- Skhembor Suchen
- Wallambok Rani
- Banteilang Kharphuli


