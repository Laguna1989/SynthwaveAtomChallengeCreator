# EC2 Setup

## Create AWS EC2 instance

* log in on aws.amazon.com
* create EC2 micro instance
* save *.pem (key signature) file locally
* when instance is created and running: go to "connect to instance" -> "ssh client", copy connection string

```
ssh -i [path to .pem file]
```

## Install docker and run container

Execute the following commands

* `sudo yum update -y`
* `sudo yum install docker`
* `sudo service docker start`
* `sudo usermod -a -G docker ec2-user`
* log out & log in again so usermod takes action
* `docker info` ## check if docker is running

# Pull and run the docker container

* pull the docker image from github registry via

``` 
docker pull ghcr.io/laguna1989/synthwaveatomchallengecreator:latest
```

* create an `.env` file that contains the discord token in the format
  `DISCORD_TOKEN=....`

* run the docker container via

```
docker run --env-file .env ghcr.io/laguna1989/synthwaveatomchallengecreator:latest
```
