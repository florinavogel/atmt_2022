import argparse
import random


def set_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True, type=str, help='file containing source data')
    ap.add_argument('--tgt', required=True, type=str, help='file containing target data')

    ap.add_argument('--shuffle', required=False, default=True, type=bool, help='whether to shuffle the new files')

    return ap.parse_args()


def autoencode(args):
    with open(args.src, "r", encoding="utf-8") as src_f:
        src_data = src_f.readlines()  # we can do this since we are working with small files

    with open(args.tgt, "r", encoding="utf-8") as tgt_f:
        tgt_data = tgt_f.readlines()

    src_data.extend(tgt_data)
    tgt_data.extend(tgt_data)

    if args.shuffle:
        zipped = list(zip(src_data, tgt_data))
        random.shuffle(zipped)
        src_data, tgt_data = zip(*zipped)

    with open(args.src, "w", encoding="utf-8") as src_out:
        [src_out.write(s) for s in src_data]

    with open(args.tgt, "w", encoding="utf-8") as tgt_out:
        [tgt_out.write(s) for s in tgt_data]


if __name__ == '__main__':
    arguments = set_args()
    autoencode(arguments)
