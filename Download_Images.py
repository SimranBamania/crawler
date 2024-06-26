import os
from scraper import scrape

male_urls = [
'https://www.myntra.com/men-tshirts',
'https://www.myntra.com/men-casual-shirts',
'https://www.myntra.com/men-formal-shirts',
'https://www.myntra.com/men-sweatshirts',
'https://www.myntra.com/men-sweaters',
'https://www.myntra.com/men-jackets',
'https://www.myntra.com/men-blazers',
'https://www.myntra.com/men-suits',
'https://www.myntra.com/rain-jacket',
'https://www.myntra.com/men-kurtas',
'https://www.myntra.com/sherwani',
'https://www.myntra.com/nehru-jackets',
'https://www.myntra.com/dhoti',
'https://www.myntra.com/men-jeans',
'https://www.myntra.com/men-casual-trousers',
'https://www.myntra.com/men-formal-trousers',
'https://www.myntra.com/mens-shorts',
'https://www.myntra.com/men-trackpants',
]

female_urls = [
'https://www.myntra.com/women-kurtas-kurtis-suits',
'https://www.myntra.com/ethnic-tops',
'https://www.myntra.com/saree',
'https://www.myntra.com/women-ethnic-wear',
'https://www.myntra.com/women-ethnic-bottomwear?f=categories%3AChuridar%2CLeggings%2CSalwar',

'https://www.myntra.com/skirts-palazzos',
'https://www.myntra.com/dress-material',
'https://www.myntra.com/lehenga-choli',
'https://www.myntra.com/dupatta-shawl',
'https://www.myntra.com/women-jackets',

'https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen',
'https://www.myntra.com/tops',
'https://www.myntra.com/myntra-fashion-store?f=Categories%3ATshirts%3A%3AGender%3Amen%20women%2Cwomen',
'https://www.myntrcom/women-trousers',
'https://www.myntra.com/women-shorts-skirts',

'https://www.myntra.com/myntra-fashion-store?f=Categories%3AClothing%20Set%2CCo-Ords%3A%3AGender%3Amen%20women%2Cwomen',
'https://www.myntra.com/playsuit?f=Gender%3Amen%20women%2Cwomen',
'https://www.myntra.com/jumpsuits?f=Gender%3Amen%20women%2Cwomen',
'https://www.myntra.com/women-shrugs',
'https://www.myntra.com/women-sweaters-sweatshirts',

'https://www.myntra.com/women-jackets-coats',
'https://www.myntra.com/women-blazers-waistcoats',
'https://www.myntra.com/women-loungewear-and-nightwear',
'https://www.myntra.com/women-swimwear',
]

for i in range(0, len(female_urls)):
     file_name = female_urls[i].split('/')[-1]
     file_path = os.path.join('women', file_name)
     scrape(female_urls[i], file_path)
     print("Saved at :", file_path)

