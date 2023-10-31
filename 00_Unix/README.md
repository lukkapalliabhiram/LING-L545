## Exercises with `grep`

#### 1. How many uppercase words are there in the Aragonese Wikipedia? Lowercase?
**Answer:** No upper and lower in Telugu.

#### 2. How many 4-letter words?
```bash
grep -o -w '\\w\\{4\\}' wiki.words | wc -l
```

#### 3. Are there any words with no vowels?
```bash
grep -E '^[^అఆఇఈఉఊఋౠఎఏఐఒఓఔ]+$' wiki.words
```

#### 4. Find '1-syllable' words (words with exactly one vowel)
```bash
grep -E '^[^అఆఇఈఉఊఋౠఎఏఐఒఓఔ]*[అఆఇఈఉఊఋౠఎఏఐఒఓఔ][^అఆఇఈఉఊఋౠఎఏఐఒఓఔ]*$' wiki.words
```
#### 5. Find '2-syllable' words (words with exactly two vowels)
```bash
grep -o -w '[^అఆఇఈఉఊఋౠఎఏఐఒఓఔ]*[అఆఇఈఉఊఋౠఎఏఐఒఓఔ][^అఆఇఈఉఊఋౠఎఏఐఒఓఔ]*[అఆఇఈఉఊఋౠఎఏఐఒఓఔ][^అఆఇఈఉఊఋౠఎఏఐఒఓఔ]*' wiki.words
```

## Exercises with `sed`

#### 1. Count word initial consonant sequences
Tokenize by word, delete the vowel and the rest of the word, and count.
```bash
sed '/^[అఆఇఈఉఊఋౠఎఏఐఒఓఔ]/d' wiki.words | # Remove words starting with a vowel using sed
sed 's/[అఆఇఈఉఊఋౠఎఏఐఒఓఔ].*//' | # Remove the vowel and everything after it
sort | uniq -c | sort -nr > initial-consonants.hist
```

#### 2. Count word final consonant sequences
```bash
sed '/[అఆఇఈఉఊఋౠఎఏఐఒఓఔ]$/d' wiki.words | # Remove words ending with a vowel using sed
sed 's/.*[అఆఇఈఉఊఋౠఎఏఐఒఓఔ]//' | # Remove everything up to and including the last vowel
sort | uniq -c | sort -nr > final-consonants.hist
```
