def encryption_key(word)
    word = input()
    password = ''
    
    for alphanumeric in word:
        if alphanumeric == 'i':
            password = password + '!'
        elif alphanumeric == 'a':
            password = password + '@'
        elif alphanumeric == 'm':
            password = password + 'M'
        elif alphanumeric == 'B':
            password = password + '8'
        elif alphanumeric == 'o':
            password = password + '.'
        else:
            password = password + alphanumeric
    
    return(password)
