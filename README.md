# cgra-submission-tool

Tool for automatically zipping and taking screenshots (currently useless) of CGRA TP submissions.

It's not really meant to be useful or anything, I just decided to make it because I was bored

## What it does

This program open all available tags that match a given pattern, zipping the content of the directory and taking a screenshot of the WebGLScene.

## Dependencies

```
selenium
geckodriver
```

## Usage

Tweak the parameters in `config.py` to get the correct class and group number config.

```sh
python3 main.py directory tpN/proj
```

Where `directory` is the base directory of the cgra repo, 
