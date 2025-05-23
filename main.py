import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

#r = Image.open("download.jpeg")
# Define the pages
PAGES = {
    "Home": "home",
    "Play 2048": "game",
    "Play 5 Nights At Freddy's": "game2",
    "Play Basketball Stars": "Wing",
    "Play Slope": "Slither",
    "Play Granny": "geo",
    "Play Bitlife": "life",
    "Play A Small World Cup": "cup",
    "Play Soccer Skills World Cup": "soccer2",
    "Play Soccer Skills Euro Cup": "soccer",
    "Play Football Legends 2019": "football",
    "Play Escape Road": "level",
    "Play Level Devil": "trial",
    "Play Gladihoppers ": "basket",
    "Play Drive Mad": "mad",
    "Play Crossy Road": "cross",
    "Play Retro Bowl": "retro",
    "Play Getaway Shootout": "get",
    "Play 1v1 LOL": "lol",
    "Play Getting Over It": 'over',
    "Play Uno": "uno",
    "Play OvO": "ovo",
    "Play Cluster Rush": "cluster",
    "Play Roblox": 'roblox',
    "Play GBA Games": 'gba',
    "Mathway(for help with math)": "math",
    "Studentontask unblocker":"student",
    "Coupons": 'coupons',
    "Information": "info",
    "Apps": "app",
    "Your Games": "dev"
}

def main():
    st.link_button("🚨🚨EMERGENCY!(Click if the teacher is near)🚨🚨", "https://www.aleks.com/login")
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    # Set session state for page navigation
    st.session_state.page = PAGES[selection]

    # Load the selected page
    if st.session_state.page == "home":
        home()
    elif st.session_state.page == "game":
        play_2048()
    elif st.session_state.page == "game2":
        play_powerline()
    elif st.session_state.page == "Wing":
        play_Wing()
    elif st.session_state.page == "Slither":
        play_Slither()
    elif st.session_state.page == "geo":
        play_geo()
    elif st.session_state.page == "dev":
        play_dev()
    elif st.session_state.page == "level":
        play_level()
    elif st.session_state.page == "trial":
        play_trial()
    elif st.session_state.page == "life":
        play_life()
    elif st.session_state.page == "app":
        play_app()
    elif st.session_state.page == "basket":
        play_basket()
    elif st.session_state.page == "cross":
        play_cross()
    elif st.session_state.page == "info":
        play_info()
    elif st.session_state.page == "retro":
        play_retro()
    elif st.session_state.page == "get":
        play_get()
    elif st.session_state.page == "lol":
        play_lol()
    elif st.session_state.page == "uno":
        play_uno()
    elif st.session_state.page == "soccer":
        play_soccer()
    elif st.session_state.page == "soccer2":
        play_soccer2()
    elif st.session_state.page == "cup":
        play_cup()
    elif st.session_state.page == "math":
        math()
    elif st.session_state.page == "mad":
        mad()
    elif st.session_state.page == "student":
        student()
    elif st.session_state.page == "cluster":
        play_cluster()
    elif st.session_state.page == "ovo":
        play_ovo()
    elif st.session_state.page == 'over':
        play_over()
    elif st.session_state.page == 'roblox':
        play_roblox()
    elif st.session_state.page == 'coupons':
        play_coupons()
    elif st.session_state.page == 'gba':
        play_gba()
    elif st.session_state.page == 'football':
        play_football()

def home():
    st.title("Welcome to CR7 Games! (Suuuuui!!!)")
    st.header("Shoutout to Isiasis")
    st.subheader('Message from Isaisis: "There ks a day keeps the blackies away')
    st.subheader("live chat fixed")
    st.subheader("use this link for another game site: https://loading123747.github.io/logan-edition/")
    st.subheader("if you want a shoutout tell me in live chat during 1st & 3rd period (you can also put a custom message)")
   # st.image(r, width=300)
    st.write("Before you start using the website read the notes in the information tab for information on how to use the website")
    st.write("Click the button below to open proxy!")
    #proxy greatsword
    st.link_button("Proxy", "https://2cpqfh-8000.csb.app/")
    st.link_button("Live Chat", "https://p6q25v-5000.csb.app/")

