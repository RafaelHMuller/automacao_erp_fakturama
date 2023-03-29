<h1 align="center">
📄<br>README - Projeto Automação ERP
</h1>

## Índice 

* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Pré requisitos](#pré-requisitos)
* [Execução](#execução)
* [Bibliotecas](#bibliotecas)

# Descrição do projeto
> Este repositório é meu projeto Python de automação de sistema ERP - Planejamento de Recursos Empresariais. O objetivo foi realizar a automação de um sistema ERP, no caso o Fakturama, por meio do cadastro de diversos produtos salvos em uma base de dados Excel.

# Funcionalidades e Demonstração da Aplicação
Cadastro de produtos em sistema ERP.

Fakturama com os produtos já cadastrados automaticamente:<br>
![Screenshot_1](https://user-images.githubusercontent.com/128300382/228542115-2e9393bc-02e2-44c5-9670-e5851b6559b0.png)

## Pré requisitos

* Sistema operacional Windows
* IDE de python (ambiente de desenvolvimento integrado de python)
* Bases de dados (arquivo Excel)
* Fakturama

## Execução

A execução do código implica na abertura automática do Fakturama (sistema ERP), desde que este esteja instalado no computador. Após a abertura do programa, os produtos presentes na base de dados (.xlsx) serão cadastrados no sistema, incluindo suas respectivas imagens (.png). A automação funciona mediante a localização de imagens na tela do computador, daí a importância da pasta 'Prints'. Por fim, como se trata de uma automação RPA, não se deve mexer no teclado e mouse enquanto não houver uma mensagem de alerta indicando o fim da automação.

## Bibliotecas

* <strong>pyautogui, pyperclip:</strong> bibliotecas de automação RPA<br>
* <strong>pandas:</strong> bibliotecas de integração de arquivos excel, csv e outros, possibilitando análise de dados<br>
* <strong>time:</strong> bibliotecas que permite o gerenciamento do tempo de execução do código<br>
