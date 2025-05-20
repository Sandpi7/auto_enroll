# Contributing to Enrollment Updater

Thank you for considering contributing to Enrollment Updater! This document provides guidelines for contribution and development.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/auto_enroll.git
   cd auto_enroll
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python enrollment_updater.py
   ```

## Development Workflow

1. Create a new branch for your feature or bugfix: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Test your changes thoroughly
4. Commit your changes: `git commit -m "Add your message here"`
5. Push to your branch: `git push origin feature/your-feature-name`
6. Create a Pull Request against the `main` branch

## Code Style

- Follow PEP 8 style guidelines for Python code
- Use descriptive variable names and add comments where necessary
- Include docstrings for functions and classes

## Building the Executable

To build the executable locally:

```bash
python build_executable.py
```

Or, use PyInstaller directly:

```bash
pyinstaller --name=Enrollment_Updater --onefile --windowed --clean --noupx --version-file=file_version_info.txt enrollment_updater.py
```

## Running Tests

Run the tests with:

```bash
# Future implementation
python -m unittest discover tests
```

## Pull Request Guidelines

- Keep your changes focused and related to a single issue
- Update documentation if you change behavior or add features
- Include a clear description of the changes in your PR
- Reference any related issues in your PR description

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.
