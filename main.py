#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import platform
import sys
import getpass
import socket
import psutil


mem = psutil.virtual_memory()

print(f"Memória total: {mem.total / (1024 ** 3):.2f} GB")
print(f"Memória disponível: {mem.available / (1024 ** 3):.2f} GB")
print(f"Memória usada: {mem.used / (1024 ** 3):.2f} GB")
print(f"Percentual de uso: {mem.percent}%")


print('Diretorio atual: ', os.getcwd())
print('Sistema Operacional: ', platform.system())
print('Nome do Sistema:', platform.node())
print('Versao do Sistema: ', platform.version())
print('Arquitetura: ', platform.machine())
print('Processador: ', platform.processor())
print('Python: ', sys.version)
print('Usuario atual: ', getpass.getuser())

# IP LOCAL

ip = socket.gethostbyname(socket.gethostname())

print('IP Local: ', ip)