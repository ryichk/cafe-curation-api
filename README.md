# Cafe Curation API

## Set UP

```sh
docker build --tag cafe-curation-api .
docker run -it --rm --name cafe-curation-api -v $PWD:/app cafe-curation-api

# Inside the Docker Container

## Install Packages
pip install -r requirements.txt

## Install Other Package
pip install <package_name>

## Export current env settings
pip freeze > requirements.txt

## Generate Spider
scrapy genspider <crawler_name> <target_site_url>

## Crawling Start
scrapy crawl <crawler_name> -o <output_file_name>

## Scrapy Shell
scrapy shell <url>
```
