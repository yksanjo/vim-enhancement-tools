# Vim Enhancement Tools

[![GitHub](https://img.shields.io/badge/GitHub-yksanjo%2Fvim--enhancement--tools-181717?logo=github)](https://github.com/yksanjo/vim-enhancement-tools)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Vim](https://img.shields.io/badge/vim-8.0%2B-brightgreen.svg?logo=vim)](https://www.vim.org/)
[![Status](https://img.shields.io/badge/status-stable-success.svg)](https://shields.io/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Python-powered enhancements for Vim editor functionality

## 🚀 Overview

The Vim Enhancement Tools provide Python-powered analysis and navigation features for Python code within Vim. These tools help developers write, navigate, and understand Python code more efficiently by offering:

- **Code Analysis**: Syntax checking, function/class extraction, import analysis
- **Navigation**: Quick access to definitions and imports
- **Integration**: Seamless integration with Vim's interface
- **Intelligence**: Smart code completion and error detection

## ✨ Features

- **Syntax Error Detection**: Identify and highlight syntax errors in real-time
- **Function/Class Extraction**: Automatically extract and list all functions and classes
- **Import Analysis**: Analyze and list all import statements
- **Code Complexity Metrics**: Calculate basic code complexity metrics
- **Quick Navigation**: Jump directly to definitions with custom commands
- **Vim Integration**: Works seamlessly with existing Vim workflows

## 📸 Screenshots

![Vim Enhancement Tools Demo](https://placehold.co/800x400/4a5568/ffffff?text=Vim+Enhancement+Tools+Demo)

*Example of code analysis output in Vim*

![Code Navigation](https://placehold.co/800x400/2d3748/ffffff?text=Code+Navigation+Features)

*Quick navigation to function definitions*

## 🛠️ Installation

### Prerequisites

- Vim 8.0+ with Python 3 support
- Python 3.8+
- pip

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yksanjo/vim-enhancement-tools.git
   cd vim-enhancement-tools
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add the following to your `.vimrc`:
   ```vim
   " Path to the Python modules
   set rtp+=/path/to/vim-enhancement-tools
   source /path/to/vim-enhancement-tools/vim_enhancements/python_analysis.vim
   ```

4. Restart Vim or reload your configuration:
   ```vim
   :source ~/.vimrc
   ```

### Vim Plugin Managers

If you're using a Vim plugin manager like vim-plug, add this to your configuration:

```vim
Plug 'yksanjo/vim-enhancement-tools', { 'do': 'pip install -r requirements.txt' }
```

## 🎮 Usage

### Vim Commands

After installation, you can use these commands in Vim when editing Python files:

- `:PyAnalyze` - Analyze the current Python file
- `:PyDefs` - Show definitions in quickfix list
- `<leader>pa` - Shortcut for PyAnalyze
- `<leader>pd` - Shortcut for PyDefs

### Command Line Usage

You can also use the analyzer from the command line:

```bash
python vim_enhancement_tool.py /path/to/your/file.py
```

This will output the analysis results directly to the terminal.

### Python API

For integration with other tools:

```python
from vim_enhancements.vim_enhancement_tool import VimPythonAnalyzer

analyzer = VimPythonAnalyzer("/path/to/your/file.py")

# Get syntax errors
errors = analyzer.get_syntax_errors()

# Get function and class definitions
definitions = analyzer.get_definitions()

# Get import statements
imports = analyzer.get_imports()

# Get complexity metrics
complexity = analyzer.get_code_complexity()
```

## 🧪 Examples

### Analyzing a Python File

```python
# example.py
def hello_world(name: str) -> str:
    """Greet the user."""
    return f"Hello, {name}!"

class Greeter:
    """A class to handle greetings."""
    
    def __init__(self, greeting: str = "Hello"):
        self.greeting = greeting
    
    def greet(self, name: str) -> str:
        return f"{self.greeting}, {name}!"
```

When you run `:PyAnalyze` on this file, you'll get:
- Function definition: `hello_world(name: str) -> str` at line 2
- Class definition: `Greeter` at line 7 with method `greet` at line 11
- Import analysis (none in this example)
- Complexity: 1 function, 1 class, 0 imports

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add examples/tests for your changes
5. Update documentation
6. Submit a pull request

### Development Setup

```bash
git clone https://github.com/yksanjo/vim-enhancement-tools.git
cd vim-enhancement-tools
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

- Check the [documentation](docs/)
- Open an [issue](https://github.com/yksanjo/vim-enhancement-tools/issues)
- Submit a [pull request](https://github.com/yksanjo/vim-enhancement-tools/pulls)

## 🙏 Acknowledgments

- Thanks to the Vim community for inspiration
- Inspired by tools like YouCompleteMe and Python-mode
- Built with Python's AST module for code analysis

---

<div align="center">

**Made with ❤️ for Vim enthusiasts**

[Back to Top](#vim-enhancement-tools)

</div>