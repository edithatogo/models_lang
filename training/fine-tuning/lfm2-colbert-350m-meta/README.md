---
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
tags:
- liquid
- lfm2
- edge
- ColBERT
- PyLate
- sentence-transformers
- sentence-similarity
- feature-extraction
pipeline_tag: sentence-similarity
library_name: PyLate
license: other
license_name: lfm1.0
license_link: LICENSE
metrics:
- MaxSim_accuracy@1
- MaxSim_accuracy@3
- MaxSim_accuracy@5
- MaxSim_accuracy@10
- MaxSim_precision@1
- MaxSim_precision@3
- MaxSim_precision@5
- MaxSim_precision@10
- MaxSim_recall@1
- MaxSim_recall@3
- MaxSim_recall@5
- MaxSim_recall@10
- MaxSim_ndcg@10
- MaxSim_mrr@10
- MaxSim_map@100
model-index:
- name: PyLate
  results:
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoClimateFEVER
      type: NanoClimateFEVER
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.4
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.52
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 0.64
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 0.8
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.4
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.20666666666666667
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.15600000000000003
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.11799999999999997
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.195
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.2733333333333334
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.31566666666666665
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.45899999999999996
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.38664978031372876
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.506095238095238
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.31298040075928324
      name: Maxsim Map@100
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoDBPedia
      type: NanoDBPedia
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.86
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.92
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 0.94
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 0.98
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.86
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.7
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.64
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.5660000000000001
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.12059669442306678
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.2074731836307263
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.28467782707772427
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.4182321427819297
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.7139105590461106
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.8975
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.5749525139913445
      name: Maxsim Map@100
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoFEVER
      type: NanoFEVER
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.96
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.98
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 0.98
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 0.98
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.96
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.3533333333333333
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.21599999999999994
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.10799999999999997
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.8966666666666667
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.9533333333333333
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.96
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.96
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.9494352279872394
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.9666666666666667
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.9396715796806541
      name: Maxsim Map@100
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoFiQA2018
      type: NanoFiQA2018
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.56
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.78
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 0.78
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 0.82
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.56
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.36
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.26
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.14799999999999996
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.34874603174603175
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.5375714285714286
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.584452380952381
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.6361984126984127
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.5909802936451645
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.6625000000000001
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.5325997234510657
      name: Maxsim Map@100
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoHotpotQA
      type: NanoHotpotQA
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.92
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.98
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 1.0
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 1.0
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.92
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.5599999999999999
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.35999999999999993
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.18799999999999997
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.46
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.84
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.9
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.94
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.8954853297530804
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.9540000000000001
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.8452079490557751
      name: Maxsim Map@100
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoMSMARCO
      type: NanoMSMARCO
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.58
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.7
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 0.76
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 0.82
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.58
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.23333333333333336
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.15200000000000002
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.08199999999999999
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.58
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.7
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.76
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.82
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.6860512766453598
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.6444126984126984
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.6563222143353721
      name: Maxsim Map@100
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoNFCorpus
      type: NanoNFCorpus
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.5
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.6
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 0.66
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 0.7
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.5
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.3933333333333333
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.36400000000000005
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.29
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.06441975062397678
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.10314642255588413
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.1276571146817061
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.15217406670771688
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.37688958487118834
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.5655
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.18401289774934215
      name: Maxsim Map@100
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoNQ
      type: NanoNQ
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.66
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.78
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 0.86
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 0.88
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.66
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.26666666666666666
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.184
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.09599999999999997
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.62
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.72
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.82
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.85
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.7462482063760048
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.7323333333333334
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.7080310107127462
      name: Maxsim Map@100
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoQuoraRetrieval
      type: NanoQuoraRetrieval
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.8
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.92
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 0.98
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 1.0
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.8
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.3666666666666666
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.23599999999999993
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.132
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.7106666666666667
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.8813333333333333
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.9346666666666666
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.9793333333333334
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.882106394646597
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.8631666666666666
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.8429613442113442
      name: Maxsim Map@100
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoSCIDOCS
      type: NanoSCIDOCS
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.5
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.68
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 0.76
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 0.86
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.5
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.3466666666666666
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.27599999999999997
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.18599999999999997
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.10566666666666666
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.21366666666666664
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.2826666666666667
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.38066666666666665
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.3835676640413774
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.6130555555555556
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.29746953473534715
      name: Maxsim Map@100
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoArguAna
      type: NanoArguAna
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.28
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.5
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 0.7
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 0.88
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.28
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.16666666666666663
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.14
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.088
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.28
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.5
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.7
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.88
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.550733304467759
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.44868253968253957
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.4511852654234456
      name: Maxsim Map@100
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoSciFact
      type: NanoSciFact
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.7
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.82
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 0.88
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 0.92
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.7
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.29333333333333333
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.19599999999999998
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.10199999999999998
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.675
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.805
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.88
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.91
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.8042579434791977
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.7707142857142858
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.7705943722943722
      name: Maxsim Map@100
  - task:
      type: py-late-information-retrieval
      name: Py Late Information Retrieval
    dataset:
      name: NanoTouche2020
      type: NanoTouche2020
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.7959183673469388
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.9795918367346939
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 1.0
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 1.0
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.7959183673469388
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.7619047619047619
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.6897959183673469
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.5489795918367346
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.054536287361574225
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.15427299614340523
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.2308549805548407
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.3471515583210746
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.629619385239878
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.8894557823129251
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.4616787350016793
      name: Maxsim Map@100
  - task:
      type: nano-beir
      name: Nano BEIR
    dataset:
      name: NanoBEIR mean
      type: NanoBEIR_mean
    metrics:
    - type: MaxSim_accuracy@1
      value: 0.6550706436420722
      name: Maxsim Accuracy@1
    - type: MaxSim_accuracy@3
      value: 0.7815070643642071
      name: Maxsim Accuracy@3
    - type: MaxSim_accuracy@5
      value: 0.8415384615384615
      name: Maxsim Accuracy@5
    - type: MaxSim_accuracy@10
      value: 0.8953846153846154
      name: Maxsim Accuracy@10
    - type: MaxSim_precision@1
      value: 0.6550706436420722
      name: Maxsim Precision@1
    - type: MaxSim_precision@3
      value: 0.3852747252747252
      name: Maxsim Precision@3
    - type: MaxSim_precision@5
      value: 0.2976766091051805
      name: Maxsim Precision@5
    - type: MaxSim_precision@10
      value: 0.20407535321821035
      name: Maxsim Precision@10
    - type: MaxSim_recall@1
      value: 0.3931768280118962
      name: Maxsim Recall@1
    - type: MaxSim_recall@3
      value: 0.5299331305821623
      name: Maxsim Recall@3
    - type: MaxSim_recall@5
      value: 0.5985109464051271
      name: Maxsim Recall@5
    - type: MaxSim_recall@10
      value: 0.6717504754237795
      name: Maxsim Recall@10
    - type: MaxSim_ndcg@10
      value: 0.6612257654240528
      name: Maxsim Ndcg@10
    - type: MaxSim_mrr@10
      value: 0.7318525204953776
      name: Maxsim Mrr@10
    - type: MaxSim_map@100
      value: 0.5828975031847518
      name: Maxsim Map@100
