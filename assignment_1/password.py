SCORES_NUM = 3

def get_input():
    '''Recieves input from the user and returns it'''
    return input("Please enter a password: ")

def get_length_score(password):
    '''Calculates password score based on password length'''
    if len(password) <= 4: # Short password
        return 0
    elif 5 <= len(password) <= 7: # Medium password
        return 5
    else: # Long password
        return 10

def get_variation_score(password):
    '''Calculates password score based on character variation'''
    if password.isdigit(): # Only digits
        return 0
    elif password.isalpha(): # Only letters
        return 3
    elif password.isalnum() and password.islower(): # Numbers & lowercase letters
        return 5
    elif password.isalnum(): # Numbers and letters
        return 7
    else: # Not only numbers and letters
        return 10

def get_common_words_score(password):
    '''Calculates password score based on common words'''
    if password.startswith('password'):
        return 0
    elif 'love' in password or 'querty' in password or 'abc' in password:
        return 0
    else:
        return 10

def get_password_strength(score):
    ''' Convert password strength from number to literal '''
    if score < 4:
        return 'Weak'
    elif 4 <= score <= 6:
        return 'Medium'
    elif 6 < score <= 8:
        return 'Strong'
    else:
        return 'Very Strong'

def main():
    password = get_input() # Get user input
    length_score = get_length_score(password) 
    variation_score = get_variation_score(password)
    common_words_score = get_common_words_score(password)
    # Get the average of scores
    avg = (length_score + variation_score + common_words_score) / float(SCORES_NUM)
    print ("Score:",avg,"-",get_password_strength(avg))


if __name__== "__main__":
	main()
