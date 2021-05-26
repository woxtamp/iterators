import os
import country_iterator

WIKI_URL = 'https://en.wikipedia.org/wiki/'
COUNTRY_FILE_PATH = 'files/countries.json'


def write_countries_to_file(url, path):
    if os.path.exists('files/wiki_links.txt'):
        os.remove('files/wiki_links.txt')
    for link in country_iterator.CountryIterate(url, path):
        with open('files/wiki_links.txt', 'a', encoding='utf-8') as f:
            f.write(f'{link}\n')


if __name__ == '__main__':
    write_countries_to_file(WIKI_URL, COUNTRY_FILE_PATH)
