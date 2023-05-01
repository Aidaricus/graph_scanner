# graph_scanner
## Мотивация
Написать аналог photomath сканирующий обычные **неориентированные графы** и познакомиться с базовыми понятиями Computer Vision. 


## Как начать работать?
Все необходимые библиотеки лежат в файле requirements. Необходимо нарисовать на чистой белой бумаге неориентированный граф красной ручкой. В качестве вершин нарисуйте окружности не больших размеров.
Ребрами графа должны быть **прямые** отрезки, соединяющие вершины. Или использовать готовое изображение нарисованное мной (img.png) 


<img src = "https://user-images.githubusercontent.com/108796735/235455722-b5a5a36b-ee7d-42dd-a814-3ac6b29a62bf.png" width = "50%"  height = "50%"  title = "Example">

Клонируем репозиторий и запускаем файл main.py. Приложение запустится, в главном окне, нажатием кнопки "Image", выберите изображение которое вы нарисовали. Справа должно появится отсканированное изображение.
Нажимаем кнопку "Scan". Получаем отсканированное изображение вашего графа в отдельном окне. Выбираем функцию нарисуй граф: matplotlib нарисует граф который вы нарисовали.


## Тестирование
В папке tests есть два файла с тестами. Один тест проверяет работу модели окружности и отрезка. Другой проверяет сам сканнер. Для тестирования сканнера, в папке test_images есть несколько изображений графов. Тесты проверяют правльное ли количество распознанных вершин получает сканнер.


### Библиотеки
OpenCV, Matplotlib, NumPy, NetworkX
