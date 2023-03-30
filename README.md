# aws-ssm-lister

## This project list all SSM parameters in AWS and their contents.

### Dependencies:
Docker

1- Clone repo.
2- Change directory to project directory.
3- Build image as "ssmimage" in current directory and run with credentials and region on port 80.

``` bash
docker build -t ssmimage .
nano ~/.aws/credentials #Copy credentials and use as environment variables. 
docker run -e AWS_ACCESS_KEY_ID="YOUR_KEY_ID" -e AWS_SECRET_ACCESS_KEY="YOUR_ACCESS_KEY" -e AWS_DEFAULT_REGION=YOUR_REGION -p 80:80 ssmimage
```

!! Instead of first option, use "aws-cli" image to attach credentials as volume.

``` bash
docker build -t ssmimage .
docker pull amazon/aws-cli
docker run --rm -ti -v ~/.aws:/root/.aws -p 80:80 hariboidevops/ssmimage:latest
```

-----------------------------------------------------------------------------------------------------

1- Pull ssmimage and aws-cli from Dockerhub.
2- Run image as "hariboidevops/ssmimage:latest" in current directory.

``` bash
docker pull hariboidevops/ssmimage:latest
docker pull amazon/aws-cli
docker run --rm -ti -v ~/.aws:/root/.aws -p 80:80 hariboidevops/ssmimage:latest
```

