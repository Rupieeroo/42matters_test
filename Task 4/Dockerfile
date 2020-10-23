FROM ubuntu:latest

# Download requirements
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install jq -y

# Create app directory
WORKDIR /scripts

# Copy files
COPY . /scripts

RUN tar -xzf top-charts-playstore-daily-04.tar.gz

# Runs shell script
CMD ["bash", "./json_conversion.sh"]