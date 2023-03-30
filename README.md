# aws-ssm-lister

## This project list all SSM parameters in AWS and their contents.

### Dependencies:
Docker

### Clone repo, change directory to project, build image as "ssmimage" in current directory and run with credentials and region on port 80.

``` bash
docker build -t ssmimage .
nano ~/.aws/credentials #Copy keys
docker run -e AWS_ACCESS_KEY_ID="YOUR_KEY_ID" -e AWS_SECRET_ACCESS_KEY="YOUR_ACCESS_KEY" -e AWS_DEFAULT_REGION=YOUR_REGION -p 80:80 ssmimage
```


## Pull from Dockerhub

``` bash
docker pull hariboidevops/ssmimage:latest
docker run -e AWS_ACCESS_KEY_ID="YOUR_KEY_ID" -e AWS_SECRET_ACCESS_KEY="YOUR_ACCESS_KEY" -e AWS_DEFAULT_REGION=YOUR_REGION -p 80:80 hariboidevops/ssmimage:latest
```
