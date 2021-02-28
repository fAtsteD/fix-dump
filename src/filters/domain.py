import os
import re
import sys


def filter(path: str, old_domain: str, new_domain: str):
    '''
    First method find name of percentage in file and replace its.

    File always (maybe not) have '%postname%'. But in the dump file it is like '{something}postname{something}'.
    Filter go through file two times.
    '''

    # Check if we have file
    if not os.path.isfile(path):
        print('File path {} does not exist.'.format(path))
        return

    # Open file for changing
    fread = open(path, 'r', encoding='utf8')

    # New data
    new_content = ''

    # Change domain
    for line in fread:
        new_content += _search_domain(line, old_domain, new_domain)

    fread.close()

    # Write changing
    with open(path, 'w', encoding='utf8') as fwrite:
        fwrite.writelines(new_content)
        fwrite.close()


def _search_domain(text: str, old_domain: str, new_domain: str) -> str:
    '''
    Search domain in text and replace
    '''

    # Special pattern for searching in serialized php
    serialized_pattern = "s:([0-9]{2,3}):(\\\\\"[^\\\"]+" + \
        re.escape(old_domain) + "[^\\\"]+\\\\\")"

    def match_serialized_pattern(matchobject):
        '''
        Change matched data with new domain with rules for serialized php
        '''
        return 's:' + str(int(matchobject.group(1)) + len(new_domain) - len(old_domain)
                          ) + ':' + matchobject.group(2).replace(old_domain, new_domain)

    # Apply serialized pattern
    text = re.sub(serialized_pattern, match_serialized_pattern, text)

    # Apply regula pattern
    text = re.sub(old_domain, new_domain, text)

    return text


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Need file for filter with old domain and new domain.')
        sys.exit()

    print('Run filter domain for file: ' + sys.argv[1])
    filter(sys.argv[1], sys.argv[2], sys.argv[3])
