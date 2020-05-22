import re

def isEnOrNb(language):
    if(language == 'en' or language == 'nb'):
        return True
    else:
        return False

def stripHtml(value):
    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    return removeExtraSpaces(tag_re.sub(' ', value.replace('&nbsp;', ' ').replace('&quot;', ' ').replace('&gt;', ' ').replace('&ldquo;', ' ').replace('&rdquo;', ' ')))

def removeExtraSpaces(value):
    return re.sub(' +', ' ', value.strip())