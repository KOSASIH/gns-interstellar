<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/KOSASIH/gns-interstellar">Galactic Navigation System ( GNS ) </a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.linkedin.com/in/kosasih-81b46b5a">KOSASIH</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>

# gns-interstellar
A Git repo for the Galactic Navigation System project, containing code for advanced algorithms for positioning, mapping, and collision avoidance.

# Galactic Navigation System (gns-interstellar)

This repository contains the codebase for the Galactic Navigation System (GNS), an advanced system for positioning, mapping, and collision avoidance.

## Table of Contents

Getting Started
Dependencies
Building
Running
Documentation
Citation
Training

# Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

Ensure you have the following installed:

- Git
- CMake
- Python 3.9
- Conda

## Installing

1. Clone the repository:

```
git clone --recurse-submodules https://github.com/KOSASIH/gns-interstellar.git`
```

2. Create a conda environment:

```
cd gns-interstellar
conda create -n gns python=3.9 cmake=3.22
conda activate gns
```

3. Download and install the Vulkan SDK:

```
mkdir vulkansdk
cd vulkansdk
wget https://sdk.lunarg.com/sdk/download/1.2.198.1/linux/vulkansdk-linux-x86_64-1.2.198.1.tar.gz
tar -xf vulkansdk-linux-x86_64-1.2.198.1.tar.gz
source 1.2.198.1/setup-env.sh
cd ../
```

5. Install PyTorch with CUDA 11.0+:

```
conda install pytorch=1.11 pytorch-cuda=11.7 -c pytorch -c nvidia
python -c "import torch; print(torch.version.cuda)"
```

6. Install the required Python packages:


`pip install -r requirements.txt`

# Dependencies

- Vulkan SDK
- PyTorch 1.11 with CUDA 11.0+
- CMake 3.22+

# Building

Build the C++ components:

```
mkdir build
cd build
cmake ..
make
```

# Running

Run the Python scripts:

`python main.py`

# Documentation

The documentation is available in the docs folder. To generate the documentation, run:

```
cd docs
make html
```

The generated documentation will be available in the _build/html folder.

# Citation

If you use this code in your research, please cite the following:

```
@article{your-paper,
  title={Your Paper Title},
  author={Your Name},
  journal={Journal Name},
  year={Year},
  publisher={Publisher},
  url={https://your-paper-url.com}
}
```

# Training

To train the neural network, run:

`python train.py`

This will train the network using the default settings. You can modify the settings in the train.py file.For more information, refer to the [Training Guide](training_guide.md) 

