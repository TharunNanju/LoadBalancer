# LoadBalancer
The base form of this project is meant to create 3 backend servers hosted in docker containers, the requests sent to these backends is balanced by the Nginx load balancer and then visualised on grafana using prometheus

Current work:
Attempting to make a VPN server to allow the load balancer to connect to any of the backends on any machine remotely, without the need for port forwarding

for running the project CD into the directory and then run the following command,

docker-compose up --build

use -d flag to not show real time CLI logs

for sending requests to backends,

ab -n 1000 -c 100 http://localhost:8080/

Grafana: http://localhost:3001
Prometheus: http://localhost:9091

In grafana if you have to create a new data source, prometheus url will be http://prometheus:9090/

to show all visualisations in grafana, import a new dashboard from the given JSON
