import sys
import os

import numpy as np
import streamlit as st

from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.data.load_data import load_database_info

DATABASE_INFO_CSV = 'database/database_info.csv'
database_info = load_database_info(DATABASE_INFO_CSV)

def find_image_in_database(uploaded_image, database_info):
    """
    Verifica se uma imagem está no banco de dados.

    Args:
        uploaded_image (Image): Imagem carregada pelo usuário.
        database_info (pd.DataFrame): DataFrame com as informações do banco de dados.

    Returns:
        str: ID da imagem se encontrada, caso contrário 'Não encontrada'.
    """
    uploaded_image_array = np.array(uploaded_image)
    for idx, row in database_info.iterrows():
        database_image = Image.open(row['image_path'])
        database_image_array = np.array(database_image)
        if np.array_equal(uploaded_image_array, database_image_array):
            return row['image_id']
    return 'Não encontrada'

st.title("Verificação de Imagem")
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    uploaded_image = Image.open(uploaded_file)
    image_id = find_image_in_database(uploaded_image, database_info)
    st.image(uploaded_image, caption=f"ID da imagem: {image_id}", use_column_width=True)
