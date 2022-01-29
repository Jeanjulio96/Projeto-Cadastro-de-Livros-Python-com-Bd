from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

numeroid = 0

conexao = mysql.connector.connect(
                host = 'localhost',
                user ='root',
                passwd='',
                database='cadastrodelivros'
)
cursor = conexao.cursor()

def pdf():
    cursor = conexao.cursor()
    sql = "SELECT * FROM livros"
    cursor.execute(sql)
    listalivros = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastrodelivros.pdf")
    pdf.setFont("Times-Bold", 14)
    pdf.drawString(200,800, "Livros Cadastrados:")
    pdf.setFont("Times-Bold", 9)

    pdf.drawString(10, 750, "ID")
    pdf.drawString(30, 750, "NOME DO LIVRO")
    pdf.drawString(170, 750, "TIPO")
    pdf.drawString(210, 750, "AUTOR")
    pdf.drawString(281, 750, "EDITORA")
    pdf.drawString(338, 750, "GÊNERO")
    pdf.drawString(392, 750, "ISBN")
    pdf.drawString(465, 750, "IDIOMA")
    pdf.drawString(520, 750, "ANO")
    pdf.drawString(555, 750, "PREÇO")

    for i in range(0, len(listalivros)):
        y = y + 20
        pdf.drawString(10, 750 - y,str(listalivros[i][0]))
        pdf.drawString(30, 750 - y, str(listalivros[i][1]))
        pdf.drawString(170, 750- y, str(listalivros[i][2]))
        pdf.drawString(210, 750 - y, str(listalivros[i][3]))
        pdf.drawString(281, 750 - y, str(listalivros[i][4]))
        pdf.drawString(338, 750 - y, str(listalivros[i][5]))
        pdf.drawString(392, 750 - y, str(listalivros[i][6]))
        pdf.drawString(465, 750 - y, str(listalivros[i][7]))
        pdf.drawString(520, 750 - y, str(listalivros[i][8]))
        pdf.drawString(555, 750 - y, str(listalivros[i][9]))

    pdf.save()
    print("SEU PDF FOI CRIADO!")


def editarDados():
    global numeroid

    salvarItemLinha = listaLivros.tableWidget.currentRow()
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM livros")
    dadoslidos = cursor.fetchall()
    valorid = dadoslidos[salvarItemLinha][0]
    cursor.execute("SELECT * FROM livros WHERE id=" + str(valorid))
    livrosEditar = cursor.fetchall()
    telaEditar.show()

    telaEditar.lineEdit.setText(str(livrosEditar[0][0]))
    telaEditar.lineEdit_2.setText(str(livrosEditar[0][1]))
    telaEditar.lineEdit_3.setText(str(livrosEditar[0][2]))
    telaEditar.lineEdit_4.setText(str(livrosEditar[0][3]))
    telaEditar.lineEdit_5.setText(str(livrosEditar[0][4]))
    telaEditar.lineEdit_6.setText(str(livrosEditar[0][5]))
    telaEditar.lineEdit_7.setText(str(livrosEditar[0][6]))
    telaEditar.lineEdit_8.setText(str(livrosEditar[0][7]))
    telaEditar.lineEdit_9.setText(str(livrosEditar[0][8]))
    telaEditar.lineEdit_10.setText(str(livrosEditar[0][9]))
    numeroid = valorid

def salvarDados():
    global numeroid

    NomeDoLivro = telaEditar.lineEdit_2.text()
    Tipo = telaEditar.lineEdit_3.text()
    Autor = telaEditar.lineEdit_4.text()
    Editora = telaEditar.lineEdit_5.text()
    Gênero = telaEditar.lineEdit_6.text()
    ISBN = telaEditar.lineEdit_7.text()
    Idioma = telaEditar.lineEdit_8.text()
    Ano = telaEditar.lineEdit_9.text()
    Preço = telaEditar.lineEdit_10.text()

    cursor = conexao.cursor()
    cursor.execute("UPDATE livros SET NomeDoLivro = '{}', Tipo = '{}', Autor = '{}', Editora ='{}',Gênero = '{}',ISBN = '{}',Idioma = '{}',Ano = '{}',Preço = '{}' WHERE id = {}".format(NomeDoLivro,Tipo,Autor,Editora,Gênero,ISBN,Idioma,Ano,Preço,numeroid))
    conexao.commit()
    telaEditar.close()
    listaLivros.close()
    listaLivros.show()
    catalogo()

def excluirDados():
    excluirlinha = listaLivros.tableWidget.currentRow()
    listaLivros.tableWidget.removeRow(excluirlinha)

    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM livros")
    dadoslidos = cursor.fetchall()
    valorid = dadoslidos[excluirlinha][0]
    cursor.execute("DELETE FROM livros WHERE id="+ str(valorid))
    cursor.execute('commit')
    conexao.close()

def sistema():
    nomedolivro = cadastro.lineEdit.text()
    autor = cadastro.lineEdit_2.text()
    editora = cadastro.lineEdit_3.text()
    genero = cadastro.lineEdit_4.text()
    isbn = cadastro.lineEdit_5.text()
    idioma = cadastro.lineEdit_6.text()
    ano = cadastro.lineEdit_7.text()
    id = cadastro.lineEdit_8.text()
    preco = cadastro.lineEdit_9.text()

    tipo = ""
    if cadastro.radioButton.isChecked():
        tipo = "Físico"
    if cadastro.radioButton_2.isChecked():
        tipo = "Digital"

        print("Nome do Livro:", nomedolivro)
        print("Autor:", autor)
        print("Editora:", editora)
        print("Gênero:", genero)
        print("ISBN:", isbn)
        print("Idioma:", idioma)
        print("Ano:", ano)
        print("ID:", id)
        print("Preço:", preco)


    sql = 'INSERT INTO livros (ID,NomeDoLivro,Tipo,Autor,Editora,Gênero,ISBN,Idioma,Ano,Preço) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    dados = (str(id), str(nomedolivro), str(tipo), str(autor),str(editora),str(genero),str(isbn),str(idioma),str(ano),str(preco))
    cursor.execute(sql, dados)
    conexao.commit()

    cadastro.lineEdit.setText("")
    cadastro.lineEdit_2.setText("")
    cadastro.lineEdit_3.setText("")
    cadastro.lineEdit_4.setText("")
    cadastro.lineEdit_5.setText("")
    cadastro.lineEdit_6.setText("")
    cadastro.lineEdit_7.setText("")
    cadastro.lineEdit_8.setText("")
    cadastro.lineEdit_9.setText("")

def catalogo():
    listaLivros.show()
    cursor = conexao.cursor()
    sql = "SELECT * FROM livros"
    cursor.execute(sql)
    dadoslidos = cursor.fetchall()
    print(dadoslidos)

    listaLivros.tableWidget.setRowCount(len(dadoslidos))
    listaLivros.tableWidget.setColumnCount(10)

    for i in range (0, len(dadoslidos)):
        for j in range (0,10):
            listaLivros.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dadoslidos[i][j])))



app=QtWidgets.QApplication([])
cadastro=uic.loadUi("CadastroDeLivros.ui")
listaLivros=uic.loadUi("LivrosCatalogados.ui")
telaEditar=uic.loadUi("TelaEditar.ui")
cadastro.pushButton.clicked.connect(sistema)
cadastro.pushButton_2.clicked.connect(catalogo)
listaLivros.pushButton.clicked.connect(pdf)
listaLivros.pushButton_2.clicked.connect(excluirDados)
listaLivros.pushButton_3.clicked.connect(editarDados)
telaEditar.pushButton.clicked.connect(salvarDados)
cadastro.show()
app.exec()