import pandas as pd
import os
import segno

entrants = pd.read_csv("Scratch Paper/Entrants.csv").values.tolist()
print(entrants)

def giveTexString(entry, round, set, captain=False):
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
        \huge {{\color{{orange}} CAPTAIN}} \hspace{{0.1cm}} \huge \textbf{{{entry[0][0].upper()}. {entry[1].upper()}}} \\ 
        \LARGE Team {entry[3]} \\ Round {round} --- Set {set} \\ \includegraphics[width=1.5in]{{code.png}}
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

    \end{{document}}""" if captain else rf"""\documentclass{{report}}
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
        \huge \textbf{{{entry[0][0].upper()}. {entry[1].upper()}}} \\ 
        \LARGE Team {entry[3]} \\ Round {round} --- Set {set} \\ \includegraphics[width=1in]{{code.png}}
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

    \end{{document}}"""

for entry in entrants:
    round = 2
    set = 3
    directory = f"Scratch Paper/PAPERS/{entry[0]} {entry[1]}"
    os.makedirs(directory, exist_ok=True)
    file_path = f"{directory}/{entry[0]} {entry[1]}.tex"

    with open(file_path, "w") as f:
        f.write(giveTexString(entry, round, set, entry[2]))
        qr = segno.make_qr(f"{entry[0]} {entry[1]}\n{entry[3]}\n{entry[2]}\nRound {round}, Set {set}")
        qr.save(f"{directory}/code.png")
