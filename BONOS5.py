contents = ['a', 'b', 'c']

fileNames = ['d.txt','e.txt','f.txt']

for content, fileName in zip(contents, fileNames):
    file = open(f"files/{fileName}", 'w')
    file.write(content)
    file.close()