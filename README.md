# Intentionally vulnerable Python project

This is just a minimal repo for testing Sonatype's `jake` against an intentionally vulnerable list of 
dependencies

Project is currently setup to use with pip. 

How to test
----------
- Clone the repository and change directory to cloned dir.
- Install packages
```
pip install -r reqiurements.txt
```
-- Run jake
```
jake ddt
```
