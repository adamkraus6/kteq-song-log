#!/bin/bash

pyinstaller -w --dist . --onefile kteq-song-log.py
pyinstaller -w --dist . --onefile shows_new.py
