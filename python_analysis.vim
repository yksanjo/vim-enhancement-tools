" Vim script to interface with Python code analysis tools
" This script provides commands to analyze Python code using Python-based tools

if !has('python3')
    echo "Error: This plugin requires Vim compiled with Python 3 support"
    finish
endif

" Command to analyze the current Python file
command! PyAnalyze call PyAnalyzeCurrentFile()

" Command to show definitions in quickfix list
command! PyDefs call PyShowDefinitions()

" Function to analyze the current file
function! PyAnalyzeCurrentFile()
    python3 << EOF
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(vim.eval('expand("<sfile>:p")')), '..'))
from vim_enhancements.vim_plugin_interface import analyze_current_file
analyze_current_file()
EOF
endfunction

" Function to show definitions in quickfix
function! PyShowDefinitions()
    python3 << EOF
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(vim.eval('expand("<sfile>:p")')), '..'))
from vim_enhancements.vim_plugin_interface import get_definitions_for_vim
get_definitions_for_vim()
EOF
endfunction

" Set up autocommands for Python files
augroup PyAnalysis
    autocmd!
    autocmd FileType python nnoremap <buffer> <leader>pa :PyAnalyze<CR>
    autocmd FileType python nnoremap <buffer> <leader>pd :PyDefs<CR>
augroup END

" Echo a message when the plugin is loaded
echo "Python Analysis Plugin loaded. Use :PyAnalyze or <leader>pa to analyze, :PyDefs or <leader>pd for definitions."