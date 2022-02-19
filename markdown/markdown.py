import re


def headers(line):
    if hash := re.match('^#+', line):
        if (hash := hash[0].count('#')) < 7:
            line = f'<h{hash}>' + line[hash+1:] + f'</h{hash}>'
            return True, line
    return False, line   


def bold_words(line):
    if bold_words := re.findall('__.*?__', line):
        for bold_word in bold_words:
            line = line.replace(bold_word, '<strong>'+bold_word.replace("__","")+'</strong>')
    return line


def italic_words(line):
    if italic_words := re.findall('_.*?_', line):
        for italic_word in italic_words:
            line = line.replace(italic_word, '<em>'+italic_word.replace("_","")+'</em>')
    return line


def lists(line, list_exist, list_curr, finish_ul):
    if re.match(r'\* (.*)', line):
    # Check if the list is already started
        if list_exist == False:
            list_exist = True
            list_curr = True
            line = '<ul><li>' + line[2:] + '</li>'
        else:
            list_curr = True
            line = '<li>' + line[2:] + '</li>'

    if list_exist and not list_curr:
            finish_ul = '</ul>'
            list_exist = False

    list_curr = False
    return line, list_exist, list_curr, finish_ul


def parse(markdown):

    lines = markdown.split('\n')
    result = ''
    finish_ul = ''
    list_exist = False
    list_curr = False  
    header_exist = False  

    
    for line in lines:


        header_exist, line = headers(line)
        line = bold_words(line)
        line = italic_words(line)
        line, list_exist, list_curr, finish_ul = lists(line, list_exist, list_curr, finish_ul)
        
        # Add paragrah if there is no list nor header in this line
        if not list_exist  and not header_exist:
            line = '<p>' + line + '</p>'


        # End current header
        header_exist = False

        # Add '</ul>' if it is necessery, case for ending the list in the middle of text
        # Othewise finish_ul shall be empty
        line = finish_ul + line

        # Add parsed line to result
        result += line

    # Close the list if we parsed all lines, case for list at the end of text
    if list_exist:
        result = result + '</ul>'

    # Return the result
    return result