cities = {
    'Nagoya': {
        'Country': 'Japan',
        'Population': 2296000,
        'Interesting Fact': 'Nagoya is the fourth largest city in Japan',
        },

        'Manila': {
        'Country': 'Philippines',
        'Population': 1780000,
        'Interesting Fact': 'The city is the centre of the country’s economic, political, social, and cultural activity.',
        },

        'Dubai': {
        'Country': 'United Arab Emirates',
        'Population': 3331000,
        'Interesting Fact': 'There are 2.3 males to every female in Dubai',
        },
}
for city, info in cities.items():
    print(f'\nCity: {city}')
    for keys in info:
        print(keys+ ':',info[keys])


    


