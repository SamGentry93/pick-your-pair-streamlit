import streamlit as st
import random

# Full image list
all_images = [
    {"id": "unicorn_dog", "label": "delusionally fabulous", "tone": "placeholder", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/I%27m%20a%20unicorn.jpg"},
    {"id": "leapfrog_child", "label": "joyfully disruptive", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/Leapfrog.jpg"},
    {"id": "sneaky_artist", "label": "stealthy chaos", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/artist.jpg"},
    {"id": "post_it_person", "label": "administrative overload", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/attack%20of%20the%20post%20it%20notes.jpg"},
    {"id": "judgy_baby", "label": "judging silently", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/baby%20not%20impressed.jpg"},
    {"id": "big_shoes", "label": "in over your head", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/big%20shoes%20to%20fill.jpg"},
    {"id": "bulldog_workout", "label": "burdened with cuteness", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/bulldog%20workout%20partner.jpg"},
    {"id": "cat_attack", "label": "unexpected vengeance", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/cat%20attack.jpg"},
    {"id": "cat_kick", "label": "backhanded betrayal", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/cat%20kicked%20in%20the%20face.jpg"},
    {"id": "penguin_zoom", "label": "existential zoom-in", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/close%20up%20time.jpg"},
    {"id": "homework_excuse", "label": "the classic excuse", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/dog%20ate%20my%20homework.jpg"},
    {"id": "mop_dog", "label": "cleaning by existence", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/dog%20as%20mop.jpg"},
    {"id": "void_box", "label": "existential packaging", "tone": "existential", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/empty%20void%20filler.jpg", "width": 300, "height": 200},
    {"id": "falling_backwards", "label": "full-body enthusiasm", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/falling%20backwards.jpg"},
    {"id": "lobster_dog", "label": "crustacean cosplay", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/lobster%20dog.jpg"},
    {"id": "catflap_dog", "label": "ambition > ability", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/not%20the%20cat%20flap.jpg"},
    {"id": "masked_pets", "label": "pandemic chic", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/pets%20in%20masks.jpg"},
    {"id": "wet_cat", "label": "drenched disappointment", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/very%20wet%20cat.jpg"},
    {"id": "tp_toddler", "label": "chaotic good", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/toilet%20roll%20play.jpg"},
    {"id": "cone_control", "label": "spiralling gloriously", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/out%20of%20cone-trol.jpg"},
    {"id": "posing_baby", "label": "modelling menace", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/posing%20baby.jpg"},
    {"id": "car_skeleton", "label": "eternal commute", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/skeleton%20driver.jpg"},
    {"id": "monkey_selfie", "label": "banana-flavoured ego", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/monkey%20selfie.jpg"},
    {"id": "cat_selfie", "label": "feline influencer", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/selfie%20cat.jpg"},
    {"id": "sheep_sass", "label": "sass in wool", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/sheep%20tongue.jpg"},
    {"id": "snoozefest", "label": "energy-saving mode", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/snoozefest.jpg"},
    {"id": "sleeping_baby", "label": "tiny sleep expert", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/sleeping%20baby.jpg"},
    {"id": "cow_fence", "label": "bad decisions, no exit", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/stuck%20cow.jpg"},
    {"id": "squirrel_surprise", "label": "shock & aww", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/surprised%20squirrel.jpg"},
    {"id": "tomato_cat", "label": "food trust issues", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/tomato%20suspicions.jpg"},
    {"id": "exit_question", "label": "existential hesitation", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/to%20exit%20or%20not.jpg"},
    {"id": "cake_ceo", "label": "CEO of snack strategy", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/toddler%20eating%20cake.jpg"},
    {"id": "tough_baby", "label": "soft and scary", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/tough%20baby.jpg"},
    {"id": "vacation_baby", "label": "tropical mindset", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/vacation%20time.jpg"},
    {"id": "flappy_confusion", "label": "flappy confusion", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/wow%20bird.jpg"}
]

# Check if an image can be loaded successfully
import requests
from PIL import Image
from io import BytesIO

def image_works(url):
    try:
        img = Image.open(BytesIO(requests.get(url, timeout=3).content))
        img.verify()
        return True
    except:
        return False

# Mood summary generator
def generate_mood(a, b):
    essence1, essence2 = a["label"], b["label"]
    tone1, tone2 = a.get("tone", "unknown"), b.get("tone", "unknown")

    pair = (tone1, tone2)
    alt_pair = (tone2, tone1)

    smart_pairings = {
        ("flat", "cheeky"): "Deadpan delivery, chaotic energy.",
        ("confident", "meh"): "Leading the way. Not sure where to.",
        ("meltdown", "overwhelmed"): "Holding it together. Just not very well.",
        ("low", "confused"): "Exhausted and baffled, a modern classic.",
        ("confident", "tough"): "Soft heart, steel vibes.",
        ("flat", "surprised"): "Didn't see that coming. Not reacting anyway.",
        ("cheeky", "chaotic"): "Flirting with disaster, literally.",
        ("existential", "high"): "Existence is thrilling. Also terrifying.",
        ("meh", "suspicious"): "Too disinterested to trust anything.",
        ("overwhelmed", "stuck"): "Over it. In it. Not moving.",
        ("low", "flat"): "Running on fumes and vibes.",
        ("chaotic", "confident"): "Disaster, but with confidence.",
        ("flat", "overwhelmed"): "Feeling everything. Expressing nothing.",
        ("existential", "low"): "Lost in thought, lying down.",
        ("meh", "flat"): "Functioning with minimal enthusiasm.",
        ("chaotic", "surprised"): "Honestly shocked we're still standing.",
        ("confused", "overwhelmed"): "Mentally buffering. Emotionally full.",
        # last safe line
    
        
        ("chaotic", "low"): "Trying to do everything at once… but lying down.",
        ("existential", "suspicious"): "Questioning everything, especially that tomato.",
        ("confident", "chaotic"): "Feeling bold enough to try... unwise things.",
        ("meh", "meltdown"): "Too tired to care, too stressed to stop spiralling.",
        ("zen", "overwhelmed"): "Namaste… but barely holding it together.",
        ("tough", "flat"): "Soft on the inside, emotionally offline.",
        ("confused", "confident"): "Wildly sure of nothing.",
        ("cheeky", "existential"): "Existential dread, but make it flirty.",
        ("overwhelmed", "overwhelmed"): "Overflowing inbox, overflowing emotions.",
        ("flat", "flat"): "Running on default mode and oat milk.",
        ("chaotic", "chaotic"): "Chaos squared. Send help or snacks.",
        ("confident", "confident"): "Main character energy. Might crash later.",
        ("low", "low"): "Quiet quitting reality.",
        ("surprised", "meh"): "Caught off guard by how little I care.",
        ("stuck", "existential"): "Not sure where I am, but I think I’ve been here a while."
    }

    if pair in smart_pairings:
        return smart_pairings[pair]
    elif alt_pair in smart_pairings:
        return smart_pairings[alt_pair]

    # Fallbacks
    templates = [
        f"Today feels like a mix of {essence1} and {essence2}. Unstable, but honest.",
        f"Somewhere between {essence1} and {essence2} — and holding it together.",
        f"{essence1} on the outside, {essence2} on the inside.",
        f"If moods were a playlist: {essence1}, then abruptly {essence2}.",
        f"Started with {essence1}, ended up in {essence2}.", 
        f"{essence1} and {essence2}. You OK, hun?"
    ]
    return random.choice(templates)

# App state
if "selected" not in st.session_state:
    st.session_state.selected = []
    valid_images = [img for img in all_images if image_works(img['url'])]
    st.session_state.images = random.sample(valid_images, 8) if len(valid_images) >= 8 else valid_images
if "mood" not in st.session_state:
    st.session_state.mood = ""

st.title("🧠 Pick Your Pair")
st.write("Choose two images that sum up your vibe. Then hit the button to see your mood summary!")

rows = [st.columns(4) for _ in range(2)]
for i, img in enumerate(st.session_state.images):
    col = rows[i // 4][i % 4]
    with col:
        is_selected = img["id"] in st.session_state.selected
        border_style = "3px solid #1E90FF" if is_selected else "1px solid #ddd"

        st.markdown(f"""
        <div style='border:{border_style}; border-radius:10px; padding:10px; text-align:center'>
            <img src='{img['url']}' style='width: 100%; height: 250px; object-fit: cover; border-radius: 8px;' />
            <p style='font-size:0.85rem'>Click to select</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Select {i+1}", key=f"select_{img['id']}"):
            if is_selected:
                st.session_state.selected.remove(img["id"])
            elif len(st.session_state.selected) < 2:
                st.session_state.selected.append(img["id"])
            st.session_state.mood = ""

if len(st.session_state.selected) == 2:
    selected_imgs = [img for img in st.session_state.images if img["id"] in st.session_state.selected]
    if st.button("🎉 Reveal My Mood"):
        st.session_state.mood = generate_mood(*selected_imgs)

if st.session_state.mood:
    st.success(st.session_state.mood)

if st.button("🔄 New Images"):
    st.session_state.selected = []
    st.session_state.mood = ""
    valid_images = [img for img in all_images if image_works(img['url'])]
    st.session_state.images = random.sample(valid_images, 8) if len(valid_images) >= 8 else valid_images
