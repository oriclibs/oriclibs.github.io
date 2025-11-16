#!/bin/python

import sys
import toml
import requests
import os
import tarfile
from datetime import datetime

def generate_index():

    chemin_docs = "docs"
    contenu_docs = os.listdir("docs")
    # repertoires = [element for element in contenu_docs
    #             if os.path.isdir(os.path.join("docs", element))]


    repertoires = sorted([d for d in os.listdir("docs")
                          if os.path.isdir(os.path.join("docs", d))],
                          reverse=True)

    index = "---\nhide:\n  - navigation\n  - toc\n---\n# Welcome to the Orix repository!\n\n"
    index += "[Download bpm](https://orix-software.github.io/bpm/installation/){ .md-button }\n\n"
    index += "<div class=\"grid cards\" markdown>\n"


    for repertoire in repertoires:
        if repertoire != "theme":
            sous_contenu_docs = os.listdir(f"docs/{repertoire}")

            sous_repertoires = sorted([element for element in sous_contenu_docs
                        if os.path.isdir(os.path.join(f"docs/{repertoire}", element))], reverse=True)
            for sous_repertoire in sous_repertoires:
                date_hours = "Unknown"
                name = repertoire
                version = sous_repertoire
                try:
                    with open(f"docs/{name}/{version}/updated_date.txt", "r") as fichier:
                        date_hours = fichier.read()

                except FileNotFoundError:
                    print(f"docs/{name}/{version}/updated_date.txt not found")
                index += f"-  __{repertoire}__ v{sous_repertoire}\n<br>Released date : {date_hours}\n[:fontawesome-solid-arrow-right: ]({repertoire}/{sous_repertoire})\n"
                break

    index += "</div>"
    with open("docs/index.md", "w") as fichier:
        fichier.write(index)
    print(index)


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


def download_file(url: str, save_path: str) -> int:
    # Envoie une requête GET avec redirection automatique (comme -L dans curl)
    response = requests.get(url, allow_redirects=True)
    # Vérifie si la requête a réussi
    if response.status_code == 200:
        # Écrit le contenu dans un fichier
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloading : {url} Fichier téléchargé et enregistré sous {save_path}")
        return 0
    else:
        print(f"Erreur lors du téléchargement : {response.status_code}")
        return 1

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



