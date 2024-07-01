# Scholastic Bowl 2024
This repository contains the documents and programs used to conduct the 2024 Scholastic Bowl.

## Questions
To view question sets, navigate to the folder titled `Round-X-Set-Y` (with "X" and "Y" replaced with round and set numbers of the document you are looking for.) Within the folder, click **only** on the file ending in `.pdf`. Other files are used to compile the `.pdf` and may not open natively on your system.

## Software
This repository includes scorekeeping software. To use it, download the repository, navigate to the `Scorekeeper` folder on a system with Python 3 installed, and run the file titled `counter.py`. It is necessary to download the entire repository because the `counter.py` file is dependent on the included virtual environment `venv`. If the entire repository is downloaded, it is **not** necessary to download *pygame* because it is installed to the virtual environment.

## Other documents
The `rules` folder contains supplemental documents. The file `rules.tex` is **not** standalone---it is only used as an `\include` statement in the `.tex` files for question sets. The `Player Notes.tex` file (located within the `Player Notes` folder) **is** standalone.
The `Title Pages` folder contains the title pages for each question set. While these documents *are* standalone, they are only used in an `\includepdf` command within each set. All documents are of type `.pdf` and will likely open natively on your system.

## File structure
    Scholastic-Bowl-2024:
    |   README.md
    |
    +---Round-1-Set-1
    |       Scholastic Bowl Round 1 Set 1 Questions.aux
    |       Scholastic Bowl Round 1 Set 1 Questions.fdb_latexmk
    |       Scholastic Bowl Round 1 Set 1 Questions.fls
    |       Scholastic Bowl Round 1 Set 1 Questions.log
    |       Scholastic Bowl Round 1 Set 1 Questions.out
    |       Scholastic Bowl Round 1 Set 1 Questions.pdf
    |       Scholastic Bowl Round 1 Set 1 Questions.synctex.gz
    |       Scholastic Bowl Round 1 Set 1 Questions.tex
    |
    +---Round-1-Set-2
    |       Scholastic Bowl Round 1 Set 2 Questions.aux
    |       Scholastic Bowl Round 1 Set 2 Questions.fdb_latexmk
    |       Scholastic Bowl Round 1 Set 2 Questions.fls
    |       Scholastic Bowl Round 1 Set 2 Questions.log
    |       Scholastic Bowl Round 1 Set 2 Questions.out
    |       Scholastic Bowl Round 1 Set 2 Questions.pdf
    |       Scholastic Bowl Round 1 Set 2 Questions.synctex.gz
    |       Scholastic Bowl Round 1 Set 2 Questions.tex
    |
    +---Rules
    |   |   Rules.aux
    |   |   Rules.tex
    |   |
    |   \---Player Notes
    |           Player Notes.aux
    |           Player Notes.fdb_latexmk
    |           Player Notes.fls
    |           Player Notes.log
    |           Player Notes.out
    |           Player Notes.pdf
    |           Player Notes.synctex.gz
    |           Player Notes.tex
    |
    +---Scorekeeper
    |       buzz.mp3
    |       counter.py
    |
    +---Title Pages
    |       Round 1 Set 1 Title Page.pdf
    |       Round 1 Set 2 Title Page.pdf
