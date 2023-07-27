# AltLinux API CLI

This program is used to compare binary package lists from two different branches in the AltLinux distribution. It utilizes the [AltLinux REST API](https://rdb.altlinux.org/api/) to obtain package lists and the [packaging.version](https://packaging.pypa.io/en/latest/version.html) module to compare package versions.

## Installation
1. Clone the [repository](https://github.com/arkrivenko/altlinux_api) to your local machine or download the files as a zip archive.

2. Install the required packages:

```
pip install requests packaging
```

## Usage
1. Run the program `cli.py` using the following command:
```
python cli.py --branch1 <branch1> --branch2 <branch2> -o <output_file>
```
Replace **&lt;branch1&gt;** and **&lt;branch2&gt;** with the names of the branches you want to compare. Replace **&lt;output_file&gt;** with the name of output file with json format.
2. The program will output the package comparison result in JSON format.

## API
The API module `api.py` contains the AltLinuxAPI class, which is used for accessing the [AltLinux REST API](https://rdb.altlinux.org/api/). The **export_branch_binary_packages** method is used to obtain binary package lists from a specific branch.

## Comparison
The comparison module `comparison.py` contains the **Comparator** class, which is used for comparing two lists of binary packages. The **compare_packages** method returns a JSON object containing three lists: ***only_in_package1***, which contains packages only in the first list; ***only_in_package2***, which contains packages only in the second list; and ***higher_in_package1***, which contains packages with a higher version-release in the first list compared to the second list.

## CLI
The CLI module `cli.py` is used to provide a command line interface to the program. The program takes three arguments: ***--branch1*** for the first branch name, ***--branch2*** for the second branch name, ***-o*** for the output filename. The output of the program is a JSON object containing package comparison results for each architecture supported by AltLinux.