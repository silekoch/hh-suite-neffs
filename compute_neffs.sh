#!/bin/bash

# Read the file with IDs
while read prot_id; do
  hhmake -id 100 -diff inf -seq 2 -i $msa_dir/$prot_id.a3m -o /tmp/$prot_id.hhm
  python3 /app/extract_neffs.py
  rm /tmp/$prot_id.hhm
done <$prot_ids
