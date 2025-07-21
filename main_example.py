# -*- coding: utf-8 -*-
#
# Copyright (c) 2025 Dominique Fourer <dominique@fourer.fr>

# You should have received a copy of the GNU General Public License
# along with TimeSide.  If not, see <http://www.gnu.org/licenses/>.

# Author: D Fourer <dominique@fourer.fr> https://www.fourer.fr

import numpy, scipy

from scipy.io import wavfile
import sys 

import timbretoolbox.my_tools as mt
import os
import timbretoolbox.timbre_descriptor as timbre_descriptor
import timbretoolbox.my_lda  as my_lda


filename = "violon.wav"

model_file = "models/model_inst.mat"

nbits = 16;
MAX_VAL = pow(2.,(nbits-1)) * 1.0;
## Load models
m 			= scipy.io.loadmat(model_file);
nb_desc		= numpy.squeeze(numpy.array(m['nb_desc']));   		## nb_desc
i_fs 		= numpy.squeeze(numpy.array(m['i_fs']))-1;   		## IRMFSP indices
Vect 		= numpy.squeeze(numpy.array(m['Vect']));   			## Projection basis
n_max		= numpy.shape(Vect)[0];
repr_mu		= numpy.squeeze(numpy.array(m['repr']));
repr_sigma	= numpy.squeeze(numpy.array(m['repr2'])) + 0.0; 	#+ mt.EPS
inst		= numpy.squeeze(numpy.array(m['inst']));
T_NOISE		= -60;												## noise threshold in dB

## read file
Fs, s = wavfile.read(filename);
s = s/MAX_VAL;

if 10 * numpy.log10(mt.rms(s)[0]+timbre_descriptor.EPS) <= T_NOISE:
	print("/!\ Warning: File possibly only contains silence (skipping) \n")
		
## 2 compute descriptors
desc = timbre_descriptor.compute_all_descriptor(s, Fs);
param_val, field_name = timbre_descriptor.temporalmodeling(desc);
param_val = param_val[i_fs];
		
field_name_fs = list();
for i in range(0,nb_desc):
	field_name_fs.append(field_name[ i_fs[i]]);
		
if numpy.isnan(param_val).any() or numpy.isinf(param_val).any():
	print("/!\ Warning: Contains spurious values", param_val, "\n")
	mt.disp_var(param_val,"param_val");
		
## 3 compare with previous model and select the most probable
gr1, gr2, p1, p2 = my_lda.pred_lda(numpy.array([param_val, ])+mt.EPS, Vect, repr_mu, repr_sigma);
i_res = gr1[0];  ## gr1 is euclidean distance criterion
		
## display result
famille = inst[i_res][0][0];
jeu 	= "";
if i_res > 0:
	jeu = inst[i_res][1][0];
	print("Detected as ", famille, " ", jeu, " according to res1: res1=",gr1[0]," res2=", gr2[0],"p1=",p1[0]," p2=", p2[0],"\n\n");

