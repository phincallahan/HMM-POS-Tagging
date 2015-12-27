import sys,pickle, numpy as np

def count(data, vocab_size, state_size):
    A = np.zeros((state_size, state_size))
    B = np.zeros((vocab_size, state_size))
    pi = np.zeros(state_size)

    for row in data:
        pi[row[1][0]] += 1
        A[row[1][1:], row[1][:-1]] += 1
        B[row[0], row[1]] += 1

    sumA = np.sum(A, axis = 0)
    A[:,np.where(sumA == 0)[0]] += 1

    sumB = np.sum(B, axis = 0)
    B[:,np.where(sumB == 0)[0]] += 1

    A  /= np.sum(A, axis = 0)
    B  /= np.sum(B, axis = 0)
    pi /= np.sum(pi)

    return A,B,pi

def learn(data, vocab_size, state_size):
    return [],[]

def main():
    mode = sys.argv[1]
    text = pickle.load(open(sys.argv[1], 'rb'))
    print(len(text))

    print('Preparing Data...')

    if mode == '-l':
        A,B = learn(text)
    elif mode == '-c':
        A,B = count(text)
    else:
        print("INVALID MODE")

if __name__=='__main__':
    main()
