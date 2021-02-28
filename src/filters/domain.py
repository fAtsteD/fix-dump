import os
import re
import sys


def filter(path: str, old_domain: str, new_domain: str):
    '''
    Find old domain and change to new.
    It has filter for serialized php object. It uses its first.
    '''

    # Open file for changing
    fread = open(path, 'r', encoding='ISO-8859-1')

    # New data
    new_content = ''

    # Change domain
    for line in fread:
        new_content += change_domain(line, old_domain, new_domain)

    fread.close()

    # Write changing
    with open(path, 'w', encoding='ISO-8859-1') as fwrite:
        fwrite.writelines(new_content)
        fwrite.close()


def change_domain(text: str, old_domain: str, new_domain: str) -> str:
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
