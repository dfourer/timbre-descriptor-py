# -*- coding: utf-8 -*-
#
# Copyright (c) 2025 Dominique Fourer <dominique@fourer.fr>

# You should have received a copy of the GNU General Public License
# along with TimeSide.  If not, see <http://www.gnu.org/licenses/>.

# Author: D Fourer <dominique@fourer.fr> https://www.fourer.fr

import numpy, scipy

from scipy.io import wavfile
import timbretoolbox.swipep as swp 

import matplotlib.pyplot as plt
import numpy as np

filename = "violon.wav"


nbits = 16;
MAX_VAL = pow(2.,(nbits-1)) * 1.0;

## read file
Fs, s = wavfile.read(filename);
s = s/MAX_VAL;

#[f0,time,s] = swp.swipep(s,Fs,numpy.array([75, 500]),0.01);
f0, time, s = swp.swipep(s, Fs, numpy.array([75, 700]),0.01)


# Optionnel : supprimer les zéros ou les valeurs nulles de f0 (non détectées)
f0 = np.array(f0)
time = np.array(time)
mask = f0 > 0
f0 = f0[mask]
time = time[mask]

# Affichage du graphe
plt.figure(figsize=(10, 4))
plt.plot(time, f0, label="F0 (Hz)", color='mediumblue')
#plt.plot(time, s, label="F0 (Hz)", color='mediumred')
plt.xlabel("Time (s)")
plt.ylabel("Fundamental Frequency (Hz)")
plt.title(filename)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
