from huggingface_hub import login, snapshot_download
from dotenv import load_dotenv
import os

load_dotenv()

huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")

if not huggingface_api_key:
    raise ValueError("HUGGINGFACE_API_KEY environment variable is not set")

os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

login(token=huggingface_api_key)

try:
    model_path = snapshot_download(
        repo_id="meta-llama/Llama-3.2-3B",
        local_dir="../../models/llama_models/llama-3.2-3B",
        token=huggingface_api_key,
        max_workers=8
    )
    print(f"Model downloaded to {model_path}")
except Exception as e:
    print(f"Error downloading model: {str(e)}")
    print(f"Current working directory: {os.getcwd()}")
    raise

# or use this: huggingface-cli download meta-llama/Llama-3.2-3B --local-dir models/llama_models/llama-3.2-3B