#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###################################################################################################################
"""
Created on Tue May 13 06:34:28 2025

@author: gabriel
"""
###################################################################################################################
# IMPORTAÇAO DE MODULOS
###################################################################################################################
import flet as ft
import os
import platform
import sys
import socket
import getpass
import psutil
###################################################################################################################
###################################################################################################################
###################################################################################################################
                    # SOLUÇAO PARA O CAMINHO
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
assets_path = os.path.join(base_path, "assets")
###################################################################################################################
###################################################################################################################
###################################################################################################################
# DEFINE A FUNÇAO PRINCIPAL
###################################################################################################################

def main(page: ft.Page):
###################################################################################################################
    # Cria o titulo do App na Janela
###################################################################################################################
    page.title = "CoreScan"
###################################################################################################################    
    # Cria um titulo acima dos Cards
###################################################################################################################
   # titulo = ft.Text("Informaçoes do Sistema", size=20, weight=ft.FontWeight.BOLD)
###################################################################################################################    
    # Recebe o ip Local
###################################################################################################################
    ip = socket.gethostbyname(socket.gethostname())
###################################################################################################################    
    # Recebe o valor da memoria RAM
###################################################################################################################
    mem = psutil.virtual_memory()
###################################################################################################################    
    # Recebe o valor total do HDD
###################################################################################################################
    disco = psutil.disk_usage('/')
###################################################################################################################
    # Define o modo de tema do aplicativo
###################################################################################################################
    page.theme_mode = ft.ThemeMode.LIGHT
    
    
###################################################################################################################
    # Cria a instancia do logotipo
###################################################################################################################
    appbar = ft.Container(
    content=ft.Row(
        controls=[
            ft.Image(src="icons/corescan-logo.png", width=40, height=40),
            ft.Text("CoreScan", size=24, weight=ft.FontWeight.BOLD),
        ],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    ),
    padding=10,
    bgcolor=ft.Colors.GREY_200,
)

    
###################################################################################################################   
    # Cria um primeiro card com a informaçao do ditetorio
###################################################################################################################
    card_DIR = ft.Card(
        content=ft.Container(
        content=ft.Column(
            [
                ft.ListTile(
                    leading=ft.Image("icons/diretorio.png", width=32, height=32),
                    title=ft.Text("Diretorio Atual", weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text(os.getcwd()),
                    bgcolor=ft.Colors.GREY_300,
                    ),
                ]
            ),
        width=400,
        padding=10,
        ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        )
###################################################################################################################
    # Cria um segundo card com a informaçao do sistema operacional
###################################################################################################################
    card_OS = ft.Card(
        content=ft.Container(
        content=ft.Column(
            [
                ft.ListTile(
                    leading=ft.Image(src="icons/sistema-operacional.png", width=32, height=32),
                    title=ft.Text("Sistema Operacional", weight=ft.FontWeight.BOLD),
                    subtitle=ft.Text(platform.system()),
                    bgcolor=ft.Colors.GREY_300,
                    ),
                ]
            ),
        width=400,
        padding=10,
        ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        )
###################################################################################################################
    # Cria um terceiro card onde mostra o nome do sistema
###################################################################################################################
    card_SYSNAM = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src="icons/nome.png", width=32, height=32),
                        title=ft.Text("Nome do Sistema", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(platform.node()),
                        bgcolor=ft.Colors.GREY_300,
                        ),
                    ]
                ),
            width=400,
            padding=10,
            ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        )
    
###################################################################################################################
    # Cria um quarto card onde mostra a versao do sistema
###################################################################################################################
    card_SYSVER = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src="icons/controle-de-versao.png", width=32, height=32),
                        title=ft.Text("Versao do Sistema", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(platform.version()),
                        bgcolor=ft.Colors.GREY_300,
                        ),
                    ]
                ),
            width=400,
            padding=10,
            ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        )
    
###################################################################################################################
    # Cria um quinto card onde mostra a Arquitetura
