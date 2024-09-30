# Onto-X Project

This project is designed to parse a CSV file containing an ontology of pathologies and retrieve the hierarchy of related pathologies (parents, siblings) based on a given entity.

## Project Structure

- `src/`: Contains the source code
  - `parsing.py`: Includes the function to parse the CSV file
  - `hierarchy.py`: Contains the functions to retrieve the hierarchy of entities
  - `main.py`: The main script to run the program

- `data/`: Contains the CSV data files

## Setup Instructions

1. Clone the repository.
2. Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # Sur Linux/macOS
venv\Scripts\activate     # Sur Windows
```
3. Install the project dependencies:
```
pip install -r requirements.txt
```
4. Place your CSV file in the `data/` folder. 

5. Run the main script  `main.py` from the `src/` directory:
   ```
   python src/main.py
   ```
   
## Key Points : To be finished!

### Pathology Hierarchy Retrieval

Each row in the CSV represents a pathology and its parent(s). For example, considering the provided sample for "CERVIX DISORDER", the hierarchy is structured as follows:

* GYNECOLOGIC DISORDERS has a depth of 2 (parent of the parent).
* CERVIX DISORDERS has a depth of 1 (direct parent).
* CERVICITIS, CERVIX NEOPLASM, and PAPANICOLAU SMEAR SUSPICIOUS have a depth of 0 (siblings).

#### Recursive Ancestor Retrieval

The get_ancestors_and_siblings function uses recursion to retrieve the complete hierarchy of a pathology, enabling it to trace all parent entities up to the root.

#### Sibling Loop Issue

### Jupyter Notebook for Testing

### Virtual Environment for Portability

Using a virtual environment helps ensure the project’s dependencies are isolated, which makes the code easier to export and later integrate with Docker for containerization.

### Code Structure and Separation of Concerns

### Documentation

Each function in the code is accompanied by detailed docstrings to ensure clarity and provide documentation directly within the codebase. The docstrings are currently written in french, and should be 

## Areas for improvement

* The docstrings are currently in French, but they should be written in English.
* The commits should contain only one keypoint at a time, note 3-4 like here.
* 