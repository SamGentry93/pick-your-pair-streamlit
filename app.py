import streamlit as st
import random

# Full image list
all_images = [
    {"id": "unicorn_dog", "label": "delusionally fabulous", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/I%27m%20a%20unicorn.jpg"},
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
    {"id": "void_box", "label": "existential packaging", "url": "https://raw.githubusercontent.com/SamGentry93/pick-your-pair-images/main/empty%20void%20filler.jpg"},
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
    essence1 = a["label"]
    essence2 = b["label"]
    templates = [
        f"When {essence1} meets {essence2}, you get a masterpiece of dysfunction.",
        f"Balancing between {essence1} and {essence2} — pray for us.",
        f"Equal parts {essence1} and {essence2}. Somehow it's working?",
        f"{essence1} energy with a dash of {essence2} madness.",
        f"Started with {essence1}, ended up in {essence2}.",
        f"{essence1} is the vibe. {essence2} is the consequence.",
        f"Somewhere between {essence1} and {essence2}, there's a cry for help.",
        f"If your day feels like {essence1} plus {essence2}, you're not alone.",
        f"{essence1} plus {essence2} = Peak 2020s energy.",
        f"A recipe for disaster: 1 cup {essence1}, 2 spoons {essence2}."
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
            <img src='{img['url']}' style='width: 100%; max-height: 250px; height: auto; object-fit: contain; border-radius: 8px;' />
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
