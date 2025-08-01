# timbre-descriptor-py

A simple Python Implementation of the Timbre Descriptors proposed by G. Peeters et al. with an application to instrument timbre classification.

timbre-descriptor-py is a Python toolbox for automatic timbre analysis and classification of musical instruments from audio recordings, based on timbre descriptors and statistical models.

Author: Dominique Fourer (dominique@fourer.fr)
https://fourer.fr

A pytorch version (only of the timbre descriptors) is available here:
https://github.com/geoffroypeeters/ttb


#  Scientific references

This work builds upon:

**Dominique Fourer, Jean-Luc Rouas, Pierre Hanna, Matthias Robine.**  
*Automatic timbre classification of ethnomusicological audio recordings.*  
Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), Taipei, Taiwan, 2014.  
[https://fourer.fr/publi/ismir14_dfourer.pdf)

**G. Peeters.**  
*A large set of audio features for sound description (similarity and classification) in the CUIDADO project.*  
Technical Report, IRCAM, 2004.  
[http://recherche.ircam.fr/anasyn/peeters/ARTICLES/Peeters_2003_cuidadoaudiofeatures.pdf)

**G. Peeters et al.**
*The timbre toolbox: Extracting audio descriptors from musical signals.*
Journal of the Acoustical Society of America, 130(5), November 2011.


#  Installation

This project was successfuly tested with Python 2.7 and Python 3.12.3 using the following packages (cf. requirements.txt):

numpy==1.26.4
matplotlib==3.6.3
matplotlib-inline==0.1.6
scipy==1.11.4


```bash
pip install numpy scipy


# Usage Example (timbre prediction)
python classify.py violin.wav

# Usage Example (F0 estimation using the SWIPE method)
python main_examplef0.py

