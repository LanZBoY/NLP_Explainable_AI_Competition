python -m venv bertEnv
.\bertEnv\Scripts\Activate.ps1
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
pip install transformers[torch]
pip install datasets
pip install evaluate