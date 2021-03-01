import os
import sys

from filters.domain import filter_text as filter_domain
from filters.percentage import filter_text as filter_percentage


def main():
    '''
    Main function for all app.
    '''

    # Check params
    if len(sys.argv) < 2:
        print('Need file for program.')
        sys.exit()

    file_path = sys.argv[1]

    # Check if we have file
    if not os.path.isfile(file_path):
        print('File path {} does not exist.'.format(file_path))
        sys.exit()

    # For filter domain
    if len(sys.argv) < 4:
        print('Domain filter needs old and new domain params.')
        sys.exit()

    old_domain = sys.argv[2]
    new_domain = sys.argv[3]

    content = ''
    with open(file_path, 'r', encoding='ISO-8859-1') as fread:
        content += fread.read()
        fread.close()

    # Accept filters
    content = filter_percentage(content)
    content = filter_domain(content, old_domain, new_domain)

    with open(file_path, 'w', encoding='ISO-8859-1') as fwrite:
        fwrite.write(content)
        fwrite.close()


if __name__ == '__main__':
    main()
