{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMEGKmKGHXAD+QbUgM9mr4F",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/talittamaceddo/repo3/blob/main/Atividade_2_classes_e_objetos.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Crie uma classe que modele uma pessoa\n",
        "(a) Atributos: nome, idade e endereço\n",
        "(b) Metodos: mostrar endereço e alterar endereço"
      ],
      "metadata": {
        "id": "gDWwPT1pnL8Y"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qRPQJi_umhmz"
      },
      "outputs": [],
      "source": [
        "class Pessoa:\n",
        "    def __init__(self, nome, idade, endereco):\n",
        "        self.nome = nome\n",
        "        self.idade = idade\n",
        "        self.endereco = endereco\n",
        "\n",
        "    def mostrar_endereco(self):\n",
        "        print(f\"Endereço de {self.nome}: {self.endereco}\")\n",
        "\n",
        "    def alterar_endereco(self, novo_endereco):\n",
        "        self.endereco = novo_endereco\n",
        "        print(f\"Endereço de {self.nome} alterado para: {self.endereco}\")\n",
        "\n",
        "pessoa1 = Pessoa(\"Talita\", 30, \"Avenida Samuel Mac Dowell, 2024\")\n",
        "pessoa1.mostrar_endereco()\n",
        "\n",
        "pessoa1.alterar_endereco(\"Rua Manuel Costa, 456\")\n",
        "pessoa1.mostrar_endereco()"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Crie uma classe que modele uma aluno\n",
        "(a) Atributos: nome, numero de matr ´ ´ıcula e curso\n",
        "(b) Metodos: mostrar curso e alterar curso"
      ],
      "metadata": {
        "id": "UxaIOnPunYR6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Aluno:\n",
        "    def __init__(self, nome, matricula, curso):\n",
        "        self.nome = nome\n",
        "        self.matricula = matricula\n",
        "        self.curso = curso\n",
        "\n",
        "    def mostrar_curso(self):\n",
        "        print(f\"O curso de {self.nome} é {self.curso}\")\n",
        "\n",
        "    def alterar_curso(self, novo_curso):\n",
        "        self.curso = novo_curso\n",
        "        print(f\"Curso de {self.nome} alterado para {self.curso}\")\n",
        "\n",
        "# Exemplo de uso\n",
        "aluno1 = Aluno(\"Ilana\", 56984, \" Pedagogia\")\n",
        "aluno1.mostrar_curso()\n",
        "\n",
        "# Alterando o curso\n",
        "aluno1.alterar_curso(\"Engenharia mecatrônica\")\n",
        "aluno1.mostrar_curso()"
      ],
      "metadata": {
        "id": "ASM6aLF-nYoh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. Crie uma classe representando os alunos de um determinado curso. A classe deve\n",
        "conter os atributos matr´ıcula do aluno, nome, nota da primeira prova, nota da segunda\n",
        "prova e nota da terceira prova. Crie metodos para acessar o nome e a m ´ edia do aluno. ´\n",
        "(a) Permita ao usuario entrar com os dados de 5 alunos. ´\n",
        "(b) Encontre o aluno com maior media geral. ´\n",
        "(c) Encontre o aluno com menor media geral ´\n",
        "(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para\n",
        "aprovac¸ao."
      ],
      "metadata": {
        "id": "-PwAyJhXneWH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Aluno:\n",
        "    def __init__(self, matricula, nome, nota1, nota2, nota3):\n",
        "        self.matricula = matricula\n",
        "        self.nome = nome\n",
        "        self.nota1 = nota1\n",
        "        self.nota2 = nota2\n",
        "        self.nota3 = nota3\n",
        "\n",
        "    def calcular_media(self):\n",
        "        return (self.nota1 + self.nota2 + self.nota3) / 3\n",
        "\n",
        "#entrar com os dados de 5 alunos\n",
        "alunos = []\n",
        "for i in range(5):\n",
        "    matricula = input(\"Matrícula do aluno: \")\n",
        "    nome = input(\"Nome do aluno: \")\n",
        "    nota1 = float(input(\"Nota da primeira prova: \"))\n",
        "    nota2 = float(input(\"Nota da segunda prova: \"))\n",
        "    nota3 = float(input(\"Nota da terceira prova: \"))\n",
        "    aluno = Aluno(matricula, nome, nota1, nota2, nota3)\n",
        "    alunos.append(aluno)\n",
        "\n",
        "#aluno com maior média geral\n",
        "aluno_maior_media = max(alunos, key=lambda x: x.calcular_media())\n",
        "\n",
        "#aluno com menor média geral\n",
        "aluno_menor_media = min(alunos, key=lambda x: x.calcular_media())\n",
        "\n",
        "#verificar se cada aluno foi aprovado ou reprovado\n",
        "for aluno in alunos:\n",
        "    media = aluno.calcular_media()\n",
        "    situacao = \"Aprovado\" if media >= 6 else \"Reprovado\"\n",
        "    print(f\"O aluno {aluno.nome} com matrícula {aluno.matricula} obteve média {media:.2f} - {situacao}\")\n",
        "\n",
        "# Resultados\n",
        "print(f\"Aluno com maior média geral: {aluno_maior_media.nome} com média {aluno_maior_media.calcular_media():.2f}\")\n",
        "print(f\"Aluno com menor média geral: {aluno_menor_media.nome} com média {aluno_menor_media.calcular_media():.2f}\")\n"
      ],
      "metadata": {
        "id": "TxPQ3f19neuD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os\n",
        "métodos para fazer as operacões de incremento (de segundos) no horário e diferença\n",
        "entre dois horarios."
      ],
      "metadata": {
        "id": "kRfRPG_entBL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Horario:\n",
        "    def __init__(self, hora, minuto, segundo):\n",
        "        self.hora = hora\n",
        "        self.minuto = minuto\n",
        "        self.segundo = segundo\n",
        "\n",
        "    def incrementar_segundos(self, segundos):\n",
        "        total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo + segundos\n",
        "        self.hora = total_segundos // 3600\n",
        "        total_segundos %= 3600\n",
        "        self.minuto = total_segundos // 60\n",
        "        self.segundo = total_segundos % 60\n",
        "\n",
        "    def diferenca_horaria(self, outro_horario):\n",
        "        total_segundos_atual = self.hora * 3600 + self.minuto * 60 + self.segundo\n",
        "        total_segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo\n",
        "        diferenca_segundos = abs(total_segundos_atual - total_segundos_outro)\n",
        "        hora_diff = diferenca_segundos // 3600\n",
        "        diferenca_segundos %= 3600\n",
        "        minuto_diff = diferenca_segundos // 60\n",
        "        segundo_diff = diferenca_segundos % 60\n",
        "        return hora_diff, minuto_diff, segundo_diff\n",
        "\n",
        "    def __str__(self):\n",
        "        return f\"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}\"\n",
        "\n",
        "# Exemplo de uso\n",
        "horario1 = Horario(10, 30, 45)\n",
        "horario2 = Horario(8, 45, 20)\n",
        "\n",
        "print(\"Horário 1:\", horario1)\n",
        "print(\"Horário 2:\", horario2)\n",
        "\n",
        "# Incrementar segundos no Horário 1\n",
        "horario1.incrementar_segundos(100)\n",
        "print(\"Horário 1 após incrementar 100 segundos:\", horario1)\n",
        "\n",
        "# Diferença entre Horário 1 e Horário 2\n",
        "diferenca = horario1.diferenca_horaria(horario2)\n",
        "print(\"Diferença de Horário 1 para Horário 2:\", f\"{diferenca[0]} horas, {diferenca[1]} minutos, {diferenca[2]} segundos\")"
      ],
      "metadata": {
        "id": "-trbQ_tWntYb"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}