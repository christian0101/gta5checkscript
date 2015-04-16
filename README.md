# gta5checkscript
A Python script that will check all files in a GTA V PC install to verify hashes and output file status of OK, CORRUPT, or Unknown.

# Execution

Place the `checkGta.py` file in the directory above your GTA V install.

For example, if you have it installed in

`C:\Program Files\Rockstar Games\Grand Theft Auto V\`

then you need to run the script from

`C:\Program Files\Rockstar Games\`

Execute using command prompt and Python. No dependencies required. Developed against Python 2.7.9.

# What to do with corrupt files

Rename the file so that the launcher downloads the file again. You must ensure that the download process does not get interrupted so that the launcher will properly verify the file when it's compelted the download. If the file fails verification, the launcher should repeat the process until the file is valid.

Once all files are downloaded, run the script once more to verify the results. The launcher does not verify files on launch, it only checks that a file exists.

# What to do with unknown files

Tell me about them. The script should handle all files in the directory by either hashing them or ignoring them. If a game file is being reported as an unknown, give me the full path to the file so that I can work with it.
