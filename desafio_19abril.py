import streamlit as st
import os
import time
import random

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
        max-width: 900px;
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
        color: #131131;
    }

    .stButton>button {
        background: #e0e5ec;
        color: #131131 !important; 
        border: none;
        border-radius: 20px;
        box-shadow: 8px 8px 16px #bebebe, -8px -8px 16px #ffffff;
        transition: all 0.3s ease;
        width: 100%;
        font-weight: 800 !important;
        font-size: 22px !important;
        min-height: 80px;
        margin: 10px auto;
    }

    .stButton>button:hover {
        box-shadow: inset 4px 4px 8px #bebebe, inset -4px -4px 8px #ffffff;
        transform: scale(0.98);
        color: #131131 !important;
    }

    h1 {
        font-size: 50px !important;
        font-weight: 900 !important;
        color: #131131 !important;
    }

    .pregunta-texto {
        font-size: 30px !important;
        font-weight: 800;
        color: #131131 !important;
        line-height: 1.2;
        margin-bottom: 20px;
    }

    .tiempo-texto {
        font-size: 20px;
        font-weight: 900;
        color: #131131 !important;
        opacity: 0.6;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- RUTAS DE LOGOS (MODIFICACIÓN MÍNIMA REALIZADA AQUÍ) ---
# Usamos la URL de SeekLogo para compatibilidad en la red
logo_alcaldia = "https://seeklogo.com/images/A/alcaldia-de-caracas-2022-logo-E9237E4D8F-seeklogo.com.png"
desktop_path = os.path.expanduser("~/Desktop")
logo_caracas = os.path.join(desktop_path, "CARACAS BELLA.png")

# --- BANCO DE PREGUNTAS (Se mantiene igual) ---
BANCO_PREGUNTAS = [
    {"pregunta": "¿Quién era el Gobernador de Venezuela en abril de 1810?", "opciones": ["Vicente de Emparan", "Fernando VII", "Juan de Casas"], "correcta": "Vicente de Emparan"},
    {"pregunta": "¿Cuál fue el pretexto inicial de Napoleón para ocupar España?", "opciones": ["Invadir Portugal", "Derrocar a Carlos IV", "Unirse al Cabildo"], "correcta": "Invadir Portugal"},
    {"pregunta": "¿A quién entregó Napoleón la corona tras la renuncia de los reyes?", "opciones": ["José Bonaparte", "Luis XIV", "Carlos V"], "correcta": "José Bonaparte"},
    {"pregunta": "¿Cómo se llamó a la renuncia forzada de Fernando VII al trono?", "opciones": ["Abdicaciones de Bayona", "Tratado de Madrid", "Pacto de Caracas"], "correcta": "Abdicaciones de Bayona"},
    {"pregunta": "¿Qué día ocurrió el levantamiento en Madrid contra los franceses?", "opciones": ["2 de mayo de 1808", "5 de julio", "19 de abril"], "correcta": "2 de mayo de 1808"},
    {"pregunta": "¿Cuál era la base legal de los caraqueños para formar su Junta?", "opciones": ["El Vacío de Poder", "El Derecho Divino", "Leyes de Indias"], "correcta": "El Vacío de Poder"},
    {"pregunta": "¿Qué institución lideró la transformación el 19 de abril?", "opciones": ["El Ayuntamiento (Cabildo)", "La Real Audiencia", "El Ejército"], "correcta": "El Ayuntamiento (Cabildo)"},
    {"pregunta": "¿Por qué el 19 de abril era un día de mucha gente en la calle?", "opciones": ["Era Jueves Santo", "Era Navidad", "Se celebraba una feria"], "correcta": "Era Jueves Santo"},
    {"pregunta": "¿Quién detuvo a Emparan en la puerta de la Catedral?", "opciones": ["Francisco Salías", "Simón Bolívar", "José Félix Ribas"], "correcta": "Francisco Salías"},
    {"pregunta": "¿Cómo llamaban a Madariaga en el nuevo gobierno?", "opciones": ["Diputado del Pueblo", "Capitán Revolucionario", "Censor Real"], "correcta": "Diputado del Pueblo"},
    {"pregunta": "¿Qué grupo social representaba Ribas en el ayuntamiento?", "opciones": ["Los Pardos", "Los Peninsulares", "Los Franceses"], "correcta": "Los Pardos"},
    {"pregunta": "¿Cómo se llamó a gobernar en nombre del rey cautivo?", "opciones": ["Máscara de Fernando VII", "Plan Caracas", "Pacto Criollo"], "correcta": "Máscara de Fernando VII"},
    {"pregunta": "¿Cuál fue el grito del pueblo en la Plaza Mayor?", "opciones": ["¡No lo queremos!", "¡Viva el Rey!", "¡Sí lo queremos!"], "correcta": "¡No lo queremos!"},
    {"pregunta": "¿Qué frase dijo Emparan al renunciar al mando?", "opciones": ["Pues yo tampoco quiero mando", "Volveré y seré millones", "Pueblo ingrato"], "correcta": "Pues yo tampoco quiero mando"},
    {"pregunta": "¿Qué provincia se negó a reconocer a la Junta de Caracas?", "opciones": ["Coro", "Cumaná", "Mérida"], "correcta": "Coro"},
    {"pregunta": "¿Qué provincia del oriente fue aliada inicial de Caracas?", "opciones": ["Margarita", "Maracaibo", "Guayana"], "correcta": "Margarita"},
    {"pregunta": "¿Cuántos meses pasaron de abril de 1810 a la Independencia?", "opciones": ["15 meses", "24 meses", "6 meses"], "correcta": "15 meses"},
    {"pregunta": "¿Qué himno se inspiró en los versos de esta gesta?", "opciones": ["Gloria al Bravo Pueblo", "Caracas Bella", "Himno de Madrid"], "correcta": "Gloria al Bravo Pueblo"},
    {"pregunta": "¿Quién fue el secretario escribano del nuevo Gobierno?", "opciones": ["José Tomás Santana", "Juan Germán Roscio", "Félix Sosa"], "correcta": "José Tomás Santana"},
    {"pregunta": "¿Cómo se llamaba oficialmente la Junta formada ese día?", "opciones": ["Junta Conservadora de los Derechos de Fernando VII", "Junta de Guerra", "Consejo de Regencia"], "correcta": "Junta Conservadora de los Derechos de Fernando VII"},
    {"pregunta": "¿Qué ciudad española era el último refugio del Consejo de Regencia?", "opciones": ["Cádiz", "Sevilla", "Madrid"], "correcta": "Cádiz"},
    {"pregunta": "¿Qué militar ordenó a la guardia de Emparan no actuar?", "opciones": ["El comandante de guardia", "Simón Bolívar", "Juan Pablo Ayala"], "correcta": "El comandante de guardia"},
    {"pregunta": "¿Qué miembro de la aristocracia era el rector del seminario?", "opciones": ["Juan Antonio Rojas Queipo", "Francisco Espejo", "Martín Tovar Ponte"], "correcta": "Juan Antonio Rojas Queipo"},
    {"pregunta": "¿Qué sentimiento predominaba en Caracas el 18 de abril?", "opciones": ["Mucha tensión y agitación", "Indiferencia", "Alegría"], "correcta": "Mucha tensión y agitación"},
    {"pregunta": "¿Quién era el 'rey legítimo' según los criollos de 1810?", "opciones": ["Fernando VII", "José I", "Napoleón"], "correcta": "Fernando VII"},
    {"pregunta": "¿Qué hacía Madariaga detrás de Emparan en el balcón?", "opciones": ["Hacía señas de que dijeran 'No'", "Rezaba", "Dormía"], "correcta": "Hacía señas de que dijeran 'No'"},
    {"pregunta": "¿En qué castillo fue recluido Fernando VII por Napoleón?", "opciones": ["Castillo en Francia", "Torre de Londres", "Castillo de Caracas"], "correcta": "Castillo en Francia"},
    {"pregunta": "¿Qué buscaba Caracas al invitar a otras provincias?", "opciones": ["Gobierno nacional unificado", "Venderles café", "Hacer la guerra"], "correcta": "Gobierno nacional unificado"},
    {"pregunta": "¿Qué documento marcó el hito jurídico tras la destitución?", "opciones": ["El Acta del 19 de abril", "La Carta de Jamaica", "Ley de Indias"], "correcta": "El Acta del 19 de abril"},
    {"pregunta": "¿Qué lema usaron los mantuanos para calmar a la masa?", "opciones": ["¡Viva nuestro Rey, Fernando VII!", "¡Independencia o Muerte!", "¡Abajo Napoleón!"], "correcta": "¡Viva nuestro Rey, Fernando VII!"},
    {"pregunta": "¿Qué día publicó Emparan sus proclamas pidiendo fidelidad?", "opciones": ["17 de abril", "19 de abril", "1 de mayo"], "correcta": "17 de abril"},
    {"pregunta": "¿Quiénes eran los 'Mantuanos'?", "opciones": ["La élite blanca criolla", "Los soldados franceses", "Los campesinos"], "correcta": "La élite blanca criolla"},
    {"pregunta": "¿Qué se considera el 19 de abril en términos de votación?", "opciones": ["Referéndum revocatorio improvisado", "Elección presidencial", "Censo"], "correcta": "Referéndum revocatorio improvisado"},
    {"pregunta": "¿Qué provincia de los llanos se sumó al movimiento?", "opciones": ["Barinas", "Guayana", "Coro"], "correcta": "Barinas"},
    {"pregunta": "¿Quién era el escribano real que firmó el acta nueva?", "opciones": ["Fausto Viana", "Lino de Clemente", "José Tomás Santana"], "correcta": "Fausto Viana"},
    {"pregunta": "¿Qué país invadió Napoleón para llegar a Portugal en 1807?", "opciones": ["España", "Francia", "Italia"], "correcta": "España"},
    {"pregunta": "¿Qué se redactó apenas 15 meses después de esta gesta?", "opciones": ["Primera Constitución Nacional", "El Acta de Bautismo", "Un tratado comercial"], "correcta": "Primera Constitución Nacional"},
    {"pregunta": "¿Qué institución sustituía al gobernador en crisis históricas?", "opciones": ["Alcaldes del Cabildo", "Capitanes franceses", "La Iglesia"], "correcta": "Alcaldes del Cabildo"},
    {"pregunta": "¿A qué hora fue invitado Emparan al Cabildo?", "opciones": ["A primera hora de la mañana", "Al atardecer", "A medianoche"], "correcta": "A primera hora de la mañana"},
    {"pregunta": "¿Qué intelectual escribía sobre el inicio de esta nueva era?", "opciones": ["Andrés Bello", "Simón Rodríguez", "Juan Lovera"], "correcta": "Andrés Bello"},
    {"pregunta": "¿Dónde se reunían los conspiradores en secreto?", "opciones": ["Casas y haciendas", "En la Catedral", "En el puerto"], "correcta": "Casas y haciendas"},
    {"pregunta": "¿Qué argumento usaron los Cabildos sobre su estatus?", "opciones": ["Igual estatus que provincias españolas", "Eran esclavos", "Eran independientes"], "correcta": "Igual estatus que provincias españolas"},
    {"pregunta": "¿Qué buscaba Napoleón realmente al invadir la península?", "opciones": ["La corona española", "Hacer turismo", "Salvar al Rey"], "correcta": "La corona española"},
    {"pregunta": "¿Qué provincia aliada está en los Andes?", "opciones": ["Mérida", "Cumaná", "Coro"], "correcta": "Mérida"},
    {"pregunta": "¿Qué provincia aliada está en el oriente?", "opciones": ["Cumaná", "Maracaibo", "Trujillo"], "correcta": "Cumaná"},
    {"pregunta": "¿Quién representaba al pueblo como diputado junto a Madariaga?", "opciones": ["Juan Germán Roscio", "Vicente de Emparan", "Napoleón"], "correcta": "Juan Germán Roscio"},
    {"pregunta": "¿Qué propuso Emparan para conservar el mando?", "opciones": ["Presidir él la nueva Junta", "Huir a España", "Nombrar a un francés"], "correcta": "Presidir él la nueva Junta"},
    {"pregunta": "¿Cómo consideraba el Cabildo al Consejo de Regencia de Cádiz?", "opciones": ["Intermediario ilegítimo", "Líder supremo", "Amigo de Caracas"], "correcta": "Intermediario ilegítimo"},
    {"pregunta": "¿En qué ciudad se formó la Junta española más relevante?", "opciones": ["Sevilla", "Cádiz", "Barcelona"], "correcta": "Sevilla"},
    {"pregunta": "¿Qué título tenía Emparan?", "opciones": ["Gobernador y Capitán General", "Virrey", "Alcalde"], "correcta": "Gobernador y Capitán General"}
]

# --- INICIALIZACIÓN DE ESTADO ---
if 'paso' not in st.session_state:
    st.session_state.paso = -1 
    st.session_state.puntos = 0
    st.session_state.feedback = None
    st.session_state.inicio_tiempo = None
    st.session_state.tiempo_total = 0
    st.session_state.preguntas_seleccionadas = []

# --- LÓGICA DE INICIO ---
if st.session_state.paso == -1:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    # Mostramos el logo directamente desde la URL
    st.image(logo_alcaldia, width=450)
    st.markdown("<h1>Desafío: 19 de Abril</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class="neumorphic-card" style="margin-top:0px; font-size: 24px; font-weight: 700;">
            ¡Bienvenido, Patriota!<br><br>
            ¿Crees conocer la historia real de la gesta caraqueña?<br>
            Responde <b>10 preguntas aleatorias</b> de los archivos oficiales.<br><br>
            <i>Pon tus pies en el suelo y demuestra tu conocimiento.</i>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if st.button("¡INICIAR EL RETO!"):
            st.session_state.preguntas_seleccionadas = random.sample(BANCO_PREGUNTAS, 10)
            st.session_state.inicio_tiempo = time.time()
            st.session_state.paso = 0
            st.rerun()
    
    if os.path.exists(logo_caracas):
        st.image(logo_caracas, width=180)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA DE PREGUNTAS ---
elif 0 <= st.session_state.paso < 10:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    cols_h = st.columns([1, 2, 1])
    with cols_h[1]:
        l, r = st.columns(2)
        l.image(logo_alcaldia, width=150)
        if os.path.exists(logo_caracas): r.image(logo_caracas, width=120)

    p = st.session_state.preguntas_seleccionadas[st.session_state.paso]

    if st.session_state.feedback:
        color_div = "#c8e6c9" if st.session_state.feedback == "correct" else "#ffcdd2"
        txt = "✨ ¡EXCELENTE! ✨" if st.session_state.feedback == "correct" else "❌ ¡POR UN PELO! ❌"
        st.markdown(f"<div style='background-color:{color_div}; padding:10px; border-radius:15px; font-weight:900; color:#131131; border:3px solid #131131;'>{txt}</div>", unsafe_allow_html=True)
        time.sleep(0.6)
        st.session_state.feedback = None
        st.rerun()

    st.markdown(f'''
        <div class="neumorphic-card">
            <div style="font-size: 16px; font-weight: 700; opacity: 0.5; margin-bottom:10px;">PROGRESO: {st.session_state.paso + 1} / 10</div>
            <div class="pregunta-texto">{p["pregunta"]}</div>
        </div>
    ''', unsafe_allow_html=True)
    
    letras = ["A", "B", "C"]
    for i, opcion in enumerate(p["opciones"]):
        if st.button(f"**{letras[i]}**: {opcion}", key=f"btn_{st.session_state.paso}_{i}"):
            if opcion == p["correcta"]:
                st.session_state.puntos += 1
                st.session_state.feedback = "correct"
            else:
                st.session_state.feedback = "wrong"
            st.session_state.paso += 1
            if st.session_state.paso == 10:
                st.session_state.tiempo_total = round(time.time() - st.session_state.inicio_tiempo, 2)
            st.rerun()

    st.markdown(f'<div class="tiempo-texto">⏱️ Tiempo transcurrido: {round(time.time() - st.session_state.inicio_tiempo, 1)}s</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA DE RESULTADOS ---
else:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div class="neumorphic-card">', unsafe_allow_html=True)
    
    pts = st.session_state.puntos
    seg = st.session_state.tiempo_total

    # --- MENSAJES DE RESULTADO ---
    if pts == 10:
        tit, col, msg = "¡VIVA LA PATRIA! 🏆", "#1a237e", f"¡MÉRRR...ITO TOTAL! 🏆 Eres Francisco Salías renacido. Respondiste todo en {seg}s."
    elif pts >= 8:
        tit, col, msg = "¡CASI PERFECTO! 📜", "#2e7d32", f"¡DIGNO HIJO DE CARACAS! 🏛️ Superaste el reto con {pts} puntos."
    elif pts >= 6:
        tit, col, msg = "¡PASASTE RASPAO'! 🤨", "#f57c00", f"ESTÁS COMO EMPARAN... 🤨 Con un pie en el barco y otro en el Cabildo. {pts}/10."
    else:
        tit, col, msg = "¡A CÁDIZ DE UNA! 🤷‍♂️", "#b71c1c", f"¡AY PAPÁ, A ESTUDIAR! 📕 Sacaste {pts}/10. La patria te necesita más preparado."

    st.markdown(f"<h1 style='color:{col} !important;'>{tit}</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size: 45px; font-weight: 900; color: {col};'>{pts}/10 PUNTOS</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='tiempo-texto' style='font-size:25px;'>⏱️ Tiempo: {seg} segundos</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size: 22px; font-weight: 700; margin: 30px 0; color:#131131;'>{msg}</div>", unsafe_allow_html=True)
    
    st.markdown("<div style='font-weight:700; color:#131131; margin-bottom:10px;'>📸 ¡Toma un capture y presume tu patriotismo!</div>", unsafe_allow_html=True)

    if st.button("🔄 REINTENTAR (Nuevas Preguntas)"):
        st.session_state.paso = -1
        st.session_state.puntos = 0
        st.session_state.feedback = None
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    if os.path.exists(logo_caracas):
        st.image(logo_caracas, width=150)
    st.markdown('</div>', unsafe_allow_html=True)
