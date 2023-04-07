# Mapmybroadband Scraper

Program which, given an address (street, city, state, zip), scrapes the available internet service providers and technology types from
the site https://mapmybroadband.dps.ny.gov/.


## Requirements

- python 3.7



## How to Run

In CLI:

1.  pip install -r requirements.txt
	
2.  python script.py
	
3. Type in your street, city, state (can be in 2 letter format or spelled out), and zip code as prompted.
	Street, city, state are not case sensitive.
	

## Example:


Please enter your street:
150 Court St

Please enter your city:
Brooklyn

Please enter your state:
(Can be in 2 letter format or spelled out)
New York

Please enter your zip code:
11201

Loading...

Scraping from
https://mapmybroadband.dps.ny.gov/explore?address=150%20Court%20St,%20Brooklyn,%20New%20York,%2011201




['Spectrum', 'COAX']
['Verizon', 'FIBER']
['Starry', 'FIXED WIRELESS']
['ViaSat', 'SATELLITE']
['HughesNet', 'SATELLITE']
['Verizon', 'DSL']