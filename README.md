# Project Description

An Artificial Intelligence ChatBot Python project which parses standard user input, persistently store data in a text file knowledge base and implement case and type sensitivity handling to enhance output accuracy. A user-centric knowledge base system was implemented, enabling each user to tailor their own personalized knowledge repositories for specialized query responses and chatbot training.

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

=======
