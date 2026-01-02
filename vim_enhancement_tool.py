"""
Vim Enhancement Tool - Python Code Analysis

This module provides Python code analysis features that can be integrated with Vim.
It offers functionality like:
- Code linting
- Import analysis
- Function/Class extraction
- Docstring generation
"""

import ast
import os
import sys
from typing import List, Dict, Any, Optional


class VimPythonAnalyzer:
    """
    A Python code analyzer designed to work with Vim for enhanced Python development.
    """
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.tree = None
        self.errors = []
        self.warnings = []
        
        # Parse the Python file
        self._parse_file()
    
    def _parse_file(self) -> None:
        """Parse the Python file and create an AST tree."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.tree = ast.parse(content)
        except SyntaxError as e:
            self.errors.append({
                'type': 'SyntaxError',
                'line': e.lineno,
                'message': e.msg,
                'filename': e.filename
            })
        except Exception as e:
            self.errors.append({
                'type': 'Error',
                'line': 0,
                'message': str(e),
                'filename': self.file_path
            })
    
    def get_syntax_errors(self) -> List[Dict[str, Any]]:
        """Return a list of syntax errors in the file."""
        return self.errors
    
    def get_definitions(self) -> List[Dict[str, Any]]:
        """Extract all function and class definitions from the file."""
        if not self.tree:
            return []
        
        definitions = []
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                definitions.append({
                    'type': 'function',
                    'name': node.name,
                    'line': node.lineno,
                    'docstring': ast.get_docstring(node),
                    'args': [arg.arg for arg in node.args.args if arg.arg != 'self'],
                    'returns': self._get_return_annotation(node)
                })
            elif isinstance(node, ast.AsyncFunctionDef):
                definitions.append({
                    'type': 'async_function',
                    'name': node.name,
                    'line': node.lineno,
                    'docstring': ast.get_docstring(node),
                    'args': [arg.arg for arg in node.args.args if arg.arg != 'self'],
                    'returns': self._get_return_annotation(node)
                })
            elif isinstance(node, ast.ClassDef):
                definitions.append({
                    'type': 'class',
                    'name': node.name,
                    'line': node.lineno,
                    'docstring': ast.get_docstring(node),
                    'methods': self._get_class_methods(node)
                })
        
        return definitions
    
    def _get_return_annotation(self, node) -> Optional[str]:
        """Extract return annotation from a function node."""
        if hasattr(node, 'returns') and node.returns:
            if isinstance(node.returns, ast.Name):
                return node.returns.id
            elif isinstance(node.returns, ast.Constant):
                return str(node.returns.value)
            elif isinstance(node.returns, ast.Subscript):
                # Handle complex types like List[str]
                if hasattr(node.returns, 'value') and hasattr(node.returns.value, 'id'):
                    return f"{node.returns.value.id}[...]"
        return None
    
    def _get_class_methods(self, class_node) -> List[Dict[str, Any]]:
        """Extract methods from a class node."""
        methods = []
        for item in class_node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                methods.append({
                    'name': item.name,
                    'line': item.lineno,
                    'docstring': ast.get_docstring(item),
                    'is_private': item.name.startswith('_')
                })
        return methods
    
    def get_imports(self) -> List[Dict[str, Any]]:
        """Extract all import statements from the file."""
        if not self.tree:
            return []
        
        imports = []
        
        for node in self.tree.body:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append({
                        'type': 'import',
                        'module': alias.name,
                        'alias': alias.asname
                    })
            elif isinstance(node, ast.ImportFrom):
                imports.append({
                    'type': 'from_import',
                    'module': node.module,
                    'names': [alias.name for alias in node.names],
                    'alias': {alias.name: alias.asname for alias in node.names}
                })
        
        return imports
    
    def get_code_complexity(self) -> Dict[str, int]:
        """Calculate basic code complexity metrics."""
        if not self.tree:
            return {'functions': 0, 'classes': 0, 'imports': 0}
        
        complexity = {
            'functions': 0,
            'classes': 0,
            'imports': 0
        }
        
        for node in ast.walk(self.tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                complexity['functions'] += 1
            elif isinstance(node, ast.ClassDef):
                complexity['classes'] += 1
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                complexity['imports'] += 1
        
        return complexity


def main():
    """Main function to demonstrate the VimPythonAnalyzer."""
    if len(sys.argv) != 2:
        print("Usage: python vim_enhancement_tool.py <python_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist")
        sys.exit(1)
    
    analyzer = VimPythonAnalyzer(file_path)
    
    # Print syntax errors if any
    errors = analyzer.get_syntax_errors()
    if errors:
        print("Syntax Errors:")
        for error in errors:
            print(f"  Line {error['line']}: {error['message']}")
        return
    
    # Print definitions
    definitions = analyzer.get_definitions()
    print("Definitions:")
    for definition in definitions:
        if definition['type'] == 'class':
            print(f"  Class: {definition['name']} (Line {definition['line']})")
            for method in definition['methods']:
                print(f"    Method: {method['name']} (Line {method['line']})")
        else:
            args_str = ', '.join(definition['args'])
            print(f"  {definition['type'].title()}: {definition['name']}({args_str}) (Line {definition['line']})")
    
    # Print imports
    imports = analyzer.get_imports()
    print("\nImports:")
    for imp in imports:
        if imp['type'] == 'import':
            if imp['alias']:
                print(f"  import {imp['module']} as {imp['alias']}")
            else:
                print(f"  import {imp['module']}")
        else:  # from_import
            names_str = ', '.join(imp['names'])
            print(f"  from {imp['module']} import {names_str}")
    
    # Print complexity
    complexity = analyzer.get_code_complexity()
    print(f"\nComplexity: {complexity['functions']} functions, {complexity['classes']} classes, {complexity['imports']} imports")


if __name__ == "__main__":
    main()