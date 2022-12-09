# Discrete Mathematics Project
<h2 align="center">
    Batik Pattern Classification using Decision Tree<br/>
</h2>
<hr>

> To watch the docs more detail [_here_](https://www.youtube.com/watch?v=xm5gqvvVv0k&ab_channel=MohammadRifqiFarhansyah). 

## Table of Contents
1. [General Info](#general-information)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Usage](#usage)
5. [Structure](#structure)
6. [Project Status](#project-status)
7. [Room for Improvement](#room-for-improvement)
8. [Acknowledgements](#acknowledgements)
9. [Contact](#contact)

<a name="general-information"></a>

## General Information
A simple Batik Pattern Classification using Decision Tree.

<a name="features"></a>

## Features
- Upload your batik pattern dataset in 'dataset' folder and analyze it by using "CREATE" command
- Train your dataset by using "TRAIN" command
- The result of classification between the uploaded photo with the database class
- Download the result (tree image) as a dot extension file

<a name="technologies-used"></a>

## Technologies Used
- OpenCV2 - version 4.5.4
- numpy - version 1.21.3
- sklearn - version 1.0.1
- h5py - version 3.6.0
- mahotas - version 1.4.13

> Note: The version of the libraries above is the version that we used in this project. You can use the latest version of the libraries.

<a name="usage"></a>

## Usage
1. clone this repository to your local directory.
2. open the terminal and go to the directory of the project.
3. make sure you have installed all the libraries that we used in this project.
4. go to 'main.py' file and run it.
5. follow the instruction in the terminal.

<a name="structure"></a>

## Structure
```bash
│   create_dataset.py
│   formatting_output.py
│   main.py
│   README.md
│   training_dataset.py
│
├───dataset
│   ├───test
│   │       1.jpg
│   │       2.jpg
│   │       3.jpg
│   │       4.jpg
│   │
│   └───train
│       ├───Ceplok
│       │
│       ├───Lereng
│       │
│       ├───Nitik
│       │
│       └───Parang
│
├───processing
│       data.h5
│       labels.h5
│
└───__pycache__
```

<a name="project-status">

## Project Status
Project is: _complete_

<a name="room-for-improvement">

## Room for Improvement
Room for Improvement:
- Adding more batik pattern of all regions in Indonesia

<a name="acknowledgements">

## Acknowledgements
- Thanks To Allah SWT
- This project was inspired by [an Article](https://www.sciencedirect.com/science/article/pii/S0950705120302598?casa_token=k3TFgg11BaoAAAAA:vVGyP-a0nQtplVtBDLvHkeyenUfKOGizEVeB7tVsLahVY6foZXoqGvMcBdfIB4BCWTGcmykZJn4)

<a name="contact"></a>

## Contact
<h4 align="center">
  Created by @me<br/>
  2022
</h4>
<hr>
