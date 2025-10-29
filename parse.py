#!/bin/python

import sys
import toml
import requests
import os
from git import Repo

def download_file(url, save_path):
    # Envoie une requête GET avec redirection automatique (comme -L dans curl)
    response = requests.get(url, allow_redirects=True)
    # Vérifie si la requête a réussi
    if response.status_code == 200:
        # Écrit le contenu dans un fichier
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Fichier téléchargé et enregistré sous {save_path}")
    else:
        print(f"Erreur lors du téléchargement : {response.status_code}")

def read_local_config_file(bpm_path):
    try:
        # Lire le fichier TOML
        with open(bpm_path, 'r') as file:
            data = toml.load(file)
        return data

    except FileNotFoundError:
        print(f"'{bpm_path}' not found")
    except toml.TomlDecodeError:
        print(f"Impossible to read d'{bpm_path}'.")



def add_indent_and_prefix(name, version, output_file):
    input_file = f"tmp/usr/share/{name}/{version}/README.md"
    input_file_bpm = f"tmp/etc/bpm//{name}/{version}/bpm.tml"

    metadata_toml = read_local_config_file(input_file_bpm)
    if "dependencies" in metadata_toml:
        dependencies = metadata_toml["dependencies"]
        if len(dependencies) != 0:
            all_dependencies = "=== \"Dependencies\"\n"
            for key, value in dependencies.items():
                all_dependencies = all_dependencies + f"    {key} {value}"



    output_file = f"{output_file}"
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        body = f"# {name}\n" + "=== \"Readme\"\n"
        for line in infile:
            if not line.startswith("# "):
                body = body + f"    {line}"
        body = body + all_dependencies
        #body = body + f"=== \"Dependencies\"\n"
        metadata = f"<h1>Metadata</h1>\n* 8 days ago\n * v1.61.0\n* MIT OR Apache-2.0\n* 272 KiB\n* Install\n* Run the following Cargo command in your project directory:\n * cargo add {name}\nOr add the following line to your Cargo.toml:\nver = \"{version}\"\n* Documentation\nfixme\nRepository\nFIXME\nOwners\FIXME\nFIXME\nCategories\nFIXME\nFIXME\n"

        outfile.write(f"#<div class=\"main-content\"><div class=\"content-left\">{body}</div>\n<div class=\"content-right\">{metadata}\n</div>\n</div>\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv[1])
        print(sys.argv[2])
        name = sys.argv[1]
        version = sys.argv[2]
        # name_nolib=$(echo "${PCK_NAME}" | sed 's/lib$//')
        # mkdir tmp/
        print(f"http://repo.orix.oric.org/dists/{version}/tgz/6502/{name}.tgz")
        # curl -L http://repo.orix.oric.org/dists/${VERSION}/tgz/6502/${PCK_NAME}.tgz | tar -xz -C tmp/
        #     # mkdir -p docs/${name_nolib}/${VERSION}/
        url = f"http://repo.orix.oric.org/dists/{VERSION}/tgz/6502/{name}.tgz"
        save_path = f"{name}.tgz"  # Nom du fichier local

        download_file(url, save_path)
        repo = Repo('.')
        add_indent_and_prefix(name, version, f"docs/{name}/{version}/index.md")
    else:
        print("Please provide a filename as an argument.")
