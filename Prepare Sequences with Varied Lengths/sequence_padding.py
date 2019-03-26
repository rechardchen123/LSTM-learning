from keras.preprocessing.sequence import pad_sequences
#define sequence 
sequences = [
    [1,2,3,4],
    [1,2,3],
    [1]
]

#pad sequence
padded = pad_sequences(sequences)
print(padded)

#post padding 
padded1 = pad_sequences(sequences,padding='post')
print(padded1)
