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
