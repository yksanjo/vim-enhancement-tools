"""
Vim Plugin Interface for Python Code Analysis

This module provides a Python interface that can be called from Vim
to analyze Python code and provide enhanced functionality.
"""

import json
import sys
import os
from vim_enhancements.vim_enhancement_tool import VimPythonAnalyzer


def analyze_current_file():
    """
    Analyze the current file in Vim and return structured data.
    This function is designed to be called from Vim using :py3 or :python3.
    """
    # Get the current file path from Vim
    try:
        import vim
        current_file = vim.current.buffer.name
    except ImportError:
        # For testing outside of Vim
        if len(sys.argv) > 1:
            current_file = sys.argv[1]
        else:
            print("No file specified")
            return
    
    if not current_file or not current_file.endswith('.py'):
        print("Not a Python file")
        return
    
    analyzer = VimPythonAnalyzer(current_file)
    
    # Prepare data for Vim
    result = {
        'file': current_file,
        'errors': analyzer.get_syntax_errors(),
        'definitions': analyzer.get_definitions(),
        'imports': analyzer.get_imports(),
        'complexity': analyzer.get_code_complexity()
    }
    
    # Output as JSON for Vim to parse
    print(json.dumps(result, indent=2))


def get_definitions_for_vim():
    """
    Return only the definitions in a format suitable for Vim's quickfix list.
    """
    try:
        import vim
        current_file = vim.current.buffer.name
    except ImportError:
        # For testing outside of Vim
        if len(sys.argv) > 1:
            current_file = sys.argv[1]
        else:
            print("No file specified")
            return
    
    if not current_file or not current_file.endswith('.py'):
        print("Not a Python file")
        return
    
    analyzer = VimPythonAnalyzer(current_file)
    definitions = analyzer.get_definitions()
    
    # Format for Vim quickfix
    quickfix_list = []
    for definition in definitions:
        if definition['type'] == 'class':
            quickfix_list.append({
                'filename': current_file,
                'lnum': definition['line'],
                'text': f"Class: {definition['name']}"
            })
            # Add methods as well
            for method in definition['methods']:
                quickfix_list.append({
                    'filename': current_file,
                    'lnum': method['line'],
                    'text': f"Method: {method['name']} in {definition['name']}"
                })
        else:
            quickfix_list.append({
                'filename': current_file,
                'lnum': definition['line'],
                'text': f"{definition['type'].title()}: {definition['name']}"
            })
    
    # Output as JSON for Vim to parse
    print(json.dumps(quickfix_list))


if __name__ == "__main__":
    # For testing outside of Vim
    if len(sys.argv) > 1:
        import sys
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        analyze_current_file()