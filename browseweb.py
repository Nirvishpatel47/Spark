import webbrowser
import os
from pytsx import say
from dforn import set_timer


def browse_the_web(query,tlk=1):
    URLS = {
    # 🌐 Search Engines
    "google": "https://www.google.com",
    "bing": "https://www.bing.com",
    "duckduckgo": "https://duckduckgo.com",
    "yahoo": "https://www.yahoo.com",

    # ✉️ Email Services
    "gmail": "https://mail.google.com",
    "outlook": "https://outlook.live.com",
    "yahoo mail": "https://mail.yahoo.com",
    "proton mail": "https://mail.proton.me",
    "zoho mail": "https://mail.zoho.com",

    # 💬 Messaging & Communication
    "whatsapp": "https://web.whatsapp.com",
    "telegram": "https://web.telegram.org/k",
    "discord": "https://discord.com/app",
    "messenger": "https://www.messenger.com",
    "slack": "https://slack.com/signin",

    # 📱 Social Media
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://twitter.com",
    "linkedin": "https://www.linkedin.com",
    "reddit": "https://www.reddit.com",
    "snapchat": "https://web.snapchat.com",

    # ☁️ Cloud & Productivity
    "google drive": "https://drive.google.com",
    "google docs": "https://docs.google.com",
    "google sheets": "https://sheets.google.com",
    "dropbox": "https://www.dropbox.com",
    "onedrive": "https://onedrive.live.com",
    "notion": "https://www.notion.so",
    "evernote": "https://www.evernote.com",
    "trello": "https://trello.com/login",
    "asana": "https://app.asana.com",

    # 📚 Learning Platforms
    "khan academy": "https://www.khanacademy.org",
    "coursera": "https://www.coursera.org",
    "edx": "https://www.edx.org",
    "udemy": "https://www.udemy.com",
    "youtube learning": "https://www.youtube.com/learning",

    # 🛒 Shopping
    "amazon": "https://www.amazon.com",
    "flipkart": "https://www.flipkart.com",
    "ebay": "https://www.ebay.com",
    "myntra": "https://www.myntra.com",
    "ajio": "https://www.ajio.com",

    # 💳 Payments
    "paypal": "https://www.paypal.com",
    "google pay": "https://pay.google.com",
    "phonepe": "https://www.phonepe.com",
    "razorpay": "https://razorpay.com",
    "paytm": "https://paytm.com",

    # 🤖 AI Tools
    "chatgpt": "https://chat.openai.com",
    "gemini": "https://gemini.google.com",
    "claude": "https://claude.ai",
    "perplexity": "https://www.perplexity.ai",
    "github copilot": "https://github.com/features/copilot",

    # 💻 Developer Tools
    "github": "https://github.com",
    "stackoverflow": "https://stackoverflow.com",
    "replit": "https://replit.com",
    "codesandbox": "https://codesandbox.io",
    "glitch": "https://glitch.com",

    # 🎵 Entertainment
    "youtube": "https://www.youtube.com",
    "you tube": "https://www.youtube.com",
    "you tub": "https://www.youtube.com",
    "you do": "https://www.youtube.com",
    "yo do": "https://www.youtube.com",
    "spotify": "https://open.spotify.com",
    "netflix": "https://www.netflix.com",
    "hotstar": "https://www.hotstar.com",
    "prime video": "https://www.primevideo.com",

    # 🏦 Banking & Finance
    "sbi": "https://www.onlinesbi.sbi",
    "icici": "https://www.icicibank.com",
    "hdfc": "https://www.hdfcbank.com",
    "axis bank": "https://www.axisbank.com",
    "kotak": "https://www.kotak.com",
    "upi": "https://pay.google.com",
    "groww": "https://groww.in",
    "zerodha": "https://kite.zerodha.com",
    "angel one": "https://www.angelone.in",

    # 🧠 AI Research & APIs
    "openai": "https://platform.openai.com",
    "huggingface": "https://huggingface.co",
    "replicate": "https://replicate.com",
    "cohere": "https://cohere.com",
    "deepmind": "https://deepmind.google",
    "anthropic": "https://www.anthropic.com",

    # 📰 News & Info
    "bbc": "https://www.bbc.com",
    "cnn": "https://www.cnn.com",
    "the hindu": "https://www.thehindu.com",
    "times of india": "https://timesofindia.indiatimes.com",
    "new york times": "https://www.nytimes.com",
    "google news": "https://news.google.com",

    # 🎨 Design & Creativity
    "canva": "https://www.canva.com",
    "figma": "https://www.figma.com",
    "pixlr": "https://pixlr.com",
    "remove bg": "https://www.remove.bg",
    "adobe express": "https://express.adobe.com",

    # 🧘 Health & Fitness
    "healthline": "https://www.healthline.com",
    "webmd": "https://www.webmd.com",
    "myfitnesspal": "https://www.myfitnesspal.com",
    "fitbit": "https://www.fitbit.com",
    "who": "https://www.who.int",

    # 🧑‍💻 Programming & Tools
    "w3schools": "https://www.w3schools.com",
    "geeksforgeeks": "https://www.geeksforgeeks.org",
    "hackerrank": "https://www.hackerrank.com",
    "leetcode": "https://leetcode.com",
    "codeforces": "https://codeforces.com",
    "codechef": "https://www.codechef.com",

    # ☁️ Cloud Tools
    "aws": "https://aws.amazon.com",
    "gcp": "https://console.cloud.google.com",
    "azure": "https://portal.azure.com",
    "vercel": "https://vercel.com",
    "netlify": "https://www.netlify.com",

    # 🌍 Travel & Maps
    "google maps": "https://www.google.com/maps",
    "makemytrip": "https://www.makemytrip.com",
    "irctc": "https://www.irctc.co.in",
    "ola": "https://www.olacabs.com",
    "uber": "https://www.uber.com",

    # 📚 Books & Notes
    "goodreads": "https://www.goodreads.com",
    "libgen": "https://libgen.is",
    "zlibrary": "https://z-lib.is",
    "notion": "https://www.notion.so",
    "ankiweb": "https://ankiweb.net",

    # 📑 Government & Education
    "digilocker": "https://www.digilocker.gov.in",
    "cbse": "https://www.cbse.gov.in",
    "nta": "https://www.nta.ac.in",
    "jeemain": "https://jeemain.nta.ac.in",
    "aicte": "https://www.aicte-india.org",

    # 📦 Project Management & Teams
    "microsoft teams": "https://teams.microsoft.com",
    "microsoft office": "https://www.office.com",
    "zoom": "https://zoom.us",
    "clickup": "https://app.clickup.com",
    "monday": "https://monday.com",

    # 🌐 Browsers & Extensions
    "chrome web store": "https://chrome.google.com/webstore",
    "mozilla addons": "https://addons.mozilla.org",
    "brave browser": "https://brave.com",
    "opera browser": "https://www.opera.com",

    # 🧑‍🎓 Student Tools
    "wolfram alpha": "https://www.wolframalpha.com",
    "overleaf": "https://www.overleaf.com",
    "desmos": "https://www.desmos.com",
    "symbolab": "https://www.symbolab.com",
    "coursera": "https://www.coursera.org",
    "chegg": "https://www.chegg.com",

    # 🌍 Government & Utility
    "uidai": "https://uidai.gov.in",
    "income tax": "https://incometaxindia.gov.in",
    "passport india": "https://portal2.passportindia.gov.in",
    "cowin": "https://www.cowin.gov.in",
    "mygov": "https://www.mygov.in",

    # 📰 Indian News
    "ndtv": "https://www.ndtv.com",
    "indiatoday": "https://www.indiatoday.in",
    "livehindustan": "https://www.livehindustan.com",
    "aajtak": "https://www.aajtak.in",

    # 🎬 Streaming India
    "sony liv": "https://www.sonyliv.com",
    "zee5": "https://www.zee5.com",
    "voot": "https://www.voot.com",
    "jio cinema": "https://www.jiocinema.com",

    # 💼 Jobs & Careers
    "naukri": "https://www.naukri.com",
    "linkedin jobs": "https://www.linkedin.com/jobs",
    "indeed": "https://www.indeed.com",
    "internshala": "https://internshala.com",
    "glassdoor": "https://www.glassdoor.com",

    # 🎨 AI Image & Creativity Tools
    "midjourney": "https://www.midjourney.com",
    "dall e": "https://openai.com/dall-e",
    "craiyon": "https://www.craiyon.com",
    "remove background": "https://www.remove.bg",
    "cleanup pictures": "https://cleanup.pictures",

    # 📈 Charts & Dashboards
    "tradingview": "https://www.tradingview.com",
    "moneycontrol": "https://www.moneycontrol.com",
    "coinmarketcap": "https://coinmarketcap.com",
    "investing": "https://www.investing.com",
    "nse india": "https://www.nseindia.com",

    # 🧘 Productivity & Habit Apps
    "todoist": "https://todoist.com",
    "habitica": "https://habitica.com",
    "pomofocus": "https://pomofocus.io",
    "ticktick": "https://ticktick.com",

    # Applicatins
    "notepad" : "notepad.exe",
    "calculator" : "calc.exe",
    "paint" : "mspaint.exe",
    "command prompt" : "cmd.exe",
    "explorer" : "explorer.exe",

    }
    command = query.lower()

    # Only continue if 'open' is in the command
    if "open" not in command:
        return "Sorry, I don't understand that."
    from rapidfuzz import fuzz, process
    # Use RapidFuzz to find best match from URL keys
    site_names = list(URLS.keys())
    match, score, idx = process.extractOne(command, site_names, scorer=fuzz.token_sort_ratio)

    # Only open if similarity is good enough
    if tlk == 1:
        if score > 60:
            print(f"Opening {match}...")
            os.system(f"start {URLS[match]}")
            webbrowser.open(URLS[match])
        else:
            return "Sorry, I don't understand that."
    elif tlk == 2:
        if score > 80:
            print(f"Opening {match}...")
            say(f"Starting {match}")
            os.system(f"start {URLS[match]}")
            webbrowser.open(URLS[match])
        else:
            return "Sorry, I don't understand that."