def play_2048():
    st.title('Play 2048')

    # URL of the game or webpage you want to embed
    game_url = 'https://2tgfnc-8080.csb.app/web/_aHR0cHM6Ly8yMDQ4Z2FtZS5jb20=_/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_Slither():
    st.title('Play Slope')

    # URL of the game or webpage you want to embed
    game_url = 'https://2tgfnc-8080.csb.app/service/hvtrs8%2F-snoreeaoeko%2Cgktju%60.ko-/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)
    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_powerline():
    st.title('Play 5 Nights At Freddys')

    # URL of the game or webpage you want to embed
    game_url = 'https://2tgfnc-8080.csb.app/web/_aHR0cHM6Ly9maXZlbmlnaHRzYXRmcmVkZHlzMy5jb20=_/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'


def play_Wing():
    #greatsword
    st.title('Play Basketball Stars')

    # URL of the game or webpage you want to embed
    game_url = 'https://6n6282-8080.csb.app/service/hvtrs8%2F-bcsievbclnsvaps%2Fgcmg.ko-/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_dev():
    st.title("Your Games")
    st.subheader("Submit requests for your favorite games")
    st.header("Get in touch with me")
    contact_form = """
    <form action="https://formsubmit.co/Panvi83@outlook.com" method="POST">
        <input type="text" name="name" placeholder = "Your Name" required>
        <input type="email" name="email" placeholder = "Your Email" required>
        <textarea name="message" placeholder="Your favorite game" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_geo():
    #Greatsword
    st.title('Play Granny')
    st.write("Click the England flag for english then click play")
    st.write("use this link while I try to fix the mouse locking problem: https://6n6282-8080.csb.app/service/hvtrs8%2F-gpaln%7B-eaoeq.aoo%2F/ ")

    # URL of the game or webpage you want to embed
    game_url = 'https://6n6282-8080.csb.app/service/hvtrs8%2F-gpaln%7B.eaoeq%2Fercnly%2Follkng%2F/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_life():
    #Greatsword
    st.title('Play Bitlife')

    # URL of the game or webpage you want to embed
    game_url = 'https://6n6282-8080.csb.app/service/hvtrs8%2F-bktnidemnnile%2Cgktju%60.ko-pna%7B.jtol/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_soccer():
    #Greatsword
    st.title('Play Soccer Skills Euro Cup')
    st.write("The display is small, sorry about that but if you can play like that go for it but I recommend fullscreen it")

    # URL of the game or webpage you want to embed
    game_url = 'https://6n6282-8080.csb.app/service/hvtrs8%2F-smcaepsiinlqwmrndaur.aoo%2F/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'
def play_soccer2():
    #Greatsword
    st.title('Play Soccer Skills World Cup')
    st.write("The display is small, sorry about that but if you can play like that go for it but I recommend fullscreen it")

    # URL of the game or webpage you want to embed
    game_url = 'https://6n6282-8080.csb.app/service/hvtrs8%2F-skppaeim04.eivhwb%2Cim%2Fqoacgr%2Fsiinlq-eaoe-/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_football():
    st.title('Play Football Legends 2019')

    # URL of the game or webpage you want to embed
    game_url = 'https://2tgfnc-8080.csb.app/web/_aHR0cHM6Ly93d3cuc25va2lkby5jb20=_/game/football-legends-2019'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_cup():
    #Greatsword
    st.title('Play A Small World Cup')
    st.write("The display is small, sorry about that but if you can play like that go for it but I recommend fullscreen it")

    # URL of the game or webpage you want to embed
    game_url = 'https://6n6282-8080.csb.app/service/hvtrs8%2F-smcaepsiinlqwmrndaur.aoo%2Fc-qmcln-uoplf-aur/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_level():
    # Greatsword
    st.title('Play Escape Road')

    # URL of the game or webpage you want to embed
    game_url = 'https://6n6282-8080.csb.app/service/hvtrs8%2F-gpaln%7B-eaoeq.aoo%2Fgsaare%2Frmaf/'

    # HTML code to embed the game in an iframe with pointer lock
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" 
    allow="fullscreen; gamepad; pointer-lock"></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_basket():
    #Greatsword
    st.title('Play Galdihoppers')
    st.write("The display is small, sorry about that but if you can play like that go for it but I recommend fullscreen it")

    # URL of the game or webpage you want to embed
    game_url = 'https://6n6282-8080.csb.app/service/hvtrs8%2F-tecmfdiaicl%2Cgktju%60.ko-gcmgs-gnafijorpgrq%2F/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'
def mad():
    st.title('Play Drive Mad')

    # URL of the game or webpage you want to embed
    game_url = 'https://2tgfnc-8080.csb.app/web/_aHR0cHM6Ly9kcml2ZW1hZC5tZQ==_/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'


def play_app():
    st.title('Apps')
    st.title("            ")
    st.link_button("Crazy Games", "https://xtyhf5-8000.csb.app/mycourses?login=aHR0cHM6Ly9jcmF6eWdhbWVzLmNvbQ%3D%3D")
    st.link_button("Now.gg", "https://xtyhf5-8000.csb.app/mycourses?login=aHR0cHM6Ly9lZHVjYXRpb25ibHVlc2t5LmNvbS9hcHBzL3JvYmxveC1jb3Jwb3JhdGlvbi81MzQ5L3JvYmxveC5odG1s")
    st.link_button("Chess.com", "https://xtyhf5-8000.csb.app/mycourses?login=aHR0cHM6Ly9jaGVzcy5jb20%3D")
    st.link_button("Tiktok", "https://xtyhf5-8000.csb.app/mycourses?login=aHR0cHM6Ly90aWt0b2suY29t")
    st.link_button("CoolMath Games", "https://xtyhf5-8000.csb.app/mycourses?login=aHR0cHM6Ly9jb29sbWF0aGdhbWVzLmNvbQ%3D%3D")
    st.link_button("9amine", "https://xtyhf5-8000.csb.app/mycourses?login=aHR0cHM6Ly85YW5pbWV0di50bw%3D%3D")
    st.link_button("Twitch", "https://xtyhf5-8000.csb.app/mycourses?login=aHR0cHM6Ly90d2l0Y2gudHY%3D")
    st.link_button('Netflix', "https://xtyhf5-8000.csb.app/mycourses?login=aHR0cHM6Ly9uZXRmbGl4LmNvbQ%3D%3D")
    st.link_button("GBA Emulator", "https://xtyhf5-8000.csb.app/mastery?auth=5sr02nn")
    st.link_button("Extra Games", "https://xtyhf5-8000.csb.app/gms")
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_trial():
    st.title('Play Level Devil')

    # URL of the game or webpage you want to embed
    game_url = 'https://2tgfnc-8080.csb.app/web/_aHR0cHM6Ly93d3cuc25va2lkby5jb20=_/game/level-devil'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_cross():
    st.title('Play Crossy Road')

    # URL of the game or webpage you want to embed
    game_url = 'https://2tgfnc-8080.csb.app/web/_aHR0cHM6Ly93d3cuc25va2lkby5jb20=_/game/crossy-road'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_retro():
    st.title('Play Retro Bowl')

    # URL of the game or webpage you want to embed
    game_url = 'https://2tgfnc-8080.csb.app/web/_aHR0cHM6Ly9yZXRyb2Jvd2wubWU=_/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_get():
    st.title('Play Getaway Shootout')

    # URL of the game or webpage you want to embed
    game_url = 'https://2tgfnc-8080.csb.app/web/_aHR0cHM6Ly90Z2NvZmZpY2lhbC5naXRodWIuaW8=_/games/getaway-shootout/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'


def play_lol():
    st.title('Play 1v1 LOL')

    # URL of the game or webpage you want to embed
    st.write("somtimes it is a bit glitchy and if it is go to this link: https://2tgfnc-8080.csb.app/web/_aHR0cHM6Ly8xdjFsb2wubWU=_/")
    st.write("to play with friends or 1v1 other real people click on the plus icon and then click create party. share the code to play with friends (only works with 2 people including you, or don't share to play by your self or online player) then click play only party leader can click play")
    game_url = 'https://2tgfnc-8080.csb.app/web/_aHR0cHM6Ly8xdjFsb2wubWU=_/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_over():
    #greatsword
    st.title('Play Getting Over It')

    # URL of the game or webpage you want to embed
    game_url = 'https://6n6282-8080.csb.app/service/hvtrs8%2F-snoreeaoeko%2Cgktju%60.ko-dgtcin%2Feevtkne-mvgr%2Fiv.jtol/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'


def play_uno():
    st.title('Play Uno')

    # URL of the game or webpage you want to embed
    game_url = 'https://2tgfnc-8080.csb.app/web/_aHR0cHM6Ly9nZXRhd2F5LXNob290b3V0LmNvbQ==_/uno-online'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'


def play_ovo():
    st.title('Play OvO')
    #use v4 proxy for this

    # URL of the game or webpage you want to embed
    game_url = 'https://use.heatmypool.com/mycourses?login=aHR0cHM6Ly91bmJsb2NrZWQtZ2FtZXMuczMuYW1hem9uYXdzLmNvbS9vdm8uaHRtbA%3D%3D'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_cluster():
    #greatsword
    st.title('Play Cluster Rush')

    # URL of the game or webpage you want to embed
    game_url = 'https://6n6282-8080.csb.app/service/hvtrs8%2F-cnuqtgrpuqh%2Cim%2F/'

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_roblox():
    #v4
    st.title('Play Roblox')
    st.subheader("You will have a 5 minute session and before it ends use the coupons in the coupons page to get the coupons and then put it in for 20 mins of gameplay")

    # URL of the game or webpage you want to embed
    st.write('https://xtyhf5-8000.csb.app/mycourses?login=aHR0cHM6Ly9lZHVjYXRpb25ibHVlc2t5LmNvbS9hcHBzL3JvYmxveC1jb3Jwb3JhdGlvbi81MzQ5L3JvYmxveC5odG1s')

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_gba():
    #rammerhead
    st.title('Play GBA Games')
    # URL of the game or webpage you want to embed
    st.write('https://xtyhf5-8000.csb.app/mycourses?login=aHR0cHM6Ly9ib2J6Z2FtZXMuZ2l0aHViLmlvL0dCQS8%3D')

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def math():
    st.title("Mathway")
    # URL of the game or webpage you want to embed
    game_url = "https://www.mathway.com/Algebra"

    # HTML code to embed the game in an iframe with fullscreen option
    iframe_code = f'''
    <iframe src="{game_url}" width="100%" height="800px" style="border:none;" allowfullscreen></iframe>
    '''

    # Render the iframe in the Streamlit app
    components.html(iframe_code, height=800)

    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def student():
    st.title("Studentontask Unblocker")
    st.write("Credits: byteme")
    st.write("click and hold control, then shift then b so that it reveal the bookmark thing under your url you should see this. If you already have this don't worry about it. Then highlight the the code below by click and hold the last letter in the code then drag it till you reach the first letter. Then after you highlight the code click it and drag it your bookmark thing under your url. Then when you get blocked or studentontasked just click on the bookmark you saved")
    st.text("""
