# NGHIÊM THE DS'S MINI-TOOL

This framework is designed for handling NLP (prompting) task with LLMs through the APIs of LLM providers.
## Installation
1. Clone this reponsitory:

```
https://github.com/NghiemCanCode/Prompt_framework.git
cd Prompt_framework
```
2. Create and activate a virtual environment:
- On Windows
    ```
    python -m venv .venv
    .venv\Scripts\activate.bat
    ```
- On Linux
    ```
    virtualenv .venv
    source .venv/bin/activate
    ```
3. Install required packages:

  ```
  pip install -r requirements.txt
  ```
## Environment Setup
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_OPENAI_key
GEMINI_API_KEY=your_GEMINI_key
# Add other environment-specific variables as needed
```
## Run the code
Use the ```main.py``` script with command-line arguments to run the system.
```
python main.py --start 0 --step 10 --provider "openai"
```
Some important arguments:
- ``--start``: Index of start data line.
- ``--step``: How many data line do you want to handle.
- ``--provider``: Provider of LLM (default is ``openai``)
- 
All arguments have document, use ```--help``` for more information.

The easiest way to parallel processing is run this script many times. (You will know the reason when you handle a big dataset).

## Project Structure
```
├── data                   # Your dataset
├── response               # Response after call API
    ├── <prompt_template_name>
        ├── <provider_name>
            ├── <data_index>.txt
            ├── ....
        ├── ....
├── prompt_template        # Your prompt template file
├── prompting              # LLM call by API
├── main.py                # Main application file
├── utils.py               # Reprocessing, postprocessing and other
├── result.ipynb           # Notebook to visualize result
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```
## Data (file) structure
- Data set file must be a ```.csv``` file with 2 columns ```text``` & ```label```
- Template for prompt must be a ```.txt``` that its content is a prompt template. Ex:
    ```
  Given the sentence "#123123123", what is this sentiment of sentence?
  Let's think step by step to answer.
    ```
  Note: ```#123123123``` is required.