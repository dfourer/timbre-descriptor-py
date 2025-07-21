#!/bin/bash

echo "python ./classify.py ./violon.wav"
python ./classify.py ./violon.wav

echo "python ./main_example.py"
python ./main_example.py
 
echo "python ./main_examplef0.py"
python ./main_examplef0.py
