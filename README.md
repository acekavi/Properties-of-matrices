#!/bin/bash

# Writing README.md content to a file

cat <<EOL > README.md
# Properties of Matrices

## Overview
This repository explores various properties of matrices, including determinant calculation, eigenvalues, eigenvectors, and matrix operations such as addition, multiplication, and inversion. It serves as a resource for understanding matrix properties and their applications in linear algebra.

## Features
- Determinant calculation
- Eigenvalues and eigenvectors computation
- Matrix addition, multiplication, and inversion
- Examples and use cases

## Installation
1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/acekavi/Properties-of-matrices.git
   cd Properties-of-matrices
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Usage
### Running the Examples
Navigate to the directory and run the example scripts:
\`\`\`bash
python examples/determinant_example.py
python examples/eigenvalues_example.py
\`\`\`

### Interactive Mode
You can also explore matrix properties interactively using the provided Jupyter notebooks. Launch Jupyter Notebook and open the notebooks in the \`notebooks/\` directory:
\`\`\`bash
jupyter notebook
\`\`\`

## File Structure
- \`src/\`: Contains the source code for matrix operations.
  - \`matrix_operations.py\`: Functions for matrix addition, multiplication, and inversion.
  - \`determinant.py\`: Functions for determinant calculation.
  - \`eigenvalues.py\`: Functions for computing eigenvalues and eigenvectors.
- \`examples/\`: Example scripts demonstrating matrix operations.
  - \`determinant_example.py\`: Example for determinant calculation.
  - \`eigenvalues_example.py\`: Example for eigenvalues and eigenvectors.
- \`notebooks/\`: Jupyter notebooks for interactive exploration.
  - \`matrix_properties.ipynb\`: Notebook covering various matrix properties.
- \`README.md\`: This file.
- \`CONTRIBUTING.md\`: Guidelines for contributing to the project.
- \`LICENSE.md\`: License information.
- \`requirements.txt\`: List of dependencies.

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
EOL
