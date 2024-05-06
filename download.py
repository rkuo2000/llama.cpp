import sys
from huggingface_hub import snapshot_download

model_id="lmsys/vicuna-13b-v1.5"
model_id = sys.argv[1]
snapshot_download(repo_id=model_id, local_dir="model-hf", local_dir_use_symlinks=False, revision="main")
