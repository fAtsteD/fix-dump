import os
import sys

from filters.domain import filter as filter_domain
from filters.percentage import filter as filter_percentage


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
        return

    # For filter domain
    if len(sys.argv) < 4:
        print('Domain filter needs old and new domain params.')
        sys.exit()

    old_domain = sys.argv[2]
    new_domain = sys.argv[3]

    # Accept filters
    filter_percentage(file_path)
    filter_domain(file_path, old_domain, new_domain)


if __name__ == '__main__':
    main()
