python sample.py  hubert100_lm \
    --path=hubert100_lm/checkpoint_best.pt --task=language_modeling --sampling --temperature=0.7 \
    --seed=1  --prompts=vits_expanded.quantized  --output=samples.txt --max-len-a=0 --max-len-b=235 \
    --prefix-size=-1 --batch-size=16 --fp16 --samples-per-prompt=1