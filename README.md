# Metodologias de la programación

### ***Alumno: Julio César Maldonado Acuña***

#### ***Este es un repositorio para la materia de metodologías de la programación***

<!-- LOGO -->
<p align="center">
  <!-- Cambia la URL del logo por la de tu imagen (por ejemplo, un logo del carrito) -->
  <img src="https://via.placeholder.com/140x140.png?text=Carrito" alt="Carrito Logo" width="140">
</p>

<h1 align="center">Carrito ESP32 + L298N 🚗</h1>

<p align="center">
  Control de motores DC con ESP32, driver L298N y comunicación Bluetooth desde el celular.
</p>

<p align="center">
  <b>MicroPython · PWM · Motores DC · Bluetooth UART</b>
</p>

---

## 🧾 Descripción general

Este proyecto implementa un **carrito controlado por ESP32**, usando un módulo **L298N** para manejar dos motores DC:

- Un motor de **tracción** (avanza / retrocede).
- Un motor de **dirección** (gira las llantas).

El ESP32 se comunica con el celular a través de **Bluetooth (UART BLE)** y recibe comandos como:

- `F` → Forward (avanzar)  
- `B` → Backward (retroceder)  
- `L` / `R` → Giro a la izquierda / derecha  
- `S` → Stop (detener)

La lógica de control está escrita en **MicroPython**, utilizando **PWM** para regular la velocidad de los motores.

---

## 🧩 Características principales

- ✅ Control remoto desde app BLE (UART).
- ✅ ESP32 como “cerebro” del carrito.
- ✅ Driver **L298N** para dos motores DC.
- ✅ Control de velocidad por **PWM**.
- ✅ Fuente independiente para motores y ESP32, con **tierra común (GND compartida)**.
- ✅ Estructura de código organizada con clases (`Motor`, `BLEUART`, etc.).

---

## 📦 Hardware utilizado

- **ESP32** (placa con soporte para MicroPython y Bluetooth).
- **Módulo L298N** (driver puente H doble).
- **2 motores DC**:
  - Motor de tracción (8 V, 1.6 A aprox.).
  - Motor de dirección (para girar las llantas).
- **Baterías para motores**:
  - 6 × pilas **AA NiMH** en serie (≈ 7.2–8 V)  
    o pack equivalente con suficiente corriente.
- **Cableado jumper macho–macho / macho–hembra**.
- **Laptop / PC** para alimentar el ESP32 por USB y cargar el código.
- Protoboard (opcional) para organizar conexiones.

---

## ⚙️ Arquitectura del sistema

```text
       +-------------------+
       |      Celular      |
       |   App BLE UART    |
       +---------+---------+
                 |
           Bluetooth (UART)
                 |
        +--------v--------+
        |      ESP32      |
        |  MicroPython    |
        +---+--------+----+
            |        |
      PWM / GPIO   PWM / GPIO
      Tracción      Dirección
            |        |
    +-------v--------v------+
    |        L298N          |
    |  Puente H doble       |
    +---+-------------+-----+
        |             |
    Motor Tracción  Motor Dirección
        |             |
     Ruedas        Mecanismo
     traseras       de giro

      Batería Motores (6xAA NiMH)
              |
             +12V / Vmot + GND
              |
             L298N
