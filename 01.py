import wx


class BMIFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(BMIFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)

        # Nome do Paciente
        self.nome_label = wx.StaticText(panel, label="Nome do Paciente:", pos=(10, 10))
        self.nome_text = wx.TextCtrl(panel, pos=(150, 10), size=(300, -1))

        # Endereço Completo
        self.endereco_label = wx.StaticText(panel, label="Endereço Completo:", pos=(10, 40))
        self.endereco_text = wx.TextCtrl(panel, pos=(150, 40), size=(300, -1))

        # Altura (cm)
        self.altura_label = wx.StaticText(panel, label="Altura (cm):", pos=(10, 70))
        self.altura_text = wx.TextCtrl(panel, pos=(150, 70), size=(300, -1))

        # Peso (Kg)
        self.peso_label = wx.StaticText(panel, label="Peso (Kg):", pos=(10, 100))
        self.peso_text = wx.TextCtrl(panel, pos=(150, 100), size=(300, -1))

        # Resultado
        self.resultado_label = wx.StaticText(panel, label="Resultado:", pos=(10, 130))
        self.resultado_text = wx.TextCtrl(panel, pos=(150, 130), size=(300, 100),
                                          style=wx.TE_MULTILINE | wx.TE_READONLY)

        # Botões
        self.calcular_button = wx.Button(panel, label="Calcular", pos=(10, 240))
        self.reiniciar_button = wx.Button(panel, label="Reiniciar", pos=(110, 240))
        self.sair_button = wx.Button(panel, label="Sair", pos=(210, 240))

        # Bind dos botões
        self.calcular_button.Bind(wx.EVT_BUTTON, self.calcular_bmi)
        self.reiniciar_button.Bind(wx.EVT_BUTTON, self.reiniciar)
        self.sair_button.Bind(wx.EVT_BUTTON, self.sair)

        self.SetSize((480, 320))
        self.SetTitle('Calculadora de IMC')

    def calcular_bmi(self, event):
        try:
            peso = float(self.peso_text.GetValue())
            altura = float(self.altura_text.GetValue()) / 100  # Convertendo altura para metros
            imc = peso / (altura ** 2)
            if imc < 18.5:
                categoria = "Abaixo do peso"
            elif 18.5 <= imc < 24.9:
                categoria = "Peso normal"
            elif 25 <= imc < 29.9:
                categoria = "Sobrepeso"
            else:
                categoria = "Obesidade"

            resultado = (f"Nome: {self.nome_text.GetValue()}\n"
                         f"Endereço: {self.endereco_text.GetValue()}\n"
                         f"IMC: {imc:.2f}\n"
                         f"Categoria: {categoria}")

            self.resultado_text.SetValue(resultado)
        except ValueError:
            wx.MessageBox("Por favor, insira valores válidos para peso e altura.", "Erro", wx.OK | wx.ICON_ERROR)

    def reiniciar(self, event):
        self.nome_text.SetValue("")
        self.endereco_text.SetValue("")
        self.altura_text.SetValue("")
        self.peso_text.SetValue("")
        self.resultado_text.SetValue("")

    def sair(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App(False)
    frame = BMIFrame(None)
    frame.Show()
    app.MainLoop()
