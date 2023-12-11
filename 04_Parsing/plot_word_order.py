import sys
import matplotlib.pyplot as plt
import pyconll

# Directory where the treebanks are stored
inp1 = './ud-treebanks-v2.11/'

# Treebank file paths
file_names = {
    'ru': 'UD_Russian-GSD/ru_gsd-ud-train.conllu',
    'en': 'UD_English-EWT/en_ewt-ud-train.conllu',
    'es': 'UD_Spanish-GSD/es_gsd-ud-train.conllu',
    'fr': 'UD_French-GSD/fr_gsd-ud-train.conllu',
    'de': 'UD_German-GSD/de_gsd-ud-train.conllu',
    'it': 'UD_Italian-ISDT/it_isdt-ud-train.conllu',
    'pt': 'UD_Portuguese-GSD/pt_gsd-ud-train.conllu',
    'zh': 'UD_Chinese-GSD/zh_gsd-ud-train.conllu',
    'ja': 'UD_Japanese-GSD/ja_gsd-ud-train.conllu',
    'tr': 'UD_Turkish-IMST/tr_imst-ud-train.conllu',
    'ar': 'UD_Arabic-PADT/ar_padt-ud-train.conllu'
}

# Initialize proportions for OV and VO orders
x = [0] * len(file_names)  # proportion of OV
y = [0] * len(file_names)  # proportion of VO
labels = {i: lang for i, lang in enumerate(file_names.keys())}

def find_verb_object_pairs(sentence):
    """
    Find all verb-object pairs in the sentence.
    Returns a list of tuples (verb_index, object_index).
    """
    pairs = []
    for token in sentence:
        if token.upos == 'VERB':
            for child in token.children:
                if child.deprel == 'obj':
                    pairs.append((token.id, child.id))
    return pairs

for index, (lang, file_path) in enumerate(file_names.items()):
    file = inp1 + file_path
    train = pyconll.load_from_file(file)

    OV_counter = 0
    VO_counter = 0
    total_pairs = 0

    for sentence in train:
        pairs = find_verb_object_pairs(sentence)
        for verb_id, obj_id in pairs:
            if verb_id < obj_id:
                VO_counter += 1
            else:
                OV_counter += 1
            total_pairs += 1

    if total_pairs > 0:
        x[index] = OV_counter / total_pairs
        y[index] = VO_counter / total_pairs

# Plotting
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.xlabel('OV')
plt.ylabel('VO')
for i in labels:
    plt.text(x[i] - 0.03, y[i] - 0.03, labels[i], fontsize=9)
plt.savefig(sys.argv[1] if len(sys.argv) > 1 else 'word_order_plot.png')
plt.show()