---

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
<div style="display: flex; justify-content: center; gap: 0.5em;">
<a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> • <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
</div>
</center>

<br>

# LFM2-ColBERT-350M

LFM2-ColBERT-350M is a late interaction retriever with excellent multilingual performance. It allows you to store documents in one language (for example, a product description in English) and retrieve them in many languages with high accuracy.

- LFM2-ColBERT-350M offers **best-in-class accuracy** across different languages.
- Inference speed is **on par with models 2.3 times smaller**, thanks to the efficient LFM2 backbone.
- You can use it as a **drop-in replacement** in your current RAG pipelines to improve performance.

Find more information about LFM2-ColBERT-350M in our [blog post](http://www.liquid.ai/blog/lfm2-colbert-350m-one-model-to-embed-them-all).

> [!NOTE]
> 🚀 Try our demo: https://huggingface.co/spaces/LiquidAI/LFM2-ColBERT

## 📄 Model details

Late interaction retrievers like LFM2-ColBERT-350M are particularly interesting because they preserve much of the **expressivity** of re-rankers while retaining the **efficiency** of bi-encoders. 
In practice, they're used to both retrieve documents at scale (like bi-encoders) and rank them at the same time (like rerankers).

![image](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/5u2Zm_bIDHUtBJrDtT_vm.png)

We recommend using this model for various RAG use cases, such as:

- **E-commerce**: Find products across many languages with semantic search at scale.
- **On-device semantic search**: Ask questions to your phone in natural language to retrieve files, emails, and notes.
- **Enterprise knowledge assistants**: Retrieve internal legal, financial, and technical documents in different languages.

| Property              | [**LFM2-ColBERT-350M**](https://huggingface.co/LiquidAI/LFM2-ColBERT-350M/) | 
| --------------------- | ------------------------------ |
| **Total parameters**  | 353,322,752                    | 
| **Layers**            | 17 (10 conv + 6 attn + 1 dense)|
| **Context length**    | 32,768 tokens                  |
| **Vocabulary size**   | 65,536                         |
| **Training precision**| BF16                           |
| **License**           | LFM Open License v1.0          | 

**Document length:** 512 tokens

**Query length:** 32 tokens

**Output dimensionality:** 128 tokens

**Similarity function:** MaxSim

**Supported languages**: English, Arabic, Chinese, French, German, Japanese, Korean, and Spanish.

```
ColBERT(
  (0): Transformer({'max_seq_length': 511, 'do_lower_case': False}) with Transformer model: Lfm2Model 
  (1): Dense({'in_features': 1024, 'out_features': 128, 'bias': False, 'activation_function': 'torch.nn.modules.linear.Identity'})
)
```

## 🏃 How to run

<a href="https://colab.research.google.com/drive/1tXSAXGpjuTvliuTrSSHDEcmIe48uolrD?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width=120 alt="Colab link"></a>

First, install the PyLate and transformers library:

```bash
pip install -U pylate
```

### Retrieval

Use this model with PyLate to index and retrieve documents. The index uses [FastPLAID](https://github.com/lightonai/fast-plaid) for efficient similarity search.

#### Indexing documents

Load LFM2-ColBERT-350M and initialize the PLAID index, then encode and index your documents:

```python
from pylate import indexes, models, retrieve

# Step 1: Load the ColBERT model
model = models.ColBERT(
    model_name_or_path="LiquidAI/LFM2-ColBERT-350M",
)
model.tokenizer.pad_token = model.tokenizer.eos_token

# Step 2: Initialize the PLAID index
index = indexes.PLAID(
    index_folder="pylate-index",
    index_name="index",
    override=True,  # This overwrites the existing index if any
)

# Step 3: Encode the documents
documents_ids = ["1", "2", "3"]
documents = ["document 1 text", "document 2 text", "document 3 text"]

documents_embeddings = model.encode(
    documents,
    batch_size=32,
    is_query=False,  # Ensure that it is set to False to indicate that these are documents, not queries
    show_progress_bar=True,
)

# Step 4: Add document embeddings to the index by providing embeddings and corresponding ids
index.add_documents(
    documents_ids=documents_ids,
    documents_embeddings=documents_embeddings,
)
```

Note that you do not have to recreate the index and encode the documents every time. Once you have created an index and added the documents, you can re-use the index later by loading it:

```python
# To load an index, simply instantiate it with the correct folder/name and without overriding it
index = indexes.PLAID(
    index_folder="pylate-index",
    index_name="index",
)
```

#### Retrieving top-k documents for queries

Once the documents are indexed, you can retrieve the top-k most relevant documents for a given set of queries.
To do so, initialize the ColBERT retriever with the index you want to search in, encode the queries and then retrieve the top-k documents to get the top matches ids and relevance scores:

```python
# Step 1: Initialize the ColBERT retriever
retriever = retrieve.ColBERT(index=index)

# Step 2: Encode the queries
queries_embeddings = model.encode(
    ["query for document 3", "query for document 1"],
    batch_size=32,
    is_query=True,  #  # Ensure that it is set to True to indicate that these are queries
    show_progress_bar=True,
)

# Step 3: Retrieve top-k documents
scores = retriever.retrieve(
    queries_embeddings=queries_embeddings,
    k=10,  # Retrieve the top 10 matches for each query
)
```

### Reranking
If you only want to use LFM2-ColBERT-350M to perform reranking on top of your first-stage retrieval pipeline without building an index, you can simply use rank function and pass the queries and documents to rerank:

```python
from pylate import rank, models

queries = [
    "query A",
    "query B",
]

documents = [
    ["document A", "document B"],
    ["document 1", "document C", "document B"],
]

documents_ids = [
    [1, 2],
    [1, 3, 2],
]

model = models.ColBERT(
    model_name_or_path="LiquidAI/LFM2-ColBERT-350M",
)

queries_embeddings = model.encode(
    queries,
    is_query=True,
)

documents_embeddings = model.encode(
    documents,
    is_query=False,
)

reranked_documents = rank.rerank(
    documents_ids=documents_ids,
    queries_embeddings=queries_embeddings,
    documents_embeddings=documents_embeddings,
)
```

## 📈 Performance

### Accuracy

We extended the NanoBEIR benchmark to include Japanese and Korean languages. We open-sourced this dataset on Hugging Face at [LiquidAI/nanobeir-multilingual-extended](https://huggingface.co/datasets/LiquidAI/nanobeir-multilingual-extended) for reproducibility. 
On this NanoBEIR benchmark, LFM2-ColBERT-350M displays significantly stronger multilingual capabilities (especially in German, Arabic, Korean, and Japanese) while maintaining English performance.

![image](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/ARs78eGhBagN_VO3VQJCD.png)

Even more interestingly, LFM2-ColBERT-350M is an excellent cross-lingual retriever. This means that it is capable of retrieving documents based on queries from other languages. This is ideal for client-facing applications, like in e-commerce, where a description might be in English but the query is in another language.

LFM2-ColBERT-350M works especially well for English, French, Spanish, Italian, Portuguese, and German, as shown with these NDCG@10 scores on NanoBEIR:

<table style="font-size: 14px;">
<thead>
<tr>
<th style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">Doc / Query</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">AR</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">DE</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">EN</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">ES</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">FR</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">IT</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">JA</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">KO</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">PT</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 700; color: black;">AVG</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">AR</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fad4a6; color: black;">0.490</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f5a08c; color: black;">0.288</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f8ba98; color: black;">0.339</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6a88f; color: black;">0.303</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6aa90; color: black;">0.304</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f59f8b; color: black;">0.286</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fac19e; color: black;">0.357</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f8ba98; color: black;">0.338</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6a48d; color: black;">0.291</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f8ba98; font-weight: 700; color: black;">33.30%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">DE</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fde6b8; color: black;">0.383</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c6e8af; color: black;">0.563</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c1e6ad; color: black;">0.547</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f4efcd; color: black;">0.498</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f8f2d1; color: black;">0.502</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f0ebca; color: black;">0.489</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcd6a8; color: black;">0.424</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fddcad; color: black;">0.368</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #ede8c8; color: black;">0.486</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcf6d5; font-weight: 700; color: black;">47.33%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">EN</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcd9ab; color: black;">0.416</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c3e7ae; color: black;">0.554</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #9edf9e; color: black;">0.661</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c6e8af; color: black;">0.553</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #cae9b1; color: black;">0.551</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e4eec3; color: black;">0.522</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fde3b3; color: black;">0.477</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fde0b0; color: black;">0.395</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #dbecbd; color: black;">0.535</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #d7eabb; font-weight: 700; color: black;">51.82%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">ES</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcd8aa; color: black;">0.412</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e8f0c6; color: black;">0.514</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #b0e3a4; color: black;">0.578</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c6e8af; color: black;">0.563</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c1e6ad; color: black;">0.547</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #d7eabb; color: black;">0.529</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fde0b0; color: black;">0.436</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fde0b0; color: black;">0.394</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c1e6ad; color: black;">0.547</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e8f0c6; font-weight: 700; color: black;">50.21%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">FR</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcd7a9; color: black;">0.408</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #d7eabb; color: black;">0.527</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #b5e4a7; color: black;">0.573</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #cae9b1; color: black;">0.552</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c3e7ae; color: black;">0.564</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e0edc0; color: black;">0.537</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fee5b5; color: black;">0.450</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fddeb0; color: black;">0.388</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c4e7af; color: black;">0.549</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #eff2cb; font-weight: 700; color: black;">50.53%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">IT</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fde0b0; color: black;">0.395</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e7efc6; color: black;">0.512</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c3e7ae; color: black;">0.554</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #dbecbd; color: black;">0.535</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #dbecbd; color: black;">0.535</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #d2e9b7; color: black;">0.543</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fde2b2; color: black;">0.439</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fddeaf; color: black;">0.386</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #d7eabb; color: black;">0.529</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcf6d5; font-weight: 700; color: black;">49.20%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">JA</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fde4b4; color: black;">0.375</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcdaac; color: black;">0.365</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcd6a8; color: black;">0.409</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fabf9d; color: black;">0.358</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f8b396; color: black;">0.345</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f9b697; color: black;">0.337</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #cae9b1; color: black;">0.557</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #eff2cb; color: black;">0.491</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f7b094; color: black;">0.330</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcd3a4; font-weight: 700; color: black;">39.63%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">KO</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f7af93; color: black;">0.326</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f59f8b; color: black;">0.274</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6ab90; color: black;">0.310</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f5a18c; color: black;">0.282</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f49c8a; color: black;">0.265</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f49d8a; color: black;">0.266</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fde1b1; color: black;">0.440</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #d7eabb; color: black;">0.527</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f49e8b; color: black;">0.271</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6a98f; font-weight: 700; color: black;">32.89%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">PT</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcd6a8; color: black;">0.402</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #eff2cb; color: black;">0.499</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c6e8af; color: black;">0.558</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c4e7af; color: black;">0.545</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #d7eabb; color: black;">0.528</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #d7eabb; color: black;">0.529</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fde0b0; color: black;">0.436</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fddcad; color: black;">0.382</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c1e6ad; color: black;">0.547</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcf6d5; font-weight: 700; color: black;">49.17%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 700; color: black;">AVG</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcd2a3; font-weight: 700; color: black;">40.07%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #feedc1; font-weight: 700; color: black;">45.51%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e8f0c6; font-weight: 700; color: black;">50.32%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f1eecf; font-weight: 700; color: black;">46.54%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcf6d5; font-weight: 700; color: black;">46.00%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fee6b6; font-weight: 700; color: black;">44.86%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fee5b5; font-weight: 700; color: black;">44.62%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcd3a5; font-weight: 700; color: black;">40.78%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #feedbe; font-weight: 700; color: black;">45.38%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; color: black;"></td>
</tr>
</tbody>
</table>

In comparison, GTE-ModernColBERT-v1 consistently gets lower scores when documents and queries are not in the same language:

<table style="font-size: 14px;">
<thead>
<tr>
<th style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">Doc / Query</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">AR</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">DE</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">EN</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">ES</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">FR</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">IT</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">JA</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">KO</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">PT</th>
<th style="text-align: center; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 700; color: black;">AVG</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">AR</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f8ba98; color: black;">0.309</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f29488; color: black;">0.089</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f39789; color: black;">0.107</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f29488; color: black;">0.089</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f39688; color: black;">0.094</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f39588; color: black;">0.092</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f18d85; color: black;">0.070</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #ef8783; color: black;">0.049</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f29488; color: black;">0.087</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f39789; font-weight: 700; color: black;">10.96%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">DE</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #ef8783; color: black;">0.039</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f4efcd; color: black;">0.499</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e7efc6; color: black;">0.454</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fbe1b0; color: black;">0.362</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fddcad; color: black;">0.393</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fce0b0; color: black;">0.367</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6ad91; color: black;">0.133</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f08a84; color: black;">0.061</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcdaac; color: black;">0.361</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f8ba98; font-weight: 700; color: black;">29.65%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">EN</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #ef8783; color: black;">0.042</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fddcad; color: black;">0.408</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #9edf9e; color: black;">0.680</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e8f0c6; color: black;">0.446</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #eff2cb; color: black;">0.484</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcd9ab; color: black;">0.420</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f7b295; color: black;">0.167</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f18d85; color: black;">0.073</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e8f0c6; color: black;">0.438</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcd6a8; font-weight: 700; color: black;">35.08%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">ES</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #ef8783; color: black;">0.044</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fce0b0; color: black;">0.360</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #eff2cb; color: black;">0.485</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #d2e9b7; color: black;">0.525</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e4eec3; color: black;">0.465</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e7efc6; color: black;">0.437</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6ae92; color: black;">0.149</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f08a84; color: black;">0.061</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #eff2cb; color: black;">0.487</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fad19f; font-weight: 700; color: black;">33.48%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">FR</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #ef8783; color: black;">0.044</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fce1b1; color: black;">0.381</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f1eecf; color: black;">0.505</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e7efc6; color: black;">0.455</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #c1e6ad; color: black;">0.546</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcd9ab; color: black;">0.428</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6af92; color: black;">0.136</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f08983; color: black;">0.057</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e4eec3; color: black;">0.467</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fad29f; font-weight: 700; color: black;">33.35%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">IT</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #ef8783; color: black;">0.043</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fce0b0; color: black;">0.369</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e8f0c6; color: black;">0.449</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e8f0c6; color: black;">0.446</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e7efc6; color: black;">0.451</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f0ebca; color: black;">0.516</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6ae92; color: black;">0.143</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #ef8883; color: black;">0.054</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e7efc6; color: black;">0.448</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fad3a1; font-weight: 700; color: black;">32.36%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">JA</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #ef8783; color: black;">0.031</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f7b295; color: black;">0.169</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f9bc99; color: black;">0.250</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f7b295; color: black;">0.172</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f7b396; color: black;">0.177</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f7b295; color: black;">0.169</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e7efc6; color: black;">0.459</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f08983; color: black;">0.059</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6af92; color: black;">0.165</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f7b194; font-weight: 700; color: black;">18.35%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">KO</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #ef8783; color: black;">0.030</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6ad91; color: black;">0.134</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f7b295; color: black;">0.169</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f5aa90; color: black;">0.127</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6ad91; color: black;">0.133</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f5ab90; color: black;">0.125</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f39688; color: black;">0.090</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fce0b0; color: black;">0.368</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f5a98f; color: black;">0.124</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f59f8b; font-weight: 700; color: black;">14.45%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 500; color: black;">PT</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #ef8783; color: black;">0.043</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fcdaac; color: black;">0.368</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f1eecf; color: black;">0.479</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f4efcd; color: black;">0.492</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e4eec3; color: black;">0.467</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #e7efc6; color: black;">0.448</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f6af92; color: black;">0.138</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f08a84; color: black;">0.062</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #d2e9b7; color: black;">0.530</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fad29f; font-weight: 700; color: black;">33.63%</td>
</tr>
<tr>
<td style="text-align: left; padding: 8px; background: #fafafa; border: 1px solid #e0e0e0; font-weight: 700; color: black;">AVG</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f19188; font-weight: 700; color: black;">6.94%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f8ba98; font-weight: 700; color: black;">30.84%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fddcad; font-weight: 700; color: black;">39.75%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fbd8a9; font-weight: 700; color: black;">34.59%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fbdaab; font-weight: 700; color: black;">35.68%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fad29f; font-weight: 700; color: black;">33.35%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f7b396; font-weight: 700; color: black;">16.53%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #f39689; font-weight: 700; color: black;">9.37%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; background-color: #fbd8a9; font-weight: 700; color: black;">34.24%</td>
<td style="text-align: center; padding: 8px; border: 1px solid #e0e0e0; color: black;"></td>
</tr>
</tbody>
</table>

This makes retrieval a lot more reliable and can replace architectures with multiple models with a single, unified retriever.

### Inference speed

Despite being more than twice as big, LFM2-ColBERT-350M demonstrates throughput performance on par with GTE-ModernColBERT-v1 for query and document encoding across various batch sizes.

Query encoding was evaluated using realistic query patterns from datasets like MS MARCO and Natural Questions.

![image](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/P2seQD9MdKHykrm35Yvp_.png)

Document encoding was measured on realistic documents with varying lengths and domains.

![image](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/naj9300CQfikdW4i15xEc.png)

## 📬 Contact

- Got questions or want to connect? [Join our Discord community](https://discord.com/invite/liquid-ai)
- If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).



## Citation

```
@article{liquidai2025lfm2,
 title={LFM2 Technical Report},
 author={Liquid AI},
 journal={arXiv preprint arXiv:2511.23404},
 year={2025}
}
```

```bibtex
@misc{PyLate,
title={PyLate: Flexible Training and Retrieval for Late Interaction Models},
author={Chaffin, Antoine and Sourty, Raphaël},
url={https://github.com/lightonai/pylate},
year={2024}
}
```