###################################################################################################################
    card_SYSAR = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src="icons/arquitetura.png", width=32, height=32),
                        title=ft.Text("Arquitetura", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(platform.machine()),
                        bgcolor=ft.Colors.GREY_300,
                        ),
                    ]
                ),
            width=400,
            padding=10,
            ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        )

###################################################################################################################
    # Cria um sexto card onde mostra o Processador
###################################################################################################################
    card_SYSPRO = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src="icons/cpu.png", width=32, height=32),
                        title=ft.Text("Processador", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(platform.processor()),
                        bgcolor=ft.Colors.GREY_300,
                        ),
                    ]
                ),
            width=400,
            padding=10,
            ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        )
    
###################################################################################################################
    # Cria um setimo card onde mostra a versao do python
###################################################################################################################
    card_PYTHON = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src="icons/syspython.png", width=32, height=32),
                        title=ft.Text("Python", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(sys.version),
                        bgcolor=ft.Colors.GREY_300,
                        ),
                    ]
                ),
            width=400,
            padding=10,
            ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        )

###################################################################################################################
    # Cria um oitavo card onde mostra o IP LOCAL
###################################################################################################################
    card_IP = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src="icons/endereco-de-ip.png", width=32, height=32),
                        title=ft.Text("IP Local", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(ip),
                        bgcolor=ft.Colors.GREY_300,
                        ),
                    ]
                ),
            width=400,
            padding=10,
            ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        )

###################################################################################################################
    # Cria um nono card onde mostra o nome de usuario
###################################################################################################################
    card_USER = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src="icons/perfil.png", width=32, height=32),
                        title=ft.Text("Usuario", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(getpass.getuser()),
                        bgcolor=ft.Colors.GREY_300,
                        ),
                    ]
                ),
            width=400,
            padding=10,
            ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        )

###################################################################################################################
    # Cria um decimo card onde mostra valores da memoria ram
###################################################################################################################
    card_MEMRAM = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src="icons/memoria-ram.png", width=32, height=32),
                        title=ft.Text("Memoria RAM", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(f"""
Memória total: {mem.total / (1024 ** 3):.2f} GB
Memória disponível: {mem.available / (1024 ** 3):.2f} GB
Memória usada: {mem.used / (1024 ** 3):.2f} GB
Percentual de uso: {mem.percent}%
                                         """),
                        bgcolor=ft.Colors.GREY_300,
                        ),
                    ]
                ),
            width=400,
            padding=10,
            ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        )

    
###################################################################################################################
    # Cria um decimo primeiro card onde mostra valores totais do HDD
###################################################################################################################
    card_DISCO = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Image(src="icons/hdd.png", width=32, height=32),
                        title=ft.Text("Armazenamento", weight=ft.FontWeight.BOLD),
                        subtitle=ft.Text(
                            f"""Total:       {disco.total / (1024**3):.2f} GB
    Usado:       {disco.used / (1024**3):.2f} GB
    Livre:       {disco.free / (1024**3):.2f} GB
    Uso:         {disco.percent}%"""
                        ),
                        bgcolor=ft.Colors.GREY_300,
                    ),
                ]
            ),
            width=400,
            padding=10,
        ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
    )
    
    
  

###################################################################################################################
    # Adiciona as variaveis na pagina
###################################################################################################################
    page.add(
    ft.Column(
        [
            appbar,
            ft.Text("Informações do Sistema", size=20, weight=ft.FontWeight.BOLD),
            ft.Container(
                content=ft.Row(
                    [
                        card_DIR, card_OS, card_SYSNAM, card_SYSVER, card_SYSAR,
                        card_SYSPRO, card_PYTHON, card_IP, card_USER,
                        card_MEMRAM, card_DISCO
                    ],
                    spacing=20,
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                expand=True,
                alignment=ft.alignment.center,
                padding=20,
            ),
        ],
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        alignment=ft.MainAxisAlignment.CENTER,
    )
)


###################################################################################################################
# Loop que inicia o aplicativo
###################################################################################################################
ft.app(target=main, assets_dir=assets_path)