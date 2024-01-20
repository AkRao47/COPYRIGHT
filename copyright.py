from pyrogram import Client, filters
import os


# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

API_ID = "25450075"
API_HASH = "278e22b00d6dd565c837405eda49e6f2"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_links_and_keywords(client, message):
    keywords = ["NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]
    
    if any(keyword.lower() in message.text.lower() for keyword in keywords) or any(link in message.text.lower() for link in ["http", "https", "www."]):
        await message.delete()
        
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()



# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_long_messages(client, message):
    if len(message.text.split()) >= 10:
        await message.delete()

app.run()



# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

print(f"""╔═════❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱════❍⊱❁۪۪
║┏━━━━━━➣
║┣⪼ ᴏᴡɴᴇʀ :- @DaxxSir3
║┣⪼ ᴘᴀʀᴛ ᴏғ :- @ALLTYPECC
║┗━━━━━━➣
║╔═════ஜ۩۞۩ஜ════╗
║    अनंत अखंड अमर अविनाशी
║             कष्ट हरण है
║             शंभु  कैलाशी
║╚═════ஜ۩۞۩ஜ════╝
╚═════════════════❍⊱❁ """)
app.run()
