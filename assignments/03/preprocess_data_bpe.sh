#!/bin/bash
# -*- coding: utf-8 -*-

set -e

pwd=`dirname "$(readlink -f "$0")"`
base=$pwd/../..
src=fr
tgt=en
data=$base/data/$tgt-$src/bpe/

# change into base directory to ensure paths are valid
cd $base

# Do BPE magic!
 cat $data/preprocessed/train.$src $data/preprocessed/train.$tgt | subword-nmt learn-bpe -s 20000 -o $data/preprocessed/codes.bpe

 for lang in $src $tgt; do
   subword-nmt apply-bpe -c $data/preprocessed/codes.bpe < $data/preprocessed/train.$lang | subword-nmt get-vocab > $data/preprocessed/vocab.$lang
 done

 for split in train test valid tiny_train; do
   for lang in $src $tgt; do
     echo "${split} ${lang}"

     subword-nmt apply-bpe -c $data/preprocessed/codes.bpe --vocabulary $data/preprocessed/vocab.$lang --vocabulary-threshold 1 < $data/preprocessed/$split.$lang > $data/preprocessed/$split.BPE.$lang
   done
 done

# preprocess all files for model training
python preprocess.py --target-lang $tgt --source-lang $src --dest-dir $data/prepared/ --train-prefix $data/preprocessed/train.BPE --valid-prefix $data/preprocessed/valid.BPE --test-prefix $data/preprocessed/test.BPE --tiny-train-prefix $data/preprocessed/tiny_train.BPE --threshold-src 1 --threshold-tgt 1 --num-words-src "-1" --num-words-tgt "-1" --vocab-src $data/preprocessed/vocab.$src --vocab-trg $data/preprocessed/vocab.$tgt

echo "done!"
