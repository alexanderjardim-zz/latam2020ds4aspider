# latam2020ds4aspider
A simple spider to make it easy to get the course materials organized.

## What does it do?
It downloads the course cases, pdf's and other materials hosted on S3. Youtube videos are not contemplated.

## usage
* clone this repo
* download the page html from `https://latam.ds4a.io/lesson-plan` and save it in the root folder of the repo
* run the command `pip install -r requirements.txt` to install dependencies
* run the command `scrapy runspider localSpider.py` to download the course content

# optional: extract zip files

* run `python unpack.py` and zipfiles will be extrated to `./extracted` folder

## todo

- [ ] authenticate with user credentials
- [X] add extraction capabilities