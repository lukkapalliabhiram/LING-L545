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

- Remove VerbForm=Fin if the preceding token is "the":
```
REMOVE FINITE IF (-1 THE) ;
```

- Remove infinitive if there's no preposition or modal verb ("will", "would", "could"):
```
REMOVE INF IF (NOT -1 PREP OR MODAL);
```

- Remove past participle if there's no auxiliary verb in the third form ("was", "were", "have", "had", "has"):
```
REMOVE PP IF (NOT -1 AUX);
```


- Remove first person verb form if there's no first person pronoun:
```
REMOVE V + FP IF (NOT -1 FP);
```
