import streamlit as st
import anthropic
import random

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Us ✨ — Our Little World",
    page_icon="💕",
    layout="centered"
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #1a0a2e 0%, #16213e 40%, #0f3460 100%);
    min-height: 100vh;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-style: italic;
    color: #f7d6e0;
    text-align: center;
    line-height: 1.2;
    text-shadow: 0 0 40px rgba(255,182,193,0.4);
    margin-bottom: 0.2rem;
}

.hero-sub {
    text-align: center;
    color: #b8a9c9;
    font-size: 1rem;
    font-weight: 300;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}

.card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 2rem;
    margin: 1rem 0;
}

.result-box {
    background: linear-gradient(135deg, rgba(247,214,224,0.12), rgba(184,169,201,0.12));
    border: 1px solid rgba(247,214,224,0.3);
    border-radius: 16px;
    padding: 1.8rem;
    margin-top: 1.5rem;
    color: #f0e6ff;
    font-size: 1.05rem;
    line-height: 1.8;
    font-family: 'DM Sans', sans-serif;
}

.section-label {
    color: #f7d6e0;
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    margin-bottom: 0.5rem;
}

.emoji-tab {
    font-size: 1.3rem;
}

/* Streamlit overrides */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
    color: #f0e6ff !important;
}

.stButton > button {
    background: linear-gradient(135deg, #e96fa0, #c06ec4) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.6rem 2.5rem !important;
    font-size: 1rem !important;
    font-family: 'DM Sans', sans-serif !important;
    letter-spacing: 0.05em;
    box-shadow: 0 4px 20px rgba(233,111,160,0.35) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    box-shadow: 0 6px 28px rgba(233,111,160,0.55) !important;
    transform: translateY(-1px);
}

label, .stSelectbox label, .stTextInput label, .stTextArea label {
    color: #b8a9c9 !important;
    font-weight: 400 !important;
}

.stTab [data-baseweb="tab"] {
    color: #b8a9c9 !important;
    font-family: 'DM Sans', sans-serif !important;
}

.stTab [aria-selected="true"] {
    color: #f7d6e0 !important;
    border-bottom-color: #e96fa0 !important;
}

hr {
    border-color: rgba(255,255,255,0.1) !important;
}

.floating-hearts {
    text-align: center;
    font-size: 1.5rem;
    opacity: 0.6;
    margin: 0.5rem 0;
}
</style>
""", unsafe_allow_html=True)


# ─── Anthropic Client ────────────────────────────────────────────────────────
def get_ai_response(prompt: str) -> str:
    try:
        client = anthropic.Anthropic()
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=600,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    except Exception as e:
        return f"✨ (AI observation unavailable — but your love is real!) \n\nError: {str(e)}"


# ─── Hero ────────────────────────────────────────────────────────────────────
st.markdown('<div class="hero-title">Us ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Our Little World — Food · Travel · Fashion · Feelings</div>', unsafe_allow_html=True)
st.markdown('<div class="floating-hearts">🌸 💕 🌙 💕 🌸</div>', unsafe_allow_html=True)
st.markdown("---")

# ─── Tabs ────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🍕 Food", "🗺️ Outing", "👗 Fashion", "💞 Feelings", "🎲 Surprise Us"
])


# ── TAB 1: Food ──────────────────────────────────────────────────────────────
with tab1:
    st.markdown('<p class="section-label">🍕 What are we craving?</p>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        your_craving = st.text_input("Your craving", placeholder="e.g. something spicy")
        your_mood_food = st.selectbox("Your mood", ["Happy 😄", "Lazy 😴", "Romantic 🌹", "Adventurous 🔥", "Cozy 🧸"])
    with col2:
        partner_craving = st.text_input("Partner's craving", placeholder="e.g. something sweet")
        cuisine_pref = st.selectbox("Cuisine type", ["Surprise me!", "Italian 🍝", "Indian 🍛", "Japanese 🍱", "Mexican 🌮", "Street Food 🌯"])

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("✨ Get Food Suggestion", key="food"):
        with st.spinner("Cooking up something magical..."):
            prompt = f"""You are a romantic food advisor for a couple.
Your craving: {your_craving}. Mood: {your_mood_food}.
Partner's craving: {partner_craving}. Cuisine preference: {cuisine_pref}.

Give a warm, fun suggestion: 1 dish or restaurant type that satisfies both.
Include: dish name, why it's perfect for them, a fun fact, and a cute date idea around this meal.
Keep it under 120 words. Use emojis. Be playful and sweet."""
            result = get_ai_response(prompt)
        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)


# ── TAB 2: Outing ────────────────────────────────────────────────────────────
with tab2:
    st.markdown('<p class="section-label">🗺️ Plan our outing</p>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        city = st.text_input("Your city / area", placeholder="e.g. Mumbai, Bali, Paris")
        budget = st.selectbox("Budget", ["Budget friendly 💸", "Mid range 💳", "Splurge mode 💎"])
    with col2:
        outing_vibe = st.selectbox("Vibe", ["Romantic & cozy 🕯️", "Adventure & fun 🎢", "Nature & peaceful 🌿", "Cultural & artsy 🎭", "Chill & lazy 🛋️"])
        duration = st.selectbox("Duration", ["A few hours 🌅", "Full day 🌞", "Weekend trip 🏕️"])

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🗺️ Plan Our Date", key="outing"):
        with st.spinner("Mapping out your perfect day..."):
            prompt = f"""You're a romantic travel planner for a couple.
City/Area: {city}. Budget: {budget}. Vibe: {outing_vibe}. Duration: {duration}.

Create a dreamy outing itinerary. Include:
- 2-3 specific place suggestions (real or descriptive types)
- Best time to visit each
- A romantic moment to create there
- A food/snack recommendation along the way

Keep it under 150 words. Use emojis. Make it feel magical and personal."""
            result = get_ai_response(prompt)
        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)


# ── TAB 3: Fashion ───────────────────────────────────────────────────────────
with tab3:
    st.markdown('<p class="section-label">👗 What should we wear?</p>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        occasion = st.selectbox("Occasion", ["Dinner date 🍷", "Beach day 🏖️", "Movie night 🎬", "Festival 🎊", "Nature walk 🌿", "House party 🎉", "Anniversary 💍"])
        weather = st.selectbox("Weather", ["Hot & sunny ☀️", "Cool & breezy 🌬️", "Cold ❄️", "Rainy 🌧️"])
    with col2:
        your_style = st.selectbox("Your style", ["Casual cool 😎", "Elegant & classy ✨", "Bohemian 🌸", "Streetwear 🔥", "Minimal & chic 🤍"])
        color_pref = st.text_input("Any color preference?", placeholder="e.g. pastels, black, matching")

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("👗 Style Us!", key="fashion"):
        with st.spinner("Picking the perfect outfits..."):
            prompt = f"""You're a fun couples fashion stylist.
Occasion: {occasion}. Weather: {weather}. Style: {your_style}. Color preference: {color_pref}.

Suggest a coordinated couple outfit idea. Include:
- His outfit (specific pieces + colors)
- Her outfit (specific pieces + colors)  
- How they complement each other
- 1 accessory tip for each
- A confidence boost compliment

Keep it under 130 words. Use emojis. Be stylish and encouraging."""
            result = get_ai_response(prompt)
        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)


# ── TAB 4: Feelings ──────────────────────────────────────────────────────────
with tab4:
    st.markdown('<p class="section-label">💞 How are we feeling?</p>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    your_feeling = st.text_area("Share your feelings...", placeholder="e.g. I've been missing them a lot today, feeling grateful for small moments...", height=100)
    feeling_type = st.selectbox("This feeling is...", ["💛 Warm & grateful", "😔 Missing them", "🥰 Head over heels", "😤 Need to talk", "🌙 Nostalgic", "🎉 On top of the world"])
    want_response = st.selectbox("I want...", ["A romantic poem 🌹", "Sweet words of comfort 🤗", "A fun relationship observation 😄", "Advice to express this feeling 💬", "A love letter opener ✉️"])

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("💞 Read My Heart", key="feelings"):
        with st.spinner("Feeling the vibes..."):
            prompt = f"""You're a warm, poetic relationship companion.
Someone shared: "{your_feeling}"
Feeling type: {feeling_type}
They want: {want_response}

Respond accordingly — be deeply human, warm, and genuine.
No clichés. Make them feel truly seen. 
Keep it under 130 words. Use emojis sparingly but meaningfully."""
            result = get_ai_response(prompt)
        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)


# ── TAB 5: Surprise ──────────────────────────────────────────────────────────
with tab5:
    st.markdown('<p class="section-label">🎲 Surprise Us!</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card" style="text-align:center;">
        <p style="color:#b8a9c9; font-size:1.05rem;">Tell us a little about yourselves and get a magical, personalized observation about your relationship ✨</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        name1 = st.text_input("Your name", placeholder="e.g. Aryan")
        trait1 = st.text_input("Your personality in 3 words", placeholder="e.g. funny, caring, lazy")
    with col2:
        name2 = st.text_input("Partner's name", placeholder="e.g. Priya")
        trait2 = st.text_input("Their personality in 3 words", placeholder="e.g. smart, bubbly, foodie")

    together_since = st.text_input("Together since / How long?", placeholder="e.g. 2 years, since college")
    one_thing = st.text_input("One thing you love doing together", placeholder="e.g. binge watching shows, cooking, road trips")

    if st.button("🎲 Surprise Us!", key="surprise"):
        with st.spinner("Working some magic just for you two..."):
            categories = ["a poetic observation about their dynamic", "a funny but true relationship insight", "a prediction about their next adventure", "a love language analysis", "a movie couple they resemble and why"]
            chosen = random.choice(categories)
            prompt = f"""You're a whimsical relationship oracle.
{name1} ({trait1}) and {name2} ({trait2}) have been together {together_since}.
They love: {one_thing}.

Give them: {chosen}.

Be creative, specific to THEM (use their names and traits), warm, and memorable.
Under 130 words. Make them smile or go "omg that's so us!" 💕"""
            result = get_ai_response(prompt)
        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)


# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#6b5b8a; font-size:0.85rem; padding: 1rem 0;">
    Made with 💕 · Powered by Claude AI · Just for the two of you
</div>
""", unsafe_allow_html=True)
