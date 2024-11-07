import argparse
import requests

def main() -> int:
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("url")
        parser.add_argument("output")
        args = parser.parse_args()
        url = args.url
        output = args.output

        response = requests.get(f"{url}")
        file = open(f"data/{output}", "w")
        file.write(response.text)
        file.close()
        return 0
    except Exception as e:
        return e

def write_fetch(url:str, output:str) -> int:
    try:
        response = requests.get(f"{url}")
        file = open(f"data/{output}", "w")
        file.write(response.text)
        file.close()
        return 0
    except Exception as e:
        return e

if __name__ == "__main__":
    main()
