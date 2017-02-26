import os
os.system('rm ./aligned-images/cache.t7')
os.system('./util/align-dlib.py ./training2/ align outerEyesAndNose ./aligned-images/ --size 96')
os.system('./batch-represent/main.lua -outDir ./generated-embeddings/ -data ./aligned-images/')
os.system('./demos/classifier.py train ./generated-embeddings/')
os.system('rm -rfv ./training2/*')
