# segmenter.py
import sys

def segment_paragraphs(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        paragraphs = f.readlines()
        for paragraph in paragraphs:
            sentences = paragraph.split('.')
            for sentence in sentences:
                if sentence.strip():  # Ensure sentence is not just whitespace
                    print(sentence.strip())

if __name__ == "__main__":
    segment_paragraphs(sys.argv[1])
