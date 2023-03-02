# Homework
Docker lecture repository at [Avito's Analytics Academy](https://avito-analytics-academy.ru/) Data Science course.

### Step 1: 
To understand how the application works, install the dependencies and open these urls (using curl or a browser):
```bash
curl http://127.0.0.1:8080/books
curl http://127.0.0.1:8080/authors
```
Then go to this url:
```bash
http://127.0.0.1:8080/metrics
```
Here you can see how many times you have opened `/books`, `/authors` or some other path. There is also a lot of additional information - server response time, etc.

### Step 2. 
Make a Dockerfile which uses python version 3.8 or higher as its base image, install dependencies and run `server.py` on port 8080. And after that build it with tag `server:0.0.1`.

### Step 3.
Run the following commands:
```bash
# create network
docker network create --driver bridge webnet

# run server
docker run \
    --name=server \
    -d \
    --rm \
    -p 8080:8080 \
    --network webnet \
    server:0.0.1

# run prometheus
docker run \
    --name=prometheus \
    -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
    -d \
    --rm \
    --network webnet \
    prom/prometheus:v2.40.7

# run grafana
docker run \
     --name=grafana \
    -v $(pwd)/grafana/config.ini:/etc/grafana/grafana.ini \
    -v $(pwd)/grafana/datasource.yml:/etc/grafana/provisioning/datasources/default.yaml \
    -v $(pwd)/grafana/dashboard.yml:/etc/grafana/provisioning/dashboards/default.yaml \
    -v $(pwd)/grafana/dashboards:/var/lib/grafana/dashboards \
    -d \
    --rm \
    -p 3000:3000 \
    --network webnet \
     grafana/grafana:9.4.2
```

### Step 4.
Go to each url several times:
```bash
curl http://127.0.0.1:8080/books
curl http://127.0.0.1:8080/authors
```

### Step 5.
Open [grafana](http://localhost:3000/d/_eX4mpl3) in your browser.

### Step 6.
Make a docker-compose file.
