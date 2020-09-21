# MMSplice-on-ClinVar
Evaluation of MMSplice pathogenicity scores on ClinVar Chr1

## Content:
- data/:
  - chr1.fa(.fai): chr1 reference sequence
  - chr1.gtf.gz: Ensembl reference annotation
  - clinvar_chr1_[benign|pathogenic].vcf.gz(.tbi): ClinVar variants on chromosome 1
- run_mmsplice.py: MMSplice to the ClinVar variants
- output: The output of the run_mmsplice.py
- analysis.ipynb: Analysis of the data
