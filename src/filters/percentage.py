import os
import re
import sys


def filter_file(path: str):
    '''
    Find percentage text and change them to the symbol percent

    File always (maybe not) have '%postname%'. But in the dump file it is like '{something}postname{something}'.
    Filter go through file two times.
    '''

    # Special word for finding percentage
    special_word = 'postname'

    # Code for percentage symbol when find its
    percentage_symbol = ''

    # Check if we have file
    if not os.path.isfile(path):
        print('File path {} does not exist.'.format(path))
        return

    fread = open(path, 'r', encoding='ISO-8859-1')

    # Search percantage text
    for line in fread:
        percentage_symbol = _find_percentage(line, special_word)
        if percentage_symbol != '':
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
        new_text += filter_text(line,
                                percentage_symbol, special_word)

    fread.close()

    # Open file and write data
    with open(path, 'w', encoding='ISO-8859-1') as fwrite:
        fwrite.writelines(new_text)
        fwrite.close()


def _find_percentage(text: str, special_word: str) -> str:
    '''
    Find text that corresponds to the symbol of percentage.
    Return percentage symbol or empty text
    '''

    match = re.search(
        '(\{[^\{^\}]+\})(' + special_word + ')(\{[^\{^\}]+\})', text)

    if not match:
        return ''

    return match.group(1)


def filter_text(text: str, percentage_symbol='', special_word='postname'):
    '''
    Find percentage symbol (or use setted) and replace its.
    '''
    # For not setted percentage text
    if percentage_symbol == '':
        percentage_symbol = _find_percentage(text, special_word)

    # Second check if nothing found, return not changed
    if percentage_symbol == '':
        return text

    return text.replace(percentage_symbol, '%')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Need file for filter')
        sys.exit()

    print('Run filter percentage for file: ' + sys.argv[1])
    filter(sys.argv[1])
