# CMSI 3801 load-testing-gacha-system

## Project Overview: 
Record load test results for a server that simulates a "gacha system" used in online games. This will be conducted using [locust](http://locust.io/), an open source load testing tool.

## Feature Specification: 
1. Server that simulates a basic gacha system
2. Client to simulate users
3. Locust implementation: swarm the system with simultaneous users, test the robustness of the server

## Technical Specification:
This will be implemented in Python to utilize Python's multithreading, allowing the server to handle more requests.

## How To Run:
1. cd test/
2. Run `locust` and navigate to the link `Starting web interface at http://localhost:XXXX`
3. In a seperate terminal run `python3 test_server.py`
4. Enter number of users and spawn rate. Use http://localhost:5555 for the host field.