import streamlit as st
import os
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Desafío 19 de Abril", layout="wide")

# --- ESTILO PREMIUM CENTRADO TOTAL (CSS) ---
st.markdown("""
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css');

    .stApp {
        background-color: #e0e5ec;
    }
    
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        max-width: 1000px;
        margin: 0 auto;
    }

    .neumorphic-card {
        background: #e0e5ec;
        border-radius: 35px;
        box-shadow: 15px 15px 30px #bebebe, -15px -15px 30px #ffffff;
        padding: 40px;
        margin: 20px auto;
        border: 1px solid rgba(255,255,255,0.4);
        width: 100%;
        animation: fadeInUp 0.8s;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .stButton>button {
        background: #e0e5ec;
        color: #131131 !important; 
        border: none;
        border-radius: 20px;
        box-shadow: 8px 8px 16px #bebebe, -8px -8px 16px #ffffff;
        transition: all 0.4s ease;
        width: 100%;
        font-weight: 900 !important;
        font-size: 26px !important;
        min-height: 110px;
        line-height: 1.1;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
        margin: 10px auto;
    }

    .stButton>button:hover {
        box-shadow: 3px 3px 6px #bebebe, -3px -3px 6px #ffffff;
        transform: translateY(-3px);
        background-color: #d1d9e6;
        color: #131131 !important;
    }

    h1 {
        font-size: 48px !important;
        font-weight: 900 !important;
        color: #131131 !important;
        margin: 20px 0 !important;
    }

    .pregunta-texto {
        font-size: 34px !important;
        font-weight: 800;
        color: #131131 !important;
        margin: 20px 0;
    }

    .bienvenida-texto {
        font-size: 24px;
        font-weight: 700;
        color: #131131 !important;
        margin-bottom: 25px;
    }

    .tiempo-texto {
        font-size: 22px;
        font-weight: 900;
        color: #2e7d32 !important;
        margin: 10px 0;
    }

    [data-testid="stHorizontalBlock"] {
        align-items: center !important;
        justify-content: center !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- RUTAS DE ARCHIVOS ---
desktop_path = os.path.expanduser("~/Desktop")
logo_alcaldia = os.path.join(desktop_path, "LOGO ALCALDIA HORIZONTAL.png")
logo_caracas = os.path.join(desktop_path, "CARACAS BELLA.png")

# --- INICIALIZACIÓN DE ESTADO ---
if 'paso' not in st.session_state:
    st.session_state.paso = -1 
    st.session_state.puntos = 0
    st.session_state.feedback = None
    st.session_state.inicio_tiempo = None
    st.session_state.tiempo_total = 0

# --- PANTALLA DE BIENVENIDA ---
if st.session_state.paso == -1:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    if os.path.exists(logo_alcaldia):
        st.image(logo_alcaldia, width=400)
    st.markdown("<h1>Desafío Histórico: 19 de Abril</h1>", unsafe_allow_html=True)
    st.markdown('<div class="bienvenida-texto">La Alcaldía de Caracas te da la bienvenida.<br>Demuestra cuánto sabes sobre nuestra gesta patriótica.</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("INICIAR DESAFÍO"):
            st.session_state.inicio_tiempo = time.time()
            st.session_state.paso = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA DE PREGUNTAS ---
elif st.session_state.paso >= 0 and st.session_state.paso < 10:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    cols_head = st.columns([1, 2, 1])
    with cols_head[1]:
        sub_l, sub_r = st.columns(2)
        with sub_l:
            if os.path.exists(logo_alcaldia): st.image(logo_alcaldia, width=150)
        with sub_r:
            if os.path.exists(logo_caracas): st.image(logo_caracas, width=150)

    preguntas = [
        {"pregunta": "¿Quién ejercía como Capitán General de Venezuela el 19 de abril de 1810?", "opciones": ["Vicente de Emparan", "Fernando VII", "José Bonaparte"], "correcta": "Vicente de Emparan"},
        {"pregunta": "¿Qué suceso en España detonó el vacío de poder en las provincias americanas?", "opciones": ["La muerte del Rey", "Las Abdicaciones de Bayona", "La firma del Tratado de París"], "correcta": "Las Abdicaciones de Bayona"},
        {"pregunta": "¿Quién interceptó a Emparan en las puertas de la Catedral para obligarlo a volver al Cabildo?", "opciones": ["Simón Bolívar", "Francisco Salías", "José Félix Ribas"], "correcta": "Francisco Salías"},
        {"pregunta": "¿Qué institución caraqueña lideró el proceso de cambio político aquel día?", "opciones": ["La Real Audiencia", "El Ayuntamiento (Cabildo)", "La Real Intendencia"], "correcta": "El Ayuntamiento (Cabildo)"},
        {"pregunta": "¿Qué personaje es recordado como el 'Diputado del Clero y del Pueblo'?", "opciones": ["Juan Germán Roscio", "José Cortés de Madariaga", "Lino de Clemente"], "correcta": "José Cortés de Madariaga"},
        {"pregunta": "¿Cuál fue la contundente respuesta del pueblo ante la pregunta de Emparan?", "opciones": ["¡Viva el Rey!", "¡No lo queremos!", "¡Queremos mando!"], "correcta": "¡No lo queremos!"},
        {"pregunta": "¿Cómo se denominó la estrategia de gobernar en nombre del Rey cautivo?", "opciones": ["El Plan de Caracas", "La Máscara de Fernando VII", "La Regencia Criolla"], "correcta": "La Máscara de Fernando VII"},
        {"pregunta": "¿Qué provincias se negaron inicialmente a reconocer a la Junta de Caracas?", "opciones": ["Cumaná y Margarita", "Coro, Maracaibo y Guayana", "Barinas y Mérida"], "correcta": "Coro, Maracaibo y Guayana"},
        {"pregunta": "¿Qué frase pronunció Emparan tras ser rechazado por la multitud?", "opciones": ["'Pues yo tampoco quiero mando'", "'Mañana volveré'", "'Pueblo ingrato'"], "correcta": "'Pues yo tampoco quiero mando'"},
        {"pregunta": "¿Qué emblemático himno surgió del fervor patriótico de esta gesta?", "opciones": ["Caracas Bella", "Gloria al Bravo Pueblo", "El Ocaso Colonial"], "correcta": "Gloria al Bravo Pueblo"}
    ]

    p = preguntas[st.session_state.paso]

    if st.session_state.feedback:
        color_bg = "#c8e6c9" if st.session_state.feedback == "correct" else "#ffcdd2"
        st.markdown(f"<div style='background-color: {color_bg}; padding: 15px; border-radius: 15px; margin: 10px auto; max-width: 400px; color: #131131; font-weight: 900; text-align: center; border: 2px solid #131131;'>{'✨ ¡CORRECTO! ✨' if st.session_state.feedback == 'correct' else '❌ INCORRECTO'}</div>", unsafe_allow_html=True)
        time.sleep(0.8)
        st.session_state.feedback = None
        st.rerun()

    st.markdown(f'''
        <div class="neumorphic-card">
            <div style="font-size: 18px; font-weight: 700; color: #131131; opacity: 0.7;">Pregunta {st.session_state.paso + 1} de 10</div>
            <div class="pregunta-texto">{p["pregunta"]}</div>
        </div>
    ''', unsafe_allow_html=True)
    
    cols = st.columns(3)
    letras = ["A", "B", "C"]
    for i, opcion in enumerate(p["opciones"]):
        with cols[i]:
            if st.button(f"{letras[i]}: {opcion}", key=f"q_{st.session_state.paso}_{i}"):
                if opcion == p["correcta"]:
                    st.session_state.puntos += 1
                    st.session_state.feedback = "correct"
                else:
                    st.session_state.feedback = "wrong"
                
                st.session_state.paso += 1
                if st.session_state.paso == 10:
                    st.session_state.tiempo_total = round(time.time() - st.session_state.inicio_tiempo, 2)
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA DE RESULTADOS ---
else:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div class="neumorphic-card">', unsafe_allow_html=True)
    
    pts = st.session_state.puntos
    segundos = st.session_state.tiempo_total
    
    # LÓGICA DE CLASIFICACIÓN DE RESULTADOS
    if pts == 10:
        categoria = "¡EXCELENTE, PRÓCER DE LA HISTORIA!"
        color_msg = "#1a237e" # Azul muy oscuro
        msg = f"¡Impresionante! Has demostrado un conocimiento absoluto de nuestras raíces. Eres un orgullo para Caracas."
        if segundos < 40: msg += " ¡Y lo hiciste a la velocidad de la luz! ⚡"
    elif pts >= 8:
        categoria = "¡MUY BUENO!"
        color_msg = "#2e7d32" # Verde
        msg = "¡Felicidades! Tienes una base histórica muy sólida. Caracas reconoce tu compromiso con nuestro pasado."
    elif pts >= 6:
        categoria = "REGULAR"
        color_msg = "#f57c00" # Naranja
        msg = "Vas por buen camino, pero aún hay detalles de la gesta patriótica por descubrir. ¡Sigue investigando!"
    elif pts >= 4:
        categoria = "DESEMPEÑO BAJO"
        color_msg = "#d32f2f" # Rojo
        msg = "Nuestra historia es fascinante y te está esperando. Te invitamos a leer más sobre el 19 de Abril en nuestras bibliotecas."
    else:
        categoria = "MUY BAJO"
        color_msg = "#b71c1c" # Rojo oscuro
        msg = "¡No te desanimes! El conocimiento es una montaña que se sube paso a paso. ¡Vuelve a intentarlo y aprende algo nuevo hoy!"

    st.markdown(f"<h1 style='margin-bottom:0px;'>{categoria}</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size: 40px; font-weight: 900; color: {color_msg};'>{pts}/10 Puntos</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='tiempo-texto'>⏱️ Tiempo: {segundos} segundos</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='bienvenida-texto' style='margin-top:20px; padding:0 20px;'>{msg}</div>", unsafe_allow_html=True)
    
    col_r1, col_r2, col_r3 = st.columns([1, 1, 1])
    with col_r2:
        if st.button("🔄 REINTENTAR"):
            st.session_state.paso = -1
            st.session_state.puntos = 0
            st.session_state.feedback = None
            st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)
