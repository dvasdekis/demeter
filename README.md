# learning_age

Learning Async with aiopg and encryption with age

Let's collect some thoughts:

Use case: Point at a directory and get a link to send to friends, who can decrypt with their private key, or the one packaged with the program

This needs:

Server-side:
* GUI to point at a directory (start with cmdline)
- Inputs: Folder path
- Outputs: Scan task to 
* Scan & Encrypter to predict how many files/Usenet sets, and give us keys
* Delta lake to write sets/keys sets to queue
* Delta lake compressed with 7zip
* Delta lake encrypted with age
* Compress and encrypt and split into sets with 7zip
* Par2 using @animetosho/parpar
* Write out NZBs
* Post with nyuu
* Update Delta lake on Dat repo
* Report secret string for NZB creation


Client-side:
1. Accept secret string
2. Generate NZB
3. Download with other tools