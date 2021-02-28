import os
import re
import sys

# Special word for finding percentage
special_word = 'postname'

# Code for percentage symbol when find its
percentage_symbol = ''


def filter(path: str):
    '''
    First method find name of percentage in file and replace its.

    File always (maybe not) have '%postname%'. But in the dump file it is like '{something}postname{something}'.
    Filter go through file two times.
    '''

    # Check if we have file
    if not os.path.isfile(path):
        print('File path {} does not exist.'.format(path))
        return

    fread = open(path, 'r', encoding='utf8')

    # Search percantage text
    for line in fread:
        if _find_percentage(line):
            break

    # File is not changed if nothing found
    if percentage_symbol == '':
        print('Percentage symbol is not found.')
        fread.close()
        return

    fread.seek(0)

    # Replaced text
    new_text = ''
    for line in fread:
        new_text += line.replace(percentage_symbol, '%')

    fread.close()

    # Open file and write data
    with open(path, 'w', encoding='utf8') as fwrite:
        fwrite.writelines(new_text)
        fwrite.close()


def _find_percentage(text: str) -> str:
    '''
    Find text that corresponds to the symbol of percentage.
    Return percentage symbol or empty text
    '''

    global percentage_symbol

    match = re.search(
        '(\{[^\{^\}]+\})(' + special_word + ')(\{[^\{^\}]+\})', text)

    if not match:
        return False

    percentage_symbol = match.group(1)

    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Need file for filter')
        sys.exit()

    print('Run filter percentage for file: ' + sys.argv[1])
    filter(sys.argv[1])
