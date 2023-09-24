![Tests](https://github.com/arsh73552/Epidemic-Simulator/actions/workflows/tests.yml/badge.svg)


https://github.com/arsh73552/Epidemic-Simulator/assets/91689879/4d200395-968c-4cc1-8003-daadd131f557



# Epidemic Simulator

Welcome to the Epidemic Simulator project! This is an epidemic simulation tool built using the ManimGL library and OpenGL renderer. It allows you to choose a point on Earth as the starting point for the epidemic and simulate the spread of various viruses. The simulator provides visualization of the epidemic's progression, including SIR graphs.

## Installation

To install the Epidemic Simulator, follow the steps below:

1. Clone the repository:

```git clone https://github.com/arsh73552/Epidemic-Simulator.git```

2. Install the required dependencies for users:

```pip install -r requirements.txt```

If you're a developer, use the following command instead:

```pip install -r requirements_dev.txt```

3. Install the Epidemic Simulator package:

```pip install -e .```

To run the Epidemic Simulator, execute the following command:

```python main.py```

Upon running the simulator, you will be prompted to select a point on Earth as the starting location for the epidemic. Once you have chosen the location, you can select a virus from a range of available options. Each virus has predefined infection rates and infection distances to simulate its behavior accurately.

The simulator will visualize the progression of the epidemic, providing insights into the spread of the virus over time. Additionally, it generates SIR (Susceptible, Infected, Recovered) graphs to help you understand the dynamics of the epidemic.

## Testing and Code Quality

This project follows good coding practices and utilizes various tools to ensure code cleanliness and reliability. The following tools are used:

- **Flake8**: A linting tool that checks the code against PEP 8 style guide and detects common programming errors.
- **Mypy**: A static type checker that identifies type-related issues and helps improve code quality.
- **Pytest**: A testing framework that allows you to write and run tests to verify the functionality and correctness of the code.

To run the tests and ensure proper usage, execute the following command:

```pytest```

## Contributing

Contributions to the Epidemic Simulator project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure they pass all tests.
4. Commit your changes and push them to your fork.
5. Submit a pull request to the main repository.

Please ensure your code adheres to the project's coding standards and passes all tests before submitting a pull request. Also, make sure to provide a clear description of the changes you have made.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the code in compliance with the terms of the license.
