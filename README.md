# feeling-feelings

###Sentiment Analysis

The Input File will have a list of audio files like:
 - a.mp3
 - b.mp3
 - c.mp3
 - d.mp3... and So on.

The program would output the emotion detected for each file (a.mp3, b.mp3 etc) in separate lines:

happy
unhappy
neutral
neutral

The above output means one.mp3 was a "happy" conversation, two.mp3 was a "unhappy" conversation etc.

###File descriptions:

  run.sh - Main bash script to be run for carrying out voice emotion recognition 
  
  important.sh - Installs all the required dependencies, calculates all the features using openEar library     
  
  convert.py - Converts all .mp3 files to .wav files for further processing 
  
  final2.py - Generates SVC models, trains it and then finally predicts the emotions from the testing

###To include in the directory:

  1. openEar library from here http://sourceforge.net/projects/openart/
  2. Training datasets (Four classes used - Happy, Unhappy, Angry, Neutral)
  3. Files to be recognised for emotions (in mp3 format)

