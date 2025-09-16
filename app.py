import streamlit as st
import time
import random

st.set_page_config(page_title="Made with ❤️ for my baby boy Kush", page_icon="❤️", layout="centered")

# --- Mochi Stickers ---
stickers = {
    0: "https://media.tenor.com/-ZCqQsj3uXgAAAAj/mochi-mochi-peach-cat-love.gif",   # LOVE page
    1: "https://media.tenor.com/uJ2cSWu5N7oAAAAi/mochi-peach-cat.gif",             # nodding
    2: "https://media.tenor.com/tJ1qfh-iTx8AAAAi/mochi-cat.gif",                   # 😝 tongue out
    3: "https://media.tenor.com/qzSru1VJ2_UAAAAi/mochi-peach.gif",                 # thinking (game)
    4: "https://media.tenor.com/Bb36GEUdKeQAAAAi/mochi-mochi-peach-cat-archer.gif",# shooting arrows
    5: "https://media.tenor.com/nZQdDCYQgPcAAAAi/mochi-peach-kiss.gif",            # blowing kisses
}

def show_sticker(step, size=150):
    st.markdown(
        f"""
        <div style='text-align:center;'>
            <img src='{stickers[step]}' width='{size}'
                 style='border-radius:50%; border:4px solid #ff4d6d; padding:5px; background:#fff;'/>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Reset Memory Game ---
def reset_game():
    st.session_state.sticker_pairs = ["🌞", "❤️", "⭐", "🍀", "🌸", "🎵", "💎", "⚡"]
    st.session_state.cards = st.session_state.sticker_pairs * 2
    random.shuffle(st.session_state.cards)
    st.session_state.flipped = [False]*16
    st.session_state.matched = [False]*16
    st.session_state.first_choice = None
    st.session_state.second_choice = None
    st.session_state.finished = False

# --- Initialize ---
if "step" not in st.session_state:
    st.session_state.step = 0
if "cards" not in st.session_state or len(st.session_state.cards) != 16:
    reset_game()

# --- Flow ---
# Page 0: Tap LOVE
if st.session_state.step == 0:
    show_sticker(0)
    st.title("💖 Made with ❤️ for my baby boy Kush 💖")
    st.caption("by your baby love Anusha")
    st.write("Tap the LOVE! 💌")
    if st.button("💌 LOVE 💌", use_container_width=True):
        st.session_state.step = 1

# Page 1: Mochi nodding
elif st.session_state.step == 1:
    show_sticker(1)
    st.markdown("## Huii baby boy 😘 >>>>")
    if st.button("Next 👉"):
        st.session_state.step = 2

# Page 2: Mochi tongue out
elif st.session_state.step == 2:
    show_sticker(2)
    st.markdown("## I have something for youuuuu 😝 >>>>")
    if st.button("Next 👉"):
        st.session_state.step = 3

# Page 3: Memory Game 4x4
elif st.session_state.step == 3:
    show_sticker(3)
    st.write("## Try to finish this memory game 😘")

    cols = st.columns(4)
    for i, card in enumerate(st.session_state.cards):
        with cols[i % 4]:
            if st.session_state.matched[i] or st.session_state.flipped[i]:
                st.button(card, key=f"but{i}", disabled=True)
            else:
                if st.button("❓", key=f"but{i}"):
                    if st.session_state.first_choice is None:
                        st.session_state.first_choice = i
                        st.session_state.flipped[i] = True
                    elif st.session_state.second_choice is None and i != st.session_state.first_choice:
                        st.session_state.second_choice = i
                        st.session_state.flipped[i] = True

    # Check for match
    if st.session_state.first_choice is not None and st.session_state.second_choice is not None:
        idx1 = st.session_state.first_choice
        idx2 = st.session_state.second_choice
        if st.session_state.cards[idx1] == st.session_state.cards[idx2]:
            st.session_state.matched[idx1] = True
            st.session_state.matched[idx2] = True
        else:
            st.write("Not a match, try again 😘")
            st.session_state.flipped[idx1] = False
            st.session_state.flipped[idx2] = False
        st.session_state.first_choice = None
        st.session_state.second_choice = None

    if all(st.session_state.matched):
        st.session_state.finished = True
    if st.session_state.finished:
        st.session_state.step = 4

# Page 4: Celebration Mochi archer
elif st.session_state.step == 4:
    show_sticker(4)
    st.balloons()
    st.markdown("## Wow baby boy, you are so smart 😘 muah muah 💋")
    st.write("Wait a moment... 💞")
    if st.button("Continue 💖"):
        st.session_state.step = 5

# Page 5: Final Mochi kisses + heart rain + waterfall
elif st.session_state.step == 5:
    show_sticker(5)

    # Falling hearts with random size, speed & delay
    hearts_html = ""
    for i in range(25):
        left = random.randint(0, 95)
        delay = round(random.uniform(0, 5), 2)
        duration = round(random.uniform(3, 7), 2)
        size = random.randint(16, 40)
        hearts_html += f"<div class='heart' style='left:{left}%; font-size:{size}px; animation-delay:{delay}s; animation-duration:{duration}s;'>💖</div>"

    st.markdown(
        f"""
        <style>
        .hearts {{
            position: fixed;
            top: -10px;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            overflow: hidden;
            z-index: 9999;
        }}
        .heart {{
            position: absolute;
            top: -10px;
            color: #ff4d6d;
            animation: fall linear infinite;
        }}
        @keyframes fall {{
            0% {{ transform: translateY(0) rotate(0deg); opacity: 1; }}
            100% {{ transform: translateY(100vh) rotate(360deg); opacity: 0; }}
        }}
        </style>
        <div class="hearts">{hearts_html}</div>
        """,
        unsafe_allow_html=True
    )

    # Waterfall love messages
    progress = st.progress(0)
    placeholder = st.empty()
    messages = []
    for pct in range(10, 101, 10):
        progress.progress(pct)
        messages.append(f"### I love you {pct}% 💖")
        placeholder.markdown("<br>".join(messages), unsafe_allow_html=True)
        time.sleep(0.6)

    st.success("Love you my dearest, the sweetest, the funniest, the cutest 💕")
    st.info("Stay healthy my love 🌹")

    if st.button("Play Again"):
        reset_game()
        st.session_state.step = 3

    st.caption("Made with ❤️ for my baby boy Kush — by your baby love Anusha")
