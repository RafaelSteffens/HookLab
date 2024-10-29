import json

# Função para ler o arquivo JSON e extrair os campos desejados
def extrair_campos_do_json(arquivo_json):
    with open(arquivo_json, 'r', encoding='utf-8') as file:
        # Carrega o conteúdo do arquivo JSON
        produtos = json.load(file)

        # Itera sobre cada chave que começa com "Product:"
        for chave, produto in produtos.items():
            if chave.startswith("Product:"):
                product_name = produto.get('productName')
                link = produto.get('link')
                # Inicializa a variável para o preço
                selling_price = None

                # Monta a chave para acessar o preço
                price_key = f"${chave}.priceRange.sellingPrice"

                # Verifica se a chave do preço existe no dicionário
                if price_key in produtos:
                    # Acessa o preço do produto
                    selling_price_info = produtos[price_key]
                    selling_price = selling_price_info.get('highPrice')  # ou 'lowPrice', dependendo da sua necessidade

                # Extrai os IDs das imagens do produto
                item_key = f"{chave}.items({{\"filter\":\"ALL\"}}).0"
                if item_key in produtos:
                    item_info = produtos[item_key]
                    image_ids = item_info.get('images', [])

                    # Para cada ID de imagem, obtém o URL correspondente
                    image_urls = []
                    for image in image_ids:
                        image_id = image.get('id')
                        if image_id and image_id in produtos:
                            image_url = produtos[image_id].get('imageUrl')
                            if image_url:
                                image_urls.append(image_url)

                # Imprime os resultados
                if product_name:
                    print(f'Titulo: {product_name},\nPreço: {selling_price}, \nLink: {link}, \nImagens: {", ".join(image_urls)}')
                    print('=============================================================================================')

arquivoJson = str(input("Coloque o arquivo na raiz desse projeto e digite o nome do Arquivo: "))
# Chama a função passando o caminho do arquivo JSON
extrair_campos_do_json(arquivoJson)
