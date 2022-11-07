#!/bin/bash
# -*- coding: utf-8 -*-

set -e

pwd=`dirname "$(readlink -f "$0")"`
base=$pwd/../..
src=fr
tgt=en
data=$base/data/$tgt-$src/autoencoded/

# change into base directory to ensure paths are valid
cd $base

# auto-encode target language
python scripts/autoencode.py --src $data/preprocessed/train.fr --tgt $data/preprocessed/train.en

# preprocess all files for model training
python preprocess.py --target-lang $tgt --source-lang $src --dest-dir $data/prepared/ --train-prefix $data/preprocessed/train --valid-prefix $data/preprocessed/valid --test-prefix $data/preprocessed/test --tiny-train-prefix $data/preprocessed/tiny_train --threshold-src 1 --threshold-tgt 1 --num-words-src 4000 --num-words-tgt 4000

echo "done!"