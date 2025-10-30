#!/bin/python

import sys
import toml
import requests
import os
from git import Repo
import tarfile


def generate_index():

    chemin_docs = "docs"
    contenu_docs = os.listdir("docs")
    repertoires = [element for element in contenu_docs
                if os.path.isdir(os.path.join("docs", element))]


    index = "# Welcome to the Oric Libraries repository!\n\n"
    index += "[Download bpm](https://orix-software.github.io/bpm/installation/){ .md-button }\n\n"
    index += "<div class=\"grid cards\" markdown>\n"


    for repertoire in repertoires:
        if repertoire != "theme":
            sous_contenu_docs = os.listdir(f"docs/{repertoire}")
            sous_repertoires = [element for element in sous_contenu_docs
                        if os.path.isdir(os.path.join(f"docs/{repertoire}", element))]
            for sous_repertoire in sous_repertoires:
                #
                index += f"-  __{repertoire}__ v{sous_repertoire}\n[:fontawesome-solid-arrow-right: ]({repertoire}/{sous_repertoire})\n"


    # index += "- __JavaScript__ for interactivity\n"
    # index += "- __CSS__ for text running out of boxes\n"
    # index += "-  __Internet Explorer__ ... huh?\n"
    index += "</div>"
    with open("docs/index.md", "w") as fichier:
        fichier.write(index)


def detar_gz(fichier_tgz, repertoire_destination):
    """
    Décompresse un fichier .tar.gz dans le répertoire de destination.

    :param fichier_tgz: Chemin vers le fichier .tar.gz à décompresser.
    :param repertoire_destination: Répertoire où extraire les fichiers.
    """
    # Crée le répertoire de destination s'il n'existe pas
    os.makedirs(repertoire_destination, exist_ok=True)

    # Ouvre le fichier .tar.gz en mode lecture
    with tarfile.open(fichier_tgz, "r:gz") as tar:
        # Extrait tous les fichiers dans le répertoire de destination
        tar.extractall(path=repertoire_destination)

    print(f"Fichier {fichier_tgz} décompressé dans {repertoire_destination}.")

# Exemple d'utilisation
fichier_tgz = "chemin/vers/ton_fichier.tgz"  # Remplace par le chemin de ton fichier
repertoire_destination = "chemin/vers/le/repertoire/de/destination"  # Remplace par le chemin de destination

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
    print(f"tmp/etc/bpm//{name}/{version}/bpm.tml")
    metadata_toml = read_local_config_file(input_file_bpm)
    all_dependencies = ""
    if "dependencies" in metadata_toml:
        dependencies = metadata_toml["dependencies"]
        if len(dependencies) != 0:
            all_dependencies = "=== \"Dependencies\"\n"
            for key, value in dependencies.items():
                all_dependencies = all_dependencies + f"    {key} {value}"

    if "package" in metadata_toml:
        package = metadata_toml["package"]
        if "description" in package:
            description = package["description"]
        if "cpu" in package:
            cpu = package["cpu"]
        if "repository" in package:
            repository = package["repository"]
        if "documentation" in package:
            documentation = package["documentation"]
        if "homepage" in package:
            homepage = package["homepage"]
        if "orix_minimal_kernel_version" in package:
            orix_minimal_kernel_version = package["orix_minimal_kernel_version"]

    output_file = f"{output_file}"
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        body = f"{name} {version}\n{description}\n" + "=== \"Readme\"\n"
        for line in infile:
            if not line.startswith("# "):
                body = body + f"    {line}"
        body = body + f"\n=== \"Versions\"\n"
        body = body + all_dependencies
        body = body + f"\n=== \"Dependencies\"\n"
        metadata = f"<h1>Metadata</h1><br>* 8 days ago<br><br>v{version}<br>* MIT OR Apache-2.0<br>* 272 KiB<br><br><b>Install</b><br><br>un the following bpm command in your project directory:<br><p class=\"encadre\">bpm add {name}</p><br>Or add the following line to your bpm.tml:<br>ver = \"{version}\"<br>* Documentation<br>fixme<br>Repository<br>{repository}<br>Owners\FIXME<br>FIXME<br>Categories<br>FIXME<br>FIXME<br>"
        body = body + f"\n=== \"Dependents\"\n"
        outfile.write(f"#<div class=\"main-content\"><div class=\"content-left\">{body}</div>\n<div class=\"content-right\">{metadata}\n</div>\n</div>\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv[1])
        print(sys.argv[2])
        name = sys.argv[1]
        version = sys.argv[2]
        skip_download = "False"
        skip_repo_add = "True"
        if sys.argv == 3:
            skip_download = sys.argv[3]
        if sys.argv == 4:
            skip_repo_add= sys.argv[4]
        # name_nolib=$(echo "${PCK_NAME}" | sed 's/lib$//')
        # mkdir tmp/
        print(f"http://repo.orix.oric.org/dists/{version}/tgz/6502/{name}.tgz")
        # curl -L http://repo.orix.oric.org/dists/${VERSION}/tgz/6502/${PCK_NAME}.tgz | tar -xz -C tmp/
        #     # mkdir -p docs/${name_nolib}/${VERSION}/
        url = f"http://repo.orix.oric.org/dists/{version}/tgz/6502/{name}.tgz"
        os.makedirs(f"tml/{name}/{version}/", exist_ok=True)
        os.makedirs(f"tmp/", exist_ok=True)
        save_path = f"docs/{name}/{version}/{name}.tgz"  # Nom du fichier local
        if skip_download == "False":
            download_file(url, f"tmp/{name}.tgz")
            detar_gz(f"tmp/{name}.tgz", "tmp/")

        # Save tml
        if skip_repo_add == "False":
            repo = Repo('.')
            tml_path = f"tmp/etc/bpm/{name}/{version}/bpm.tml"
            if not os.path.exists(tml_path):
                repo.index.add([tml_path])
            commit_message = f"Ajout du fichier {tml_path} via script Python"
            repo.index.commit(commit_message)

            # Push sur la branche main
            origin = repo.remote(name="origin")
            origin.push("main")


        add_indent_and_prefix(name, version, f"docs/{name}/{version}/index.md")
        if skip_repo_add == "False":
            repo = Repo('.')
            markdown_path = f"docs/{name}/{version}/index.md"
            if not os.path.exists(markdown_path):
                repo.index.add([markdown_path])
            commit_message = f"Ajout du fichier {markdown_path} via script Python"
            repo.index.commit(commit_message)

            # Push sur la branche main
            origin = repo.remote(name="origin")
            origin.push("main")

        generate_index()

        if skip_repo_add == "False":
            repo = Repo('.')
            index_path = f"docs/index.md"
            #repo.index.add([index_path])
            commit_message = f"Ajout du fichier {index_path} via script Python"
            repo.index.commit(commit_message)

            # Push sur la branche main
            origin = repo.remote(name="origin")
            origin.push("main")

    else:
        print("Please provide a filename as an argument.")
