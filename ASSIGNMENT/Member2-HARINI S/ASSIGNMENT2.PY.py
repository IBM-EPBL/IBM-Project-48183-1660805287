{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": []
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
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "vjmyfOJcmhdo"
      },
      "outputs": [],
      "source": [
        "#1Load the dataset\n",
        "from google.colab import drive"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vj3vwj8EnA27",
        "outputId": "777383f1-a7f3-49e1-e97f-8bdbacb2f870"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from pandas.io.formats.style import plt\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from matplotlib import rcParams\n"
      ],
      "metadata": {
        "id": "f6sunV-_pEN-"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df=pd.read_csv('/content/drive/MyDrive/IBM/dataset')"
      ],
      "metadata": {
        "id": "evwrT90Es2bs"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GD2MJYgh_WDv",
        "outputId": "cc4de9f2-5ba1-4089-d611-b023f99a366f"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "wbTKmzFYtHcu",
        "outputId": "518658be-017d-43b6-a109-49a45a2185e6"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
              "0          1    15634602  Hargrave          619    France  Female   42   \n",
              "1          2    15647311      Hill          608     Spain  Female   41   \n",
              "2          3    15619304      Onio          502    France  Female   42   \n",
              "3          4    15701354      Boni          699    France  Female   39   \n",
              "4          5    15737888  Mitchell          850     Spain  Female   43   \n",
              "\n",
              "   Tenure    Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
              "0       2       0.00              1          1               1   \n",
              "1       1   83807.86              1          0               1   \n",
              "2       8  159660.80              3          1               0   \n",
              "3       1       0.00              2          0               0   \n",
              "4       2  125510.82              1          1               1   \n",
              "\n",
              "   EstimatedSalary  Exited  \n",
              "0        101348.88       1  \n",
              "1        112542.58       0  \n",
              "2        113931.57       1  \n",
              "3         93826.63       0  \n",
              "4         79084.10       0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-82b5aabd-13f9-4263-8e2a-3d7c36f88708\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>Surname</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>15634602</td>\n",
              "      <td>Hargrave</td>\n",
              "      <td>619</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>42</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101348.88</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>15647311</td>\n",
              "      <td>Hill</td>\n",
              "      <td>608</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>41</td>\n",
              "      <td>1</td>\n",
              "      <td>83807.86</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>112542.58</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>15619304</td>\n",
              "      <td>Onio</td>\n",
              "      <td>502</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>42</td>\n",
              "      <td>8</td>\n",
              "      <td>159660.80</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>113931.57</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>15701354</td>\n",
              "      <td>Boni</td>\n",
              "      <td>699</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>39</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>93826.63</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>15737888</td>\n",
              "      <td>Mitchell</td>\n",
              "      <td>850</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>43</td>\n",
              "      <td>2</td>\n",
              "      <td>125510.82</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>79084.10</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-82b5aabd-13f9-4263-8e2a-3d7c36f88708')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-82b5aabd-13f9-4263-8e2a-3d7c36f88708 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-82b5aabd-13f9-4263-8e2a-3d7c36f88708');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#6 check for categorical column and perform encoding\n",
        "dummy=pd.get_dummies(df['Gender'])\n",
        "dummy.head()"
      ],
      "metadata": {
        "id": "sqGlGBDfgVCG",
        "outputId": "4dfdc9dc-e921-4fb5-e82d-33c175f64d21",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        }
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Female  Male\n",
              "0       1     0\n",
              "1       1     0\n",
              "2       1     0\n",
              "3       1     0\n",
              "4       1     0"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-18207cb5-ede6-4179-8897-eba17bb82161\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Female</th>\n",
              "      <th>Male</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-18207cb5-ede6-4179-8897-eba17bb82161')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-18207cb5-ede6-4179-8897-eba17bb82161 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-18207cb5-ede6-4179-8897-eba17bb82161');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df2=pd.concat((df,dummy),axis=1)\n",
        "df2.head()"
      ],
      "metadata": {
        "id": "oiWQ9DPlgg3j",
        "outputId": "cdc8b04f-baaf-467c-98a7-64a0b737b6d9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        }
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
              "0          1    15634602  Hargrave          619    France  Female   42   \n",
              "1          2    15647311      Hill          608     Spain  Female   41   \n",
              "2          3    15619304      Onio          502    France  Female   42   \n",
              "3          4    15701354      Boni          699    France  Female   39   \n",
              "4          5    15737888  Mitchell          850     Spain  Female   43   \n",
              "\n",
              "   Tenure    Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
              "0       2       0.00              1          1               1   \n",
              "1       1   83807.86              1          0               1   \n",
              "2       8  159660.80              3          1               0   \n",
              "3       1       0.00              2          0               0   \n",
              "4       2  125510.82              1          1               1   \n",
              "\n",
              "   EstimatedSalary  Exited  Female  Male  \n",
              "0        101348.88       1       1     0  \n",
              "1        112542.58       0       1     0  \n",
              "2        113931.57       1       1     0  \n",
              "3         93826.63       0       1     0  \n",
              "4         79084.10       0       1     0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3e9153a3-d4ea-466f-8263-62ab2ed14019\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>Surname</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "      <th>Female</th>\n",
              "      <th>Male</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>15634602</td>\n",
              "      <td>Hargrave</td>\n",
              "      <td>619</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>42</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101348.88</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>15647311</td>\n",
              "      <td>Hill</td>\n",
              "      <td>608</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>41</td>\n",
              "      <td>1</td>\n",
              "      <td>83807.86</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>112542.58</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>15619304</td>\n",
              "      <td>Onio</td>\n",
              "      <td>502</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>42</td>\n",
              "      <td>8</td>\n",
              "      <td>159660.80</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>113931.57</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>15701354</td>\n",
              "      <td>Boni</td>\n",
              "      <td>699</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>39</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>93826.63</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>15737888</td>\n",
              "      <td>Mitchell</td>\n",
              "      <td>850</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>43</td>\n",
              "      <td>2</td>\n",
              "      <td>125510.82</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>79084.10</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3e9153a3-d4ea-466f-8263-62ab2ed14019')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-3e9153a3-d4ea-466f-8263-62ab2ed14019 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-3e9153a3-d4ea-466f-8263-62ab2ed14019');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df2.drop(['Gender'],axis=1)"
      ],
      "metadata": {
        "id": "MD6awtjQg9gN",
        "outputId": "ef450225-6871-40b1-f3ed-0a627cebf3cd",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        }
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      RowNumber  CustomerId    Surname  CreditScore Geography  Age  Tenure  \\\n",
              "0             1    15634602   Hargrave          619    France   42       2   \n",
              "1             2    15647311       Hill          608     Spain   41       1   \n",
              "2             3    15619304       Onio          502    France   42       8   \n",
              "3             4    15701354       Boni          699    France   39       1   \n",
              "4             5    15737888   Mitchell          850     Spain   43       2   \n",
              "...         ...         ...        ...          ...       ...  ...     ...   \n",
              "9995       9996    15606229   Obijiaku          771    France   39       5   \n",
              "9996       9997    15569892  Johnstone          516    France   35      10   \n",
              "9997       9998    15584532        Liu          709    France   36       7   \n",
              "9998       9999    15682355  Sabbatini          772   Germany   42       3   \n",
              "9999      10000    15628319     Walker          792    France   28       4   \n",
              "\n",
              "        Balance  NumOfProducts  HasCrCard  IsActiveMember  EstimatedSalary  \\\n",
              "0          0.00              1          1               1        101348.88   \n",
              "1      83807.86              1          0               1        112542.58   \n",
              "2     159660.80              3          1               0        113931.57   \n",
              "3          0.00              2          0               0         93826.63   \n",
              "4     125510.82              1          1               1         79084.10   \n",
              "...         ...            ...        ...             ...              ...   \n",
              "9995       0.00              2          1               0         96270.64   \n",
              "9996   57369.61              1          1               1        101699.77   \n",
              "9997       0.00              1          0               1         42085.58   \n",
              "9998   75075.31              2          1               0         92888.52   \n",
              "9999  130142.79              1          1               0         38190.78   \n",
              "\n",
              "      Exited  Female  Male  \n",
              "0          1       1     0  \n",
              "1          0       1     0  \n",
              "2          1       1     0  \n",
              "3          0       1     0  \n",
              "4          0       1     0  \n",
              "...      ...     ...   ...  \n",
              "9995       0       0     1  \n",
              "9996       0       0     1  \n",
              "9997       1       1     0  \n",
              "9998       1       0     1  \n",
              "9999       0       1     0  \n",
              "\n",
              "[10000 rows x 15 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-5119f9ad-64ac-4ee1-8da9-d30c4b0d1e46\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>Surname</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "      <th>Female</th>\n",
              "      <th>Male</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>15634602</td>\n",
              "      <td>Hargrave</td>\n",
              "      <td>619</td>\n",
              "      <td>France</td>\n",
              "      <td>42</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101348.88</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>15647311</td>\n",
              "      <td>Hill</td>\n",
              "      <td>608</td>\n",
              "      <td>Spain</td>\n",
              "      <td>41</td>\n",
              "      <td>1</td>\n",
              "      <td>83807.86</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>112542.58</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>15619304</td>\n",
              "      <td>Onio</td>\n",
              "      <td>502</td>\n",
              "      <td>France</td>\n",
              "      <td>42</td>\n",
              "      <td>8</td>\n",
              "      <td>159660.80</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>113931.57</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>15701354</td>\n",
              "      <td>Boni</td>\n",
              "      <td>699</td>\n",
              "      <td>France</td>\n",
              "      <td>39</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>93826.63</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>15737888</td>\n",
              "      <td>Mitchell</td>\n",
              "      <td>850</td>\n",
              "      <td>Spain</td>\n",
              "      <td>43</td>\n",
              "      <td>2</td>\n",
              "      <td>125510.82</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>79084.10</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9995</th>\n",
              "      <td>9996</td>\n",
              "      <td>15606229</td>\n",
              "      <td>Obijiaku</td>\n",
              "      <td>771</td>\n",
              "      <td>France</td>\n",
              "      <td>39</td>\n",
              "      <td>5</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>96270.64</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9996</th>\n",
              "      <td>9997</td>\n",
              "      <td>15569892</td>\n",
              "      <td>Johnstone</td>\n",
              "      <td>516</td>\n",
              "      <td>France</td>\n",
              "      <td>35</td>\n",
              "      <td>10</td>\n",
              "      <td>57369.61</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101699.77</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9997</th>\n",
              "      <td>9998</td>\n",
              "      <td>15584532</td>\n",
              "      <td>Liu</td>\n",
              "      <td>709</td>\n",
              "      <td>France</td>\n",
              "      <td>36</td>\n",
              "      <td>7</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>42085.58</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9998</th>\n",
              "      <td>9999</td>\n",
              "      <td>15682355</td>\n",
              "      <td>Sabbatini</td>\n",
              "      <td>772</td>\n",
              "      <td>Germany</td>\n",
              "      <td>42</td>\n",
              "      <td>3</td>\n",
              "      <td>75075.31</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>92888.52</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9999</th>\n",
              "      <td>10000</td>\n",
              "      <td>15628319</td>\n",
              "      <td>Walker</td>\n",
              "      <td>792</td>\n",
              "      <td>France</td>\n",
              "      <td>28</td>\n",
              "      <td>4</td>\n",
              "      <td>130142.79</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>38190.78</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>10000 rows × 15 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-5119f9ad-64ac-4ee1-8da9-d30c4b0d1e46')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-5119f9ad-64ac-4ee1-8da9-d30c4b0d1e46 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-5119f9ad-64ac-4ee1-8da9-d30c4b0d1e46');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df2=df2.drop(['Gender'],axis=1)\n",
        "df2.head()"
      ],
      "metadata": {
        "id": "Xs9Jy4V8h9HK",
        "outputId": "bc12f207-edd9-4a0c-92fa-8abd4b8032f6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        }
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   RowNumber  CustomerId   Surname  CreditScore Geography  Age  Tenure  \\\n",
              "0          1    15634602  Hargrave          619    France   42       2   \n",
              "1          2    15647311      Hill          608     Spain   41       1   \n",
              "2          3    15619304      Onio          502    France   42       8   \n",
              "3          4    15701354      Boni          699    France   39       1   \n",
              "4          5    15737888  Mitchell          850     Spain   43       2   \n",
              "\n",
              "     Balance  NumOfProducts  HasCrCard  IsActiveMember  EstimatedSalary  \\\n",
              "0       0.00              1          1               1        101348.88   \n",
              "1   83807.86              1          0               1        112542.58   \n",
              "2  159660.80              3          1               0        113931.57   \n",
              "3       0.00              2          0               0         93826.63   \n",
              "4  125510.82              1          1               1         79084.10   \n",
              "\n",
              "   Exited  Female  Male  \n",
              "0       1       1     0  \n",
              "1       0       1     0  \n",
              "2       1       1     0  \n",
              "3       0       1     0  \n",
              "4       0       1     0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c73ae9cd-47ea-44fd-a239-efac10f981cc\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>Surname</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "      <th>Female</th>\n",
              "      <th>Male</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>15634602</td>\n",
              "      <td>Hargrave</td>\n",
              "      <td>619</td>\n",
              "      <td>France</td>\n",
              "      <td>42</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101348.88</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>15647311</td>\n",
              "      <td>Hill</td>\n",
              "      <td>608</td>\n",
              "      <td>Spain</td>\n",
              "      <td>41</td>\n",
              "      <td>1</td>\n",
              "      <td>83807.86</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>112542.58</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>15619304</td>\n",
              "      <td>Onio</td>\n",
              "      <td>502</td>\n",
              "      <td>France</td>\n",
              "      <td>42</td>\n",
              "      <td>8</td>\n",
              "      <td>159660.80</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>113931.57</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>15701354</td>\n",
              "      <td>Boni</td>\n",
              "      <td>699</td>\n",
              "      <td>France</td>\n",
              "      <td>39</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>93826.63</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>15737888</td>\n",
              "      <td>Mitchell</td>\n",
              "      <td>850</td>\n",
              "      <td>Spain</td>\n",
              "      <td>43</td>\n",
              "      <td>2</td>\n",
              "      <td>125510.82</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>79084.10</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c73ae9cd-47ea-44fd-a239-efac10f981cc')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-c73ae9cd-47ea-44fd-a239-efac10f981cc button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-c73ae9cd-47ea-44fd-a239-efac10f981cc');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df2=df2.drop(['Male'],axis=1)\n",
        "df2.head()"
      ],
      "metadata": {
        "id": "JJpiKZ6aiEau",
        "outputId": "b47ffdb3-d483-4b08-d2e6-4bc09a8f7fc6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        }
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   RowNumber  CustomerId   Surname  CreditScore Geography  Age  Tenure  \\\n",
              "0          1    15634602  Hargrave          619    France   42       2   \n",
              "1          2    15647311      Hill          608     Spain   41       1   \n",
              "2          3    15619304      Onio          502    France   42       8   \n",
              "3          4    15701354      Boni          699    France   39       1   \n",
              "4          5    15737888  Mitchell          850     Spain   43       2   \n",
              "\n",
              "     Balance  NumOfProducts  HasCrCard  IsActiveMember  EstimatedSalary  \\\n",
              "0       0.00              1          1               1        101348.88   \n",
              "1   83807.86              1          0               1        112542.58   \n",
              "2  159660.80              3          1               0        113931.57   \n",
              "3       0.00              2          0               0         93826.63   \n",
              "4  125510.82              1          1               1         79084.10   \n",
              "\n",
              "   Exited  Female  \n",
              "0       1       1  \n",
              "1       0       1  \n",
              "2       1       1  \n",
              "3       0       1  \n",
              "4       0       1  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-02599203-b463-47b2-a763-703b9bf74c6d\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>Surname</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "      <th>Female</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>15634602</td>\n",
              "      <td>Hargrave</td>\n",
              "      <td>619</td>\n",
              "      <td>France</td>\n",
              "      <td>42</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101348.88</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>15647311</td>\n",
              "      <td>Hill</td>\n",
              "      <td>608</td>\n",
              "      <td>Spain</td>\n",
              "      <td>41</td>\n",
              "      <td>1</td>\n",
              "      <td>83807.86</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>112542.58</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>15619304</td>\n",
              "      <td>Onio</td>\n",
              "      <td>502</td>\n",
              "      <td>France</td>\n",
              "      <td>42</td>\n",
              "      <td>8</td>\n",
              "      <td>159660.80</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>113931.57</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>15701354</td>\n",
              "      <td>Boni</td>\n",
              "      <td>699</td>\n",
              "      <td>France</td>\n",
              "      <td>39</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>93826.63</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>15737888</td>\n",
              "      <td>Mitchell</td>\n",
              "      <td>850</td>\n",
              "      <td>Spain</td>\n",
              "      <td>43</td>\n",
              "      <td>2</td>\n",
              "      <td>125510.82</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>79084.10</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-02599203-b463-47b2-a763-703b9bf74c6d')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-02599203-b463-47b2-a763-703b9bf74c6d button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-02599203-b463-47b2-a763-703b9bf74c6d');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df2.rename(columns={\"Female\":\"Gender\"})"
      ],
      "metadata": {
        "id": "efuDXZOziwcZ",
        "outputId": "b4585cb7-b72a-4f51-bcaf-49a8cd58a3b6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        }
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      RowNumber  CustomerId    Surname  CreditScore Geography  Age  Tenure  \\\n",
              "0             1    15634602   Hargrave          619    France   42       2   \n",
              "1             2    15647311       Hill          608     Spain   41       1   \n",
              "2             3    15619304       Onio          502    France   42       8   \n",
              "3             4    15701354       Boni          699    France   39       1   \n",
              "4             5    15737888   Mitchell          850     Spain   43       2   \n",
              "...         ...         ...        ...          ...       ...  ...     ...   \n",
              "9995       9996    15606229   Obijiaku          771    France   39       5   \n",
              "9996       9997    15569892  Johnstone          516    France   35      10   \n",
              "9997       9998    15584532        Liu          709    France   36       7   \n",
              "9998       9999    15682355  Sabbatini          772   Germany   42       3   \n",
              "9999      10000    15628319     Walker          792    France   28       4   \n",
              "\n",
              "        Balance  NumOfProducts  HasCrCard  IsActiveMember  EstimatedSalary  \\\n",
              "0          0.00              1          1               1        101348.88   \n",
              "1      83807.86              1          0               1        112542.58   \n",
              "2     159660.80              3          1               0        113931.57   \n",
              "3          0.00              2          0               0         93826.63   \n",
              "4     125510.82              1          1               1         79084.10   \n",
              "...         ...            ...        ...             ...              ...   \n",
              "9995       0.00              2          1               0         96270.64   \n",
              "9996   57369.61              1          1               1        101699.77   \n",
              "9997       0.00              1          0               1         42085.58   \n",
              "9998   75075.31              2          1               0         92888.52   \n",
              "9999  130142.79              1          1               0         38190.78   \n",
              "\n",
              "      Exited  Gender  \n",
              "0          1       1  \n",
              "1          0       1  \n",
              "2          1       1  \n",
              "3          0       1  \n",
              "4          0       1  \n",
              "...      ...     ...  \n",
              "9995       0       0  \n",
              "9996       0       0  \n",
              "9997       1       1  \n",
              "9998       1       0  \n",
              "9999       0       1  \n",
              "\n",
              "[10000 rows x 14 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-08af26fd-9c7f-45ed-90cc-c49ee3e214b2\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>Surname</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "      <th>Gender</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>15634602</td>\n",
              "      <td>Hargrave</td>\n",
              "      <td>619</td>\n",
              "      <td>France</td>\n",
              "      <td>42</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101348.88</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>15647311</td>\n",
              "      <td>Hill</td>\n",
              "      <td>608</td>\n",
              "      <td>Spain</td>\n",
              "      <td>41</td>\n",
              "      <td>1</td>\n",
              "      <td>83807.86</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>112542.58</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>15619304</td>\n",
              "      <td>Onio</td>\n",
              "      <td>502</td>\n",
              "      <td>France</td>\n",
              "      <td>42</td>\n",
              "      <td>8</td>\n",
              "      <td>159660.80</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>113931.57</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>15701354</td>\n",
              "      <td>Boni</td>\n",
              "      <td>699</td>\n",
              "      <td>France</td>\n",
              "      <td>39</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>93826.63</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>15737888</td>\n",
              "      <td>Mitchell</td>\n",
              "      <td>850</td>\n",
              "      <td>Spain</td>\n",
              "      <td>43</td>\n",
              "      <td>2</td>\n",
              "      <td>125510.82</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>79084.10</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9995</th>\n",
              "      <td>9996</td>\n",
              "      <td>15606229</td>\n",
              "      <td>Obijiaku</td>\n",
              "      <td>771</td>\n",
              "      <td>France</td>\n",
              "      <td>39</td>\n",
              "      <td>5</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>96270.64</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9996</th>\n",
              "      <td>9997</td>\n",
              "      <td>15569892</td>\n",
              "      <td>Johnstone</td>\n",
              "      <td>516</td>\n",
              "      <td>France</td>\n",
              "      <td>35</td>\n",
              "      <td>10</td>\n",
              "      <td>57369.61</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101699.77</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9997</th>\n",
              "      <td>9998</td>\n",
              "      <td>15584532</td>\n",
              "      <td>Liu</td>\n",
              "      <td>709</td>\n",
              "      <td>France</td>\n",
              "      <td>36</td>\n",
              "      <td>7</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>42085.58</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9998</th>\n",
              "      <td>9999</td>\n",
              "      <td>15682355</td>\n",
              "      <td>Sabbatini</td>\n",
              "      <td>772</td>\n",
              "      <td>Germany</td>\n",
              "      <td>42</td>\n",
              "      <td>3</td>\n",
              "      <td>75075.31</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>92888.52</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9999</th>\n",
              "      <td>10000</td>\n",
              "      <td>15628319</td>\n",
              "      <td>Walker</td>\n",
              "      <td>792</td>\n",
              "      <td>France</td>\n",
              "      <td>28</td>\n",
              "      <td>4</td>\n",
              "      <td>130142.79</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>38190.78</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>10000 rows × 14 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-08af26fd-9c7f-45ed-90cc-c49ee3e214b2')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-08af26fd-9c7f-45ed-90cc-c49ee3e214b2 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-08af26fd-9c7f-45ed-90cc-c49ee3e214b2');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HsDTAhHytOGn",
        "outputId": "ddcaa2de-fa7f-480c-9709-a9c187105bee"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(10000, 14)"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q8dI5WwNtUvv",
        "outputId": "cf54ebdd-08b5-40e4-e9f8-a99cef607f64"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 10000 entries, 0 to 9999\n",
            "Data columns (total 14 columns):\n",
            " #   Column           Non-Null Count  Dtype  \n",
            "---  ------           --------------  -----  \n",
            " 0   RowNumber        10000 non-null  int64  \n",
            " 1   CustomerId       10000 non-null  int64  \n",
            " 2   Surname          10000 non-null  object \n",
            " 3   CreditScore      10000 non-null  int64  \n",
            " 4   Geography        10000 non-null  object \n",
            " 5   Gender           10000 non-null  object \n",
            " 6   Age              10000 non-null  int64  \n",
            " 7   Tenure           10000 non-null  int64  \n",
            " 8   Balance          10000 non-null  float64\n",
            " 9   NumOfProducts    10000 non-null  int64  \n",
            " 10  HasCrCard        10000 non-null  int64  \n",
            " 11  IsActiveMember   10000 non-null  int64  \n",
            " 12  EstimatedSalary  10000 non-null  float64\n",
            " 13  Exited           10000 non-null  int64  \n",
            "dtypes: float64(2), int64(9), object(3)\n",
            "memory usage: 1.1+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#4 Handling Missing Values\n",
        "df.isnull().any()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4Kr3OYs8tep8",
        "outputId": "3c5159b9-ab04-4938-ab6b-338992c379ed"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "RowNumber          False\n",
              "CustomerId         False\n",
              "Surname            False\n",
              "CreditScore        False\n",
              "Geography          False\n",
              "Gender             False\n",
              "Age                False\n",
              "Tenure             False\n",
              "Balance            False\n",
              "NumOfProducts      False\n",
              "HasCrCard          False\n",
              "IsActiveMember     False\n",
              "EstimatedSalary    False\n",
              "Exited             False\n",
              "dtype: bool"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4fWLnEPtQKp8",
        "outputId": "5b0d8410-b12a-44f0-9895-a75bda3b6a31"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "RowNumber          0\n",
              "CustomerId         0\n",
              "Surname            0\n",
              "CreditScore        0\n",
              "Geography          0\n",
              "Gender             0\n",
              "Age                0\n",
              "Tenure             0\n",
              "Balance            0\n",
              "NumOfProducts      0\n",
              "HasCrCard          0\n",
              "IsActiveMember     0\n",
              "EstimatedSalary    0\n",
              "Exited             0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "__4GZUh-QR6M",
        "outputId": "fb25d9cb-593a-42c6-f9d8-0118c408fda5"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#7 split the data into independent and dependent variable\n",
        "y=df2['Tenure']\n",
        "y\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JFJTRI4tbbGr",
        "outputId": "fca6d83c-dd06-4b38-d397-c58d0c2b2b78"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0        2\n",
              "1        1\n",
              "2        8\n",
              "3        1\n",
              "4        2\n",
              "        ..\n",
              "9995     5\n",
              "9996    10\n",
              "9997     7\n",
              "9998     3\n",
              "9999     4\n",
              "Name: Tenure, Length: 10000, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X=df.drop(columns=['Balance'],axis=1)\n",
        "X.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "smsN6jyPbgAa",
        "outputId": "24243955-69b7-48d4-abc5-3bd26414f3eb"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
              "0          1    15634602  Hargrave          619    France  Female   42   \n",
              "1          2    15647311      Hill          608     Spain  Female   41   \n",
              "2          3    15619304      Onio          502    France  Female   42   \n",
              "3          4    15701354      Boni          699    France  Female   39   \n",
              "4          5    15737888  Mitchell          850     Spain  Female   43   \n",
              "\n",
              "   Tenure  NumOfProducts  HasCrCard  IsActiveMember  EstimatedSalary  Exited  \n",
              "0       2              1          1               1        101348.88       1  \n",
              "1       1              1          0               1        112542.58       0  \n",
              "2       8              3          1               0        113931.57       1  \n",
              "3       1              2          0               0         93826.63       0  \n",
              "4       2              1          1               1         79084.10       0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-9076ba98-a047-4d4c-9e33-d892a68ebd9d\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>Surname</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>15634602</td>\n",
              "      <td>Hargrave</td>\n",
              "      <td>619</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>42</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101348.88</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>15647311</td>\n",
              "      <td>Hill</td>\n",
              "      <td>608</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>41</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>112542.58</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>15619304</td>\n",
              "      <td>Onio</td>\n",
              "      <td>502</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>42</td>\n",
              "      <td>8</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>113931.57</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>15701354</td>\n",
              "      <td>Boni</td>\n",
              "      <td>699</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>39</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>93826.63</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>15737888</td>\n",
              "      <td>Mitchell</td>\n",
              "      <td>850</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>43</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>79084.10</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-9076ba98-a047-4d4c-9e33-d892a68ebd9d')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-9076ba98-a047-4d4c-9e33-d892a68ebd9d button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-9076ba98-a047-4d4c-9e33-d892a68ebd9d');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X=df.iloc[:,7:10]\n",
        "X"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "ore62i0hb9sv",
        "outputId": "8ab6681e-8b41-4731-c0f2-3db961513198"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      Tenure    Balance  NumOfProducts\n",
              "0          2       0.00              1\n",
              "1          1   83807.86              1\n",
              "2          8  159660.80              3\n",
              "3          1       0.00              2\n",
              "4          2  125510.82              1\n",
              "...      ...        ...            ...\n",
              "9995       5       0.00              2\n",
              "9996      10   57369.61              1\n",
              "9997       7       0.00              1\n",
              "9998       3   75075.31              2\n",
              "9999       4  130142.79              1\n",
              "\n",
              "[10000 rows x 3 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3a26ce00-2c8e-4c1a-8bfa-0de364e77b43\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>83807.86</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>8</td>\n",
              "      <td>159660.80</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2</td>\n",
              "      <td>125510.82</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9995</th>\n",
              "      <td>5</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9996</th>\n",
              "      <td>10</td>\n",
              "      <td>57369.61</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9997</th>\n",
              "      <td>7</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9998</th>\n",
              "      <td>3</td>\n",
              "      <td>75075.31</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9999</th>\n",
              "      <td>4</td>\n",
              "      <td>130142.79</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>10000 rows × 3 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3a26ce00-2c8e-4c1a-8bfa-0de364e77b43')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-3a26ce00-2c8e-4c1a-8bfa-0de364e77b43 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-3a26ce00-2c8e-4c1a-8bfa-0de364e77b43');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(X.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nDLEhJFUuLy8",
        "outputId": "6d81f58b-8bfa-41cf-a1fa-5b76067b99ed"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(10000, 3)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Y=df.iloc[:,7]\n",
        "Y"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_yGEfef1cVj_",
        "outputId": "41acb1dc-6b67-4580-ad65-5e6f2783ebcc"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0        2\n",
              "1        1\n",
              "2        8\n",
              "3        1\n",
              "4        2\n",
              "        ..\n",
              "9995     5\n",
              "9996    10\n",
              "9997     7\n",
              "9998     3\n",
              "9999     4\n",
              "Name: Tenure, Length: 10000, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(y.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kgWrAk5cuQKU",
        "outputId": "5d6fed5c-908a-4184-ece6-c5d1304997ed"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(10000,)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#8 Scale the independent variable\n",
        "from sklearn.preprocessing import scale\n",
        "x_scaled=pd.DataFrame(scale(X),columns=X.columns)\n",
        "x_scaled.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "cn_y03UllQRT",
        "outputId": "72d6de64-6db5-4a43-ca07-b7ba96bcc914"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     Tenure   Balance  NumOfProducts\n",
              "0 -1.041760 -1.225848      -0.911583\n",
              "1 -1.387538  0.117350      -0.911583\n",
              "2  1.032908  1.333053       2.527057\n",
              "3 -1.387538 -1.225848       0.807737\n",
              "4 -1.041760  0.785728      -0.911583"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-39bbb3bc-eb15-429b-a9f9-d95b79126ea4\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>-1.041760</td>\n",
              "      <td>-1.225848</td>\n",
              "      <td>-0.911583</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>-1.387538</td>\n",
              "      <td>0.117350</td>\n",
              "      <td>-0.911583</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1.032908</td>\n",
              "      <td>1.333053</td>\n",
              "      <td>2.527057</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>-1.387538</td>\n",
              "      <td>-1.225848</td>\n",
              "      <td>0.807737</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>-1.041760</td>\n",
              "      <td>0.785728</td>\n",
              "      <td>-0.911583</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-39bbb3bc-eb15-429b-a9f9-d95b79126ea4')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-39bbb3bc-eb15-429b-a9f9-d95b79126ea4 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-39bbb3bc-eb15-429b-a9f9-d95b79126ea4');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#9 Train test split\n",
        "from sklearn.model_selection import train_test_split"
      ],
      "metadata": {
        "id": "povK9iyIsUsw"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Split data (train & test data)\n",
        "X_train, X_test, y_train, y_test = train_test_split(X,y)"
      ],
      "metadata": {
        "id": "m3TZ_uB6sZaO"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#display shape\n",
        "print(X_train.shape)\n",
        "print(X_test.shape)\n",
        "print(y_train.shape)\n",
        "print(y_test.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aSbcDvwFulkK",
        "outputId": "7c57137a-5b5a-45bf-9823-deba9a22f811"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(7500, 3)\n",
            "(2500, 3)\n",
            "(7500,)\n",
            "(2500,)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.30,random_state=0)\n",
        "print(X_train.shape)\n",
        "print(X_test.shape)\n",
        "print(y_train.shape)\n",
        "print(y_test.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mL7x6wc_vroT",
        "outputId": "0e086e73-41dd-4258-bf95-d887a7ff3b7f"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(7000, 3)\n",
            "(3000, 3)\n",
            "(7000,)\n",
            "(3000,)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(np.mean(X_train))\n",
        "print(np.mean(X_test))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ox5MkCfKwNdP",
        "outputId": "c7c4c81b-185e-4b86-91b8-40752f75354e"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Tenure               4.989429\n",
            "Balance          75204.853421\n",
            "NumOfProducts        1.534286\n",
            "dtype: float64\n",
            "Tenure               5.067333\n",
            "Balance          79474.972977\n",
            "NumOfProducts        1.520667\n",
            "dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#3 Descriptive stastical analysis\n",
        "df.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "ITMBIXdPub69",
        "outputId": "158c09f3-161b-4a3e-92ca-34dc20b37d18"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         RowNumber    CustomerId   CreditScore           Age        Tenure  \\\n",
              "count  10000.00000  1.000000e+04  10000.000000  10000.000000  10000.000000   \n",
              "mean    5000.50000  1.569094e+07    650.528800     38.921800      5.012800   \n",
              "std     2886.89568  7.193619e+04     96.653299     10.487806      2.892174   \n",
              "min        1.00000  1.556570e+07    350.000000     18.000000      0.000000   \n",
              "25%     2500.75000  1.562853e+07    584.000000     32.000000      3.000000   \n",
              "50%     5000.50000  1.569074e+07    652.000000     37.000000      5.000000   \n",
              "75%     7500.25000  1.575323e+07    718.000000     44.000000      7.000000   \n",
              "max    10000.00000  1.581569e+07    850.000000     92.000000     10.000000   \n",
              "\n",
              "             Balance  NumOfProducts    HasCrCard  IsActiveMember  \\\n",
              "count   10000.000000   10000.000000  10000.00000    10000.000000   \n",
              "mean    76485.889288       1.530200      0.70550        0.515100   \n",
              "std     62397.405202       0.581654      0.45584        0.499797   \n",
              "min         0.000000       1.000000      0.00000        0.000000   \n",
              "25%         0.000000       1.000000      0.00000        0.000000   \n",
              "50%     97198.540000       1.000000      1.00000        1.000000   \n",
              "75%    127644.240000       2.000000      1.00000        1.000000   \n",
              "max    250898.090000       4.000000      1.00000        1.000000   \n",
              "\n",
              "       EstimatedSalary        Exited  \n",
              "count     10000.000000  10000.000000  \n",
              "mean     100090.239881      0.203700  \n",
              "std       57510.492818      0.402769  \n",
              "min          11.580000      0.000000  \n",
              "25%       51002.110000      0.000000  \n",
              "50%      100193.915000      0.000000  \n",
              "75%      149388.247500      0.000000  \n",
              "max      199992.480000      1.000000  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-57014919-1e5c-4277-bef0-f0bdd3089dd3\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>10000.00000</td>\n",
              "      <td>1.000000e+04</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.00000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>5000.50000</td>\n",
              "      <td>1.569094e+07</td>\n",
              "      <td>650.528800</td>\n",
              "      <td>38.921800</td>\n",
              "      <td>5.012800</td>\n",
              "      <td>76485.889288</td>\n",
              "      <td>1.530200</td>\n",
              "      <td>0.70550</td>\n",
              "      <td>0.515100</td>\n",
              "      <td>100090.239881</td>\n",
              "      <td>0.203700</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>2886.89568</td>\n",
              "      <td>7.193619e+04</td>\n",
              "      <td>96.653299</td>\n",
              "      <td>10.487806</td>\n",
              "      <td>2.892174</td>\n",
              "      <td>62397.405202</td>\n",
              "      <td>0.581654</td>\n",
              "      <td>0.45584</td>\n",
              "      <td>0.499797</td>\n",
              "      <td>57510.492818</td>\n",
              "      <td>0.402769</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.00000</td>\n",
              "      <td>1.556570e+07</td>\n",
              "      <td>350.000000</td>\n",
              "      <td>18.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.00000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>11.580000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2500.75000</td>\n",
              "      <td>1.562853e+07</td>\n",
              "      <td>584.000000</td>\n",
              "      <td>32.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.00000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>51002.110000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>5000.50000</td>\n",
              "      <td>1.569074e+07</td>\n",
              "      <td>652.000000</td>\n",
              "      <td>37.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>97198.540000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.00000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>100193.915000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>7500.25000</td>\n",
              "      <td>1.575323e+07</td>\n",
              "      <td>718.000000</td>\n",
              "      <td>44.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>127644.240000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.00000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>149388.247500</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>10000.00000</td>\n",
              "      <td>1.581569e+07</td>\n",
              "      <td>850.000000</td>\n",
              "      <td>92.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>250898.090000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>1.00000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>199992.480000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-57014919-1e5c-4277-bef0-f0bdd3089dd3')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-57014919-1e5c-4277-bef0-f0bdd3089dd3 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-57014919-1e5c-4277-bef0-f0bdd3089dd3');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.NumOfProducts.value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yppvNeiFuxmi",
        "outputId": "1698c3a2-2b7e-4727-de65-a1194248ddc9"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1    5084\n",
              "2    4590\n",
              "3     266\n",
              "4      60\n",
              "Name: NumOfProducts, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.corr()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 394
        },
        "id": "SL2TeEmEM53v",
        "outputId": "261858be-9d9e-4f6b-cfd5-c33751e22d4e"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                 RowNumber  CustomerId  CreditScore       Age    Tenure  \\\n",
              "RowNumber         1.000000    0.004202     0.005840  0.000783 -0.006495   \n",
              "CustomerId        0.004202    1.000000     0.005308  0.009497 -0.014883   \n",
              "CreditScore       0.005840    0.005308     1.000000 -0.003965  0.000842   \n",
              "Age               0.000783    0.009497    -0.003965  1.000000 -0.009997   \n",
              "Tenure           -0.006495   -0.014883     0.000842 -0.009997  1.000000   \n",
              "Balance          -0.009067   -0.012419     0.006268  0.028308 -0.012254   \n",
              "NumOfProducts     0.007246    0.016972     0.012238 -0.030680  0.013444   \n",
              "HasCrCard         0.000599   -0.014025    -0.005458 -0.011721  0.022583   \n",
              "IsActiveMember    0.012044    0.001665     0.025651  0.085472 -0.028362   \n",
              "EstimatedSalary  -0.005988    0.015271    -0.001384 -0.007201  0.007784   \n",
              "Exited           -0.016571   -0.006248    -0.027094  0.285323 -0.014001   \n",
              "\n",
              "                  Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
              "RowNumber       -0.009067       0.007246   0.000599        0.012044   \n",
              "CustomerId      -0.012419       0.016972  -0.014025        0.001665   \n",
              "CreditScore      0.006268       0.012238  -0.005458        0.025651   \n",
              "Age              0.028308      -0.030680  -0.011721        0.085472   \n",
              "Tenure          -0.012254       0.013444   0.022583       -0.028362   \n",
              "Balance          1.000000      -0.304180  -0.014858       -0.010084   \n",
              "NumOfProducts   -0.304180       1.000000   0.003183        0.009612   \n",
              "HasCrCard       -0.014858       0.003183   1.000000       -0.011866   \n",
              "IsActiveMember  -0.010084       0.009612  -0.011866        1.000000   \n",
              "EstimatedSalary  0.012797       0.014204  -0.009933       -0.011421   \n",
              "Exited           0.118533      -0.047820  -0.007138       -0.156128   \n",
              "\n",
              "                 EstimatedSalary    Exited  \n",
              "RowNumber              -0.005988 -0.016571  \n",
              "CustomerId              0.015271 -0.006248  \n",
              "CreditScore            -0.001384 -0.027094  \n",
              "Age                    -0.007201  0.285323  \n",
              "Tenure                  0.007784 -0.014001  \n",
              "Balance                 0.012797  0.118533  \n",
              "NumOfProducts           0.014204 -0.047820  \n",
              "HasCrCard              -0.009933 -0.007138  \n",
              "IsActiveMember         -0.011421 -0.156128  \n",
              "EstimatedSalary         1.000000  0.012097  \n",
              "Exited                  0.012097  1.000000  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-917bbec6-f6aa-481f-a61b-540ead18c029\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>RowNumber</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.004202</td>\n",
              "      <td>0.005840</td>\n",
              "      <td>0.000783</td>\n",
              "      <td>-0.006495</td>\n",
              "      <td>-0.009067</td>\n",
              "      <td>0.007246</td>\n",
              "      <td>0.000599</td>\n",
              "      <td>0.012044</td>\n",
              "      <td>-0.005988</td>\n",
              "      <td>-0.016571</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>CustomerId</th>\n",
              "      <td>0.004202</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.005308</td>\n",
              "      <td>0.009497</td>\n",
              "      <td>-0.014883</td>\n",
              "      <td>-0.012419</td>\n",
              "      <td>0.016972</td>\n",
              "      <td>-0.014025</td>\n",
              "      <td>0.001665</td>\n",
              "      <td>0.015271</td>\n",
              "      <td>-0.006248</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>CreditScore</th>\n",
              "      <td>0.005840</td>\n",
              "      <td>0.005308</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>-0.003965</td>\n",
              "      <td>0.000842</td>\n",
              "      <td>0.006268</td>\n",
              "      <td>0.012238</td>\n",
              "      <td>-0.005458</td>\n",
              "      <td>0.025651</td>\n",
              "      <td>-0.001384</td>\n",
              "      <td>-0.027094</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Age</th>\n",
              "      <td>0.000783</td>\n",
              "      <td>0.009497</td>\n",
              "      <td>-0.003965</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>-0.009997</td>\n",
              "      <td>0.028308</td>\n",
              "      <td>-0.030680</td>\n",
              "      <td>-0.011721</td>\n",
              "      <td>0.085472</td>\n",
              "      <td>-0.007201</td>\n",
              "      <td>0.285323</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Tenure</th>\n",
              "      <td>-0.006495</td>\n",
              "      <td>-0.014883</td>\n",
              "      <td>0.000842</td>\n",
              "      <td>-0.009997</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>-0.012254</td>\n",
              "      <td>0.013444</td>\n",
              "      <td>0.022583</td>\n",
              "      <td>-0.028362</td>\n",
              "      <td>0.007784</td>\n",
              "      <td>-0.014001</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Balance</th>\n",
              "      <td>-0.009067</td>\n",
              "      <td>-0.012419</td>\n",
              "      <td>0.006268</td>\n",
              "      <td>0.028308</td>\n",
              "      <td>-0.012254</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>-0.304180</td>\n",
              "      <td>-0.014858</td>\n",
              "      <td>-0.010084</td>\n",
              "      <td>0.012797</td>\n",
              "      <td>0.118533</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>NumOfProducts</th>\n",
              "      <td>0.007246</td>\n",
              "      <td>0.016972</td>\n",
              "      <td>0.012238</td>\n",
              "      <td>-0.030680</td>\n",
              "      <td>0.013444</td>\n",
              "      <td>-0.304180</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.003183</td>\n",
              "      <td>0.009612</td>\n",
              "      <td>0.014204</td>\n",
              "      <td>-0.047820</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>HasCrCard</th>\n",
              "      <td>0.000599</td>\n",
              "      <td>-0.014025</td>\n",
              "      <td>-0.005458</td>\n",
              "      <td>-0.011721</td>\n",
              "      <td>0.022583</td>\n",
              "      <td>-0.014858</td>\n",
              "      <td>0.003183</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>-0.011866</td>\n",
              "      <td>-0.009933</td>\n",
              "      <td>-0.007138</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>IsActiveMember</th>\n",
              "      <td>0.012044</td>\n",
              "      <td>0.001665</td>\n",
              "      <td>0.025651</td>\n",
              "      <td>0.085472</td>\n",
              "      <td>-0.028362</td>\n",
              "      <td>-0.010084</td>\n",
              "      <td>0.009612</td>\n",
              "      <td>-0.011866</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>-0.011421</td>\n",
              "      <td>-0.156128</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <td>-0.005988</td>\n",
              "      <td>0.015271</td>\n",
              "      <td>-0.001384</td>\n",
              "      <td>-0.007201</td>\n",
              "      <td>0.007784</td>\n",
              "      <td>0.012797</td>\n",
              "      <td>0.014204</td>\n",
              "      <td>-0.009933</td>\n",
              "      <td>-0.011421</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.012097</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Exited</th>\n",
              "      <td>-0.016571</td>\n",
              "      <td>-0.006248</td>\n",
              "      <td>-0.027094</td>\n",
              "      <td>0.285323</td>\n",
              "      <td>-0.014001</td>\n",
              "      <td>0.118533</td>\n",
              "      <td>-0.047820</td>\n",
              "      <td>-0.007138</td>\n",
              "      <td>-0.156128</td>\n",
              "      <td>0.012097</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-917bbec6-f6aa-481f-a61b-540ead18c029')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-917bbec6-f6aa-481f-a61b-540ead18c029 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-917bbec6-f6aa-481f-a61b-540ead18c029');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Age'].mean()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R2tDUEmwNDqR",
        "outputId": "7b00703c-a49a-48ed-84b0-910ddb078cde"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "38.9218"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Gender'].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jJvqkOBrNKlD",
        "outputId": "12785a61-578f-4b1e-d860-fc0d5fd2eadc"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Male      5457\n",
              "Female    4543\n",
              "Name: Gender, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#2 Visualization"
      ],
      "metadata": {
        "id": "9ZQ_u9-af-lA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#univariate analysis\n",
        "sns.displot(df.Exited)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 386
        },
        "id": "bqsmbirTvm6G",
        "outputId": "c52d5e3e-1059-4f51-d969-6dea9c77bb28"
      },
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.FacetGrid at 0x7f8a972818d0>"
            ]
          },
          "metadata": {},
          "execution_count": 61
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 360x360 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.displot(df.Balance)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 386
        },
        "id": "hogDYB67wRGN",
        "outputId": "ee4bce92-7be4-4e9a-9ad6-162d65855641"
      },
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.FacetGrid at 0x7f8a97db4a50>"
            ]
          },
          "metadata": {},
          "execution_count": 60
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 360x360 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.hist(figsize=(10,10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 833
        },
        "id": "0qS3ZZuuD4z_",
        "outputId": "7bacb193-0de5-456c-8705-5f4c6eab4416"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f8a9ca3a150>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f8a9c9ee790>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f8a9c9a4d90>],\n",
              "       [<matplotlib.axes._subplots.AxesSubplot object at 0x7f8a9c96a3d0>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f8a9c924cd0>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f8a9c8e9550>],\n",
              "       [<matplotlib.axes._subplots.AxesSubplot object at 0x7f8a9c8a1d10>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f8a9c869290>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f8a9c8692d0>],\n",
              "       [<matplotlib.axes._subplots.AxesSubplot object at 0x7f8a9c81c550>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f8a9c7fdb50>,\n",
              "        <matplotlib.axes._subplots.AxesSubplot object at 0x7f8a9c74b690>]],\n",
              "      dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 37
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x720 with 12 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Boxplot\n",
        "sns.boxplot(x='Geography',y='EstimatedSalary',data=df)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 279
        },
        "id": "4P49QmDfEEBs",
        "outputId": "5e854bd7-d6dc-413e-a643-9df1994bdf32"
      },
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZgAAAEGCAYAAABYV4NmAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3df5xVdb3v8dcb1PxBhj+IiIHAGOuSp1AnpdsvyzL0aGg/TOsImleyNOxaJ7U6RzK9WeekN/pBURJ4T4nmjyQPRlySPJWoI5gopoz4awgRUVFTMeRz/ljfLctxz8yemb32Zs+8n4/Hfuy1Puv7/a7vZgGfvdb67u9SRGBmZlZtg+rdATMz65+cYMzMrBBOMGZmVggnGDMzK4QTjJmZFWKHendge7H33nvHmDFj6t0NM7OGcttttz0WEcPKbXOCScaMGUNra2u9u2Fm1lAkPdjZNl8iMzOzQjjBmJlZIZxgzMysEE4wZmZWCCcYMzMrRGEJRtIoSTdIWiXpLklnpPiekhZLWp3e90hxSZopqU3SHZIOyLU1NZVfLWlqLn6gpJWpzkxJ6mofZmZWO0WewWwBvhgR44GJwGmSxgNnA0siohlYktYBDgea02saMAuyZAGcCxwMHAScm0sYs4BTcvUmpXhn+zAzsxop7HcwEbEOWJeWn5Z0NzASmAwckorNA5YCZ6X4pZE9P2CZpKGSRqSyiyPicQBJi4FJkpYCu0fEshS/FDgauL6LfWzXZs6cSVtbW9XbbW9vB6CpqanqbY8bN47p06dXvd1G04jHDnz8Shrx+DXCsavJDy0ljQH2B24GhqfkA/AIMDwtjwQezlVrT7Gu4u1l4nSxj479mkZ2tsTo0aN7+Kkax3PPPVfvLlgv+dg1toF+/ApPMJKGAFcBX4iIp9JtEgAiIiQV+sSzrvYREbOB2QAtLS11f/JaUd9GSu3OnDmzkPbNx67R+fgVo9BRZJJ2JEsuP4+Iq1N4fbr0RXp/NMXXAqNy1ZtSrKt4U5l4V/swM7MaKXIUmYBLgLsj4qLcpgVAaSTYVODaXHxKGk02EdiULnMtAg6TtEe6uX8YsChte0rSxLSvKR3aKrcPMzOrkSIvkb0TOAFYKen2FPsKcCFwhaSTgQeBY9O2hcARQBvwLHASQEQ8LukbwK2p3HmlG/7A54C5wC5kN/evT/HO9mFmZjVS5CiyPwDqZPOhZcoHcFonbc0B5pSJtwL7lYlvLLcPMzOrHf+S38zMCuEEY2ZmhXCCMTOzQjjBmJlZIZxgzMysEE4wZmZWCCcYMzMrhBOMmZkVwgnGzMwK4QRjZmaFcIIxM7NCOMGYmVkhnGDMzKwQTjBmZlYIJxgzMyuEE4yZmRWiyEcmz5H0qKQ7c7HLJd2eXg+UnnQpaYyk53LbfpSrc6CklZLaJM1Mj0dG0p6SFktand73SHGlcm2S7pB0QFGf0czMOlfkGcxcYFI+EBGfiIgJETEBuAq4Orf5vtK2iDg1F58FnAI0p1epzbOBJRHRDCxJ6wCH58pOS/XNzKzGCkswEXEj8Hi5beks5Fjgsq7akDQC2D0ilqVHKl8KHJ02TwbmpeV5HeKXRmYZMDS1Y2ZmNVSvezDvBtZHxOpcbKykFZJ+L+ndKTYSaM+VaU8xgOERsS4tPwIMz9V5uJM6LyNpmqRWSa0bNmzow8cxM7OO6pVgjuflZy/rgNERsT9wJvALSbtX2lg6u4mediIiZkdES0S0DBs2rKfVzcysCzvUeoeSdgA+AhxYikXEZmBzWr5N0n3AvsBaoClXvSnFANZLGhER69IlsEdTfC0wqpM6ZmZWI/U4g/kA8JeIeOnSl6Rhkgan5X3IbtCvSZfAnpI0Md23mQJcm6otAKam5akd4lPSaLKJwKbcpTQzM6uRIocpXwbcBLxJUrukk9Om43jlzf33AHekYctXAqdGRGmAwOeAnwJtwH3A9Sl+IfBBSavJktaFKb4QWJPK/yTVNzOzGivsEllEHN9J/MQysavIhi2XK98K7FcmvhE4tEw8gNN62F0zM6sy/5LfzMwK4QRjZmaFcIIxM7NCOMGYmVkhnGDMzKwQTjBmZlYIJxgzMyuEE4yZmRXCCcbMzArhBGNmZoVwgjEzs0I4wZiZWSGcYMzMrBBOMGZmVggnGDMzK0SRDxybI+lRSXfmYjMkrZV0e3odkdt2jqQ2SfdI+lAuPinF2iSdnYuPlXRzil8uaacUf1Vab0vbxxT1Gc3MrHNFnsHMBSaViV8cERPSayGApPFkT7p8S6rzQ0mD02OUfwAcDowHjk9lAb6V2hoHPAGUnph5MvBEil+cypmZWY0V+UTLG3tw9jAZmB8Rm4H7JbUBB6VtbRGxBkDSfGCypLuB9wOfTGXmATOAWamtGSl+JfB9SUpPujSzBjVz5kza2trq3Y0eWb16NQDTp0+vc096Zty4cVXpc2EJpgunS5oCtAJfjIgngJHAslyZ9hQDeLhD/GBgL+DJiNhSpvzIUp2I2CJpUyr/WDU677/ktVOtv+TWP7S1tbHirhUwtN496YGt2duKtSvq24+eeLJ6TdU6wcwCvgFEev8O8Oka9+ElkqYB0wBGjx5dUZ22tjZWrFzF1l33LLJrVaUXspO32+57pM49qdygZx+vdxdsezQUth6ytd696NcGLa3enZOaJpiIWF9alvQT4Lq0uhYYlSvalGJ0Et8IDJW0QzqLyZcvtdUuaQfgNal8uf7MBmYDtLS0VHwJbeuue/L8+CMrLW69sPOq67ov1AuNdgbqs09rZDVNMJJGRMS6tHoMUBphtgD4haSLgNcDzcAtgIBmSWPJEsdxwCcjIiTdAHwMmA9MBa7NtTUVuClt/53vv1hJW1sb9965nNFDXqx3Vyqy09+zb5PPP3BrnXtSuYeeGVzvLth2orAEI+ky4BBgb0ntwLnAIZImkF0iewD4DEBE3CXpCmAVsAU4LSJeTO2cDiwCBgNzIuKutIuzgPmSzgdWAJek+CXA/0sDBR4nS0pmLxk95EW+1vJMvbvRb53fOqTeXbDtRJGjyI4vE76kTKxU/gLggjLxhcDCMvE1bBtplo8/D3y8R501M7Oq8y/5zcysEE4wZmZWCCcYMzMrhBOMmZkVwgnGzMwK4QRjZmaFqCjBSDpKkpORmZlVrNKk8QlgtaRvS3pzkR0yM7P+oaIEExH/BOwP3AfMlXSTpGmSXl1o78zMrGFVfNkrIp4ie77KfGAE2VxiyyV9vqC+mZlZA6v0HsxkSdcAS4EdgYMi4nDgbcAXi+uemZk1qkrnIjuG7PHEN+aDEfGspJM7qWNmZgNYt2cwkgYDb+iYXEoiYknVe2VmZg2v2wSTps3fKuk1NeiPmZn1E5VeInsGWClpMfC3UjAi/Mg6MzMrq9IEc3V6mZmZVaSiBBMR83rasKQ5wJHAoxGxX4r9G3AU8ALZb2pOiognJY0B7gbuSdWXRcSpqc6BwFxgF7IHj52RHpm8J3A5MIbs6ZjHRsQTkgR8FzgCeBY4MSKW97T/ZmbWN5UOU26WdKWkVZLWlF7dVJsLTOoQWwzsFxFvBe4Fzsltuy8iJqTXqbn4LOAUoDm9Sm2eDSyJiGZgSVoHODxXdlqqb2ZmNVbpDy1/RvYf9RbgfcClwH90VSGNOnu8Q+y3EbElrS4DmrpqQ9IIYPeIWBYRkfZ7dNo8GSidWc3rEL80MsuAoakdMzOroUoTzC5pOLIi4sGImAH8Yx/3/Wng+tz6WEkrJP1e0rtTbCTQnivTnmIAwyNiXVp+BBieq/NwJ3VeJk130yqpdcOGDX34KGZm1lGlN/k3p9mUV0s6HVgLDOntTiV9lexs6OcptA4YHREb0z2XX0l6S6XtpXsy0dN+RMRsYDZAS0tLj+ubmVnnKj2DOQPYFZgOHAicAEztzQ4lnUh28/9T6bIXEbE5Ijam5dvIBgDsS5bI8pfRmlIMYH3p0ld6fzTF1wKjOqljZmY1UulsyrdGxDMR0R4RJ0XER9L9jR6RNAn4MvDhiHg2Fx+WZgxA0j5kN+jXpEtgT0mamEaHTQGuTdUWsC3JTe0Qn6LMRGBT7lKamZnVSJeXyCT9Guj00lFEfLiLupcBhwB7S2oHziUbNfYqYHGWL14ajvwe4DxJfwe2AqdGRGmAwOfYNkz5erbdt7kQuCLNhfYgcGyKLyQbotxGNkz5pK4+o5mZFaO7ezD/3tuGI+L4MuFLOil7FXBVJ9tagf3KxDcCh5aJB3BajzprZmZV12WCiYjf16ojZmbWv1Q0ikxSM/BNYDywcykeEfsU1C8zM2twhf3Q0szMBrZ6/tDSzMz6sbr80NLMzPq/mv/Q0szMBoZKp+u/NS0+I+lM4MnSr/DNzMzK6fIMRtK/SnpzWn6VpBvIpnFZL+kDteigmZk1pu4ukX2CbQ8BK10SGwa8F/g/RXXKzMwaX3cJ5oXcpbAPAfMj4sWIuJvKBwiYmdkA1F2C2SxpP0nDyH7/8tvctl2L65aZmTW67s5CvgBcSXZZ7OKIuB9A0hHAioL7ZmZmDay7uciWAW8uE19INmuxmZlZWd1N139mV9sj4qLqdsfMzPqL7i6RvTq9vwl4O9nDvACOAm4pqlNmZtb4urtE9nUASTcCB0TE02l9BvCfhffOzMwaVqVDjYcDL+TWX0ixLkmaAxwJPBoR+6XYnsDlwBjgAeDYiHgiPRL5u2RPo3wWODEilqc6U4GvpWbPj4h5KX4g2552uRA4IyKis31U+FnNbDvU3t4Om2DQ0kpnuLJeeRLao70qTVV6pC4FbpE0I5293AzMq6DeXGBSh9jZwJKIaAaWpHWAw4Hm9JpG9niAUkI6FzgYOAg4V9Ieqc4s4JRcvUnd7MPMzGqk0rnILpB0PfDuFDopIrodphwRN0oa0yE8GTgkLc8DlgJnpfil6YedyyQNlTQilV0cEY8DSFoMTJK0FNg9jXRD0qXA0cD1XezDBrj29nb+9vRgzm/1ZOBFefDpwezWXp1vwHlNTU1s0Aa2HrK16m3bNoOWDqJpZFNV2urJr/F3BZ6KiJ9JGiZpbOl3MT00PCLWpeVH2HapbSTwcK5ce4p1FW8vE+9qHy8jaRrZ2RKjR4+uqPPt7e0MenYTO6+6rqLy1juDnt1Ie/uWenfDzPqg0kcmnwu0kI0m+xmwI9kTLd/Zl52n+yWFzsrc1T4iYjYwG6ClpcWzQw8ATU1NPL9lHV9reabeXem3zm8dws5N1fkGbI2t0jOYY4D9geUAEfFXSa/uukqn1ksaERHr0iWwR1N8LTAqV64pxday7XJXKb40xZvKlO9qH33W1NTE+s078Pz4I6vVpJWx86rraGp6Xb27YWZ9UOlN/tKklwEgabc+7HMB22Zmngpcm4tPUWYisCld5loEHCZpj3Rz/zBgUdr2lKSJaQTalA5tlduHmZnVSKVnMFdI+jEwVNIpwKeBn3ZXSdJlZGcfe0tqJxsNdmFq72TgQeDYVHwh2RDlNrJhyicBRMTjkr4BlB56dl7phj/wObYNU74+vehiH2ZmViOVjiL7d0kfBJ4iuw/zrxGxuIJ6x3ey6dAyZQM4rZN25gBzysRbgf3KxDeW24eZmdVOpTf5vxURZwGLy8TMzMxeodJ7MB8sEzu8mh0xM7P+pbvZlD9Ldp9jH0l35Da9GvhjkR0zM7PG1t0lsl+Q3Tj/Ji+fbuXp3I12MzOzV+huNuVNwCbgeABJrwV2BoZIGhIRDxXfRTMza0QV3YORdJSk1cD9wO/JZii+vstKZmY2oFV6k/98YCJwb0SMJRsCvKywXpmZWcOrNMH8Pf22ZJCkQRFxA9ncZGZmZmVV+kv+JyUNAW4Efi7pUeBvxXXLzMwaXaVnMJOB54D/DfwGuA84qqhOmZlZ46t0qpi/AUjaHfh1oT0yM7N+odKpYj4DfB14HtgKiGxm5X2K65qZmTWySu/BfAnYLyIeK7IzZmbWf1R6D+Y+sin0zczMKlLpGcw5wJ8k3QxsLgUjYnohvTIzs4ZXaYL5MfA7YCXZPRgzM7MuVZpgdoyIM6uxQ0lvAi7PhfYB/hUYCpwCbEjxr0TEwlTnHOBk4EVgekQsSvFJwHeBwcBPI+LCFB8LzAf2Am4DToiIF6rRfzMzq0yl92CulzRN0ghJe5ZevdlhRNwTERMiYgJwINm9nWvS5otL23LJZTxwHPAWYBLwQ0mDJQ0GfkD2XJrxwPGpLMC3UlvjgCfIkpOZmdVQpWcwpUcfn5OLVWOY8qHAfRHxoKTOykwG5kfEZuB+SW3AQWlbW0SsAZA0H5gs6W7g/cAnU5l5wAxgVh/7amZmPVDpDy3HFrT/44DLcuunS5oCtAJfjIgngJG8fGLN9hQDeLhD/GCyy2JPRsSWMuVfRtI0YBrA6NGj+/ZJzMzsZbq8RCbp/en9I+VefdmxpJ2ADwO/TKFZwBuBCcA64Dt9ab8SETE7IloiomXYsGFF787MbEDp7gzmvWSjx8rNOxbA1X3Y9+HA8ohYD1B6B5D0E+C6tLoWGJWr15RidBLfCAyVtEM6i8mXNzOzGunuiZbnpsXzIuL+/LY0Uqsvjid3eUzSiIhYl1aPAe5MywuAX0i6CHg90AzcQjZdTXPqx1qyy22fjIiQdAPwMbKRZFOBa/vYVzMz66FKR5FdVSZ2ZW93Kmk34IO8/Azo25JWSroDeB/ZzM1ExF3AFcAqspmcT4uIF9PZyenAIuBu4IpUFuAs4Mw0IGAv4JLe9tXMzHqnyzMYSW8mGx78mg73XHYHdu7tTtPszHt1iJ3QRfkLgAvKxBcCC8vE17BtpJmZmdVBd/dg3gQcSfYjyPx9mKfJfhRpZmZWVnf3YK4FrpX0joi4qUZ9MjOzfqDSezDHSNpd0o6SlkjaIOmfCu2ZmZk1tEoTzGER8RTZ5bIHgHHAPxfVKTMza3yVJpgd0/s/Ar+MiE0F9cfMzPqJSuci+7WkvwDPAZ+VNIzs8clmZmZlVXQGExFnA/8TaImIv5PNgDy5yI6ZmVlj624usi/nVg+NiBfhpd+x+GmWZmbWqe7OYI7LLZ/TYdukKvfFzMz6ke4SjDpZLrduZmb2ku4STHSyXG7dzMzsJd2NInubpKfIzlZ2Scuk9V7PRWZmZv1fd1PFDK5VR8zMrH+p9IeWZmZmPeIEY2ZmhahbgpH0QHrA2O2SWlNsT0mLJa1O73ukuCTNlNQm6Q5JB+TamZrKr5Y0NRc/MLXflup61JuZWQ1VOlVMUd4XEY/l1s8GlkTEhZLOTutnAYeTPSq5GTgYmAUcLGlP4FyghWxU222SFkTEE6nMKcDNZA8lmwRcX41OD3r2cXZedV01mqoJPZ+NzYidd69zTyo36NnHgdfVuxtm1gf1TjAdTQYOScvzgKVkCWYycGlEBLBM0lBJI1LZxRHxOICkxcAkSUuB3SNiWYpfChxNFRLMuHHj+tpEza1e/TQAzW9spP+wX1fYn/VDzwzm/NYhhbRdbeufzS4yDN91a517UrmHnhnMvkU1/iQMWtpAV/afSe+N8dct8yQwsjpN1TPBBPBbSQH8OCJmA8MjYl3a/ggwPC2PBB7O1W1Psa7i7WXifTZ9euPNkFPq88yZM+vck/prtC8IL6xeDcDOY5rr3JPK7Usxf86NduwAVqfj1zyycY4fI6v3Z13PBPOuiFgr6bXA4jRb80siIlLyKYykacA0gNGjRxe5K9tONNoXBH852KbRjh34+NXtXDMi1qb3R4FrgIOA9enSF+n90VR8LTAqV70pxbqKN5WJd+zD7IhoiYiWYcOGVeNjmZlZUpcEI2k3Sa8uLQOHAXcCC4DSSLCpwLVpeQEwJY0mmwhsSpfSFgGHSdojjTg7DFiUtj0laWIaPTYl15aZmdVAvS6RDQeuSSOHdwB+ERG/kXQrcIWkk4EHgWNT+YXAEUAb2bNoTgKIiMclfQO4NZU7r3TDH/gcMBfYhezmflVGkJmZWWXqkmAiYg3wtjLxjcChZeIBnNZJW3OAOWXircB+fe6smZn1SgON9zMzs0biBGNmZoVwgjEzs0I4wZiZWSGcYMzMrBBOMGZmVggnGDMzK4QTjJmZFcIJxszMCuEEY2ZmhXCCMTOzQjjBmJlZIZxgzMysEE4wZmZWCCcYMzMrhBOMmZkVouYJRtIoSTdIWiXpLklnpPgMSWsl3Z5eR+TqnCOpTdI9kj6Ui09KsTZJZ+fiYyXdnOKXS9qptp/SzMzqcQazBfhiRIwHJgKnSRqftl0cERPSayFA2nYc8BZgEvBDSYMlDQZ+ABwOjAeOz7XzrdTWOOAJ4ORafTgzM8vUPMFExLqIWJ6WnwbuBkZ2UWUyMD8iNkfE/UAbcFB6tUXEmoh4AZgPTJYk4P3Alan+PODoYj6NmZl1pq73YCSNAfYHbk6h0yXdIWmOpD1SbCTwcK5ae4p1Ft8LeDIitnSIl9v/NEmtklo3bNhQhU9kZmYldUswkoYAVwFfiIingFnAG4EJwDrgO0X3ISJmR0RLRLQMGzas6N2ZmQ0oO9Rjp5J2JEsuP4+IqwEiYn1u+0+A69LqWmBUrnpTitFJfCMwVNIO6SwmX97MzGqkHqPIBFwC3B0RF+XiI3LFjgHuTMsLgOMkvUrSWKAZuAW4FWhOI8Z2IhsIsCAiArgB+FiqPxW4tsjPZGZmr1SPM5h3AicAKyXdnmJfIRsFNgEI4AHgMwARcZekK4BVZCPQTouIFwEknQ4sAgYDcyLirtTeWcB8SecDK8gSmpmZ1VDNE0xE/AFQmU0Lu6hzAXBBmfjCcvUiYg3ZKDMzM6sT/5LfzMwK4QRjZmaFcIIxM7NCOMGYmVkhnGDMzKwQTjBmZlYIJxgzMyuEE4yZmRXCCcbMzArhBGNmZoVwgjEzs0I4wZiZWSGcYMzMrBBOMGZmVggnGDMzK4QTjJmZFaLfJhhJkyTdI6lN0tn17o+Z2UDTLxOMpMHAD4DDgfFkj2MeX99emZkNLIqIeveh6iS9A5gRER9K6+cARMQ3O6vT0tISra2tNepheTNnzqStra3q7a5evRqA5ubmqrc9btw4pk+fXvV2G00jHjvw8StpxOO3vRw7SbdFREu5bTvUujM1MhJ4OLfeDhzcsZCkacA0gNGjR9emZ3Wwyy671LsL1ks+do1toB+//noG8zFgUkT8r7R+AnBwRJzeWZ3t4QzGzKzRdHUG0y/vwQBrgVG59aYUMzOzGumvCeZWoFnSWEk7AccBC+rcJzOzAaVf3oOJiC2STgcWAYOBORFxV527ZWY2oPTLBAMQEQuBhfXuh5nZQNVfL5GZmVmdOcGYmVkhnGDMzKwQTjBmZlaIfvlDy96QtAF4sN79KNDewGP17oT1io9dY+vvx+8NETGs3AYnmAFCUmtnv7a17ZuPXWMbyMfPl8jMzKwQTjBmZlYIJ5iBY3a9O2C95mPX2Abs8fM9GDMzK4TPYMzMrBBOMGZmVggnmAYh6UVJt+deY+rdJ+sdSV+VdJekO9KxfMXTVito48OSzi6ifwOZpOGSfiFpjaTbJN0k6Zh696tR+R5Mg5D0TEQM6WSbyI7l1hp3y3pI0juAi4BDImKzpL2BnSLir3Xu2oCX/h39CZgXET9KsTcAH46I71VQf4eI2FJwNxuKz2AalKQxku6RdClwJzBK0ixJrenb8ddzZR+Q9HVJyyWtlPTmFB8i6Wcpdoekj6b4Yemb23JJv5RUNrFZr4wAHouIzQAR8VhE/DUdo2+nY3GLpHEAko6SdLOkFZL+v6ThKX6ipO+n5bmSZkr6U/rm/bG6fbrG9n7ghVJyAYiIByPie5IGS/o3SbemfyufAZB0iKT/krQAWJXWfy/p2nQsLpT0qXRMV0p6Y6rX2XGdIWmOpKWp/vQUP0/SF0r9knSBpDNq+YfTG04wjWOX3OWxa1KsGfhhRLwlIh4Evpp+MfxW4L2S3pqr/1hEHADMAr6UYv8CbIqIf4iItwK/S9+ovwZ8IJVvBc6swecbKH5L9mXgXkk/lPTe3LZNEfEPwPeB/5tifwAmRsT+wHzgy520OwJ4F3AkcGExXe/33gIs72TbyWTH5+3A24FTJI1N2w4AzoiIfdP624BTgf8BnADsGxEHAT8FPp/KdHVc3wx8CDgIOFfSjsAcYAqApEFkT+n9j7593OL12weO9UPPRcSE0kq6B/NgRCzLlTlW0jSy4zoCGA/ckbZdnd5vAz6Slj9A9hcVgIh4QtKRqd4fsysG7ATcVO0PM1BFxDOSDgTeDbwPuDx3L+Wy3PvFabkplRlBdizu76TpX6VLpKtK34atbyT9gCxpv0A2T+Fbc2eHryH7gvcCcEtE5I/LrRGxLrVxH9mXCoCVZMccuj6u/5nOcDdLehQYHhEPSNooaX9gOLAiIjZW+SNXnRNMY/tbaSF9m/oS8PaUKOYCO+fKbk7vL9L1cRewOCKOr3JfLYmIF4GlwFJJK4GppU35Yun9e8BFEbFA0iHAjE6a3ZxbVtU6O7DcBXy0tBIRp6Uz+lbgIeDzEbEoXyEdk7/xcvljsTW3vpVt//a6Oq75+vl/rz8FTgReR3ZGs93zJbL+Y3eyv+ib0jfYwyuosxg4rbQiaQ9gGfDO3D2A3STt20l96yFJb5LUnAtNYNss3p/IvZfOGl8DrE3LU7Ei/Q7YWdJnc7Fd0/si4LPpchWS9pW0Wx/21Zvjeg0wiewS3aJuym4XfAbTT0TEnyWtAP4CPAz8sYJq5wM/kHQn2Telr0fE1ZJOBC6T9KpU7mvAvQV0eyAaAnxP0lBgC9AGTCO7d7KHpDvIvsGWziBnAL+U9ATZf4BjX9GiVUVEhKSjgYslfRnYQPal7Szgl8AYYLmya8cbgKP7sLsZ9PC4RsQLkm4Ankxnwds9D1M22w5IegBoiYj+/NwQ64N0c3858PGIWF3v/lTCl8jMzLZzksaTne0uaZTkAj6DMTOzgvgMxszMCuEEY2ZmhXCCMTOzQjjBmPWSGmDm3fycZWa15gRj1gvptxC/Am6MiH0i4kCyaXeaCtzn4KLaNiuCE4xZ7/Rm5l2l+J1pZt1PpPigNPHlXyQtlrSwNOeVslmWvyVpOfBxSaekdv8s6SpJu6ZycyX9SNls2vemOeVKXi/pN5JWS/p2Kv9pSaUJNSOHSBwAAAHpSURBVEntXoxZFfmX/Ga9U9HMu2k2hD9K+i3ZrLsTyGbb3Ru4VdKNwDvJfiU+HngtcDcvn2tqY5rZGkl7RcRP0vL5aV+lZ5WMIZuB943ADaXpftI+9yebIeAeSd8DrgC+KumfI+LvwEnAZ3r/x2H2Sk4wZlVQ4cy77wIuS9N8rJf0e7J5pd4F/DLNhvxImg4k7/Lc8n4psQwlm3YmPyfVFamN1ZLWkE37DtmP8zalfq4C3hARD0v6HXCkpLuBHSNiZRX+KMxe4gRj1ju9mXm3kglIy8nP1jsXODrNPXcicEhuW8dfTZfWu5qd9ytk89f9rJd9M+uU78GY9U5vZt79L+AT6R7NMOA9wC1kE5N+NN2LGc7Lk0ZHrwbWpbY/1WHbx1MbbwT2Ae7p6gNExM3AKOCTbHsWjVnV+AzGrBd6OfPuNcA7gD+TnV18OSIekXQVcCiwimwm7OXApk52/S/AzanNm8kSTslDZAlrd+DUiHg+232XrgAmRMQTlX96s8p4LjKz7YCkIelpl3uRJYl3RsQjPag/F7guIq7s4X6vAy6OiCU96rBZBXwGY7Z9uC49I2Yn4Bs9SS69kfZ1C/BnJxcris9gzMysEL7Jb2ZmhXCCMTOzQjjBmJlZIZxgzMysEE4wZmZWiP8GXwprYy3Sk+AAAAAASUVORK5CYII=\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Bivariate Analysis on continuous variable\n",
        "sns.lineplot(df.Age,df.Exited)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 351
        },
        "id": "NDjrHnItgJkB",
        "outputId": "b1f1f0f4-de10-4b47-edc5-ef1f1e8918ff"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f8a9c438650>"
            ]
          },
          "metadata": {},
          "execution_count": 39
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.scatterplot(df.Age,df.Balance)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 351
        },
        "id": "MOPEMQ8xyW_C",
        "outputId": "5c459e70-5105-4523-e445-ef97b9295f5d"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f8a9c308b10>"
            ]
          },
          "metadata": {},
          "execution_count": 40
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Bivariate Analysis on categorical variable\n",
        "sns.barplot(df.Tenure.value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 351
        },
        "id": "8f5AIcrC2_yt",
        "outputId": "3c62d8e7-9bdd-4012-dbe2-69c6d459a3b2"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f8a9c313150>"
            ]
          },
          "metadata": {},
          "execution_count": 41
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWAAAAEGCAYAAABbzE8LAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAKoklEQVR4nO3dXYzld13H8c93d90W1qZPW9mVVqZNCBFNLC1pukEN8aGSxuhNEyGYLT6ERL0QTTRtNFEvuKBFg6iRNooBo4gCUdLEFCjgBReFXQXsA6WLPLUBS0kEaWIL7c+L/3+2pxtgZzpz9js75/VKJnPO//zn7O93fifvnfM/D1NjjABw5u3pHgDAqhJggCYCDNBEgAGaCDBAk32b2fngwYNjbW1tSUMB2J2OHz/+6BjjklO3byrAa2trOXbs2PaNCmAFVNXnv912hyAAmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATTb1Rznvf+irufp33r6ssQA8w/Fbj3YPYan8BgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoIkAAzQRYIAmAgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoIkAAzQRYIAmAgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoIkAAzQRYIAmAgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE32dQ8AOPMOPPi+7Hnise5hnNbRox/oHsJJhw4dyi233LKt13naAFfVa5O8Nkn2n3fxtv7jQI89TzyWvY9/vXsYp/Xwwzt/jFtx2gCPMW5PcnuSHDh0+Vj6iICle2r/ge4hbMgPHDyvewgnHTp0aNuv0yEIWEGPvfC67iFsyNtvPdo9hKXyJBxAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoIkAAzQRYIAmAgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoIkAAzQRYIAmAgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoIkAAzQRYIAmAgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoMm+zez8g5denGO3Hl3WWABWit+AAZoIMEATAQZoIsAATQQYoIkAAzQRYIAmAgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKBJjTE2vnPV/yZ5YHnD2bEOJnm0exBNzH01rerclzXvF4wxLjl146b+LH2SB8YYL92mAZ01qurYKs47MXdzXy1net4OQQA0EWCAJpsN8O1LGcXOt6rzTsx9Va3q3M/ovDf1JBwA28chCIAmAgzQZEMBrqpXVNUDVXWiqm5a9qDOtKq6rKo+VFX3VdW9VfWb8/aLqur9VfXg/P3CeXtV1Zvn2+OTVXVV7wy2pqr2VtV/VNUd8/nLq+rueX7vrKr98/Zz5vMn5svXOse9VVV1QVW9q6o+VVX3V9WRFVrz35rv6/dU1Tuq6tzduu5V9daqeqSq7lnYtul1rqob5/0frKobt2VwY4zv+pVkb5LPJLkiyf4kn0jy4tP93Nn0leRwkqvm0+cl+XSSFye5JclN8/abkrxhPn19kn9NUkmuTXJ39xy2OP/fTvL3Se6Yz/9jklfOp9+S5Nfm07+e5C3z6VcmeWf32Lc477cl+dX59P4kF6zCmid5fpLPJnnOwnq/Zreue5IfT3JVknsWtm1qnZNclOS/5u8Xzqcv3PLYNjD4I0nuXDh/c5Kbu2/UJS/YvyT56Uzv+js8bzuc6Y0oSXJbklct7H9yv7PtK8mlSe5K8hNJ7pjveI8m2Xfq+ie5M8mR+fS+eb/qnsOznPf5c4TqlO2rsObPT/LFOSb75nX/md287knWTgnwptY5yauS3Law/Rn7PduvjRyCWF+sdQ/N23al+eHVS5LcneR5Y4wvzRd9Ocnz5tO76TZ5U5LfTfLUfP7iJP8zxvjWfH5xbifnPV/+tXn/s9HlSb6S5G/mwy9/VVUHsgJrPsZ4OMkbk3whyZcyrePxrMa6r9vsOi9l/T0Jt6CqvjfJu5O8bozx9cXLxvTf3q56zV5V/WySR8YYx7vH0mBfpoelfznGeEmSxzI9FD1pN655kszHO38+039C35/kQJJXtA6qUec6byTADye5bOH8pfO2XaWqvidTfP9ujPGeefN/V9Xh+fLDSR6Zt++W2+RlSX6uqj6X5B8yHYb40yQXVNX654Qszu3kvOfLz0/y1TM54G30UJKHxhh3z+fflSnIu33Nk+Snknx2jPGVMcY3k7wn031hFdZ93WbXeSnrv5EAfyzJC+dnSPdnOgj/3q3+wztJVVWSv05y/xjjTxYuem+S9Wc7b8x0bHh9+9H5GdNrk3xt4eHMWWOMcfMY49Ixxlqmdf3gGOPVST6U5IZ5t1PnvX573DDvf1b+hjjG+HKSL1bVi+ZNP5nkvuzyNZ99Icm1VfXc+b6/Pvddv+4LNrvOdya5rqounB9BXDdv25oNHsC+PtMrAz6T5Pe6D6gv4QD9j2Z6CPLJJB+fv67PdJzrriQPJvlAkovm/SvJX8y3x38meWn3HLbhNnh5nn4VxBVJPprkRJJ/SnLOvP3c+fyJ+fIruse9xTlfmeTYvO7/nOnZ7ZVY8yR/lORTSe5J8rdJztmt657kHZmOdX8z0yOfX3k265zkl+fb4ESSX9qOsXkrMkATT8IBNBFggCYCDNBEgAGaCDBAk83+UU7YdlW1/pKgJDmU5MlMbxNOkmvGGE+0DAyWzMvQ2FGq6g+TfGOM8cYlXf/eMcaTy7hu2CyHINiRqurqqvq3qjpeVXcuvG30w1X1hqr6aFV9uqp+bN7+mqr684Wfv6OqXj6f/kZV/XFVfSLJkar6xfnnP15Vt1XV3o45ggCzE1WSP0tywxjj6iRvTfL6hcv3jTGuSfK6JH+wges7kOlzXX8k02cY/EKSl40xrsx0uOPV2zl42CjHgNmJzknyw0neP31UQfZmeivpuvUPSzqe6XNeT+fJTB+0lEyfe3B1ko/N1/2cPP1BLHBGCTA7USW5d4xx5Dtc/vj8/ck8fR/+Vp75iO7chdP/t3Dct5K8bYxx83YNFp4thyDYiR5PcklVHUmmjwqtqh86zc98LsmVVbWnqi5Lcs132O+uJDdU1ffN131RVb1gm8YNm+I3YHaipzJ97OGbq+r8TPfTNyW597v8zEcy/Ymh+5Lcn+Tfv91OY4z7qur3k7yvqvZk+oSs30jy+e0bPmyMl6EBNHEIAqCJAAM0EWCAJgIM0ESAAZoIMEATAQZo8v+ciuEPNYAYhAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fig=plt.figure(figsize=(10,8))\n",
        "sns.heatmap(df.corr(),annot=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 576
        },
        "id": "NmiI9VvENtlU",
        "outputId": "752cf45b-c677-436f-d6e5-186161f282ae"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f8a9c313050>"
            ]
          },
          "metadata": {},
          "execution_count": 42
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 720x576 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.barplot(df.NumOfProducts.value_counts().index,df.NumOfProducts.value_counts())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 337
        },
        "id": "VYbeNcJt4Hq0",
        "outputId": "c2be3f42-4a00-4cd9-d2c7-4bc7167ca913"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f8a9c04b6d0>"
            ]
          },
          "metadata": {},
          "execution_count": 43
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.violinplot(x='NumOfProducts',y='Age',data=df,size=8)\n",
        "plt.show\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 296
        },
        "id": "SyhtezXdd_rB",
        "outputId": "3959c5af-35a9-4aac-b308-b633fd19bbc8"
      },
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<function matplotlib.pyplot.show(*args, **kw)>"
            ]
          },
          "metadata": {},
          "execution_count": 65
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.boxplot(df.Age)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 351
        },
        "id": "XMRBeTY6xJv6",
        "outputId": "82fc29ba-4db2-4b95-eb3b-50a5aeb03a1e"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f8a9a8329d0>"
            ]
          },
          "metadata": {},
          "execution_count": 45
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWAAAAEGCAYAAABbzE8LAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAPyUlEQVR4nO3da4xc9XmA8ee1t8HGTrnYQF2bdhNtAVEgBKMUCEUDMcXcQikGYXExEoIvlW2gqGrBNZgCEhK4IEupZEoLpG1SIGkpyJjYAUpbJKJdwv2STBs3scUthpCaW2r498M5s9lZNnjXHvadxc9PsuwzZ87M65njx2ePZ4+jlIIkafxNyh5AknZWBliSkhhgSUpigCUpiQGWpCQ9Y7nzzJkzS29v7yc0iiR9+sycOZMHH3zwwVLK/OHrxhTg3t5e+vv7OzeZJO0EImLmSLd7CkKSkhhgSUpigCUpiQGWpCQGWJKSGGBJSmKAJSmJAZakJAZYkpIYYElKYoAlKYkBlqQkBliSkhhgSUpigCUpiQGWpCQGWJKSGGBJSmKAJSnJmP5POH28VatW0Ww2O/Z4mzZtAmD27Nkde8zR6OvrY/HixeP6nNLOyAB3ULPZ5MlnX+CDXffsyONNfuctAF55f/zepsnvvDFuzyXt7Axwh32w6568e8BJHXmsqS+uAejY443lOSV98jwHLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUnGJcCrVq1i1apV4/FU0rhwn1Yn9IzHkzSbzfF4GmncuE+rEzwFIUlJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAUgc0Go3BHyMtL1y4kEajwbnnnjuq+wOcddZZNBoNFi5cCMBpp51Go9Hg9NNPH/ExTzjhBBqNBvPnzwfg9NNPp9FocMYZZwCwZMkSGo0Gl1122Yjb33DDDTQaDW666SYArrjiChqNBsuXLx+cacWKFTQaDa677joA7r33XhqNBvfddx8ADz30EI1Gg4cffhiA/v5+jjvuOAYGBkZcv3nzZpYsWcLmzZtHXG42m5x88sk0m80R14/G9mwz1PAZOskAS+Pg5ZdfBmDjxo2j3ua1115r2/att94C4M033xzxMd9//30A3nvvvbb7tcLz9NNPA/DEE0+MuP0DDzwAMBjTxx57DIBHH310cKZWONetWwfAzTffDMDKlSsBuP766wEGA3311Vfz4YcfctVVV424/o477uCZZ57hzjvvHHH52muv5e233+baa68dcf1obM82Qw2foZMMsLSDhh61dmr5rLPO6uhjHnvssW3L8+bNa1tuHTW3nHnmmW3Ly5cvZ8WKFW23XXzxxZRSACilcOONN7J161YAtm7dym233caWLVsA2LJlC7feemvb+vvuu4+1a9dSSmHt2rU0m8225YGBATZs2ADAhg0bGBgYaFs/miPazZs3j3mboZrNZtsMnT4KjtYLOBqHH3546e/vH/OTLFiwgHfffZe+vr4xbzuRNJtN/vcXhbcPPbsjjzf1xTUAvHvASR15vNGY9uQ3+exn4lP/Xu2oZrPJ1KlTueeeez4SO41ORDB58mS2bt1KT08Pc+bMYePGjYPLU6ZMGQw4wPTp03nvvfcG15988slceumlH/scK1euZM2aNWPaZqgLLrhgMMAAvb293H777WP9rRIRA6WUw4ffvs0j4Ii4OCL6I6L/9ddfH/MTS9JISiltR8QbNmxoWx4aX6iOooeub50G+Tjr168f8zZDDY3vSMs7qmdbdyilrAZWQ3UEvD1PMnv2bABuueWW7dl8wli6dCkD//1q9hg75MMpv07f5/f51L9XO2rp0qXZI0x4O3oEfPzxx2/zOebNm9d2BDyabYbq7e39yBFwJ3kOWOpCe++9d0cfLyLalnt62o+9pkyZ0ra81157tS0fc8wxHzmPvN9++7Utn3LKKW3L5513XtvyOeec07Z82WWXMWlSlaDJkyezbNmytuXh55xXrFjRtv78889nWxYtWjTm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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Multivariate analysis\n",
        "sns.pairplot(data=df,hue='Geography',height=3)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "FHzCYHrNnfpk",
        "outputId": "3763b687-2d37-4511-f26b-4a68adcb6808"
      },
      "execution_count": 66,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 2457.88x2376 with 132 Axes>"
            ],
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#5 Find the outlier and replace the outlier\n",
        "#find the limits\n",
        "upper_limit=df['Age'].mean()+3*df['Age'].std()\n",
        "lower_limit=df['Age'].mean()-3*df['Age'].std()\n",
        "print('upper_limit',upper_limit)\n",
        "print('lower_limit',lower_limit)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_Xd_7SEZCGUM",
        "outputId": "9cd97525-8e61-401e-e098-00c3a3d67770"
      },
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "upper_limit 70.38521935511383\n",
            "lower_limit 7.458380644886169\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.loc[(df['Age']>upper_limit)|(df['Age']<lower_limit)]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "rWr-Mh5KV2E9",
        "outputId": "b47d3afe-131c-4dfe-966c-b2a0c3755781"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      RowNumber  CustomerId     Surname  CreditScore Geography  Gender  Age  \\\n",
              "85           86    15805254     Ndukaku          652     Spain  Female   75   \n",
              "158         159    15589975     Maclean          646    France  Female   73   \n",
              "230         231    15808473    Ringrose          673    France    Male   72   \n",
              "252         253    15793726   Matveyeva          681    France  Female   79   \n",
              "310         311    15712287  Pokrovskii          652    France  Female   80   \n",
              "...         ...         ...         ...          ...       ...     ...  ...   \n",
              "9646       9647    15603111        Muir          850     Spain    Male   71   \n",
              "9671       9672    15636061        Pope          649   Germany    Male   78   \n",
              "9736       9737    15644103       Wells          659     Spain    Male   78   \n",
              "9894       9895    15704795       Vagin          521    France  Female   77   \n",
              "9936       9937    15653037       Parks          609    France    Male   77   \n",
              "\n",
              "      Tenure    Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
              "85        10       0.00              2          1               1   \n",
              "158        6   97259.25              1          0               1   \n",
              "230        1       0.00              2          0               1   \n",
              "252        0       0.00              2          0               1   \n",
              "310        4       0.00              2          1               1   \n",
              "...      ...        ...            ...        ...             ...   \n",
              "9646      10   69608.14              1          1               0   \n",
              "9671       4   68345.86              2          1               1   \n",
              "9736       2  151675.65              1          0               1   \n",
              "9894       6       0.00              2          1               1   \n",
              "9936       1       0.00              1          0               1   \n",
              "\n",
              "      EstimatedSalary  Exited  \n",
              "85          114675.75       0  \n",
              "158         104719.66       0  \n",
              "230         111981.19       0  \n",
              "252         170968.99       0  \n",
              "310         188603.07       0  \n",
              "...               ...     ...  \n",
              "9646         97893.40       1  \n",
              "9671        142566.75       0  \n",
              "9736         49978.67       0  \n",
              "9894         49054.10       0  \n",
              "9936         18708.76       0  \n",
              "\n",
              "[133 rows x 14 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-af519247-9565-4bdd-93d9-bead3a0c449e\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>Surname</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>85</th>\n",
              "      <td>86</td>\n",
              "      <td>15805254</td>\n",
              "      <td>Ndukaku</td>\n",
              "      <td>652</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>75</td>\n",
              "      <td>10</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>114675.75</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>158</th>\n",
              "      <td>159</td>\n",
              "      <td>15589975</td>\n",
              "      <td>Maclean</td>\n",
              "      <td>646</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>73</td>\n",
              "      <td>6</td>\n",
              "      <td>97259.25</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>104719.66</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>230</th>\n",
              "      <td>231</td>\n",
              "      <td>15808473</td>\n",
              "      <td>Ringrose</td>\n",
              "      <td>673</td>\n",
              "      <td>France</td>\n",
              "      <td>Male</td>\n",
              "      <td>72</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>111981.19</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>252</th>\n",
              "      <td>253</td>\n",
              "      <td>15793726</td>\n",
              "      <td>Matveyeva</td>\n",
              "      <td>681</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>79</td>\n",
              "      <td>0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>170968.99</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>310</th>\n",
              "      <td>311</td>\n",
              "      <td>15712287</td>\n",
              "      <td>Pokrovskii</td>\n",
              "      <td>652</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>80</td>\n",
              "      <td>4</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>188603.07</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9646</th>\n",
              "      <td>9647</td>\n",
              "      <td>15603111</td>\n",
              "      <td>Muir</td>\n",
              "      <td>850</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Male</td>\n",
              "      <td>71</td>\n",
              "      <td>10</td>\n",
              "      <td>69608.14</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>97893.40</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9671</th>\n",
              "      <td>9672</td>\n",
              "      <td>15636061</td>\n",
              "      <td>Pope</td>\n",
              "      <td>649</td>\n",
              "      <td>Germany</td>\n",
              "      <td>Male</td>\n",
              "      <td>78</td>\n",
              "      <td>4</td>\n",
              "      <td>68345.86</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>142566.75</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9736</th>\n",
              "      <td>9737</td>\n",
              "      <td>15644103</td>\n",
              "      <td>Wells</td>\n",
              "      <td>659</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Male</td>\n",
              "      <td>78</td>\n",
              "      <td>2</td>\n",
              "      <td>151675.65</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>49978.67</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9894</th>\n",
              "      <td>9895</td>\n",
              "      <td>15704795</td>\n",
              "      <td>Vagin</td>\n",
              "      <td>521</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>77</td>\n",
              "      <td>6</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>49054.10</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9936</th>\n",
              "      <td>9937</td>\n",
              "      <td>15653037</td>\n",
              "      <td>Parks</td>\n",
              "      <td>609</td>\n",
              "      <td>France</td>\n",
              "      <td>Male</td>\n",
              "      <td>77</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>18708.76</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>133 rows × 14 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-af519247-9565-4bdd-93d9-bead3a0c449e')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-af519247-9565-4bdd-93d9-bead3a0c449e button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-af519247-9565-4bdd-93d9-bead3a0c449e');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#trimming - delete the outlier\n",
        "new_df=df.loc[(df['Age']<upper_limit)&(df['Age']>lower_limit)]\n",
        "print('Before removing outlier:',len(df))\n",
        "print('After removing outlier:',len(new_df))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rav4587VYCRC",
        "outputId": "1593b93a-76d0-48bb-e855-733ba154b83a"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Before removing outlier: 10000\n",
            "After removing outlier: 9867\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.boxplot(new_df['Age'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 351
        },
        "id": "JlUCh3BLZiMK",
        "outputId": "62760ce3-a7e0-4a73-d8c4-80e51b28f113"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f8a97f01790>"
            ]
          },
          "metadata": {},
          "execution_count": 50
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWAAAAEGCAYAAABbzE8LAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAL5UlEQVR4nO3db4xld13H8c+3uzYU0HZL/7jZRRayBlL/UGiDIMRUjEYMYa02GybWEGPCE7NZEo1Rn6nhAU/UZhNNCGqM1dUCNjUNERukRn0A2UIJf9rqiKDdbNlCy6K2Qlp+Prhn2t1td5fZ3rnfmTuvV7KZub97957fb+fMe86cvXOmxhgBYPEu6Z4AwHYlwABNBBigiQADNBFggCY71/Pgq666auzbt2+DpgKwnO67776vjjGuPnt8XQHet29fjh07Nr9ZAWwDVfXl5xt3CgKgiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoIkAAzQRYIAm6/qdcPQ6cuRIVldXF7rN48ePJ0n27Nmz0O2ey/79+3Po0KHuacBcCPAWsrq6mvs/90CefvGVC9vmjidOJUke+Wb/rrLjice6pwBz1f9Zxbo8/eIr8+RrfmZh27vswY8kyUK3eS5rc4Fl4RwwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoIkAAzQRYIAmAgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMECThQT4yJEjOXLkyCI2BcyZz9+Ns3MRG1ldXV3EZoAN4PN34zgFAdBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoIkAAzQRYIAmAgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoMnO7gkAW9NNN930zPv33nvvecfX89jzja+srOTEiRPZu3dvbr/99ot+noMHD+bkyZPZvXt3jh49miQ5cOBATp06lV27duXOO++84DbnwREwsGWcOHEiSfLwww+/oOc5efLkGc+XJKdOnUqSPP744xuyzecjwMC6nX5kefrt5xtfz2PPN76ysnLG+K233npRz3Pw4MEzxldWVnLgwIEzxm6++ebzbnNeFnIK4vjx43nyySdz+PDhRWxuaa2uruaSb43uabS55P++kdXV/7YfLdjq6mouu+yy7mmccbSaXPwR6drR77meN3n2KHhe2zyXCx4BV9W7q+pYVR179NFH57pxgO3sgkfAY4z3J3l/ktx4440Xdfi1Z8+eJMltt912MX+dyeHDh3PfF7/SPY02337R92T/q661Hy2Y7zg2jnPAwJawe/fuM27v3bv3op7nmmuuec7zXn755WeM7dq1a67bPBcBBtbt9Jd0nX77+cbX89jzja+9XGzN2kvC1vs8d9xxxxnjR48ezV133XXG2NrL0M61zXkRYGDLWDsifaFHomtHwacf4a4dBa8d/c57m8/HD2IAF+XsI8zzja/nsecbP/uI9GKf5+yj4CTPOQq+0DbnwREwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoIkAAzQRYIAmAgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJjsXsZH9+/cvYjPABvD5u3EWEuBDhw4tYjPABvD5u3GcggBoIsAATQQYoIkAAzQRYIAmAgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATQQYoIkAAzQRYIAmAgzQRIABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAk53dE2B9djzxWC578CML3N7XkmSh2zyXHU88luTa7mnA3AjwFrJ///6Fb/P48aeSJHv2bIbwXdvybwAbRYC3kEOHDnVPAZgj54ABmggwQBMBBmgiwABNBBigiQADNBFggCYCDNBEgAGaCDBAEwEGaCLAAE0EGKCJAAM0EWCAJgIM0ESAAZoIMEATAQZoIsAATWqM8Z0/uOrRJF/euOmc4aokX13Qtjptl3Um22et22WdyfZZ6wtd5yvGGFefPbiuAC9SVR0bY9zYPY+Ntl3WmWyftW6XdSbbZ60btU6nIACaCDBAk80c4Pd3T2BBtss6k+2z1u2yzmT7rHVD1rlpzwEDLLvNfAQMsNQEGKBJe4Cr6uVV9fGq+kJVfb6qDk/jV1bVPVX1b9PbXd1zfaGq6kVV9cmq+sy01t+exl9ZVZ+oqtWq+uuqurR7rvNQVTuq6tNVdfd0e1nX+aWq+mxV3V9Vx6axZdx/r6iqD1XVg1X1QFW9aUnX+erpY7n25xtV9Z6NWGt7gJM8leRXxxjXJXljkl+pquuS/EaSj40xvj/Jx6bbW903k7x1jPHaJNcn+emqemOS9yX5/THG/iSPJ/nlxjnO0+EkD5x2e1nXmSQ/Psa4/rTXii7j/ntbkr8bY7wmyWsz+9gu3TrHGA9NH8vrk9yQ5Ikkd2Yj1jrG2FR/ktyV5CeTPJRk9zS2O8lD3XOb8zpfnORTSX4ks5+w2TmNvynJR7vnN4f17Z120rcmuTtJLeM6p7V8KclVZ40t1f6b5PIk/5HpP+6XdZ3Ps+6fSvIvG7XWzXAE/Iyq2pfkdUk+keTaMcaJ6a5HklzbNK25mr4tvz/JyST3JPn3JF8fYzw1PeThJHu65jdHf5Dk15N8e7r9siznOpNkJPn7qrqvqt49jS3b/vvKJI8m+dPptNIHquolWb51nu2dSY5O7899rZsmwFX10iQfTvKeMcY3Tr9vzL7kLMXr5cYYT4/ZtzZ7k7whyWuapzR3VfX2JCfHGPd1z2VB3jLGeH2St2V2Cu3HTr9zSfbfnUlen+SPxhivS/K/Oetb8CVZ5zOm/6N4R5IPnn3fvNa6KQJcVd+VWXz/YozxN9PwV6pq93T/7syOGJfGGOPrST6e2bfiV1TVzumuvUmOt01sPt6c5B1V9aUkf5XZaYjbsnzrTJKMMY5Pb09mdq7wDVm+/ffhJA+PMT4x3f5QZkFetnWe7m1JPjXG+Mp0e+5rbQ9wVVWSP07ywBjj906762+TvGt6/12ZnRve0qrq6qq6Ynr/sszOdT+QWYhvmR625dc6xvjNMcbeMca+zL6F+4cxxi9kydaZJFX1kqr67rX3Mztn+Lks2f47xngkyX9V1aunoZ9I8oUs2TrPspJnTz8kG7DW9p+Eq6q3JPmnJJ/Ns+cLfyuz88B3JPm+zC6BeXCM8VjLJOekqn44yZ8l2ZHZF787xhi/U1WvyuxI8cokn05y6xjjm30znZ+quinJr40x3r6M65zWdOd0c2eSvxxjvLeqXpbl23+vT/KBJJcm+WKSX8q0H2eJ1pk888X0P5O8aoxxahqb+8e0PcAA21X7KQiA7UqAAZoIMEATAQZoIsAATQSYLaGqfraqRlUt3U8Osn0JMFvFSpJ/nt7CUhBgNr3pOiFvyezyle+cxi6pqj+crk17T1V9pKpume67oar+cbo4zkfXfnwUNhsBZis4kNl1aP81ydeq6oYkP5dkX5LrkvxiZtfUWLuuyJEkt4wxbkjyJ0ne2zFpuJCdF34ItFvJ7GI+yexHmVcy23c/OMb4dpJHqurj0/2vTvKDSe6ZXWYkO5KcCGxCAsymVlVXZnY1tR+qqpFZUEeevf7Cc/5Kks+PMd60oCnCRXMKgs3uliR/PsZ4xRhj3xjj5Zn9ZobHkvz8dC742iQ3TY9/KMnVVfXMKYmq+oGOicOFCDCb3Uqee7T74STfm9k1ar+Q5PbMfr3TqTHGtzKL9vuq6jNJ7k/yo4ubLnznXA2NLauqXjrG+J/pMoGfTPLm6bq1sCU4B8xWdvd0gftLk/yu+LLVOAIGaOIcMEATAQZoIsAATQQYoIkAAzT5f2g4vQZbmV+TAAAAAElFTkSuQmCC\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#copying-change the outlier value to upper or lower limits values\n",
        "new_df=df.copy()\n",
        "new_df.loc[(new_df['Age']>upper_limit),'Age']=upper_limit\n",
        "new_df.loc[(new_df['Age']<lower_limit),'Age']=lower_limit"
      ],
      "metadata": {
        "id": "LxxvCoJZZzvp"
      },
      "execution_count": 51,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sns.boxplot(new_df['Age'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 351
        },
        "id": "PSqTshzCah0J",
        "outputId": "8df11487-88ee-4161-f41f-047629e22d58"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f8a98031ad0>"
            ]
          },
          "metadata": {},
          "execution_count": 52
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "len(new_df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l1O3cJJBbBBE",
        "outputId": "f7334c81-5125-4b97-ef7c-1163f0d7ac15"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "10000"
            ]
          },
          "metadata": {},
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#IQR method\n",
        "q1=df['Age'].quantile(0.25)\n",
        "q3=df['Age'].quantile(0.75)\n",
        "iqr=q3-q1"
      ],
      "metadata": {
        "id": "-Cnwr1pobNFY"
      },
      "execution_count": 54,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "q1,q3,iqr"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GOjnK-qZbsEB",
        "outputId": "dff3a728-8330-4aa9-d3a0-b0632ab8661b"
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(32.0, 44.0, 12.0)"
            ]
          },
          "metadata": {},
          "execution_count": 55
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "upper_limit=q3+(1.5*iqr)\n",
        "lower_limit=q3-(1.5*iqr)\n",
        "lower_limit,upper_limit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ET0MDyJ4cLDu",
        "outputId": "9f3c82ea-d89b-4a3f-b24a-4bd7216f5eae"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(26.0, 62.0)"
            ]
          },
          "metadata": {},
          "execution_count": 56
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.boxplot(df['Age'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 351
        },
        "id": "_pcISTQschZs",
        "outputId": "49f7a5b1-b20b-4da8-8999-e2fdc65e2a5f"
      },
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f8a98077ed0>"
            ]
          },
          "metadata": {},
          "execution_count": 57
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWAAAAEGCAYAAABbzE8LAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAPyUlEQVR4nO3da4xc9XmA8ee1t8HGTrnYQF2bdhNtAVEgBKMUCEUDMcXcQikGYXExEoIvlW2gqGrBNZgCEhK4IEupZEoLpG1SIGkpyJjYAUpbJKJdwv2STBs3scUthpCaW2r498M5s9lZNnjXHvadxc9PsuwzZ87M65njx2ePZ4+jlIIkafxNyh5AknZWBliSkhhgSUpigCUpiQGWpCQ9Y7nzzJkzS29v7yc0iiR9+sycOZMHH3zwwVLK/OHrxhTg3t5e+vv7OzeZJO0EImLmSLd7CkKSkhhgSUpigCUpiQGWpCQGWJKSGGBJSmKAJSmJAZakJAZYkpIYYElKYoAlKYkBlqQkBliSkhhgSUpigCUpiQGWpCQGWJKSGGBJSmKAJSnJmP5POH28VatW0Ww2O/Z4mzZtAmD27Nkde8zR6OvrY/HixeP6nNLOyAB3ULPZ5MlnX+CDXffsyONNfuctAF55f/zepsnvvDFuzyXt7Axwh32w6568e8BJHXmsqS+uAejY443lOSV98jwHLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUnGJcCrVq1i1apV4/FU0rhwn1Yn9IzHkzSbzfF4GmncuE+rEzwFIUlJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAUgc0Go3BHyMtL1y4kEajwbnnnjuq+wOcddZZNBoNFi5cCMBpp51Go9Hg9NNPH/ExTzjhBBqNBvPnzwfg9NNPp9FocMYZZwCwZMkSGo0Gl1122Yjb33DDDTQaDW666SYArrjiChqNBsuXLx+cacWKFTQaDa677joA7r33XhqNBvfddx8ADz30EI1Gg4cffhiA/v5+jjvuOAYGBkZcv3nzZpYsWcLmzZtHXG42m5x88sk0m80R14/G9mwz1PAZOskAS+Pg5ZdfBmDjxo2j3ua1115r2/att94C4M033xzxMd9//30A3nvvvbb7tcLz9NNPA/DEE0+MuP0DDzwAMBjTxx57DIBHH310cKZWONetWwfAzTffDMDKlSsBuP766wEGA3311Vfz4YcfctVVV424/o477uCZZ57hzjvvHHH52muv5e233+baa68dcf1obM82Qw2foZMMsLSDhh61dmr5rLPO6uhjHnvssW3L8+bNa1tuHTW3nHnmmW3Ly5cvZ8WKFW23XXzxxZRSACilcOONN7J161YAtm7dym233caWLVsA2LJlC7feemvb+vvuu4+1a9dSSmHt2rU0m8225YGBATZs2ADAhg0bGBgYaFs/miPazZs3j3mboZrNZtsMnT4KjtYLOBqHH3546e/vH/OTLFiwgHfffZe+vr4xbzuRNJtN/vcXhbcPPbsjjzf1xTUAvHvASR15vNGY9uQ3+exn4lP/Xu2oZrPJ1KlTueeeez4SO41ORDB58mS2bt1KT08Pc+bMYePGjYPLU6ZMGQw4wPTp03nvvfcG15988slceumlH/scK1euZM2aNWPaZqgLLrhgMMAAvb293H777WP9rRIRA6WUw4ffvs0j4Ii4OCL6I6L/9ddfH/MTS9JISiltR8QbNmxoWx4aX6iOooeub50G+Tjr168f8zZDDY3vSMs7qmdbdyilrAZWQ3UEvD1PMnv2bABuueWW7dl8wli6dCkD//1q9hg75MMpv07f5/f51L9XO2rp0qXZI0x4O3oEfPzxx2/zOebNm9d2BDyabYbq7e39yBFwJ3kOWOpCe++9d0cfLyLalnt62o+9pkyZ0ra81157tS0fc8wxHzmPvN9++7Utn3LKKW3L5513XtvyOeec07Z82WWXMWlSlaDJkyezbNmytuXh55xXrFjRtv78889nWxYtWjTm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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#copying-change the outlier value to upper or lower limits values\n",
        "new_df=df.copy()\n",
        "new_df.loc[(new_df['Age']>upper_limit),'Age']=upper_limit\n",
        "new_df.loc[(new_df['Age']<lower_limit),'Age']=lower_limit"
      ],
      "metadata": {
        "id": "opzf9Xnncrfv"
      },
      "execution_count": 58,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sns.boxplot(new_df['Age'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 351
        },
        "id": "zM6WOKmGc8Fp",
        "outputId": "f43084c2-ca55-40be-a046-e866999a14a6"
      },
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f8a97e1a690>"
            ]
          },
          "metadata": {},
          "execution_count": 59
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}