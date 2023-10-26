# asset reconciler backend


## Getting Started

To use this code, follow the steps below to set up the environment:

### Prerequisites

- Python 3.x

### Clone the Repository

```bash
git clone git@github.com:achrefbenmbarek1/assetReconcilerBackend.git
cd inventoryMatcher 
```
### Install the virtual environment

```bash
python3 -m pip install virtualenv
```
### Create a virtual environment

Create a new virtual environment named .venv/inventoryMatcher

```bash
python3 -m venv .venv/inventoryMatcher
```

### Activate the virtual environment
On macOS and Linux:

```bash
source .venv/inventoryMatcher/bin/activate
```
On Windows:
.venv/inventoryMatcher\Scripts\activate

### Install dependencies
Once the virtual environment is activated, use the following command to install the required dependencies:

```bash
python3 -m pip install -r requirements.txt
```

### Running the project
Now that everything is set up, from the root of the project go to the inventoryMatcher/src directory you can run the project using the python3 command:

```bash
cd inventoryMatcher/src
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

```
And in an other terminal go to the inventoryMatcher directory and run
```bash
source .venv/inventoryMatcher/bin/activate
celery -A tasks worker --loglevel=info

```
### Running tests
from the root of the project(the directory inventoryMatcher) go to the test directory :

####Unit tests
go to the unitTest directory and run pytest as shown:

```bash
cd unitTest
pytest -vv
```

