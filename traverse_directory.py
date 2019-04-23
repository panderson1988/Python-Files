import os

def check( name, word ):
    'check whether word occurs in file name'
    try:
        infile = open( name, 'r' )
        s = infile.read()
        infile.close()
        return ( word in s )

    except: #if file cannot be opened, or file format cannot be read
        return False


def scan( pathname, word ): # test with pathname = 'test', word = 'nevermore', 'hustle'
    'scan folders within pathname recursively, looking for word'
    print( 'Scanning: {}'.format( pathname ) )

    for name in os.listdir( pathname ):
        subname = os.path.join( pathname, name )

        if os.path.isfile( subname ):
            if check( subname, word ):
                print('Found in {}.'.format( subname ) )
                
        elif os.path.isdir( subname ):
            scan( subname, word )


def removePunctuation( s ):
    'remove punctuation from s'
    p = '!-_,.:;!?"`\''
    
    for symbol in p:
        #note that strings are immutable, so we need to reassign replace result
        s = s.replace(symbol, ' ')

    return s



def countWord( fname, findWord ):
    '''
    check number of times findWord occurs in file: fname
    if file cannot be opened or file format cannot be read, return -1
    '''

    word_cnt = { findWord:0 }
    
    try:
        infile = open( fname, 'r' )
        content = infile.read()
        infile.close()

        content = removePunctuation( content )
        words = content.split()
        for word in words:
            if word.lower() in word_cnt:
                word_cnt[ findWord ] += 1
        
        return word_cnt[ findWord ]

    except Exception as e: #if file cannot be opened, or file format cannot be read
        print( e )
        return -1


def scanCount( pathname, word ): # test with pathname = 'test', word = 'tapping', 'evil', 'coat'
    'scan folders within pathname recursively, looking for word'

    print( 'Scanning: {}'.format( pathname ) )

    for name in os.listdir( pathname ):
        subname = os.path.join( pathname, name )

        if os.path.isfile( subname ):
            cnt = countWord( subname, word )
            print('Found {0} occurrences of {1} in {2}.'.format( cnt, word, subname ) )
                
        elif os.path.isdir( subname ):
            scanCount( subname, word )
            

def count( pathname ):
    'count number of files in pathname'

    print('Scanning: {}'.format( pathname ) )
    cnt = 0
    for name in os.listdir( pathname ):
        subname = os.path.join( pathname, name )

        if os.path.isfile( subname ):
            cnt += 1
            print('cnt', cnt)
            
        elif os.path.isdir( subname ):
            cnt += count( subname )
            print('cnt', cnt)
       
    return cnt


def traverseDir( pathname ): # test with pathname = 'test'
    'print the pathname of every file and subfoler contained in pathname'
    for item in os.listdir( pathname ):
        fullpath = os.path.join( pathname, item )
        print( fullpath )

        if os.path.isfile( fullpath ): # base case
            pass
        
        else:
            traverseDir( fullpath ) # recursive step



def search( pathname, filename ): # test with pathname = 'test', 'fileD.txt'
    '''
    searches pathname and all subfolders for filename.
    prints full path and name of file if found, else None is returned
    '''

    #print('Scanning: {}'.format( pathname ) )
    for item in os.listdir( pathname ):
        fullpath = os.path.join( pathname, item )

        if os.path.isdir( fullpath ):
            search( fullpath, filename )

        if filename in fullpath:
            print( '{0} found in {1}'.format( item, pathname ) )

 


        
