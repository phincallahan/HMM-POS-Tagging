import os, sys, string, pickle

def main():
    folder = sys.argv[1]

    sentences = []
    extend = sentences.extend
    for f in os.listdir(folder):
        data = open(folder+f).read().split('\n')
        extend(clean(data))
        print('Cleaned: '+f)

    o = open('clean_POS_data', 'wb')
    pickle.dump(sentences, o)

def clean(data):
    end_sentence = set(['.', '?', '!'])

    data = [x.split('\t') for x in data]
    sentences = [[],]
    s_append = sentences.append
    for line in data[1:]:
        if len(line) != 3 or line[2] == 'null':
            continue

        sentences[-1].append((line[0], line[-1]))
        if line[2] in end_sentence:
            s_append([])

    def incomplete(s):
        return '@' not in [x[0] for x in s]

    sentences = list(filter(incomplete, sentences))
    return sentences

if __name__=='__main__':
    main()
