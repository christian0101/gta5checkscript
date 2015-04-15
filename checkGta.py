import hashlib
import os

gtaDirectory = 'Grand Theft Auto V'

hashList = {}
with open('hashes.txt', 'r') as hashFile:
  lineType = 0
  fileName = ''
  for line in hashFile:
    newLineIndex = line.find('\n')
    if lineType == 0:
      if newLineIndex > -1:
        fileName = os.path.join(gtaDirectory, line[:newLineIndex])
      else:
        fileName = os.path.join(gtaDirectory, line)
      lineType += 1
      print fileName
    elif lineType == 1:
      # Skip this line
      lineType += 1
    elif lineType == 2:
      fileHash = -1
      if newLineIndex > -1:
        fileHash = line[:newLineIndex]
      else:
        fileHash = line
      hashList[fileName] = fileHash
      lineType = 0

okayFiles = 0
badFiles = 0
unknownFiles = 0

for dirpath, dirnames, filenames in os.walk(gtaDirectory):
  for filename in filenames:
    gtaFile = os.path.join(dirpath, filename)

    if gtaFile in hashList:
      # Hash this file
      BLOCKSIZE = 65536
      hasher = hashlib.new('sha256')
      with open(gtaFile, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
          hasher.update(buf)
          buf = afile.read(BLOCKSIZE)
      gtaHash = hasher.hexdigest()
      #print('%s %s' % (gtaFile, gtaHash))

      # Pull the hash for this file
      if gtaFile in hashList:
        fileHash = hashList[gtaFile]
        if fileHash == gtaHash:
          print '%s OK!' % gtaFile
          okayFiles += 1
        else:
          print '%s CORRUPT!' % gtaFile
          print 'Expected \'%s\' but found \'%s\'' % (fileHash, gtaHash)
          badFiles += 1
    else:
      print 'Unknown file: %s' % gtaFile
      unknownFiles += 1

print '%s files OK, %s files CORRUPT, %s files unknown' % (okayFiles, badFiles, unknownFiles)
