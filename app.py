from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    perfil = {
        "nome": "Conceição Queiroz",
        "corretora": "RE/MAX DREAMS",
        "subtitulo": "Conduzo decisões imobiliárias com clareza, segurança e confiança.",
        "foto": "corretora.png"  # Certifique-se de que a foto está na pasta /static
    }

    imoveis = [
        {
            "id": 1,
            "titulo": "Apartamento no Renascença",
            "preco": "R$ 1.750.000",
            "localizacao": "São Luís, MA",
            "imagem": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=800&auto=format&fit=crop",
            "link": "#"
        },
        {
            "id": 2,
            "titulo": "Casa no Araçagy",
            "preco": "R$ 1.850.000",
            "localizacao": "São Luís, MA",
            "imagem": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=800&auto=format&fit=crop",
            "link": "#"
        },
        {
            "id": 3,
            "titulo": "Cobertura na Península",
            "preco": "R$ 3.200.000",
            "localizacao": "São Luís, MA",
            "imagem": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=800&auto=format&fit=crop",
            "link": "#"
        },
        {
            "id": 4,
            "titulo": "Mansão no Calhau",
            "preco": "R$ 4.500.000",
            "localizacao": "São Luís, MA",
            "imagem": "https://images.unsplash.com/photo-1613977257363-707ba9348227?q=80&w=800&auto=format&fit=crop",
            "link": "#"
        }
    ]

    return render_template("index.html", perfil=perfil, imoveis=imoveis)

if __name__ == '__main__':
    # O host='0.0.0.0' diz ao Python para liberar o acesso na rede Wi-Fi
    app.run(host='0.0.0.0', port=5000, debug=True)