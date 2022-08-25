from os import listdir
from os.path import isfile, join

dataset_path = "/mnt/datasets/vits_ss_slt_eval"
output_path = "manifest"
audio_files = [f for f in listdir(dataset_path)
               if isfile(join(dataset_path, f)) and (".wav" in f)
               ]
audio_files.sort()

with open(output_path, "w+") as f:
    f.write(dataset_path+"\n")
    for idx, audio_file in enumerate(audio_files):
        f.write(f"{audio_file}\t{str(idx)}\n")
