
# Ami G. Sangster


import h5py
import csv
from protT5_embedder import get_embeddings
from functions import *





# options

# path and file name for the protein segment boundaries (required)
seg_bounds_path = "name0.tsv"

# save the per-residue embeddings (prot_t5_xl_half_uniref50-enc) for the whole protein
save_whole_emb_to_hdf5 = False
# if true include a path and file name for the embeddings
whole_emb_path = "name1.hdf5"

# save the embeddings of protein segments defined by zero-shot protein segmentation
save_seg_emb_to_hdf5 = False
# if true include a path and file name for the embeddings
seg_emb_path = "name2.hdf5"





# generate ProtT5 embeddings (prot_t5_xl_half_uniref50-enc)
emb_dict = get_embeddings(seq_path="protein_sequences_demo.fasta", model_dir="", 
                          per_protein=False, max_residues=4000, max_seq_len=4000, max_batch=100)

# change the keys of the dictionary from the whole protein identifier (as seen in fastas)
# to only the UniProt ID
for k in emb_dict.keys():
    new_k = k.split("|")[1]
    emb_dict[new_k] = emb_dict[k]
    del emb_dict[k]

# save per-residue embeddings of the proteins (optional)
if save_whole_emb_to_hdf5:
    with h5py.File(str(whole_emb_path), "a") as hf:
        for sequence_id, embedding in emb_dict.items():
            # noinspection PyUnboundLocalVariable
            hf.create_dataset(sequence_id, data=embedding)





# identify segment boundaries using change point analysis 
protein_segments = get_protein_segments(emb_dict, max_bkps_per100aa=3)

# save segment boundaries
with open(seg_bounds_path, 'w', newline='') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
    for protein_id, protein_seg in protein_segments.items():
        writer.writerow([protein_id, protein_seg])





# make and save segment embeddings (optional)
if save_seg_emb_to_hdf5:
    protein_segment_embeddings = get_protein_segment_embeddings(emb_dict, protein_segments)

    with h5py.File(str(seg_emb_path), "a") as hf:
        for sequence_key, embedding in protein_segment_embeddings.items():
            # noinspection PyUnboundLocalVariable
            hf.create_dataset(sequence_key, data=embedding)



