from keras.preprocessing.sequence import pad_sequences

#define sequences
sequences = [
    [1,2,3,4],
    [1,2,3],
    [1]
]

# truncate sequence

truncated = pad_sequences(sequences, maxlen=2)
print(truncated)

#post truncated 
truncated1 = pad_sequences(sequences,maxlen=2,truncating='post')
print(truncated1)
