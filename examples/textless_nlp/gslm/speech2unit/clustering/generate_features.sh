python3 quantize_with_kmeans.py --feature_type hubert \
  --manifest_path manifest \
  --out_quantized_file_path vits.quantized \
  --acoustic_model_path hubert/hubert_base_ls960.pt \
  --kmeans_model_path hubert/km_100.bin \
  --layer 6