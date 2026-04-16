import streamlit as st
import os
import time
import random

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Desafío 19 de Abril | Noticia058", layout="wide")

# --- ESTILO PREMIUM NEUMÓRFICO (CSS) ---
# REGLA DE ORO: Texto siempre #131131, fondo e0e5ec, sin letras blancas.
st.markdown("""
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css');

    .stApp {
        background-color: #e0e5ec;
        color: #131131;
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
        border: 1px solid rgba(19, 17, 49, 0.1);
        width: 100%;
        animation: fadeInUp 0.8s;
        color: #131131 !important;
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
    }

    h1, h2, h3, p, span, div {
        color: #131131 !important;
    }

    h1 {
        font-size: 50px !important;
        font-weight: 900 !important;
        margin-bottom: 0px;
    }

    .pregunta-texto {
        font-size: 28px !important;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 20px;
    }

    .tiempo-texto {
        font-size: 18px;
        font-weight: 900;
        opacity: 0.7;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- RUTAS DE LOGOS (URLs para Web) ---
# Se usan URLs directas para que funcione en cualquier servidor
logo_alcaldia = "https://upload.wikimedia.org/wikipedia/commons/b/be/Logo_Alcald%C3%ADa_Caracas_%282021-2025%29.png"
logo_caracas = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSN_NSenNxemRIXYGLNSXBCj7fcPzvysLD2Fg&s" # Sustituye por la URL de Caracas Bella

# --- BANCO DE 50 PREGUNTAS (Basado estrictamente en el texto) ---
BANCO_PREGUNTAS = [
    {"p": "¿Quién era el Gobernador de Venezuela en abril de 1810?", "o": ["Vicente de Emparan", "Fernando VII", "Juan de Casas"], "c": "Vicente de Emparan"},
    {"p": "¿Cuál fue el pretexto de Napoleón para ocupar España?", "o": ["Invadir Portugal", "Derrocar a Carlos IV", "Unirse al Cabildo"], "c": "Invadir Portugal"},
    {"p": "¿A quién entregó Napoleón la corona española?", "o": ["José Bonaparte", "Luis XIV", "Carlos V"], "c": "José Bonaparte"},
    {"p": "¿Cómo se llamó a la renuncia forzada de los reyes al trono?", "o": ["Abdicaciones de Bayona", "Tratado de Madrid", "Pacto de Caracas"], "c": "Abdicaciones de Bayona"},
    {"p": "¿Qué día ocurrió el levantamiento en Madrid contra los franceses?", "o": ["2 de mayo de 1808", "5 de julio", "19 de abril"], "c": "2 de mayo de 1808"},
    {"p": "¿Cuál fue la base legal de los caraqueños para formar su Junta?", "o": ["El Vacío de Poder", "El Derecho Divino", "Leyes de Indias"], "c": "El Vacío de Poder"},
    {"p": "¿Qué institución lideró la transformación el 19 de abril?", "o": ["El Ayuntamiento (Cabildo)", "La Real Audiencia", "El Ejército"], "c": "El Ayuntamiento (Cabildo)"},
    {"p": "¿Por qué el 19 de abril era un día de mucha gente en la calle?", "o": ["Era Jueves Santo", "Era Navidad", "Se celebraba una feria"], "c": "Era Jueves Santo"},
    {"p": "¿Quién detuvo a Emparan en la puerta de la Catedral?", "o": ["Francisco Salías", "Simón Bolívar", "José Félix Ribas"], "c": "Francisco Salías"},
    {"p": "¿Cómo llamaban a Madariaga en el nuevo gobierno?", "o": ["Diputado del Pueblo", "Capitán Revolucionario", "Censor Real"], "c": "Diputado del Pueblo"},
    {"p": "¿Qué grupo social representaba Ribas en el ayuntamiento?", "o": ["Los Pardos", "Los Peninsulares", "Los Franceses"], "c": "Los Pardos"},
    {"p": "¿Cómo se llamó a gobernar en nombre del rey cautivo?", "o": ["Máscara de Fernando VII", "Plan Caracas", "Pacto Criollo"], "c": "Máscara de Fernando VII"},
    {"p": "¿Cuál fue el grito del pueblo en la Plaza Mayor?", "o": ["¡No lo queremos!", "¡Viva el Rey!", "¡Sí lo queremos!"], "c": "¡No lo queremos!"},
    {"p": "¿Qué frase dijo Emparan al renunciar al mando?", "o": ["Pues yo tampoco quiero mando", "Volveré y seré millones", "Pueblo ingrato"], "c": "Pues yo tampoco quiero mando"},
    {"p": "¿Qué provincia se negó a reconocer a la Junta de Caracas?", "o": ["Coro", "Cumaná", "Mérida"], "c": "Coro"},
    {"p": "¿Qué provincia del oriente fue aliada inicial de Caracas?", "o": ["Margarita", "Maracaibo", "Guayana"], "c": "Margarita"},
    {"p": "¿Cuántos meses pasaron de abril de 1810 a la Independencia?", "o": ["15 meses", "24 meses", "6 meses"], "c": "15 meses"},
    {"p": "¿Qué himno se inspiró en los versos de esta gesta?", "o": ["Gloria al Bravo Pueblo", "Caracas Bella", "Himno de Madrid"], "c": "Gloria al Bravo Pueblo"},
    {"p": "¿Quién fue el secretario escribano del nuevo Gobierno?", "o": ["José Tomás Santana", "Juan Germán Roscio", "Félix Sosa"], "c": "José Tomás Santana"},
    {"p": "¿Cómo se llamaba oficialmente la Junta formada ese día?", "o": ["Junta Conservadora de los Derechos de Fernando VII", "Junta de Guerra", "Consejo de Regencia"], "c": "Junta Conservadora de los Derechos de Fernando VII"},
    {"p": "¿Qué ciudad española era el último refugio de la Regencia?", "o": ["Cádiz", "Sevilla", "Madrid"], "c": "Cádiz"},
    {"p": "¿Qué militar ordenó a la guardia de Emparan no actuar?", "o": ["El comandante de guardia", "Simón Bolívar", "Juan Pablo Ayala"], "c": "El comandante de guardia"},
    {"p": "¿Qué miembro de la aristocracia era el rector del seminario?", "o": ["Juan Antonio Rojas Queipo", "Francisco Espejo", "Martín Tovar Ponte"], "c": "Juan Antonio Rojas Queipo"},
    {"p": "¿Qué sentimiento predominaba en Caracas el 18 de abril?", "o": ["Mucha tensión y agitación", "Indiferencia", "Alegría"], "c": "Mucha tensión y agitación"},
    {"p": "¿Quién era el 'rey legítimo' según los criollos de 1810?", "o": ["Fernando VII", "José I", "Napoleón"], "c": "Fernando VII"},
    {"p": "¿Qué hacía Madariaga detrás de Emparan en el balcón?", "o": ["Hacía señas de que dijeran 'No'", "Rezaba", "Dormía"], "c": "Hacía señas de que dijeran 'No'"},
    {"p": "¿En qué castillo fue recluido Fernando VII por Napoleón?", "o": ["Castillo de Valençay", "Torre de Londres", "Castillo de Caracas"], "c": "Castillo de Valençay"},
    {"p": "¿Qué buscaba Caracas al invitar a otras provincias?", "o": ["Gobierno nacional unificado", "Venderles café", "Hacer la guerra"], "c": "Gobierno nacional unificado"},
    {"p": "¿Qué documento marcó el hito jurídico tras la destitución?", "o": ["El Acta del 19 de abril", "La Carta de Jamaica", "Ley de Indias"], "c": "El Acta del 19 de abril"},
    {"p": "¿Qué lema usaron los mantuanos para calmar a la masa?", "o": ["¡Viva nuestro Rey, Fernando VII!", "¡Independencia o Muerte!", "¡Abajo Napoleón!"], "c": "¡Viva nuestro Rey, Fernando VII!"},
    {"p": "¿Qué día publicó Emparan sus proclamas pidiendo fidelidad?", "o": ["17 de abril", "19 de abril", "1 de mayo"], "c": "17 de abril"},
    {"p": "¿Quiénes eran los 'Mantuanos'?", "o": ["La élite blanca criolla", "Los soldados franceses", "Los campesinos"], "c": "La élite blanca criolla"},
    {"p": "¿Qué se considera el 19 de abril en términos de votación?", "o": ["Referéndum revocatorio improvisado", "Elección presidencial", "Censo"], "c": "Referéndum revocatorio improvisado"},
    {"p": "¿Qué provincia de los llanos se sumó al movimiento?", "o": ["Barinas", "Guayana", "Coro"], "c": "Barinas"},
    {"p": "¿Quién era el escribano real que firmó el acta nueva?", "o": ["Fausto Viana", "Lino de Clemente", "José Tomás Santana"], "c": "Fausto Viana"},
    {"p": "¿Qué país invadió Napoleón para llegar a Portugal?", "o": ["España", "Francia", "Italia"], "c": "España"},
    {"p": "¿Qué se redactó 15 meses después de esta gesta?", "o": ["Primera Constitución Nacional", "El Acta de Bautismo", "Un tratado comercial"], "c": "Primera Constitución Nacional"},
    {"p": "¿Qué institución sustituía al gobernador en crisis?", "o": ["Alcaldes del Cabildo", "Capitanes franceses", "La Iglesia"], "c": "Alcaldes del Cabildo"},
    {"p": "¿A qué hora fue invitado Emparan al Cabildo?", "o": ["A primera hora de la mañana", "Al atardecer", "A medianoche"], "c": "A primera hora de la mañana"},
    {"p": "¿Qué intelectual escribía sobre el inicio de esta nueva era?", "o": ["Andrés Bello", "Simón Rodríguez", "Juan Lovera"], "c": "Andrés Bello"},
    {"p": "¿Dónde se reunían los conspiradores en secreto?", "o": ["Casas y haciendas", "En la Catedral", "En el puerto"], "c": "Casas y haciendas"},
    {"p": "¿Qué argumento usaron los Cabildos sobre su estatus?", "o": ["Igual estatus que provincias españolas", "Eran esclavos", "Eran independientes"], "c": "Igual estatus que provincias españolas"},
    {"p": "¿Qué buscaba Napoleón realmente al invadir la península?", "o": ["La corona española", "Hacer turismo", "Salvar al Rey"], "c": "La corona española"},
    {"p": "¿Qué provincia aliada está en los Andes?", "o": ["Mérida", "Cumaná", "Coro"], "c": "Mérida"},
    {"p": "¿Qué provincia aliada está en el oriente?", "o": ["Cumaná", "Maracaibo", "Trujillo"], "c": "Cumaná"},
    {"p": "¿Quién representaba al pueblo junto a Madariaga?", "o": ["Juan Germán Roscio", "Vicente de Emparan", "Napoleón"], "c": "Juan Germán Roscio"},
    {"p": "¿Qué propuso Emparan para conservar el mando?", "o": ["Presidir él la nueva Junta", "Huir a España", "Nombrar a un francés"], "c": "Presidir él la nueva Junta"},
    {"p": "¿Cómo consideraba el Cabildo a la Regencia de Cádiz?", "o": ["Intermediario ilegítimo", "Líder supremo", "Amigo de Caracas"], "c": "Intermediario ilegítimo"},
    {"p": "¿En qué ciudad se formó la Junta española más relevante?", "o": ["Sevilla", "Cádiz", "Barcelona"], "c": "Sevilla"},
    {"p": "¿Qué título tenía Emparan?", "o": ["Gobernador y Capitán General", "Virrey", "Alcalde"], "c": "Gobernador y Capitán General"}
]

# --- INICIALIZACIÓN DE ESTADO ---
if 'paso' not in st.session_state:
    st.session_state.paso = -1 
    st.session_state.puntos = 0
    st.session_state.feedback = None
    st.session_state.inicio_tiempo = None
    st.session_state.preguntas_seleccionadas = []

# --- LÓGICA DE INICIO ---
if st.session_state.paso == -1:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.image(logo_alcaldia, width=150)
    
    st.markdown("<h1>Desafío Histórico</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class="neumorphic-card">
            <h3 style="font-weight: 800;">¡Pies en el suelo, Patriota!</h3>
            <p style="font-size: 22px;">¿Sabes qué pasó realmente en el Cabildo de 1810?<br>
            Te retamos a responder <b>10 preguntas</b> aleatorias.<br><br>
            <b>¡Demuestra que Caracas sigue dando el ejemplo!</b></p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if st.button("🚀 INICIAR EL RETO"):
            # Seleccionamos 10 y barajamos las opciones para romper el patrón "A"
            seleccion = random.sample(BANCO_PREGUNTAS, 10)
            for p in seleccion:
                random.shuffle(p["o"])
            st.session_state.preguntas_seleccionadas = seleccion
            st.session_state.inicio_tiempo = time.time()
            st.session_state.paso = 0
            st.rerun()
    
    if os.path.exists(logo_caracas): st.image(logo_caracas, width=180)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA DE PREGUNTAS ---
elif 0 <= st.session_state.paso < 10:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Logos centrados arriba
    col_l, col_r = st.columns(2)
    with col_l: 
        st.image(logo_alcaldia, width=150)
    with col_r:
        if os.path.exists(logo_caracas): st.image(logo_caracas, width=180)

    p_actual = st.session_state.preguntas_seleccionadas[st.session_state.paso]

    # Feedback sutil
    if st.session_state.feedback:
        color_f = "#c8e6c9" if st.session_state.feedback == "correct" else "#ffcdd2"
        txt_f = "✨ ¡EXCELENTE! ✨" if st.session_state.feedback == "correct" else "❌ ¡CASI, PATRIOTA! ❌"
        st.markdown(f"<div style='background-color:{color_f}; padding:10px; border-radius:15px; font-weight:900; margin-bottom:10px;'>{txt_f}</div>", unsafe_allow_html=True)
        time.sleep(0.5)
        st.session_state.feedback = None
        st.rerun()

    st.markdown(f'''
        <div class="neumorphic-card">
            <div style="font-size: 14px; opacity: 0.6; margin-bottom:10px;">PROGRESO: {st.session_state.paso + 1} / 10</div>
            <div class="pregunta-texto">{p_actual["p"]}</div>
        </div>
    ''', unsafe_allow_html=True)
    
    for i, opcion in enumerate(p_actual["o"]):
        if st.button(opcion, key=f"btn_{st.session_state.paso}_{i}"):
            if opcion == p_actual["c"]:
                st.session_state.puntos += 1
                st.session_state.feedback = "correct"
            else:
                st.session_state.feedback = "wrong"
            
            st.session_state.paso += 1
            st.rerun()

    tiempo_transcurrido = round(time.time() - st.session_state.inicio_tiempo, 1)
    st.markdown(f'<div class="tiempo-texto">⏱️ Tiempo: {tiempo_transcurrido}s</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA DE RESULTADOS ---
else:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    pts = st.session_state.puntos
    seg = round(time.time() - st.session_state.inicio_tiempo, 2)

    # Mensajes Históricos Graciosos
    if pts == 10:
        opciones_msg = [
            f"¡MÉRRR...ITO TOTAL! 🏆 Eres Francisco Salías renacido. Hiciste todo en {seg}s. ¡Pide tu estatua en la Plaza Bolívar ya!",
            f"¡NIVEL PRÓCER! 🎖️ Has dejado a Emparan en el exilio con esos {pts}/10. Caracas está orgullosa de tu memoria de acero.",
            f"¡DIPUTADO DEL PUEBLO! 📜 Madariaga te daría la mano (y no señas). {pts} puntos y una velocidad de rayo independentista."
        ]
        tit, color = "¡VIVA LA PATRIA! 🏆", "#1a237e"
    elif pts >= 8:
        opciones_msg = [
            f"¡CASI MANTUANO! ☕ {pts}/10. Te faltó un pelito de pardo para ser perfecto. ¡Muy buen conocimiento, patriota!",
            f"¡DIGNO HIJO DE CARACAS! 🏛️ Superaste el reto con {pts} puntos. Estás listo para firmar el acta del 19 de abril.",
            f"¡CASI DIPUTADO! 📜 {pts}/10. Emparan te tiene miedo. Un poco más y Napoleón se retira de la península por ti."
        ]
        tit, color = "¡CASI PERFECTO! 📜", "#2e7d32"
    elif pts >= 6:
        opciones_msg = [
            f"ESTÁS COMO EMPARAN... 🤨 Con un pie en el barco y otro en el Cabildo. {pts}/10. ¡Dale otra leída al acta!",
            f"¡CUIDADO CON LA REGENCIA! 🏰 Sacaste {pts}. Estás en el limbo entre ser patriota o quedarte en casa rezando.",
            f"ESTÁS EN EL BALCÓN... 👀 Pero Madariaga no sabe si hacerte señas de sí o de no. {pts}/10. ¡Puedes mejorar!"
        ]
        tit, color = "¡PASASTE RASPAO'! 🤨", "#f57c00"
    elif pts >= 4:
        opciones_msg = [
            f"¡AY PAPÁ, A ESTUDIAR! 📕 Sacaste {pts}/10... Te mandaron a cuidar el Castillo de San Carlos por despistado.",
            f"¡NIVEL REALISTA! 🤴 ¿Sólo {pts}? Emparan sabe más de historia que tú ahora mismo. ¡Vuelve a intentarlo!",
            f"¡TE QUEDASTE EN EL REZO! 🕯️ El Jueves Santo pasó y tú seguías en la Catedral. {pts} puntos. ¡Repite el reto!"
        ]
        tit, color = "¡PÉSIMO SERVICIO! 📕", "#d32f2f"
    else:
        opciones_msg = [
            f"¡PUES YO TAMPOCO QUIERO MANDO! 🤷‍♂️ Con {pts}/10 mejor vete con Emparan a Cádiz. ¡Estudia o la historia se repite!",
            f"¡ALERTA ROJA! 🚨 Napoleón nos conquista si dependemos de tu memoria. {pts} puntos. ¡Regresa al seminario!",
            f"¡SOCORRO! 🆘 Estás más perdido que Fernando VII en su castillo. {pts}/10. ¡Reintenta antes del 5 de julio!"
        ]
        tit, color = "¡A CÁDIZ DE UNA! 🤷‍♂️", "#b71c1c"

    st.markdown(f"""
        <div class="neumorphic-card">
            <h1 style='color:{color} !important;'>{tit}</h1>
            <div style='font-size: 55px; font-weight: 900; margin: 10px 0;'>{pts}/10 PUNTOS</div>
            <p style='font-size: 20px; font-weight: 800; opacity: 0.6;'>⏱️ Tiempo Total: {seg} segundos</p>
            <div style='font-size: 24px; font-weight: 700; margin: 25px 0;'>{random.choice(opciones_msg)}</div>
            <p style='font-weight: 900; border-top: 2px solid #131131; padding-top: 15px;'>
                📸 ¡Toma un capture y presume tu patriotismo en redes!
            </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 REINTENTAR (Preguntas Nuevas)"):
        st.session_state.paso = -1
        st.session_state.puntos = 0
        st.rerun()

    if os.path.exists(logo_caracas): st.image(logo_caracas, width=150)
    st.markdown('</div>', unsafe_allow_html=True)
