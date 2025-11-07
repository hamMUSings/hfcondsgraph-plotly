# hfcondsgraph-plotly
This docker container reformats data from http://hamqsl.com⁠ to two png images to post on a website using plotly. It generates both images hourly after the start time of the container. It publishes the pngs to /home/plotly/output which in the example docker-compose.yaml is bound to the web image folder on the host for automatic updates to the website. This folder can be bound anywhere by changing the docker-compose.yaml volume.

# Example images

# Docker
Pre-built docker image available at  [Docker Hub](https://hub.docker.com/repository/docker/hammusings/hfconds-plotly-hourly-generator/general)