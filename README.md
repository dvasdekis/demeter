# learning_age

Learning Async with aiopg and encryption with age

Let's collect some thoughts:

Use case: Point at a directory and get a link, who can decrypt with their private key, or the one packaged with the program

Big problem: I've got all this stuff sitting on the drive. As 7zip creates encrypted xz files, I need to As XZ

This needs:

## Server-side:
* GUI to point at a directory (start with cmdline path)
    - Inputs: Folder path
    - Action: Generate RNG string to encrypt archive with
    - Outputs: Compress function [compress_folder(data_path, output_archive, archive_pw)]
* Compress & Encrypt with RNG string to give us symmetric key [compress_folder(data_path, output_archive, archive_pw)]
    - Inputs: Invoked from main
    - Actions: Invoke 7z to encrypt, compress as xz
    - Outputs: xz archive on file system
* Par2 using @animetosho/parpar [generate_pars(output_archive)]
    - Inputs: output_archive
    - Actions: Par2 archive generation
    - Outputs: par2 archives on file system
* Upload datafiles with nyuu  [compress_folder()]
    - Inputs: List of 
    - Actions: 
    - Outputs: 
* Create  [compress_folder()]
    - Inputs: 
    - Actions: 
    - Outputs: 
* Delta lake to write sets/keys sets to queue
* Delta lake compressed with 7zip
* Delta lake encrypted with age
* Compress and encrypt and split into sets with 7zip

* Write out NZBs
* Post with nyuu
* Update Delta lake on Dat repo
* Report secret string for NZB creation

Future enhancements:
* Stream existing content from disk into archive files -> par2 -> uploader (avoids need to hold temp space)
* Run base file upload and par2 at the same time
* split to 20GB archives on 200GB+ archive size (20GB is rough max limit of what we can post before par2 needs more than 1 article per chunk at 768KB article size)
    - Run a second par2 pass over the 200GB+ archive (doing another par2 step) as we have hit the limit of piece size



## Client-side:
1. Accept secret string
2. Generate NZB
3. Download with other tools
