# Hand Tracking Control

**Отслеживание рук и пальцев через веб-камеру в реальном времени**

---

## 📌 О проекте

`Hand Tracking Control` — это приложение для компьютерного зрения, которое в реальном времени отслеживает руки и пальцы пользователя через веб-камеру. Проект использует современный API MediaPipe (версия >=0.10.31) для детекции 21 ключевой точки на каждой руке и отображает их на экране.

---

## 🚀 Возможности

- **Детекция 21 ключевой точки** на каждой руке.
- **Визуализация скелета руки** (соединения между точками).
- **Работа в реальном времени** с веб-камеры (30+ FPS).
- **Автоматическая загрузка модели** при первом запуске.

---

## 🛠️ Технологии

![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-009688?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 📦 Установка и запуск

### Требования

- Python 3.9 — 3.12 (MediaPipe не поддерживает 3.13+)
- Веб-камера

### 1. Клонируй репозиторий

```bash
git clone https://github.com/yourusername/hand-tracking-control
cd hand-tracking-control
