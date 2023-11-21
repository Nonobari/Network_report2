---

title: Web Security Report
author: Noé BACKERT, Antoine BANCHET
date: November 7, 2023
---

# Web Security Report

## Table of Contents

1. [Introduction](#1-introduction)
2. [How to run the app](#2-how-to-run-the-app)
3. [Structure](#3-structure)
4. [References](#references)
5. [Authors](#authors)
## 1. Introduction

This is the Pyflasql web server for the web security course at Ecole des Mines de Saint-Etienne ISMIN.

## 2. How to run the app

> activate a virtual environment (optional)

go in the directory srie/repos/pyflasql and run :
    
    pip install -r requirements.txt

then run

    python run.py


## 3. Structure

MVC architecture : 
    model, view, controller

To change html pages and the style, you have to go to view<br>
To change the functions, in the controller.py <br>

We only added :
- srie/SQL_Injection
- srie/File_Upload
- srie/Brut_Force

and deleted the tp1... tp4 from initial git :
https://gitlab.emse.fr/raphael.viera/pyflasql

## References

- [OWASP](https://owasp.org/) website
- [PortSwigger](https://portswigger.net/web-security/sql-injection) - SQL Injection

## Authors
[Noé Backert](https://github.com/Nonobari)<br>
[Antoine Banchet](https://github.com/AntoineDevFr)
