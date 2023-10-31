import sys
from jiwer import wer

def calculate_wer(file1, file2):
    with open(file1, 'r', encoding='utf8') as ref_file, open(file2, 'r', encoding='utf8') as hyp_file:
        ref_sentences = ref_file.readlines()
        hyp_sentences = hyp_file.readlines()

    # Check if both files have the same number of lines
    if len(ref_sentences) != len(hyp_sentences):
        print("Error: The files have a different number of lines.")
        sys.exit(1)

    # Calculate and print WER for each sentence pair
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
