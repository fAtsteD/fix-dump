import os
import re
import sys


def filter_file(path: str, old_domain: str, new_domain: str):
    '''
    Find old domain and change to new.
    It has filter for serialized php object. It uses its first.
    '''

    # Check if we have file
    if not os.path.isfile(path):
        print('File path {} does not exist.'.format(path))
        return

    # Open file for changing
    fread = open(path, 'r', encoding='ISO-8859-1')

    # New data
    new_content = ''

    # Change domain
    for line in fread:
        new_content += filter_text(line, old_domain, new_domain)

    fread.close()

    # Write changing
    with open(path, 'w', encoding='ISO-8859-1') as fwrite:
        fwrite.writelines(new_content)
        fwrite.close()


def filter_text(text: str, old_domain: str, new_domain: str) -> str:
    '''
    Search domain in text and replace
    '''

    # Special pattern for searching in serialized php
    serialized_pattern = "(s:([0-9]*):(\\\\\"[^\\\"]*" + \
        re.escape(old_domain) + "[^\\\"]+\\\\\"))|(" + \
        re.escape(old_domain) + ")"

    def match_serialized_pattern(matchobject):
        '''
        Change matched data with new domain with rules for serialized php
        '''
        # For serialized str
        if matchobject.group(1) is not None:
            return 's:' + str(int(matchobject.group(2)) + len(new_domain) - len(old_domain)
                              ) + ':' + matchobject.group(3).replace(old_domain, new_domain)

        # For regular srg
        return matchobject.group(4).replace(old_domain, new_domain)

    text = re.sub(serialized_pattern, match_serialized_pattern, text)

    return text


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Need file for filter with old domain and new domain.')
        sys.exit()

    print('Run filter domain for file: ' + sys.argv[1])
    filter(sys.argv[1], sys.argv[2], sys.argv[3])
