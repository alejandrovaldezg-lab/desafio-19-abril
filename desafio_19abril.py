import streamlit as st
import os
import time
import random

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Desafío 19 de Abril", layout="wide")

# --- ESTILO PREMIUM CENTRADO TOTAL (CSS) ---
# Se mantiene el estilo Neumórfico con alto contraste (Azul #131131)
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
    }

    /* Botones de respuesta grandes y negritos */
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

    /* Ocultar elementos de Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- RUTAS DE LOGOS ---
desktop_path = os.path.expanduser("~/Desktop")
logo_alcaldia = os.path.join(desktop_path, "LOGO ALCALDIA HORIZONTAL.png")
logo_caracas = os.path.join(desktop_path, "CARACAS BELLA.png")

# --- BANCO DE PREGUNTAS (Basado en el documento oficial) ---
BANCO_PREGUNTAS = [
    {"pregunta": "¿Quién era el Gobernador y Capitán General de Venezuela en abril de 1810?", "opciones": ["Vicente de Emparan", "Fernando VII", "Juan de Casas"], "correcta": "Vicente de Emparan"},
    {"pregunta": "¿Qué suceso europeo provocó el vacío de poder en las provincias americanas?", "opciones": ["La Revolución Francesa", "Las Abdicaciones de Bayona", "La Batalla de Waterloo"], "correcta": "Las Abdicaciones de Bayona"},
    {"pregunta": "¿A quién entregó Napoleón la corona española tras la renuncia de Fernando VII?", "opciones": ["José Bonaparte", "Luis XIV", "Carlos V"], "correcta": "José Bonaparte"},
    {"pregunta": "¿Qué día ocurrió el levantamiento popular en Madrid contra las tropas francesas?", "opciones": ["5 de julio", "12 de octubre", "2 de mayo de 1808"], "correcta": "2 de mayo de 1808"},
    {"pregunta": "¿Cuál era la base legal de los caraqueños para formar una Junta propia?", "opciones": ["El Derecho Divino", "El principio de Vacío de Poder", "El Tratado de Tordesillas"], "correcta": "El principio de Vacío de Poder"},
    {"pregunta": "¿Qué institución lideró la transformación política el 19 de abril?", "opciones": ["La Real Audiencia", "El Ayuntamiento (Cabildo)", "La Iglesia"], "correcta": "El Ayuntamiento (Cabildo)"},
    {"pregunta": "¿Por qué el 19 de abril de 1810 era un día de especial concurrencia?", "opciones": ["Era Jueves Santo", "Era Año Nuevo", "Se celebraba un natalicio"], "correcta": "Era Jueves Santo"},
    {"pregunta": "¿Qué joven patriota detuvo a Emparan en la puerta de la Catedral?", "opciones": ["Simón Bolívar", "Francisco Salías", "Antonio José de Sucre"], "correcta": "Francisco Salías"},
    {"pregunta": "¿A quién se conocía como el 'Diputado del Clero y del Pueblo'?", "opciones": ["José Cortés de Madariaga", "Juan Germán Roscio", "Feliciano Palacios"], "correcta": "José Cortés de Madariaga"},
    {"pregunta": "¿Qué grupo social representaba José Félix Ribas en el ayuntamiento?", "opciones": ["Los Peninsulares", "Los Pardos", "El Clero"], "correcta": "Los Pardos"},
    {"pregunta": "¿Cómo se llamó a la estrategia de gobernar en nombre del rey cautivo?", "opciones": ["La Máscara de Fernando VII", "El Plan Caracas", "La Regencia Criolla"], "correcta": "La Máscara de Fernando VII"},
    {"pregunta": "¿Cuál fue la respuesta unánime del pueblo en la Plaza Mayor?", "opciones": ["¡Sí lo queremos!", "¡No lo queremos!", "¡Queremos al Rey!"], "correcta": "¡No lo queremos!"},
    {"pregunta": "¿Cuál fue la frase final de Emparan al renunciar al mando?", "opciones": ["'Volveré y seré millones'", "'Pues yo tampoco quiero mando'", "'Pueblo ingrato'"], "correcta": "'Pues yo tampoco quiero mando'"},
    {"pregunta": "¿Qué provincia se negó a reconocer la autoridad de la Junta de Caracas?", "opciones": ["Cumaná", "Coro", "Mérida"], "correcta": "Coro"},
    {"pregunta": "¿Cuál de estas provincias fue aliada inicial del movimiento caraqueño?", "opciones": ["Maracaibo", "Guayana", "Barinas"], "correcta": "Barinas"},
    {"pregunta": "¿En qué se convirtió el movimiento de 1810 apenas 15 meses después?", "opciones": ["En una Monarquía", "En la Independencia del 5 de julio", "En un tratado de paz"], "correcta": "En la Independencia del 5 de julio"},
    {"pregunta": "¿Qué intelectual escribió sobre el inicio de esta nueva era en 1810?", "opciones": ["Andrés Bello", "Simón Rodríguez", "Francisco de Miranda"], "correcta": "Andrés Bello"},
    {"pregunta": "¿Qué himno nacional tiene sus raíces en los versos inspirados por esta gesta?", "opciones": ["Gloria al Bravo Pueblo", "Caracas Bella", "Himno a la Alegría"], "correcta": "Gloria al Bravo Pueblo"},
    {"pregunta": "¿Quién fue el secretario escribano del nuevo Gobierno formado ese día?", "opciones": ["José Tomás Santana", "Juan Germán Roscio", "Lino de Clemente"], "correcta": "José Tomás Santana"},
    {"pregunta": "¿Cómo se llamaba oficialmente la Junta formada el 19 de abril?", "opciones": ["Junta de Guerra", "Junta Conservadora de los Derechos de Fernando VII", "Junta Republicana"], "correcta": "Junta Conservadora de los Derechos de Fernando VII"},
    {"pregunta": "¿Qué ciudad española era el último refugio del Consejo de Regencia?", "opciones": ["Madrid", "Sevilla", "Cádiz"], "correcta": "Cádiz"},
    {"pregunta": "¿Qué militar ordenó a la guardia de Emparan no intervenir?", "opciones": ["Juan Pablo Ayala", "El propio comandante de guardia", "Simón Bolívar"], "correcta": "El propio comandante de guardia"},
    {"pregunta": "¿Qué miembro de la aristocracia era el rector del seminario en ese entonces?", "opciones": ["Juan Antonio Rojas Queipo", "Francisco Espejo", "Martín Tovar Ponte"], "correcta": "Juan Antonio Rojas Queipo"},
    {"pregunta": "¿Qué figura representaba a los líderes de los pardos como diputado?", "opciones": ["Félix Sosa", "Juan Germán Roscio", "Nicolás de Castro"], "correcta": "Félix Sosa"},
    {"pregunta": "¿Qué sentimiento predominaba en Caracas el 18 de abril al llegar noticias de España?", "opciones": ["Indiferencia", "Mucha tensión y agitación", "Alegría"], "correcta": "Mucha tensión y agitación"},
    {"pregunta": "¿A qué se referían las 'Abdicaciones de Bayona'?", "opciones": ["A la muerte del Papa", "A la renuncia de los reyes de España", "A la creación de una ley"], "correcta": "A la renuncia de los reyes de España"},
    {"pregunta": "¿Quién era el 'rey legítimo' según los criollos de 1810?", "opciones": ["Fernando VII", "Carlos IV", "José I"], "correcta": "Fernando VII"},
    {"pregunta": "¿Qué hizo Madariaga mientras Emparan preguntaba al pueblo desde el balcón?", "opciones": ["Dormía", "Hacía señas de que dijeran 'No'", "Rezaba un rosario"], "correcta": "Hacía señas de que dijeran 'No'"},
    {"pregunta": "¿Qué provincia del oriente venezolano se sumó al movimiento?", "opciones": ["Margarita", "Maracaibo", "Coro"], "correcta": "Margarita"},
    {"pregunta": "¿En qué castillo fue recluido Fernando VII por Napoleón?", "opciones": ["Castillo de Valençay", "Castillo de Versalles", "Torre de Londres"], "correcta": "Castillo de Valençay"},
    {"pregunta": "¿Qué institución sustituía al Gobernador en periodos de crisis históricamente?", "opciones": ["Los Alcaldes del Cabildo", "La Inquisición", "El Ejército"], "correcta": "Los Alcaldes del Cabildo"},
    {"pregunta": "¿Qué personaje era el canónigo chileno que participó en la gesta?", "opciones": ["José Cortés de Madariaga", "Francisco de Berrío", "Agustín García"], "correcta": "José Cortés de Madariaga"},
    {"pregunta": "¿Qué buscaba la Junta de Caracas al invitar a otras provincias?", "opciones": ["Venderles productos", "Crear un gobierno nacional unificado", "Hacer una guerra"], "correcta": "Crear un gobierno nacional unificado"},
    {"pregunta": "¿Qué documento marcó el hito jurídico tras la destitución de Emparan?", "opciones": ["El Acta del 19 de abril", "La Carta de Jamaica", "El Decreto de Guerra a Muerte"], "correcta": "El Acta del 19 de abril"},
    {"pregunta": "¿Quién fue el escribano real que firmó el acta del nuevo Gobierno?", "opciones": ["Fausto Viana", "Lino de Clemente", "Nicolás Anzola"], "correcta": "Fausto Viana"},
    {"pregunta": "¿Qué lema usaron los mantuanos para calmar a la masa popular?", "opciones": ["¡Independencia o Muerte!", "¡Viva nuestro Rey, Fernando VII!", "¡Libertad para todos!"], "correcta": "¡Viva nuestro Rey, Fernando VII!"},
    {"pregunta": "¿Qué militar era coronel y participó activamente en los eventos?", "opciones": ["Nicolás de Castro", "Francisco Salías", "Juan Pablo Ayala"], "correcta": "Nicolás de Castro"},
    {"pregunta": "¿Qué día publicó Emparan sus proclamas exhortando a la fidelidad?", "opciones": ["17 de abril", "19 de abril", "1 de mayo"], "correcta": "17 de abril"},
    {"pregunta": "¿Quiénes eran los 'Mantuanos'?", "opciones": ["La élite blanca criolla", "Los esclavizados", "Los soldados franceses"], "correcta": "La élite blanca criolla"},
    {"pregunta": "¿Qué instrumento jurídico se considera la primera Constitución del continente?", "opciones": ["La de 1830", "La redactada por el Congreso de 1811", "La Constitución de Cádiz"], "correcta": "La redactada por el Congreso de 1811"}
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
    if os.path.exists(logo_alcaldia):
        st.image(logo_alcaldia, width=450)
    st.markdown("<h1>Desafío: 19 de Abril</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class="neumorphic-card" style="margin-top:0px;">
            <div style="font-size: 24px; font-weight: 700; color: #131131;">
                ¡Bienvenido, Patriota!<br><br>
                ¿Crees conocer la historia real de la gesta caraqueña?<br>
                Te retamos a responder <b>10 preguntas aleatorias</b> basadas en los archivos oficiales.<br><br>
                <i>Pon tus pies en el suelo y demuestra tu conocimiento.</i>
            </div>
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
    
    # Cabecera con logos
    cols_h = st.columns([1, 2, 1])
    with cols_h[1]:
        l, r = st.columns(2)
        if os.path.exists(logo_alcaldia): l.image(logo_alcaldia, width=150)
        if os.path.exists(logo_caracas): r.image(logo_caracas, width=120)

    p = st.session_state.preguntas_seleccionadas[st.session_state.paso]

    # Feedback visual rápido
    if st.session_state.feedback:
        color = "#c8e6c9" if st.session_state.feedback == "correct" else "#ffcdd2"
        txt = "✨ ¡EXCELENTE! ✨" if st.session_state.feedback == "correct" else "❌ ¡POR UN PELO! ❌"
        st.markdown(f"<div style='background-color:{color}; padding:10px; border-radius:15px; font-weight:900; color:#131131; border:3px solid #131131;'>{txt}</div>", unsafe_allow_html=True)
        time.sleep(0.6)
        st.session_state.feedback = None
        st.rerun()

    # Card de pregunta
    st.markdown(f'''
        <div class="neumorphic-card">
            <div style="font-size: 16px; font-weight: 700; color: #131131; opacity: 0.5; margin-bottom:10px;">PROGRESO: {st.session_state.paso + 1} / 10</div>
            <div class="pregunta-texto">{p["pregunta"]}</div>
        </div>
    ''', unsafe_allow_html=True)
    
    # Opciones A, B, C
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
    
    # Mensajes cómicos y variados
    if pts == 10:
        tit = "¡MÉRRR...ITO TOTAL! 🏆"
        color = "#1a237e"
        msg = f"¡Eres el mismísimo Francisco Salías renacido! Has respondido todo en {seg}s. Caracas está orgullosa, ¡pide tu estatua en la Plaza Bolívar!"
    elif pts >= 8:
        tit = "¡CASI DIPUTADO! 📜"
        color = "#2e7d32"
        msg = f"¡Brillante! {pts}/10. Te faltó un pelito de pardo para ser perfecto. Madariaga te daría la mano (y te haría señas)."
    elif pts >= 6:
        tit = "ESTÁS COMO EMPARAN... 🤨"
        color = "#f57c00"
        msg = f"Sacaste {pts}/10. Estás con un pie en el barco y otro en el Cabildo. ¡Dale otra leída al acta para que no te boten!"
    elif pts >= 4:
        tit = "¡AY PAPÁ, A ESTUDIAR! 📕"
        color = "#d32f2f"
        msg = f"{pts}/10... Te mandaron a cuidar el Castillo de San Carlos por despistado. ¡La patria necesita que sepas más!"
    else:
        tit = "¡PUES YO TAMPOCO QUIERO MANDO! 🤷‍♂️"
        color = "#b71c1c"
        msg = f"¿{pts}/10? Emparan sabe más de historia que tú. ¡Vuelve a intentarlo antes de que Napoleón nos conquiste!"

    st.markdown(f"<h1 style='color:{color} !important;'>{tit}</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size: 45px; font-weight: 900; color: {color};'>{pts}/10 PUNTOS</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='tiempo-texto' style='font-size:25px;'>⏱️ Tiempo: {seg} segundos</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size: 22px; font-weight: 700; margin: 30px 0; color:#131131;'>{msg}</div>", unsafe_allow_html=True)
    
    if st.button("🔄 REINTENTAR (Preguntas Nuevas)"):
        st.session_state.paso = -1
        st.session_state.puntos = 0
        st.session_state.feedback = None
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    if os.path.exists(logo_caracas):
        st.image(logo_caracas, width=150)
    st.markdown('</div>', unsafe_allow_html=True)

