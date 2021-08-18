import PyPDF2
from gtts import gTTS

livro = "LB02"
language = "pt"

with open(f'{livro}.pdf', 'rb') as book:
    full_text = ""

    reader = PyPDF2.PdfFileReader(book)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_text += content

    audio_reader = gTTS(text=full_text, lang=language,tld='com.br', slow=False)
    audio_reader.save(f"{livro}.mp3")
