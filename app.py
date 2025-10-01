import streamlit as st

st.set_page_config(page_title="Quiz de Tensión Eléctrica en Perú", layout="centered")

st.title("⚡ Quiz: Niveles de Tensión Eléctrica en Perú")

# Preguntas y respuestas
preguntas = [
    {
        "pregunta": "¿Cuál es el nivel de tensión considerado como 'alta tensión' en Perú?",
        "opciones": ["> 30 kV", "> 60 kV", "> 220 kV"],
        "respuesta_correcta": "> 60 kV"
    },
    {
        "pregunta": "¿Qué nivel de tensión corresponde típicamente al transporte de energía a largas distancias en Perú?",
        "opciones": ["Media tensión", "Alta tensión", "Baja tensión"],
        "respuesta_correcta": "Alta tensión"
    },
    {
        "pregunta": "¿Cuál es un valor típico de media tensión en Perú?",
        "opciones": ["220 V", "22.9 kV", "500 kV"],
        "respuesta_correcta": "22.9 kV"
    },
    {
        "pregunta": "¿Qué nivel de tensión se usa normalmente en hogares peruanos?",
        "opciones": ["220 V", "10 kV", "440 V"],
        "respuesta_correcta": "220 V"
    },
    {
        "pregunta": "¿Qué organismo regula el sistema eléctrico en Perú?",
        "opciones": ["COES", "SUNAT", "MINSA"],
        "respuesta_correcta": "COES"
    }
]

respuestas_usuario = []

with st.form("quiz_form"):
    for i, q in enumerate(preguntas):
        respuesta = st.radio(f"{i+1}. {q['pregunta']}", q["opciones"], key=f"q{i}")
        respuestas_usuario.append(respuesta)
    submitted = st.form_submit_button("Enviar respuestas")

if submitted:
    score = 0
    for i, r in enumerate(respuestas_usuario):
        if r == preguntas[i]["respuesta_correcta"]:
            score += 1

    st.write(f"Tu puntaje: **{score} / {len(preguntas)}**")

    if score == len(preguntas):
        st.success("¡Felicidades! Respondiste todo correctamente ⚡🌩️")
        st.image("lightning.gif", caption="Rayos de celebración", use_column_width=True)
    else:
        st.warning("No acertaste todas. ¡Inténtalo de nuevo!")
