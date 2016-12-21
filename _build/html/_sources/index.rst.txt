.. BodePlotFilter documentation master file, created by
   sphinx-quickstart on Tue Dec 20 15:38:34 2016.

BodePlotFilter's Software documentation
=======================================

The program BodePlotFilter has been created to test the functionalities of Python programming Language and the versatility of its tools regarding Instrumentation management and control.

This program is based on Python programming language. 
The version used is: Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18)
The only particularity of this program is the use of PyVisa Library. PyVISA is a Python package that enables you to control all kinds of measurement devices independently of the interface (e.g. GPIB, RS232, USB, Ethernet).
Libraries tkinter and matplotlib are used too but in a common way readings esthetics and graphs representation.

Based on GPIB and USB communication, this program plots the Amplitude and Phase Bode graphs of a passive filter response. For that we will manage a Function Generator to generate an electrical waveform of our choice and inject that to any external passive filter then with Oscilloscope's readings we will Plot the information captured. 

Download :download:`BodePlotFilter <BodePlotFilter.py>`

.. image:: SchemaProject.png

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Project
   GUI
   Technical Guide
   User Guide
   code


Indices and tables
==================

* :ref:`search`
