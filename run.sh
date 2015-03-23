#!/usr/bin/env bash

chmod a+x ./src/word_count.py
chmod a+x ./src/running_median.py

python ./src/word_count.py >./wc_output/wc_result.txt
python ./src/running_median.py >./wc_output/med_result.txt
