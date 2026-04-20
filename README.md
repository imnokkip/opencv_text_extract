# Text extractor

**Извлечение текста с изображений и сохранение на чёрный фон**

---

## 📌 О проекте

`Text extractor` — это простое приложение для распознавания текста с изображений с использованием Tesseract OCR. Программа обрабатывает изображение, извлекает текст (поддержка русского и английского языков) и сохраняет его на черном фоне с автоматическим подбором размера изображения под длину текста.

Проект написан на **Python** с использованием **OpenCV** для предобработки изображения и **PIL (Pillow)** для создания итогового изображения с текстом.

---

## 🚀 Возможности

- **Распознавание текста** на русском и английском языках.
- **Автоматическая предобработка** изображения (увеличение, бинаризация).
- **Автоматический подбор размера** выходного изображения под длину текста.
- **Сохранение результата** в виде изображения с белым текстом на черном фоне.
- **Поддержка командной строки** — простой запуск с аргументами.
- **Аннотации типов** для удобства разработки и поддержки кода.

---

## 🛠️ Технологии

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![Tesseract](https://img.shields.io/badge/Tesseract-3A75C4?style=for-the-badge&logo=tesseract&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-2496ED?style=for-the-badge&logo=python&logoColor=white)

---

## 📦 Установка и запуск

### Требования

- Python 3.9 — 3.12
- Tesseract OCR установлен на системе

### 1. Установка Tesseract OCR

**Windows:**
- Скачайте установщик с [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- Установите, запомнив путь (обычно `C:\Program Files\Tesseract-OCR\tesseract.exe`)

### 2. Установка зависимостей
bash
```
pip install opencv-python pytesseract pillow numpy
```

### 2. Запуск
bash
```
python main.py {путь к изображению} {как сохранить изображение}
```

###📑 Планы по доработке

[] - Создать GUI интерфейс для удобного выбора файлов.
[] - Улучшить распознование.
[] - Улучшить обработку для изображений с плохим качеством.