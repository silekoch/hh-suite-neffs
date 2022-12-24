FROM hhsuite_custom
RUN apt-get update
RUN apt-get install -y python3
ENV msa_dir=/mnt/project/marquet/MSA/Data/Proteomes/CF_MMSeqs2_MSA/UP000005640_9606/msas
ENV neff_dir=/mnt/project/koch/af22c/data/UP000005640_9606/neffs_hhsuite
ENV prot_ids=/mnt/project/koch/af22c/data/prot_ids.csv
RUN mkdir /app
COPY compute_neffs.sh /app
COPY extract_neffs.py /app
CMD /app/compute_neffs.sh
