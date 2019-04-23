def stringCount(filename, item):
    infile = open (filename, 'r')
    content = infile.read()
    infile.close()
    cnt = content.count(item)
    return cnt
