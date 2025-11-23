import cv2
import mediapipe as mp
import pyttsx3
import time

# ----------------------- CONFIGURACIÓN MEDIAPIPE -----------------------
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# ----------------------- CONTROL DE VOZ (MULTIPLATAFORMA) -----------------------
last_spoken = 0  # Evita hablar muchas veces seguidas

def speak(text):
    """
    Habla usando pyttsx3 de forma sencilla.
    Es multiplataforma (Windows, macOS, Linux).
    Puede generar una pequeña pausa mientras habla, lo cual es normal.
    """
    global last_spoken
    now = time.time()
    # Bloqueo de 1 segundo para no saturar con voz
    if now - last_spoken < 1:
        return
    last_spoken = now

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ----------------------- DETECCIÓN DE MANO ABIERTA (4 DEDOS) -----------------------
def is_hand_open(landmarks, width, height):
    """Detecta si la mano está abierta comparando puntas de dedos con nudillos."""
    # Índices de puntas de dedos y nudillos (NO se considera pulgar)
    finger_tips = [8, 12, 16, 20]     # índice, medio, anular, meñique
    finger_pips = [6, 10, 14, 18]     # nudillos intermedios

    open_fingers = 0
    for tip, pip in zip(finger_tips, finger_pips):
        tip_y = landmarks.landmark[tip].y * height
        pip_y = landmarks.landmark[pip].y * height
        if tip_y < pip_y:  # si la punta está más arriba → dedo extendido
            open_fingers += 1

    # Solo considerar mano abierta si 4 dedos están extendidos
    return open_fingers >= 4

# ----------------------- PROGRAMA PRINCIPAL -----------------------
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ No se pudo acceder a la cámara.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    gesture_text = ""
    last_detected_time = 0
    last_gesture = None  # Registro del último gesto hablado

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    ) as hands:

        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Error leyendo la cámara.")
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            h, w, _ = frame.shape
            current_gesture = None

            # ----------------------- PROCESAR MANO -----------------------
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                    )

                    # Detectar mano abierta estricta
                    if is_hand_open(hand_landmarks, w, h):
                        current_gesture = "HOLA"

            # ----------------------- GESTIÓN DE VOZ -----------------------
            if current_gesture != last_gesture:
                if current_gesture == "HOLA":
                    speak("Hola")  # Solo suena UNA VEZ por gesto nuevo
                last_gesture = current_gesture

            # ----------------------- TEXTO EN PANTALLA -----------------------
            if current_gesture == "HOLA":
                gesture_text = "HOLA"
                last_detected_time = time.time()

            # Borrar texto si pasa el tiempo sin seña
            if time.time() - last_detected_time > 1.5:
                gesture_text = ""

            if gesture_text:
                cv2.putText(
                    frame,
                    gesture_text,
                    (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2,
                    (255, 255, 255),
                    3,
                )

            cv2.putText(
                frame,
                "Levanta la mano abierta para decir 'HOLA'",
                (10, 460),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                1,
            )

            cv2.imshow("Prototipo Traductor LSC - TRL5", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()

# --------------------------------------------------------------------------
if __name__ == "__main__":
    main()
