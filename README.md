# Challenge Martinez Escoda
## *Giuliano Crenna*

Resolución del challenge brindado por la firma Martinez Escoda 
---

El script genera $n$ scripts que le ingrese el usuario, y el mismo genera los precios futuros y las cantidades en base al TNA (que se utiliza para crear el drift) y un factor de volatibilidad. Los cálculos se hacen mediante el uso de generacion de numeros aleatorios uniformes y gaussianos.

Pasos de instalación de dependencias en linux.
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

Pasos de instalación de dependencias en windows.
```bash
python -m venv .venv
source .venv\script\activate
pip install -r requirements.txt
```

Pasos para correr
```
python main.py
```
