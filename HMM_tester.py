import sys, pickle, itertools, random, numpy as np, HMM
from viterbi import viterbi

def main():
    mode = sys.argv[1]
    test = float(sys.argv[2])
    data = pickle.load(open(sys.argv[3], 'rb'))

    if mode == '-c':
        train_method = HMM.count
    elif mode == '-l':
        train_method = HMM.learn
    else:
        print("INVALID MODE")

    print("Data preprocessing...")
    test_i = random.sample(range(len(data)), int(test*len(data)))

    states = list(set(list(itertools.chain(*data))[1::2]))

    random.shuffle(data)
    train = data[int(len(data)*test):]
    test  = data[:int(len(data)*test)]

    vocab = list(set(list(itertools.chain(*train))[0::2]))

    state_map = {state:i for i,state in enumerate(states)}
    vocab_map = {word:i for i,word in enumerate(vocab)}

    for i,sentence in enumerate(train):
        words_i = [vocab_map[x] for x in sentence[0::2]]
        states_i =[state_map[x] for x in sentence[1::2]]
        train[i] = [words_i, states_i]

    print("Training HMM...")
    A,B,pi = train_method(train, len(vocab), len(states))

    correct = 0
    total = 0

    for sentence in test:
        words =  sentence[0::2]
        states = sentence[1::2]

        for i,word in enumerate(words):
            if word in vocab_map:
                words[i] = vocab_map[word]
            else:
                words[i] = '<UNK>'

        p_states = viterbi(A,B,pi,words)
        total += len(states)
        for i in range(len(states)):
            if states[i] == p_states[i]:
                correct += 1

    print('Accuracy: '+str(correct/total))

if __name__=='__main__':
    main()
