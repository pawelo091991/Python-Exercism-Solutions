import re


def parse(markdown):

    lines = markdown.split('\n')
    result = ''
    finish_ul = ''
    list_exist = False
    list_curr = False  
    header_exist = False  

    
    for line in lines:

        # Find headers 
        if re.match('###### .*', line):
            line =  '<h6>' + line[7:] + '</h6>'
            header_exist = True 
        elif re.match('##### .*', line):
            line =  '<h5>' + line[6:] + '</h5>'
            header_exist = True 
        elif re.match('#### .*', line):
            line =  '<h4>' + line[5:] + '</h4>'
            header_exist = True 
        elif re.match('### .*', line):
            line =  '<h3>' + line[4:] + '</h3>'
            header_exist = True 
        elif re.match('## .*', line):
            line =  '<h2>' + line[3:] + '</h2>'
            header_exist = True 
        elif re.match('# .*', line):
            line =  '<h1>' + line[2:] + '</h1>'
            header_exist = True 

        # Lists
        if re.match(r'\* (.*)', line):
            # Check if the list is already started
            if list_exist == False:
                list_exist = True
                list_curr = True
                line = '<ul><li>' + line[2:] + '</li>'
            else:
                list_curr = True
                line = '<li>' + line[2:] + '</li>'
        
        # Find bold words in line and parse them
        bold_words = re.findall('__.*?__', line)
        if bold_words:
            for bold_word in bold_words:
                line = line.replace(bold_word, '<strong>'+bold_word.replace("__","")+'</strong>')

        
        # Find italic words in line and parse them
        italic_words = re.findall('_.*?_', line)
        if italic_words:
            for italic_word in italic_words:
                line = line.replace(italic_word, '<em>'+italic_word.replace("_","")+'</em>')

        
        # Check if list ended (list exist but there is no '*' in this line)
        if list_exist and not list_curr:
            finish_ul = '</ul>'
            list_exist = False

        # Add paragrah if there is no list nor header in this line
        if not list_exist  and not header_exist:
            line = '<p>' + line + '</p>'


        # End current list entry
        list_curr = False

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