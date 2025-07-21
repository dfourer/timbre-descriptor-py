# timbre-descriptor-py
Python Implementation of the Timbre Descriptors proposed by G. Peeters et al and application to instrument classification


timbre-descriptor-py is a Python toolbox for automatic timbre analysis and classification of musical instruments from audio recordings, based on timbre descriptors and statistical models.

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

#  Installation

This project was tester with Python 2.7 using the following packages:

```bash
pip install numpy scipy


# Usage Example
python classify.py violin.wav


