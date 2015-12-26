import os, sys, string, pickle

def main():
    folder = sys.argv[1]
    output_folder = sys.argv[2]


    for f in os.listdir(folder):
        print('Completed: '+f)
        clean(folder,f,output_folder)

def clean(folder, f, output_folder):
    end_sentence = set(['.', '?', '!'])

    data = open(folder+'/'+f).read().split('\n')
    data = [x.split('\t') for x in data]
    sentences = [[],]
    s_append = sentences.append
    for line in data[1:]:
        if len(line) != 3 or line[2] == 'null':
            continue

        sentences[-1].append([line[0], line[-1]])
        if line[2] in end_sentence:
            s_append([])

    def incomplete(s):
        return '@' not in [x[0] for x in s]


    sentences = list(filter(incomplete, sentences))
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    o = open(output_folder+'/clean_'+f, 'wb')
    pickle.dump(sentences, o)

if __name__=='__main__':
    main()
