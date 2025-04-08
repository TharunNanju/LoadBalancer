# LoadBalancer
for running the project CD into the directory and then run the following command,

docker-compose up --build

use -d flag to not show real time CLI logs

for sending requests to backends,

ab -n 1000 -c 100 http://localhost:8080/

Grafana: localhost:3001
Prometheus: localhost:9091

In grafana if you have to create a new data source, prometheus url will be http://prometheus:9090/

to show all visualisations in grafana, import a new dashboard from the given JSON
