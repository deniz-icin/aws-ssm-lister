# aws-ssm-lister

This project list all SSM parameters and their contents in AWS.

### How to use?

- **Cloning repo**

1. Clone repo.
2. Build image as **_ssmimage_** in current directory and run on port 80.

``` bash
git clone https://github.com/deniz-icin/aws-ssm-lister.git
docker build -t ssmimage .
docker run --rm -ti -v ~/.aws:/root/.aws -p 80:80 ssmimage
```

-----------------------------------------------------------------------------------------------------

- **Use image from Dockerhub**

1. Run image as **_hariboidevops/ssmimage:latest_** in current directory.

``` bash
docker run --rm -ti -v ~/.aws:/root/.aws -p 80:80 hariboidevops/ssmimage:latest
```
> `docker run` command will automatically pull image from Dockerhub.
