# Step-by-step Guide for converting a .pt file to a .hef file, using WSL

1. Convert .pt file to .onnx, there is a sample script in this repository called ONNX_converter.py

2. Enable WSL

```
wsl --list --online
wsl --install -d Ubuntu-22.04
```

3. Restart your computer and then launch the Ubuntu WSL image
   
5. Install the dependencies on the Ubuntu images

```
sudo apt install python3-pip
sudo apt install python3.10-venv
sudo apt-get install python3.10-dev python3.10-distutils python3-tk libfuse2 graphviz libgraphviz-dev
sudo pip install pygraphviz
sudo apt install wslu
```

6. 
