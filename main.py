import argparse
import os

from tqdm import tqdm
from prompting import open_ai_prompt
from text_processing import read_data

parser = argparse.ArgumentParser()
parser.add_argument('--start')
parser.add_argument('--step')
parser.add_argument('--provider')
args = parser.parse_args()

PROMPT_TEMPLATE_NAME = "chain-of-thought"
DATA_PATH = "data/test.csv"
RESPONSE_DIR = "response"

def main():
    start = int(args.start)
    step = int(args.step)
    provider = args.provider

    response_path = os.path.join(RESPONSE_DIR, PROMPT_TEMPLATE_NAME, provider)
    if not os.path.exists(response_path):
        os.makedirs(response_path)

    with open("prompt_template/" + PROMPT_TEMPLATE_NAME + ".txt", "r", encoding="utf-8") as f:
        cot_prompt_template = f.read()
    content, label = read_data(DATA_PATH)

    if provider == "openai":
        prompt_fnc = open_ai_prompt
    elif provider == "google-ai":
        prompt_fnc = ""
    else:
        raise ValueError("Unsupported provider")

    for i in tqdm(range(start, start + step), desc="Processing", unit="step"):
        if i >= len(content):
            break

        prompt_rs = prompt_fnc(content[i], cot_prompt_template)
        prompt_rs_name = str(i) + ".txt"
        with open(os.path.join(response_path, prompt_rs_name),"w", encoding="utf-8") as fp:
            fp.write(prompt_rs)
            fp.write("\n")


if __name__ == '__main__':
    main()