def add_indent_and_prefix(name, version, output_file, date_heure="Unknown"):
    input_file = f"tmp/usr/share/{name}/{version}/README.md"
    input_file_bpm = f"tmp/etc/bpm//{name}/{version}/bpm.tml"
    print(f"tmp/etc/bpm//{name}/{version}/bpm.tml")
    metadata_toml = read_local_config_file(input_file_bpm)
    if metadata_toml is None:
        print(f"ERROR : No metadata toml found for this package {name} {version}.")
        return
    all_dependencies = ""
    if "dependencies" in metadata_toml:
        dependencies = metadata_toml["dependencies"]
        if len(dependencies) != 0:
            for key, value in dependencies.items():
                all_dependencies = all_dependencies + f"    !!! abstract \"[{key} {value}](../../{key}/{value} )\"\n"

    all_versions = ""
    repertoires = sorted([d for d in os.listdir(f"docs/{name}") if os.path.isdir(os.path.join(f"docs/{name}", d))], reverse=True)
    for repertoire in repertoires:
        print(f"ici {repertoire}")
        if repertoire != version:
            #[Lien vers le répertoire toto](../toto)
            all_versions = all_versions + f"    !!! abstract \"[{name} : {repertoire}](../{repertoire})\"\n"

    if "package" in metadata_toml:
        package = metadata_toml["package"]
        if "description" in package:
            description = package["description"]
        if "cpu" in package:
            cpu = package["cpu"]
        repository = ""
        if "repository" in package:
            repository = package["repository"]
        if "documentation" in package:
            documentation = package["documentation"]
        if "homepage" in package:
            homepage = package["homepage"]
        if "authors" in package:
            authors = package["authors"]
            for author in authors:
                authors = author + ", "
        if "orix_minimal_kernel_version" in package:
            orix_minimal_kernel_version = package["orix_minimal_kernel_version"]

    output_file = f"{output_file}"
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        body = f"{name} {version}\n{description}\n" + "=== \"Readme\"\n"
        for line in infile:
            if not line.startswith("# "):
                body = body + f"    {line}"
        body = body + f"\n=== \"Versions\"\n\n{all_versions}"
        body = body + f"\n=== \"Dependencies\"\n\n"
        body = body + all_dependencies
        metadata = f"<h1>Metadata</h1><br><b>Version :</b> {version}<br><br><b>Install:</b><br><br><i>Orix</i><br>download tgz : http://repo.orix.oric.org/dists/{version}/tgz/6502/{name}.tgz<br><i><br><br>Install as library (for development purposes):</i><br>Use the following bpm command in your project directory:<br><p class=\"encadre\">bpm add {name}@{version}</p><br>"
        metadata = metadata + f"<b>Documentation :</b> {documentation}<br><br><b>Repository : </b>{repository}<br><br><b>Authors:</b> {authors}"
        body = body + f"\n=== \"Dependents\"\n"
        outfile.write(f"---\nhide:\n  - navigation\n  - toc\n---\n#<div class=\"\"><div class=\"content-left\">{body}</div>\n<div class=\"content-right\">{metadata}\n</div>\n</div>\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv[1])
        print(sys.argv[2])
        name = sys.argv[1]
        version = sys.argv[2]
        skip_download = "False"
        typepck = "lib"
        if sys.argv == 3:
            skip_download = sys.argv[3]
        if sys.argv == 4:
            typepck = sys.argv[4]

        # name_nolib=$(echo "${PCK_NAME}" | sed 's/lib$//')
        # mkdir tmp/

        url = f"http://repo.orix.oric.org/dists/{version}/tgz/6502/{name}.tgz"
        os.makedirs(f"tml/{name}/{version}/", exist_ok=True)
        os.makedirs(f"tmp/", exist_ok=True)
        save_path = f"docs/{name}/{version}/{name}.tgz"  # Nom du fichier local
        if skip_download == "False":
            val = download_file(url, f"tmp/{name}.tgz")
            if val == 0:
                detar_gz(f"tmp/{name}.tgz", "tmp/")
            else:
                print("Download failed, exiting.")
                sys.exit(1)


        # Obtenir la date et l'heure actuelles
        maintenant = datetime.now()

        # Formater la date et l'heure
        date_heure = maintenant.strftime("%Y-%m-%d %H:%M:%S")

        os.makedirs(f"docs/{name}/{version}", exist_ok=True)
        add_indent_and_prefix(name, version, f"docs/{name}/{version}/index.md", date_heure)


        # Écrire dans un fichier
        with open(f"docs/{name}/{version}/updated_date.txt", "w") as fichier:
            fichier.write(date_heure)


        generate_index()

    else:
        print("Please provide a filename as an argument.")
        contenu_docs = os.listdir("docs")
        repertoires = [element for element in contenu_docs
                    if os.path.isdir(os.path.join("docs", element))]

        index = "# Welcome to the Orix repository!\n\n"
        for repertoire in repertoires:
            if repertoire != "theme":
                sous_contenu_docs = os.listdir(f"docs/{repertoire}")
                sous_repertoires = [element for element in sous_contenu_docs
                            if os.path.isdir(os.path.join(f"docs/{repertoire}", element))]
                for sous_repertoire in sous_repertoires:
                    version = sous_repertoire
                    name = repertoire
                    url = f"http://repo.orix.oric.org/dists/{version}/tgz/6502/{name}.tgz"
                    os.makedirs(f"tml/{name}/{version}/", exist_ok=True)
                    os.makedirs(f"tmp/", exist_ok=True)
                    save_path = f"docs/{name}/{version}/{name}.tgz"  # Nom du fichier local
                    download_file(url, f"tmp/{name}.tgz")
                    detar_gz(f"tmp/{name}.tgz", "tmp/")
                    add_indent_and_prefix(name, version, f"docs/{name}/{version}/index.md")
        generate_index()