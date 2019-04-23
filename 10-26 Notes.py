#Notes 10/26

def palindromeRecursive(word):

    if len (word)<1:
        return True

    else:
        if word [0] == word [-1]:
            return palindromeRecursive(word[1:-1]) #Slice

        else:
            return False
