import os
import csvkit
import collections


COUNTIES_PATH = os.path.join(
    os.path.dirname(__file__),
    'data',
    '2017_Gaz_counties_national.txt'
)
COUNTIES_LIST = csvkit.DictReader(open(COUNTIES_PATH, 'r'), delimiter="\t")
COUNTIES_DICT = collections.defaultdict(dict)
for row in COUNTIES_LIST:
    COUNTIES_DICT[row['USPS']][row['NAME']] = row['GEOID']


def county(usps, name):
    return COUNTIES_DICT[usps][name]
