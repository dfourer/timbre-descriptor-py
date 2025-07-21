#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# classify.py
#
# MIT License
# 
# Copyright (c) 2025 Dominique Fourer (dominique@fourer.fr)
# https://fourer.fr
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# ------------------------------------------------------------------------------
# Instrument classification from audio recordings using timbre descriptors.
# Refer to the following publication for the underlying method:
#
# Dominique Fourer, Jean-Luc Rouas, Pierre Hanna, and Matthias Robine.
# "Automatic timbre classification of ethnomusicological audio recordings."
# Proceedings of the International Society for Music Information Retrieval
# Conference (ISMIR), Taipei, Taiwan, 2014.
# ------------------------------------------------------------------------------

"""
Instrument Recognition using timbre descriptors and LDA projection.

Dependencies:
- numpy
- scipy
- my_tools.py
- timbre_descriptor.py
- my_lda.py
- model_inst.mat

Usage:
    python main_timbre.py <audiofile.wav>
    
"""

import os
import sys
import numpy as np
from scipy.io import wavfile
import scipy.io

import timbretoolbox.my_tools as mt
import timbretoolbox.timbre_descriptor as timbre_descriptor
import timbretoolbox.my_lda as my_lda


NBITS = 16
MAX_VAL = float(2 ** (NBITS - 1))
MODEL_PATH = "models/model_inst.mat"
T_NOISE = -60  # dB threshold


def load_model(path):
    if not os.path.exists(path):
        raise IOError("Model file not found: {}".format(path))

    m = scipy.io.loadmat(path)
    model = {
        "nb_desc": np.squeeze(np.array(m["nb_desc"])),
        "i_fs": np.squeeze(np.array(m["i_fs"])) - 1,
        "Vect": np.squeeze(np.array(m["Vect"])),
        "repr_mu": np.squeeze(np.array(m["repr"])),
        "repr_sigma": np.squeeze(np.array(m["repr2"])) + 0.0,
        "inst": np.squeeze(np.array(m["inst"]))
    }
    return model


def is_silent(signal):
    rms_val = mt.rms(signal)[0]
    level_db = 10 * np.log10(rms_val + timbre_descriptor.EPS)
    return level_db <= T_NOISE


def compute_descriptor(signal, Fs, i_fs):
    desc = timbre_descriptor.compute_all_descriptor(signal, Fs)
    param_val, field_name = timbre_descriptor.temporalmodeling(desc)
    param_val = param_val[i_fs]

    if np.isnan(param_val).any() or np.isinf(param_val).any():
        print("[WARNING] Descriptor contains NaN or Inf values:")
        mt.disp_var(param_val, "param_val")
    return param_val, [field_name[i] for i in i_fs]


def classify(param_val, model):
    vect = model["Vect"]
    mu = model["repr_mu"]
    sigma = model["repr_sigma"]
    inst = model["inst"]

    # Add small epsilon to avoid division by zero in LDA
    sample = np.array([param_val]) + mt.EPS
    gr1, gr2, p1, p2 = my_lda.pred_lda(sample, vect, mu, sigma)
    i_res = gr1[0]
    famille = inst[i_res][0][0]
    jeu = inst[i_res][1][0] if i_res > 0 else ""

    return {
        "famille": famille,
        "jeu": jeu,
        "res1": gr1[0],
        "res2": gr2[0],
        "p1": p1[0],
        "p2": p2[0]
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: {} classify.py <audiofile.wav>".format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("[ERROR] Audio file not found: {}".format(filename))
        sys.exit(1)

    try:
        Fs, s = wavfile.read(filename)
        s = s.astype(np.float32) / MAX_VAL
    except Exception as e:
        print("[ERROR] Cannot read audio:", e)
        sys.exit(1)

    if is_silent(s):
        print("[WARNING] File possibly only contains silence. Skipping.")
        sys.exit(0)

    print("[INFO] Computing descriptors...")
    model = load_model(MODEL_PATH)
    param_val, field_names = compute_descriptor(s, Fs, model["i_fs"])

    print("[INFO] Classifying...")
    result = classify(param_val, model)

    print("\n Detected Instrument:")
    print("   Famille:", result["famille"])
    print("   Jeu    :", result["jeu"])
    print("   Score1 :", result["res1"])
    print("   Score2 :", result["res2"])
    print("   p1     :", result["p1"])
    print("   p2     :", result["p2"])
    print()

if __name__ == "__main__":
    main() 
