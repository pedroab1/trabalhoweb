import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT

BASE_URL = "https://www.rioclaro.sp.gov.br/"

def gerar_pdf(nome_arquivo, titulo_doc, noticias):
    doc = SimpleDocTemplate(
        nome_arquivo,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )
 
    styles = getSampleStyleSheet()
 
    estilo_titulo = ParagraphStyle(
        "Titulo",
        parent=styles["Title"],
        fontSize=18,
        spaceAfter=16,
    )
    estilo_noticia = ParagraphStyle(
        "Noticia",
        parent=styles["Normal"],
        fontSize=12,
        leading=16,
        spaceAfter=8,
        alignment=TA_LEFT,
    )
    estilo_link = ParagraphStyle(
        "Link",
        parent=estilo_noticia,
        textColor="#1a56db",
        fontSize=10,
    )
 
    story = []
    story.append(Paragraph(titulo_doc, estilo_titulo))
    story.append(Spacer(1, 12))
 
    if not noticias:
        story.append(Paragraph("Nenhuma informação pôde ser extraída no momento.", estilo_noticia))
    else:
        for noticia in noticias:
            titulo_texto = f"<b>{noticia['titulo']}</b>"
            link_texto = f"Acesse: {noticia['link']}"
            
            story.append(Paragraph(titulo_texto, estilo_noticia))
            story.append(Paragraph(link_texto, estilo_link))
            story.append(Spacer(1, 14))
 
    doc.build(story)
    print(f"\n[+] PDF gerado com sucesso: {nome_arquivo}")

def buscar_informacoes_cidadao():
    print(f"\nAcessando portal do cidadão: {BASE_URL}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        resposta = requests.get(BASE_URL, headers=headers)
        resposta.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página. Detalhes: {e}")
        return

    soup = BeautifulSoup(resposta.text, "html.parser")
    noticias = []
    
    tags_busca = soup.find_all(['h2', 'h3'])

    for tag in tags_busca:
        link_tag = tag.find('a')
        if link_tag and link_tag.get('href'):
            titulo = link_tag.get_text(strip=True)
            link = link_tag.get('href')
            
            if titulo and len(titulo) > 10:
                if link.startswith('/'):
                    link = BASE_URL.rstrip('/') + link
                
                noticias.append({"titulo": titulo, "link": link})

    noticias_unicas = []
    titulos_vistos = set()
    for n in noticias:
        if n['titulo'] not in titulos_vistos:
            titulos_vistos.add(n['titulo'])
            noticias_unicas.append(n)

    print(f"Foram encontrados {len(noticias_unicas)} avisos/notícias em destaque.\n")
    
    for n in noticias_unicas[:5]:
        print(f"- {n['titulo']}")
    
    if len(noticias_unicas) > 5:
        print("... (veja o PDF para a lista completa).")

    nome_pdf = "Boletim_Rio_Claro.pdf"
    titulo_pdf = "Resumo de Destaques - Prefeitura de Rio Claro"
    gerar_pdf(nome_pdf, titulo_pdf, noticias_unicas)

if __name__ == "__main__":
    buscar_informacoes_cidadao()