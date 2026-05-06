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

6. Create a virutal enviroment using venv

```
python3 -m venv hailofdc
source hailodfc/bin/activate
```

7. Go to the Hailo Developer Zone and download Hailo Dataflow Compiler version 3.33.0

8. Next open the wsl file location. This can be done using

```
wslview .
```

9. Move the downloaded Dataflow Compiler to the opened folder

10. Install the Dataflow Compiler

```
pip3 install hailo_dataflow_compiler-3.28.0-py3-none-linux_x86_64.whl
```

11. Verify the installation

```
hailo -h
pip freeze | grep hailo
```

12. Now install the Hailo Model Zoo

```
git clone https://github.com/hailo-ai/hailo_model_zoo.git
```

13. Run the setup script

```
cd hailo_model_zoo; pip install -e .
```

14. 
