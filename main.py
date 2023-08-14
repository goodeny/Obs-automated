import requests
from bs4 import BeautifulSoup
import time

#goodeny s2 s2

class Software:
    def __init__(self):
        #variavel que armazena as noticias
        self.news = []
    
    #função que pega as noticias da globo obs: para outros sites adicionar uma nova função
    def get_news_globo(self):
        url = "https://g1.globo.com/"
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            eventos = soup.find_all(class_="bastian-feed-item")
            
            textos = []
            
            for evento in eventos:
                titulo_element = evento.find("a", class_="feed-post-link")
                if titulo_element:
                    texto = titulo_element.get_text().strip()
                    textos.append(texto)
            
            return textos
        else:
            return f"not found: {response.status_code}"

    #Adiciona as noticias na lista <self.news>
    def add_to_list(self):
        for i in self.get_news_globo():
            self.news.append(f" [Globo]: {i}\n ")

    #Adiciona a noticia em um text que é usado no OBS(GDI+)
    def add_text(self, n):
        with open("data.txt", "w", encoding="utf-8") as data:
            data.write(self.news[n])
        data.close()

    #Atualiza as noticias a cada x segundos
    def update_text(self, x):
        c = 0
        while True:
            if c == len(self.news):
                c = 0
            else:
                self.add_text(c)
                time.sleep(x)
                c += 1

if __name__ == "__main__":
    s = Software()
    s.add_to_list()
    s.update_text(15)
