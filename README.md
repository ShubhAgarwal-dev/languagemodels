# languagemodels

This is the the official **DevHack 4.0** Hackathon Repository. Participants list:
-  Divy Jain (210010015)
-  Vivek Pillai (210010058)
-  Karthik Hegde (210010022)
-  Shubh Agarwal (210020047)

[Report Link](https://docs.google.com/document/d/1X2Ip_jUD6hoqVXg88Mf6ZKAaGaZh2mznHGZjWrpNxDk/edit?usp=sharing) <br />
[Sample Research Paper](https://drive.google.com/file/d/1KT31DzDvVDgHAxSjYrNYfeb53NkoiIHM/view?usp=sharing)

## Installation Guide

We assume *Linux* environment for local installation, `python>=3.9` is required. Follow the given steps to replicate:

```sh
# the steps given in this block are optional, but RECOMMENDED 
sudo apt-get install python3-virtualenv
# go to languagemodels directory, the one you will get after cloning
virtualenv ./env
source ./env/bin/activate
```

The replication parts starts from below:

```sh
git clone https://github.com/ShubhAgarwal-dev/languagemodels.git
cd languagemodels
# activate the environment using source ./env/bin/activate, if made
pip install "fastapi[all]"
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install python-multipart
pip install transformers
```

For Summary Model:
```sh
pip install sentencepiece
```

For Question-Answer Pair Generator Model:
```sh
pip install nltk
python -m nltk.downloader punkt
pip install protobuf==3.15.8
```

For translation Model:
```sh
pip install sentencepiece
pip install sacremoses
```

For PDF Text-Retriver:
```sh
pip install PyPDF2
```

**Now to start the server**
```
uvicorn main:app --reload
```

If you want to run API Server and clinet on different machines connected to the same network,  you can get your IP using `ifconfig`:
```sh
uvicorn --host <YOUR_IP_HERE> main:app --reload
```

If running the server for the first time, it is going to take a lot of time as a lot of models will be downloaded locally. Good internet connection is recommended. 

After everything is done, you can go to `localhost:8000/docs` or `<YOUR_IP_HERE>:8000/docs` for using the interface.
