def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    file1 = open(source)
    file2 = open(dest,'w')
    for line in file1:
        newline = line.replace(pattern or pattern2, replace)
        file2.write(newline)
    file1.close()
    file2.close()



pattern = 'Hey Jude'
pattern = 'hey Jude'
replace = 'Hey Donald'
source = 'sed_tester.txt'
dest = 'output.txt'
sed(pattern, replace, source, dest)