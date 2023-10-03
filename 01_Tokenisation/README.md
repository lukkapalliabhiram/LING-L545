# MaxMatch Tokenization and Evaluation

A step-by-step guide to implementing the MaxMatch tokenization algorithm, testing it, and evaluating its performance using Word Error Rate (WER).

## Prerequisites

- Python 3
- Git (for cloning the GitHub repository)
- Pip (for installing Python packages)

## Step 1: Fetching the Dataset

### Get the `.conllu` files from GitHub

```bash
git clone [GitHub Repository URL]
cd [Repository Directory]
```

## Step 2: Extracting a Dictionary of Surface Forms

### Extract Word Forms from UD Treebank

Use the following Unix command to extract the dictionary of surface forms from the `.conllu` file.

```bash
cat ja_gsd-ud-train.conllu | grep -v '^#' | awk -F'\t' '{print $2}' | sort | uniq > dictionary.txt
```
## Step 3: Implementing MaxMatch Algorithm

In this step, we will implement the MaxMatch algorithm in Python and then utilize it to tokenize the sentences.

### MaxMatch Algorithm Implementation

Save the Python code below as `maxmatch.py`. This script tokenizes an input sentence by iteratively finding the longest matching word in the dictionary, starting from the left side of the sentence.

```python
def maxmatch(sentence, dictionary):
    if not sentence:
        return []
    for i in range(len(sentence), 0, -1):
        first_word = sentence[:i]
        remainder = sentence[i:]
        if first_word in dictionary:
            return [first_word] + maxmatch(remainder, dictionary)
    return [sentence[0]] + maxmatch(sentence[1:], dictionary)

def main():
    import sys
    with open(sys.argv[1], 'r') as f:
        dictionary = set(f.read().splitlines())
    for line in sys.stdin:
        line = line.strip()
        tokens = maxmatch(line, dictionary)
        for token in tokens:
            print(token)

if __name__ == "__main__":
    main()
```
### Tokenization Testing
Use the following command to tokenize sentences and save the output.

```bash
cat ja_gsd-ud-test.conllu | grep -v '^#' | awk -F'\t' '{print $2}' | python3 maxmatch.py dictionary.txt > tokenized_output.txt
```

## Step-4

### Convert Tokenized Output to Sentences
Use the following Unix command to convert the tokenized output into sentences.

```bash
cat tokenized_output.txt | tr '\n' ' ' | sed 's/ \. /\
/g' > tokenized_sentences.txt
```

## Step-5
### Install jiwer Package

```bash
pip install jiwer
```

## WER Calculation Script
Save the following Python code as calculate_wer.py.

```python
import sys
from jiwer import wer

def calculate_wer(file1, file2):
    with open(file1, 'r', encoding='utf8') as ref_file, open(file2, 'r', encoding='utf8') as hyp_file:
        ref_sentences = ref_file.readlines()
        hyp_sentences = hyp_file.readlines()
    if len(ref_sentences) != len(hyp_sentences):
        print("Error: The files have a different number of lines.")
        sys.exit(1)
    for ref, hyp in zip(ref_sentences, hyp_sentences):
        error = wer(ref.strip(), hyp.strip())
        print(f"\nReference: {ref.strip()}\nHypothesis: {hyp.strip()}\nWER: {error:.2%}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py reference.txt hypothesis.txt")
        sys.exit(1)
    file1, file2 = sys.argv[1], sys.argv[2]
    calculate_wer(file1, file2)

if __name__ == "__main__":
    main()
```
### Run the WER Evaluation
Execute the following command to calculate and display the WER for each sentence.
```bash
python3 calculate_wer.py original_sentences.txt tokenized_sentences.txt
```
## Step 6: Performance Analysis

### Word Error Rates (WER) Analysis

The following WERs were observed for each sentence in the test file:

1. 9.71%
2. 0%
3. 10.42%
4. 0%
5. 19.64%
6. 0%
7. 0%
8. 14.95%
9. 18.68%
10. 23.33%
11. 19.05%
12. 16.96%

### Observations and Insights

- **Variable Performance:** The MaxMatch algorithm demonstrates a range of WERs across different sentences. Several sentences achieved a WER of 0%, indicating perfect matches, while others exhibited higher WER, up to 23.33%.
  
- **Average Performance:** The average WER, considering the provided rates, is approximately 12.22%.

- **Inconsistency:** The inconsistency in WERs suggests that while the algorithm performs well for certain sentences, it may struggle with others, likely due to the complexity or uncommon vocabulary.

## Step 7: Conclusion and Future Work

### Summary

- **Varying Success:** MaxMatch demonstrates varied success across different sentences, with perfect tokenization in some cases and notable errors in others.

- **Dependency on Dictionary:** Its performance is heavily reliant on the comprehensiveness and quality of the utilized dictionary.

### Future Considerations

- **Refinement:** Further refinement of the dictionary and exploration of alternative segmentation methods may enhance performance.

- **Handling Ambiguity:** Addressing linguistic ambiguities and employing a more context-aware approach might reduce mis-segmentations.

- **Utilizing Morphological Analysis:** Incorporating morphological analysis or machine learning models might enhance tokenization, especially for sentences with a higher WER.

### Final Note

While MaxMatch provides a straightforward and deterministic approach to tokenization, addressing its limitations and enhancing its capabilities will be pivotal for improving its application to diverse and complex texts in natural language processing tasks.

## Additional Resources

- [Universal Dependencies Documentation](https://universaldependencies.org/)
- [MaxMatch Algorithm Explanation](https://www.aclweb.org/anthology/Y17-1039.pdf)
- [Word Error Rate (WER) Explanation](https://en.wikipedia.org/wiki/Word_error_rate)

---

