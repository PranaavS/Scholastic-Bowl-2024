# Scholastic Bowl 2024
This repository contains the documents and programs used to conduct the 2024 Scholastic Bowl.

## Questions
To view question sets, navigate to the folder titled `Round-X-Set-Y` (with "X" and "Y" replaced with round and set numbers of the document you are looking for.) Within the folder, click **only** on the file ending in `.pdf`. Other files are used to compile the `.pdf` and may not open natively on your system.

## Software
This repository includes custom scorekeeping software. To use it, download the repository, navigate to the `Scorekeeper` folder on a system with Python 3 installed, and run the file titled `counter.py`. It is necessary to download the entire repository because the `counter.py` file is dependent on the included virtual environment `venv`. If the entire repository is downloaded, it is **not** necessary to download the pygame package because it is installed to the virtual environment.

## Other documents
The `rules` folder contains supplemental documents. The file `rules.tex` is **not** standalone---it is only used as an `\include` statement in the `.tex` files for question sets. The `Player Notes.tex` (located within the `Player Notes` folder) file **is** standalone.
The `Title Pages` folder contains the title pages for each question set. All documents are of type `.pdf` and will likely open natively on your system.
