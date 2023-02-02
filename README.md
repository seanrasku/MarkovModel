# MarkovModel

Small project modeling how a markov model works in Python, added a test file to aid running. For those who want to run, command is:

```
python3 fix_corrupted.py (kgram length of your choice) (message using "~" for noisy characters) < data/file.txt
```

```
python3 text_generator.py (kgram length of your choice) (Length of string to estimate) < data/file.txt
```

```
python3 markov_model.py (string to create markov model off of) (kgram length of your choice)
```

For last command, also input next characters you'd like frequency of, e.g. for string "markovmodel":
ma r
ar k
rk o
vm o
lm a
...
