# Project Description
I am working on a simple Python Artificially Intelligent ChatBot project to take standard user input from the user, store it to a "knowledge base" (in this project a txt file), and ensure no case or type sensitive issues cause faulty output results from it. Additionally each user can create their oen personalized knowledge base to access answers to questions pertaining to them, along with training their chatbot to their liking.


# Added on fauxtrot fork:

## Installation: 

```bash
git clone https://github.com/fauxtrot/SkyFlareAI
```

## Conda Environment Management

With a conda environment, you can now get your dependencies:

```bash
conda env create -f=env.yml
```

## Ensure that you have the spacey language file
- Windows

```bash
setup.bat
```

-linux
```bash
./setup.sh
```


Then start the process:
```bash
python ./AI.py
```

# TODOs

- Add args for loading an initial file.
- update file security
- Using python3 classify the chatbot
- starlit interface?
- Add conversational interface using huggingface libraries.
- Ability to save output from conversational model to file.
- Additional Model Management (default is spacy `en-core-web-lg`)