javascript:fetch("https://raw.githubusercontent.com/Loading123747/studentontask/refs/heads/main/link").then((byst) => {
    byst.text().then((src) => {
        document.body.innerHTML = `<iframe width="100%" height="100%" src="${src}"></iframe>`;
    });
})
""")

    img = Image.open("unblocker.jpg")
    st.image(img, width = 1000)
    # Button to go back to the home page
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_coupons():
    st.header("This is only if you are playing Roblox. If one coupons work then try another coupons")
    st.write("TLJTFVGY")
    st.write("ORYHXZ9W")
    st.write("3AJODUXV")
    st.write("1KRGFJYT")
    if st.button('Back to Home'):
        st.session_state.page = 'home'

def play_info():
    st.title("Information")
    st.subheader("Notes before we begin:")
    st.write("This website is still under development and is sometimes a bit glitchly. when you open or use any of the games give it some time to load and if it does not work reload the page a few times. New games will be added often so if you think that his website has very little games or games that you don't like, suggest some games to me in the your games tab. I also wish that you use the live chat website in the home page so that you can talk with other people that are using the website(or the people using the chat app) it is also realtime and I will be on it 24/7(I hope)")
    st.subheader("Information:")
    st.write("If you want to use the proxy in the home tab know that it does not work most of the time due to development, so if you want to use the proxy go to the apps tab and use the better proxy. If you do use the proxy in the home tab you need a url or it won't work(By the way I Fixed the proxy in the home tab so it will work fine) For more games there is also a link to my other website for more games. Just like I said in the notes if the games don't work reload the website a few times, the same goes for the proxy that the extra games. If you want to play any of the games in the fullscreen version scroll down in the game window and you will see a fullscreen button. If you are play any of the soccer games give it some time because it is a big games with lots of files so it might take time. Also if you are playing Galdihoppers and any of the soccer games I am sorry for the small screen I recommend using fullscreen. The website goes down every 1 - 2 weeks due to devolopment. I hope that you enjoy the website and good luck")
left_column, right_column = st.columns(2)
if __name__ == "__main__":
    main()
