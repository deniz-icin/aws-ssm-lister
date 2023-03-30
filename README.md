# aws-ssm-lister

This project list all SSM parameters and their contents in AWS.

## Dependencies:
[Docker](https://docs.docker.com/get-docker/)

### How to use?

- **Cloning repo**

1. Clone repo.
2. Change directory to project directory.
3. Build image as **_ssmimage_** in current directory and run with credentials and region on port 80.

``` bash
docker build -t ssmimage .
nano ~/.aws/credentials #Copy credentials and use as environment variables. 
docker run -e AWS_ACCESS_KEY_ID="YOUR_KEY_ID" -e AWS_SECRET_ACCESS_KEY="YOUR_ACCESS_KEY" -e AWS_DEFAULT_REGION=YOUR_REGION -p 80:80 ssmimage
```

> Instead of first option, use **_aws-cli_** image to attach credentials as volume. 
> When you run the `docker run`, it will automatically pull aws-cli.

``` bash
docker build -t ssmimage .
docker pull amazon/aws-cli
docker run --rm -ti -v ~/.aws:/root/.aws -p 80:80 ssmimage
```

-----------------------------------------------------------------------------------------------------

- **Pull from Dockerhub**

1. Pull ssmimage and aws-cli.
2. Run image as **_hariboidevops/ssmimage:latest_** in current directory.

``` bash
docker pull hariboidevops/ssmimage:latest
docker pull amazon/aws-cli
docker run --rm -ti -v ~/.aws:/root/.aws -p 80:80 hariboidevops/ssmimage:latest
```
