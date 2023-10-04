#!/bin/bash
. ~/.bashrc
cd /gscratch/stf/is28/biobias || exit
conda activate biobias || exit
#python3 download_bios_batched.py 2018-34 --parallel 36
python3 download_bios_batched.py 2018-13 --parallel 36
#python3 download_bios_batched.py 2013-20 --parallel 36
python3 download_bios_batched.py 2017-43 --parallel 36
#python3 download_bios_batched.py 2016-44 --parallel 36
python3 download_bios_batched.py 2018-05 --parallel 36
#python3 download_bios_batched.py 2014-41 --parallel 36
python3 download_bios_batched.py 2017-47 --parallel 36
#python3 download_bios_batched.py 2017-26 --parallel 36
python3 download_bios_batched.py 2017-34 --parallel 36
#python3 download_bios_batched.py 2017-13 --parallel 36
python3 download_bios_batched.py 2018-43 --parallel 36
python3 download_bios_batched.py 2017-39 --parallel 36
python3 download_bios_batched.py 2018-39 --parallel 36
python3 download_bios_batched.py 2018-09 --parallel 36
python3 download_bios_batched.py 2018-26 --parallel 36
python3 preprocess.py CC*.pkl -o BIOS.pkl
