import pytesseract
from PIL import Image
from pdf2image import convert_from_path

images = convert_from_path("./管理規約集.pdf")
# Tesseractの実行ファイルへのパスを設定（Windowsの場合）
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

# 画像を読み込み
# image = Image.open("./ローレル.pdf")

# 画像からテキストを抽出（言語を指定）
# text = pytesseract.image_to_string(image, lang="jpn")
# print(text)

# 抽出したテキストを保存するファイル
output_text_file = "./output_text_file.txt"
with open(output_text_file, "w") as f:
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, lang="jpn")  # 日本語のテキストを抽出
        f.write(f"Page {i+1}:\n{text}\n\n")
