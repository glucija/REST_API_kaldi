#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from tools.nnet_recognizer import recognition
import sys
from tools.data_prepare import prepare_wav, make_wav_scp
from pathlib import Path


def asr(wav,recognizer):
#prepare wav file
    wav = prepare_wav(wav)
    wav_stem = Path(wav).stem

#make scp
    make_wav_scp(wav)


    try:
        print("Zacenjam z razpoznavo")
        rec = recognition(recognizer)
        print("Za razpoznavo")
        return(rec)
        print("Razpoznava zakljucena")
    except Exception as e:
        return("Razpoznava neuspesna: " + e)
