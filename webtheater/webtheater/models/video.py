class Video:

    def __init__(self, id, url_video, url_img, titulo, descricao, qtd_visualizacao, qtd_curtida, data_publi)-> None:
        self.id = id
        self.url_video = url_video
        self.url_img = url_img
        self.titulo = titulo
        self.descricao = descricao
        self.qtd_visualizacao = qtd_visualizacao
        self.qtd_curtida = qtd_curtida
        self.data_publi = data_publi

    def get_id(self):
        return self.id

    def get_url_video(self):
        return self.url_video

    def get_url_img(self):
        return self.url_img

    def get_titulo(self):
        return self.titulo

    def get_descricao(self):
        return self.descricao

    def get_qtd_visualizacao(self):
        return self.qtd_visualizacao

    def get_qtd_curtida(self):
        return self.qtd_curtida

    def get_data_publi(self):
        return self.data_publi