# Constraint Grammar
## Steps:

1. Clone the scripts repository:
```
$ git clone https://github.com/ftyers/ud-scripts.git
```

2. Clone a UD corpus:
```
$ git clone https://github.com/UniversalDependencies/UD_English-GUM
```

3. Make the morphological analyser:
```
$ cat UD_English-GUM/*.conllu | python3 ud-scripts/conllu-analyser.py -t eng-analyser.tsv
```


4. Analyse new sentences:
```
$ echo "At the start of the century, the majority of English people worked in the countryside economy." | python3 ud-scripts/conllu-analyser eng-analyser.tsv
```


## Output:
```
"<At>"
        "at" ADP
        "at" ADV
"<the>"
        "the" DET Definite=Def PronType=Art
        "the" DET Definite=Def PronType=Art Typo=Yes
        "to" PART Typo=Yes
        "_" X
"<start>"
        "start" VERB VerbForm=Inf
        "start" NOUN Number=Sing
        "start" VERB Mood=Ind Number=Plur Person=1 Tense=Pres VerbForm=Fin
        "start" VERB Mood=Ind Number=Plur Person=3 Tense=Pres VerbForm=Fin
        "start" VERB Mood=Ind Number=Sing Person=2 Tense=Pres VerbForm=Fin
        "start" VERB Mood=Imp Person=2 VerbForm=Fin
"<of>"
        "of" ADP
        "of" SCONJ
        "of" ADV
        "of" ADP Typo=Yes
"<the>"
        "the" DET Definite=Def PronType=Art
        "the" DET Definite=Def PronType=Art Typo=Yes
        "to" PART Typo=Yes
        "_" X
"<century>"
        "century" NOUN Number=Sing
"<,>"
        "," PUNCT
        "," PUNCT Foreign=Yes
        "." PUNCT

"<the>"
        "the" DET Definite=Def PronType=Art
        "the" DET Definite=Def PronType=Art Typo=Yes
        "to" PART Typo=Yes
        "_" X
"<majority>"
        "majority" NOUN Number=Sing
"<of>"
        "of" ADP
        "of" SCONJ
        "of" ADV
        "of" ADP Typo=Yes
"<English>"
        "English" PROPN Number=Sing
        "English" ADJ Degree=Pos
        "English" ADJ Degree=Pos Number=Sing
"<people>"
        "person" NOUN Number=Plur
        "people" NOUN Number=Sing
"<worked>"
        "work" VERB Mood=Ind Number=Sing Person=3 Tense=Past VerbForm=Fin
        "work" VERB Mood=Ind Number=Plur Person=3 Tense=Past VerbForm=Fin
        "work" VERB Tense=Past VerbForm=Part
        "work" VERB Mood=Ind Number=Sing Person=1 Tense=Past VerbForm=Fin
"<in>"
        "in" SCONJ
        "in" ADP
        "in" ADV
        "in" ADV Degree=Pos
        "in" X
        "in" ADP Typo=Yes
"<the>"
        "the" DET Definite=Def PronType=Art SELECT:27
        "the" DET Definite=Def PronType=Art Typo=Yes SELECT:27
;       "to" PART Typo=Yes SELECT:27
;       "_" X SELECT:27
"<countryside>"
        "countryside" NOUN Number=Sing
"<economy>"
        "economy" NOUN Number=Sing
"<.>"
        "." PUNCT
        "." PUNCT Typo=Yes
```

## Rules:

- Rule 1: Remove finite verbs if preceded by 'the'.
```
REMOVE FINITE IF (-1C DET);
```

- Rule 2: Remove adpositions if not followed by a determiner or noun.
```
REMOVE ADP IF (NOT 1C DET) (NOT 1C NOUN);
```

- Rule 3: Remove 'English' as a proper noun if followed by 'people'.
```
REMOVE PROPN IF (1C COMMON_NOUN);
```

- Rule 4: Remove past tense verbs if they do not follow a noun or pronoun.
```
REMOVE VERB_PAST IF (NOT -1C NOUN) (NOT -1C PRON);
```
- Rule 5: Select 'the' as a determiner if followed by a common noun.
```
SELECT DET IF (1C COMMON_NOUN);
```
