# get root permission in terminal by sudo su
# sudo su
# pip install matplotlib
# pip install pydub
# pip install python-praat-scripts
# apt-get install ffmpeg
# apt-get install praat
# run this python file 
# get pitch  (actually any script you want)


from pydub import AudioSegment
import glob
import os

rootdir = os.getcwd() + '/'
trainpath = rootdir + 'training_dataset/'
# define important directories here
print rootdir
print trainpath

# obtain list of training dataset files
angrylist = glob.glob(trainpath+'angry/*.mp3')
unhappylist = glob.glob(trainpath+'unhappy/*.mp3')
neutrallist = glob.glob(trainpath+'neutral/*.mp3')
happylist = glob.glob(trainpath+'happy/*.mp3')
mp3list = glob.glob(rootdir+'*.mp3')

print mp3list
print happylist

# read data
for filename in angrylist:
	# import file
	sound = AudioSegment.from_mp3(filename)
	print('imported' + filename + '...')
	filename = filename.replace('mp3', 'wav')
	print('exporting to ' + filename)
	sound.export(filename, format = 'wav')

# read data
for filename in unhappylist:
	# import file
	sound = AudioSegment.from_mp3(filename)
	print('imported' + filename + '...')
	filename = filename.replace('mp3', 'wav')
	print('exporting to ' + filename)
	sound.export(filename, format = 'wav')

# read data
for filename in neutrallist:
	# import file
	sound = AudioSegment.from_mp3(filename)
	print('imported' + filename + '...')
	filename = filename.replace('mp3', 'wav')
	print('exporting to ' + filename)
	sound.export(filename, format = 'wav')

# read data
for filename in happylist:
	# import file
	sound = AudioSegment.from_mp3(filename)
	print('imported' + filename + '...')
	filename = filename.replace('mp3', 'wav')
	print('exporting to ' + filename)
	sound.export(filename, format = 'wav')

for filename in mp3list:
	# import file
	sound = AudioSegment.from_mp3(filename)
	print('imported' + filename + '...')
	filename = filename.replace('mp3', 'wav')
	print('exporting to ' + filename)
	sound.export(filename, format = 'wav')
