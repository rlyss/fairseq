import os

quantized_path = "vits.quantized"
with open(quantized_path, "r") as f, \
    open(f"{quantized_path}.temp", "w+") as out:
    for line in f:
        [id, features] = line.split("|")
        tokens = features.split(" ")

        for i in range(0, len(tokens)):
            out_tokens = ' '.join(tokens[0:i+1])
            out.write(f"{id}_{i+1}|{out_tokens}")
            if i != len(tokens) - 1:
                out.write("\n")


with open(f"{quantized_path}.temp") as infile, open(f"{quantized_path}.expanded", 'w+') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output

os.remove(f"{quantized_path}.temp")