#!/bin/bash

echo "Installing python dependencies"

sudo pip install numpy
sudo pip install scipy
sudo pip install pydub
sudo pip install sklearn
sudo pip install liac-arff
sudo apt-get install ffmpeg


rootdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
rootdir=$rootdir"/"
perldir=$rootdir"openEAR-0.1.0/scripts/modeltrain/"
traindir=$rootdir"training_dataset/"
trainarff=$rootdir"myfeatures_988_train.arff"
testarff=$rootdir"myfeatures_988_test.arff"

python convert.py

cd $perldir
echo $trainarff
echo $traindir

perl stddirectory_smileextract.pl $traindir emobase.conf $trainarff

perl stddirectory_smileextract.pl $rootdir emobase.conf $testarff

cd $rootdir

sudo python final2.py












