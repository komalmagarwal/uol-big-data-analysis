#!/usr/bin/env python3
import sys
from sentence_transformers import SentenceTransformer, util

THRESHOLD = 0.65

model = SentenceTransformer("all-MiniLM-L6-v2", cache_folder=".")

for line in sys.stdin:
    try:
        row_id, ticket1, ticket2 = line.strip().split("\t", 2)

        emb1 = model.encode(ticket1, convert_to_tensor=True)
        emb2 = model.encode(ticket2, convert_to_tensor=True)

        similarity = util.cos_sim(emb1, emb2).item()
        label = "True" if similarity >= THRESHOLD else "False"

        print(f"{row_id}\t{similarity:.4f}\t{label}\t{ticket1}\t{ticket2}")

    except Exception:
        continue