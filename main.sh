#!/bin/bash

PYTHON_CMD=$(command -v python3 || command -v python)

if [ -z "$PYTHON_CMD" ]; then
  echo "Erreur : Python is not available."
  exit 1
fi

echo "$PYTHON_CMD ./classify.py ./violon.wav"
"$PYTHON_CMD" ./classify.py ./violon.wav

echo "$PYTHON_CMD ./main_example.py"
"$PYTHON_CMD" ./main_example.py

echo "$PYTHON_CMD ./main_examplef0.py"
"$PYTHON_CMD" ./main_examplef0.py
