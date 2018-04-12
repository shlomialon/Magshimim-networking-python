def show_hidden_word_wrong(word,letters):
	ans = ""
	index = 0
	while(index < len(word)):
		if index == len(word) - 1:
			if word[index] in letters:
				ans += word[index]
			else:
				ans += "_"
		elif word[index] in letters:
			ans += word[index] + " "
		else:
			ans += "_ "
		index = index + 1
	return ans

def show_hidden_word(word,letters):
	ans = ""
	index = 0
	while(index < len(word)):
		if word[index] in letters:
			ans += word[index] + " "
		else:
			ans += "_ "
		index = index + 1
	return ans[:-1]

def check_valid_input(letter,old_letter):
    return len(letter) == 1 and letter.isalpha() \
           and not letter.lower() in old_letter

def get_char_arr_wrong(words, letter):
    ans = ""
    for i in range(len(words)):
        if words[i] == letter:
            ans += words[i]
        else:
            ans += "_ "
    return ans

def get_char_arr(words,letter):
    ans = ""
    for char in words:
        if char == letter:
            ans += char
        else:
            ans += "_ "
    return ans

def main():
    print(show_hidden_word_wrong("Hey man!!", "eyn"))
    print(show_hidden_word("Hey man!!", "eyn!"))
    print(check_valid_input("d","affd"))
    print(get_char_arr_wrong("david","d"))
    print(get_char_arr("david","d"))

if __name__== "__main__":
    main()
