#!/usr/bin/env python3
import sys
import os

def solution_7():
    
    files = sys.argv[1:]
    
    for file in files:
        file_name = f'{file}.txt'
        try:
            with open(file_name,'r') as f:
                n_lines = len(f.readlines())
                print(f'{file_name} -> {n_lines} lines')
        except Exception as e:
            print(f'Error reading {file_name}. Skipping...')

solution_7()