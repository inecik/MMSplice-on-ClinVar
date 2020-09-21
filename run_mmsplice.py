#!/Users/kemalinecik/miniconda3/envs/mrkdwn/bin/python

# Kemal Inecik
# k.inecik@gmail.com

import subprocess
from mmsplice.vcf_dataloader import SplicingVCFDataloader
from mmsplice import MMSplice, predict_save

# Data files
gtf = "data/chr1.gtf"
vcf_ben = "data/clinvar_chr1_benign"
vcf_pat = "data/clinvar_chr1_pathogenic"
fasta = "data/chr1.fa"

# Repeat the process for benign and pathogenic variants
for vcf, typ in zip([vcf_ben, vcf_pat], ["benign", "pathogenic"]):
    print(f"\n\n\nRunning MMSPlice for {typ}.\n\n\n")

    # Filtering VCF file
    subprocess.call(f"echo 'Quality filtering has not been applied for {typ}.'", shell=True)
    subprocess.call(f"bcftools norm -m-both -o {vcf + '_temp.vcf'} {vcf + '.vcf.gz'}", shell=True)
    subprocess.call(f"bcftools norm -f {fasta} -o {vcf + '.vcf'} {vcf + '_temp.vcf'}", shell=True)
    vcf = vcf + '.vcf'

    # Run MMSplice
    dl = SplicingVCFDataloader(gtf, fasta, vcf, tissue_specific=False)
    model = MMSplice()
    predict_save(model, dl, f"mmsplice_output/predictions_{typ}.csv", pathogenicity=True, splicing_efficiency=True)
