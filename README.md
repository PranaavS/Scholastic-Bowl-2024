# Scholastic Bowl 2024
This repository contains the documents and programs used to conduct the 2024 Scholastic Bowl.

## Questions
To view question sets, navigate to the folder titled `Round-X-Set-Y` (with "X" and "Y" replaced with round and set numbers of the document you are looking for.) Within the folder, click **only** on the file ending in `.pdf`. Other files are used to compile the `.pdf` and may not open natively on your system.

## Scratch Paper
To view contestant scratch paper for a given game, navigate to the folder titled `Round-X-Set-Y` (with "X" and "Y" replaced with round and set numbers of the game you are looking for.) Then, open the `Scratch Paper` folder and find the `.pdf` there.

## Software
Before using any software, it is important to install the required dependencies. To do so, first download the repository. Then, navigate to the download location and double click on the folder titled `Scholastic-Bowl-2024`. Then, double click on the path (displayed, by default, near the top of the file explorer) and replace the text with *cmd*. Press enter. A command line should open. There, paste the command `venv\Scripts\activate` and press enter. Then, in the same terminal, paste the command `pip3 install -r requirements.txt` and press enter. Wait until the command line says *Successfully installed...* You can now run any `.py` file within the repository.

### Scorekeeper
This repository includes scorekeeping software. To use it, download the repository, navigate to the `Scorekeeper` folder on a system with Python 3 installed, and run the file titled `counter.py`.

### Scratch Paper Generator
**Note: to view contestant scratch paper for a given game, navigate to the folder titled `Round-X-Set-Y` and find the `.pdf` there.** Competitors' scratch paper is scanned and saved within this repository. To organize this process, a program to generate scratch paper for each contestant (given a `.csv` containing contestant data) is included in this repository. To run it, navigate to the `Scratch Paper` folder and run the `generator.py` file. Then, the `PAPERS` folder (within the `Scratch Paper` folder) will be populated with the required scratch paper for each contestant.

## Other documents
The `rules` folder contains supplemental documents. The file `rules.tex` is **not** standalone---it is only used as an `\include` statement in the `.tex` files for question sets. The `Player Notes.tex` file (located within the `Player Notes` folder) **is** standalone.
The `Title Pages` folder contains the title pages for each question set. While these documents *are* standalone, they are only used in an `\includepdf` command within each set. All documents are of type `.pdf` and will likely open natively on your system.