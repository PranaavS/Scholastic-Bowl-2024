import pandas as pd
import os
import segno
import shutil


def deleteContents(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    except Exception as e:
        print(f"Failed to list contents of {folder_path}. Reason: {e}")


entrants = pd.read_csv("Scratch Paper/Entrants.csv").values.tolist()
print(entrants)

def giveTexString(entry, round, set):
    set = ("Set " + str(set)) if round != max_round else "Finals"
    return rf"""\documentclass{{report}}
    \usepackage{{helvet}}
    \renewcommand{{\familydefault}}{{\sfdefault}}   
    \usepackage{{hyperref}}
    \usepackage{{graphicx}}
    \usepackage{{enumerate}}
    \usepackage{{enumitem}}
    \usepackage{{xcolor}}
    \usepackage{{import}}
    \usepackage{{pdfpages}}
    \usepackage{{microtype}}
    \usepackage[framemethod=TikZ]{{mdframed}}
    \usepackage[T1]{{fontenc}}
    \usepackage{{moresize}}
    \usepackage{{geometry}}
    \usepackage{{tikz}}

    \geometry{{
    left=0.2in,
    right=0.3in,
    bottom=0.2in,
    top=0.5in
    }}

    \setlength\parindent{{0pt}}
    \definecolor{{lightGray}}{{HTML}}{{d8dde6}}

    % Define a new style for the content box
    \newmdenv[
    topline=false,
    bottomline=false,
    leftline=false,
    rightline=false,
    linecolor=gray,
    outerlinewidth=1pt,
    roundcorner=0pt,
    innertopmargin=0pt,
    innerbottommargin=0pt,
    innerrightmargin=0pt,
    innerleftmargin=0pt,
    backgroundcolor=white
    ]{{contentbox}}

    \begin{{document}}
    \thispagestyle{{empty}}

    \begin{{flushright}}
        \huge {{\color{{orange}} CAPTAIN}} \hspace{{0.1cm}} \huge \textbf{{{entry[4]}}} \\ 
        \LARGE Team {entry[3]} \\ Round {round} --- {set} \\ \vspace*{{0.4cm}} \fbox{{\includegraphics[width=1.5in]{{code.png}}}} \hspace*{{0.1cm}} \\ \vspace*{{-0.45cm}} \small Do \textbf{{not}} write here. \hspace{{0.80cm}}.
    \end{{flushright}}

    \vspace*{{\fill}}
    \begin{{center}}
        This page may be used for scratch work. Do \textbf{{not}} write outside this box. This page will be scanned.
    \end{{center}}

    % Draw the box around the margins
    \begin{{tikzpicture}}[remember picture, overlay]
        \draw[black, line width=1pt]
            ([shift={{(0.2in,-0.4in)}}] current page.north west) --
            ([shift={{(-0.2in,-0.4in)}}] current page.north east) --
            ([shift={{(-0.2in,0.4in)}}] current page.south east) --
            ([shift={{(0.2in,0.4in)}}] current page.south west) -- cycle;
    \end{{tikzpicture}}

    \newpage

    \thispagestyle{{empty}}

    \begin{{flushright}}
        \vspace*{{-0.2cm}} \fbox{{\includegraphics[width=1.5in]{{code.png}}}} \hspace*{{0.1cm}} \\ \vspace*{{-0.45cm}} \small Do \textbf{{not}} write here. \hspace{{0.80cm}}.
    \end{{flushright}}

    \vspace*{{\fill}}
    \begin{{center}}
        This page may be used for scratch work. Do \textbf{{not}} write outside this box. This page will be scanned.
    \end{{center}}

    % Draw the next box around the margins
    \begin{{tikzpicture}}[remember picture, overlay]
        \draw[black, line width=1pt]
            ([shift={{(0.2in,-0.4in)}}] current page.north west) --
            ([shift={{(-0.2in,-0.4in)}}] current page.north east) --
            ([shift={{(-0.2in,0.4in)}}] current page.south east) --
            ([shift={{(0.2in,0.4in)}}] current page.south west) -- cycle;
    \end{{tikzpicture}}

    \end{{document}}""" if entry[2] else rf"""\documentclass{{report}}
    \usepackage{{helvet}}
    \renewcommand{{\familydefault}}{{\sfdefault}}
    \usepackage{{hyperref}}
    \usepackage{{graphicx}}
    \usepackage{{enumerate}}
    \usepackage{{enumitem}}
    \usepackage{{xcolor}}
    \usepackage{{import}}
    \usepackage{{pdfpages}}
    \usepackage{{microtype}}
    \usepackage[framemethod=TikZ]{{mdframed}}
    \usepackage[T1]{{fontenc}}
    \usepackage{{moresize}}
    \usepackage{{geometry}}
    \usepackage{{tikz}}

    \geometry{{
    left=0.2in,
    right=0.3in,
    bottom=0.2in,
    top=0.5in
    }}

    \setlength\parindent{{0pt}}
    \definecolor{{lightGray}}{{HTML}}{{d8dde6}}

    % Define a new style for the content box
    \newmdenv[
    topline=false,
    bottomline=false,
    leftline=false,
    rightline=false,
    linecolor=gray,
    outerlinewidth=1pt,
    roundcorner=0pt,
    innertopmargin=0pt,
    innerbottommargin=0pt,
    innerrightmargin=0pt,
    innerleftmargin=0pt,
    backgroundcolor=white
    ]{{contentbox}}

    \begin{{document}}
    \thispagestyle{{empty}}

    \begin{{flushright}}
        \huge \textbf{{{entry[4]}}} \\ 
        \LARGE Team {entry[3]} \\ Round {round} --- {set} \\ \vspace*{{0.4cm}} \fbox{{\includegraphics[width=1.5in]{{code.png}}}} \hspace*{{0.1cm}} \\ \vspace*{{-0.45cm}} \small Do \textbf{{not}} write here. \hspace{{0.80cm}}.
    \end{{flushright}}

    \vspace*{{\fill}}
    \begin{{center}}
        This page may be used for scratch work. Do \textbf{{not}} write outside this box. This page will be scanned.
    \end{{center}}

    % Draw the box around the margins
    \begin{{tikzpicture}}[remember picture, overlay]
        \draw[black, line width=1pt]
            ([shift={{(0.2in,-0.4in)}}] current page.north west) --
            ([shift={{(-0.2in,-0.4in)}}] current page.north east) --
            ([shift={{(-0.2in,0.4in)}}] current page.south east) --
            ([shift={{(0.2in,0.4in)}}] current page.south west) -- cycle;
    \end{{tikzpicture}}

    \newpage

    \thispagestyle{{empty}}

    \begin{{flushright}}
        \vspace*{{-0.2cm}} \fbox{{\includegraphics[width=1.5in]{{code.png}}}} \hspace*{{0.1cm}} \\ \vspace*{{-0.45cm}} \small Do \textbf{{not}} write here. \hspace{{0.80cm}}.
    \end{{flushright}}

    \vspace*{{\fill}}
    \begin{{center}}
        This page may be used for scratch work. Do \textbf{{not}} write outside this box. This page will be scanned.
    \end{{center}}

    % Draw the next box around the margins
    \begin{{tikzpicture}}[remember picture, overlay]
        \draw[black, line width=1pt]
            ([shift={{(0.2in,-0.4in)}}] current page.north west) --
            ([shift={{(-0.2in,-0.4in)}}] current page.north east) --
            ([shift={{(-0.2in,0.4in)}}] current page.south east) --
            ([shift={{(0.2in,0.4in)}}] current page.south west) -- cycle;
    \end{{tikzpicture}}

    \end{{document}}"""

deleteContents("Scratch Paper/PAPERS")

# group people by last name
last_name_dict = {}
first_names = [entry[0].capitalize() for entry in entrants]
last_names = [entry[1].upper() for entry in entrants]

for last_name in last_names:
    last_name_dict[last_name] = []

for i in range(len(last_names)):
    last_name_dict[last_names[i]].append(first_names[i])

print(last_name_dict)

def containsDuplicates(list):
    return len(list) > len(set(list)) # number of elements is greater than number of unique elements


char_limit = 15
def generateInitials(first_names): # gives first initial(s) for a list of first names
    j = 1
    initials = [first_name[0] for first_name in first_names]
    while (containsDuplicates(initials) and j < char_limit):
        initials_copy = initials[:]
        for i in range(len(initials)):
            initials_copy.pop(i)
            if initials[i] in initials_copy:
                try:
                    initials[i] += first_names[i][j]
                except:
                    pass
            initials_copy = [first_name[:j] for first_name in first_names]
        j += 1
    return initials


print(generateInitials(last_name_dict["DOE"]))
for last_name in last_name_dict:
    last_name_dict[last_name] = generateInitials(last_name_dict[last_name])

print(last_name_dict)

entrants_abbrev = []
for last_name, first_names in last_name_dict.items():
    for first_name in first_names:
        entrants_abbrev.append(f"{first_name}. {last_name}")

entrants.sort(key=lambda x: x[0])
entrants_abbrev.sort()

for i in range(len(entrants)):
    entrants[i].append(entrants_abbrev[i])

max_round = 3
for i in range(max_round): # round
    for j in range(int(2**max_round / 2**(i + 1))): # set
        for entry in entrants:

            if entry[2] not in ('TRUE', 'FALSE', True, False):
                raise TypeError(f"Captain field for entry {entry[0]} {entry[1]} is neither TRUE nor FALSE")

            round = i + 1
            set = j + 1
            set_text = ("Set " + str(set)) if round != max_round else "Finals"
            directory = f"Scratch Paper/PAPERS/Round {round}, {set_text}/{entry[0].upper()} {entry[1].upper()}"
            os.makedirs(directory, exist_ok=True)
            file_path = f"{directory}/{entry[0]} {entry[1]}.tex"

            with open(file_path, "w") as f:
                f.write(giveTexString(entry, round, set))
                formatted_set_text = ("Set-" + str(set)) if round != max_round else "Finals"
                qr = segno.make_qr(f"{entry[0]} {entry[1]}\n{entry[3]}\n{entry[2]}\nRound-{round}-{formatted_set_text}")
                qr.save(f"{directory}/code.png")

print("Finished.")
