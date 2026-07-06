#!/bin/bash

# ============================================
# DSM010 Question 2
# Apache Mahout K-Means Workflow
# ============================================

# Convert text documents to sequence files
bin/mahout seqdirectory \
-i /user/komal/dsm010/q2/text_docs_200 \
-o /user/komal/dsm010/q2/sequence_200

# Convert sequence files to TF-IDF vectors
bin/mahout seq2sparse \
-i /user/komal/dsm010/q2/sequence_200 \
-o /user/komal/dsm010/q2/vectors_200 \
-wt tfidf

# K-Means (Cosine Distance)

bin/mahout kmeans \
-i /user/komal/dsm010/q2/vectors_200/tfidf-vectors \
-c /user/komal/dsm010/q2/clusters_k2_cosine \
-o /user/komal/dsm010/q2/kmeans_k2_cosine \
-k 2 \
-x 10 \
-dm org.apache.mahout.common.distance.CosineDistanceMeasure \
-cl

bin/mahout kmeans \
-i /user/komal/dsm010/q2/vectors_200/tfidf-vectors \
-c /user/komal/dsm010/q2/clusters_k3 \
-o /user/komal/dsm010/q2/kmeans_k3 \
-k 3 \
-x 10 \
-dm org.apache.mahout.common.distance.CosineDistanceMeasure \
-cl

bin/mahout kmeans \
-i /user/komal/dsm010/q2/vectors_200/tfidf-vectors \
-c /user/komal/dsm010/q2/clusters_k4_cosine \
-o /user/komal/dsm010/q2/kmeans_k4_cosine \
-k 4 \
-x 10 \
-dm org.apache.mahout.common.distance.CosineDistanceMeasure \
-cl

# K-Means (Euclidean Distance)

bin/mahout kmeans \
-i /user/komal/dsm010/q2/vectors_200/tfidf-vectors \
-c /user/komal/dsm010/q2/clusters_k2_euclidean \
-o /user/komal/dsm010/q2/kmeans_k2_euclidean \
-k 2 \
-x 10 \
-dm org.apache.mahout.common.distance.EuclideanDistanceMeasure \
-cl

bin/mahout kmeans \
-i /user/komal/dsm010/q2/vectors_200/tfidf-vectors \
-c /user/komal/dsm010/q2/clusters_k3_euclidean \
-o /user/komal/dsm010/q2/kmeans_k3_euclidean \
-k 3 \
-x 10 \
-dm org.apache.mahout.common.distance.EuclideanDistanceMeasure \
-cl

bin/mahout kmeans \
-i /user/komal/dsm010/q2/vectors_200/tfidf-vectors \
-c /user/komal/dsm010/q2/clusters_k4_euclidean \
-o /user/komal/dsm010/q2/kmeans_k4_euclidean \
-k 4 \
-x 10 \
-dm org.apache.mahout.common.distance.EuclideanDistanceMeasure \
-cl

# Dump clusters

bin/mahout clusterdump \
-i /user/komal/dsm010/q2/kmeans_k3/clusters-2-final \
-p /user/komal/dsm010/q2/kmeans_k3/clusteredPoints \
-d /user/komal/dsm010/q2/vectors_200/dictionary.file-0 \
-dt sequencefile \
-o ~/Downloads/BigDataAnalysis/04_Output/q2_results/k3_cosine_clusters.txt