# Training LLM

Ce projet utilise un **LLM** (Large Language Model) avec [Ollama](https://ollama.com) et [Langchain](https://python.langchain.com/en/latest/). 

Le but est de permettre aux développeurs de s'entraîner et de manipuler des LLM en local.


## Prérequis

Avant de commencer, assurez-vous que les éléments suivants sont installés sur votre machine :
- Python 3.8 ou supérieur
- Installez les dépendances Python requises :
    ```bash
    pip install -r requirements.txt
    ```
- [Ollama](https://ollama.com), pour télécharger et utiliser les modèles **LLM** en local : 
    - Téléchargez et installez **Ollama** depuis le site officiel : [Ollama Download](https://ollama.com/download).

    - Vérifiez que l'installation d'**Ollama** a réussi en exécutant la commande suivante dans votre terminal :
        ```bash
        ollama --version
        ```
    - Exécutez la commande suivante dans votre terminal pour télécharger le modèle LLaMA3 our pouvoir l'utiliser dans votre projet :
        ```bash
        ollama pull llama3
        ```
    