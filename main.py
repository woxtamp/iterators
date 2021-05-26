import hashlib
import os
import country_iterator

WIKI_URL = 'https://en.wikipedia.org/wiki/'
COUNTRY_FILE_PATH = 'files/countries.json'
OUTPUT_FILE_PATH = 'files/wiki_links.txt'


def write_countries_to_file(url, path_to_input, path_to_output):
    if os.path.exists(path_to_output):
        os.remove(path_to_output)
    for link in country_iterator.CountryIterate(url, path_to_input):
        with open(path_to_output, 'a', encoding='utf-8') as f:
            f.write(f'{link}\n')
            f.close()


def get_string_hash_file(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            while True:
                line = f.readline()
                if line:
                    yield hashlib.md5(line.encode()).hexdigest()
                if not line:
                    f.close()
                    break
    else:
        print(f'Ошибка! Файла {path} не существует!')


if __name__ == '__main__':
    # Задание 1
    write_countries_to_file(WIKI_URL, COUNTRY_FILE_PATH, OUTPUT_FILE_PATH)
    # Задание 2
    for item in get_string_hash_file(OUTPUT_FILE_PATH):
        print(item)
