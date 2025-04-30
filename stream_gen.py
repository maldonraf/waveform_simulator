import numpy as np

def stream_gen(length=None, levels=2, seed=None):
    if seed != None:
        np.random.seed(seed)

    stream = np.random.randint(0, high=levels, size=length)
    
    return stream

if __name__ == '__main__':
    length = 10
    levels = 4
    print(f"Length: {length} | Levels: {levels} | {stream_gen(length=length, levels=levels)}")