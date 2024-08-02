if __name__ == '__main__':

    texxt = input("Input your text:")  #input text into variable

def add_space_after_dot(input_string):  # define funstion that replace "." for ". "
    return input_string.replace('.', '. ')





def norm_text(texxt):             # define function that replace

    normalized_text = texxt.split('.') # split sring by dot and add it parts like a list elements to a list


    normalized_text = [s.strip()[:1].upper() + s.strip()[1:].lower() for s in normalized_text if s]  #Create a new list sentences where each element is a string from the original sentences list but with leading and trailing whitespace removed and the first character in uppercase and the rest in lowercase, ignoring any empty strings


    string_conv = '.'.join(normalized_text) + '.'  # join elements from a list to a string as a string and add a dot between and at the end
    return string_conv

def last_word_sent(xxx):
    last_word_sentense = []  # create new list
    ls = xxx.split((' ')) # split string by whitespace and add to a list
    for word in ls:  # itterate over ls elements
        if word.endswith('.'):  # add element ends with . to new list and remove . at the end
            last_word_sentense.append(word[:-1])

    lws_joined = ' '.join(last_word_sentense)  # join list elements to a string

    text_joined = ' '.join(ls)  # join list elements to a string

    plus_sent = text_joined + lws_joined.capitalize() + '.'  # add last sentence



    #plus_sent_new_line = plus_sent.replace('.', '.\n')  # add new line after .
    return plus_sent

def iz_is(sss):
    corrected = sss.replace(" iz", " is")  # change  " iz" to " is"
    return corrected

def count_whitespaces(wst):
    total_whitespaces = wst.count(' ') + wst.count('\n') + wst.count('\t')       #count whitespaces, newline and tab characters
    return total_whitespaces

    output_text = norm_text(texxt)   # apply function to a variable andn save it to new var

    output_text = add_space_after_dot(output_text)  #apply function and save it to var

    plus_sent = last_word_sent(output_text) #apply function and save it to var

    corr_text = iz_is(plus_sent) #apply function and save it to var

    print(count_whitespaces(texxt)) # print result

    print(output_text) # print var
    print(plus_sent)  # print var
    print(corr_text)  # print var




