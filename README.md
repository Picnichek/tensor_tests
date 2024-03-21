# tests

## В данном репозитории реализованы 3 сценария тестирования
### Для локального запуска должен быть скачан и прописан в "path" "web-driver chrome"

**клонируем репозиторий и переходим в него**

```bash
git clone https://github.com/Picnichek/tensor_tests.git
cd tensor_tests
```

**Создаем виртуальное окружение и устанавливаем зависимости**
для windows

```bash

py -3.9 -m venv venv

source venv/Scripts/activate 

pip install -r requirements.txt
```

для linux

```bash

python3 -m venv venv

source source venv/bin/activate

pip install -r requirements.txt
```

**Запускаем тесты**

```bash

pytest tests/
```


