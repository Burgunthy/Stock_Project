{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "stock_project.ipynb",
      "provenance": [],
      "mount_file_id": "1aYXc6bEKI76M-onl2YwsINq9y2lHdM0K",
      "authorship_tag": "ABX9TyO1tiAHC3OddKe/fdkLk5Kf",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Burgunthy/Stock_Project/blob/main/AutoConnect.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TdlUmY84lOYV"
      },
      "source": [
        "from pywinauto import application\n",
        "import time\n",
        "import os\n",
        "\n",
        "os.system('taskkill /IM coStarter* /F /T')\n",
        "os.system('taskkill /IM CpStart* /F /T')\n",
        "os.system('wmic process where \"name like \\'%coStarter%\\'\" call terminate')\n",
        "os.system('wmic process where \"name like \\'%CpStart%\\'\" call terminate')\n",
        "time.sleep(5)        \n",
        "\n",
        "app = application.Application()\n",
        "app.start('D:\\sale\\stock\\CREON\\STARTER\\coStarter.exe /prj:cp /id:.... /pwd:.... /pwdcert:.... /autostart')\n",
        "time.sleep(60)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}