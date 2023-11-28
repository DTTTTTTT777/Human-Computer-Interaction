# README

[TOC]

## 1. Development Environment

- Operating System: Windows 11 Home Chinese Edition
- Python Interpreter: Python environment deployed via conda, with Python version 3.9.1.

## 2. Project Structure

```
│  README.md   
│  Report - Information Retrieval.md  
│  Report - Information Retrieval.pdf   
│  
└─server  
	│  image_vectorizer.py
    │  rest-server.py   
    │  search.py
    │  
    ├─uploads
    ├─imagenet
    ├─database   
    │  ├─dataset   
    │  └─tags
    ├─static       
    │  ├─images   
    │  │  │  ajax-loader.gif      
    │  ├─result     
    │  └─favorite       
    └─templates      
       ├─main.html     
       └─favorite.html   
```

## 3. How to Run the Project

### 3.1 Install packages

```
Flask==2.3.2
PyQt5==5.12.3
numpy==1.23.5
tensorflow==2.12.0
Flask-HTTPAuth==4.8.0
scipy==1.10.1
imageio==2.28.1
matplotlib==3.7.1
sklearn==0.0.post5
protobuf==4.23.0
ruamel.yaml==0.17.26
```

### 3.2 Execution

1. Start Anaconda Prompt and navigate to the "server" directory.

2. Run the code:

   ```
   python image_vectorizer.py
   python rest-server.py
   ```

3. After running, access the provided local URL through a web browser.

