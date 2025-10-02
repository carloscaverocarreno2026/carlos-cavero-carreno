import streamlit as st
import time

st.set_page_config(page_title="Juego de Preguntas - Tensiones Eléctricas Perú", page_icon="⚡")

st.title("⚡ Juego de Preguntas: Niveles de Tensión Eléctrica en Perú ⚡")
st.write("Responde las siguientes preguntas sobre los niveles de tensión eléctrica en el Perú. ¡Pon a prueba tus conocimientos!")

# Preguntas y respuestas
preguntas = {
    "1. ¿Cuál es el nivel de tensión típico de distribución primaria en Perú?": {
        "opciones": ["10 kV", "22.9 kV", "66 kV", "220 kV"],
        "respuesta": "22.9 kV"
    },
    "2. ¿Qué nivel de tensión se considera transmisión en el Perú?": {
        "opciones": ["6.6 kV", "22.9 kV", "60 kV y superiores", "380 V"],
        "respuesta": "60 kV y superiores"
    },
    "3. ¿Cuál es el voltaje nominal de distribución secundaria en baja tensión residencial en Perú?": {
        "opciones": ["110 V", "220 V", "440 V", "24 V"],
        "respuesta": "220 V"
    },
    "4. ¿Cuál de los siguientes se considera nivel de subtransmisión en Perú?": {
        "opciones": ["22.9 kV", "60 kV", "220 kV", "500 kV"],
        "respuesta": "60 kV"
    },
    "5. ¿Cuál es el mayor nivel de tensión del sistema eléctrico peruano?": {
        "opciones": ["220 kV", "400 kV", "500 kV", "750 kV"],
        "respuesta": "500 kV"
    }
}

# Guardar respuestas del usuario
respuestas_usuario = {}

for i, (pregunta, data) in enumerate(preguntas.items()):
    respuestas_usuario[pregunta] = st.radio(
        f"{i+1}. {pregunta}",
        data["opciones"],
        key=f"pregunta_{i}"
    )

# Botón para verificar
if st.button("Verificar respuestas"):
    correctas = 0
    for pregunta, data in preguntas.items():
        if respuestas_usuario[pregunta] == data["respuesta"]:
            correctas += 1
    
    if correctas == len(preguntas):
        st.success("🎉 ¡Felicitaciones! Todas tus respuestas son correctas. 🎉")
        # Animación simple con confetti
        for _ in range(3):
            st.balloons()
            time.sleep(1)
    else:
        st.error(f"Obtuviste {correctas} de {len(preguntas)} correctas. ¡Sigue intentando!")
