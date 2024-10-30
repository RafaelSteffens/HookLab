import json

def extrair_campos_do_json(arquivo_json):
    with open(arquivo_json, 'r', encoding='utf-8') as file:

        produtos = json.load(file)

   
        for chave, produto in produtos.items():
            if chave.startswith("Product:"):
                product_name = produto.get('productName')
                link = produto.get('link')
               
                selling_price = None

            
                price_key = f"${chave}.priceRange.sellingPrice"

                
                if price_key in produtos:
                    selling_price_info = produtos[price_key]
                    selling_price = selling_price_info.get('highPrice')  


                item_key = f"{chave}.items({{\"filter\":\"ALL\"}}).0"
                if item_key in produtos:
                    item_info = produtos[item_key]
                    image_ids = item_info.get('images', [])


                    image_urls = []
                    for image in image_ids:
                        image_id = image.get('id')
                        if image_id and image_id in produtos:
                            image_url = produtos[image_id].get('imageUrl')
                            if image_url:
                                image_urls.append(image_url)


                if product_name:
                    print(f'Titulo: {product_name},\nPreço: {selling_price}, \nLink: {link}, \nImagens: {", ".join(image_urls)}')
                    print('=============================================================================================')

arquivoJson = str(input("Coloque o arquivo na raiz desse projeto e digite o nome do Arquivo: "))

extrair_campos_do_json(arquivoJson)
