class script(object):

    # 🍿 आपके लाइव फीचर्स और प्रीमियम मॉडल के अनुसार स्टार्ट टेक्स्ट (DM locked logic ready)
    START_TXT = """<b>ʜᴇʏ {}, <i>{}</i>
    
ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ & ꜱᴍᴀʀᴛ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ʙᴏᴛ! ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇꜱ ᴀɴᴅ ꜱᴇʀɪᴇꜱ ᴡɪᴛʜ ᴅɪʀᴇᴄᴛ ꜱᴛʀᴇᴀᴍ & ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋꜱ. 🚀

🍿 <u>ᴍʏ ᴍᴀɪɴ ғᴇᴀᴛᴜʀᴇꜱ:</u>
• ꜱᴍᴀʀᴛ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ ɢʀᴏᴜᴘꜱ
• 📱 ᴀᴅᴠᴀɴᴄᴇᴅ ᴍɪɴɪ ᴀᴘᴘ ꜰᴏʀ ᴄɪɴᴇᴍᴀᴛɪᴄ ꜱᴇᴀʀᴄʜ
• 🎬 ɪɴ-ʙᴜɪʟᴛ ᴘʟᴀʏᴇʀ ᴡɪᴛʜ 10ꜱ ᴅᴏᴜʙʟᴇ-ᴛᴀᴘ ꜱᴋɪᴘ
• ⚡ ꜱᴜᴘᴇʀғᴀꜱᴛ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋꜱ
• 🧠 ɢᴇᴍɪɴɪ 2.5 ғʟᴀsʜ ᴀɪ ᴄʜᴀᴛ ᴀssɪsᴛᴀɴᴛ
• 🛡️ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇ ǫᴜᴇᴜᴇ (ʀᴇꜱᴛᴀʀᴛ-ᴘʀᴏᴏғ)

✨ <i>ᴊᴏɪɴ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ꜰᴏʀ ᴀɴ ᴀᴅ-ꜰʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ!</i></b>"""

    # 📊 ✅ NEW PREMIUM UI: एकदम नया मॉडर्न लुक जिसमें Directory भी शामिल है (Admin Only)
    STATUS_TXT = """<b>🤖 𝐅ᴀ𝐬ᴛ 𝐅ɪ𝐧𝐝ᴇʀ 𝐒ʏ𝐬ᴛᴇᴍ 𝐓ᴇʟᴇᴍᴇᴛʀʏ</b>

<b>👥 <u>ɴᴇᴛᴡᴏʀᴋ ᴅʏɴᴀᴍɪᴄs:</u></b>
<blockquote><b>🤵 ᴜsᴇʀs:</b> <code>{}</code>
<b>🏘️ ɢʀᴏᴜᴘs:</b> <code>{}</code>
<b>💎 ᴘʀᴇᴍɪᴜᴍ:</b> <code>{}</code></blockquote>

<b>🗄️ <u>ᴅᴀᴛᴀ ᴄᴇɴᴛʀᴇ (ᴛᴏᴛᴀʟ: {}):</u></b>
<blockquote><b>🟢 ᴘʀɪᴍᴀʀʏ:</b> <code>{}</code> (🖼️ <code>{}</code>)
<b>🔵 ᴄʟᴏᴜᴅ:</b> <code>{}</code> (🖼️ <code>{}</code>)
<b>🟠 ᴀʀᴄʜɪᴠᴇ:</b> <code>{}</code> (🖼️ <code>{}</code>)</blockquote>

<b>🗂️ <u>ᴜɴɪᴠᴇʀsᴀʟ ᴅɪʀᴇᴄᴛᴏʀʏ (ᴛᴏᴛᴀʟ: {}):</u></b>
<blockquote><b>🎭 ᴀᴄᴛᴏʀs:</b> <code>{}</code>
<b>📱 ᴀᴘᴘs:</b> <code>{}</code>
<b>🌐 ᴡᴇʙsɪᴛᴇs:</b> <code>{}</code></blockquote>

<b>⚙️ <u>ᴇɴɢɪɴᴇ ᴍᴇᴛʀɪᴄs:</u></b>
<blockquote><b>🖼️ ɢʟᴏʙᴀʟ ᴛʜᴜᴍʙs:</b> <code>{}</code>
<b>⏱️ ᴜᴘᴛɪᴍᴇ:</b> <code>{}</code></blockquote>"""

    # ✅ सिर्फ प्रीमियम/नॉर्मल यूज़र्स के लिए ग्लोबल लाइब्रेरी स्टैट्स
    USER_STATUS_TXT = """<b>📊 𝐅ᴀ𝐬ᴛ 𝐅ɪ𝐧𝐝ᴇʀ 𝐆ʟᴏʙᴀʟ 𝐋ɪʙʀᴀʀʏ</b>

<b>🗄️ <u>ᴄᴏɴᴛᴇɴᴛ ᴠᴀᴜʟᴛ:</u></b>
<blockquote><b>🚀 ᴛᴏᴛᴀʟ ᴛɪᴛʟᴇs:</b> <code>{}</code>
<b>🟢 ᴘʀɪᴍᴀʀʏ:</b> <code>{}</code>
<b>🔵 ᴄʟᴏᴜᴅ:</b> <code>{}</code>
<b>🟠 ᴀʀᴄʜɪᴠᴇ:</b> <code>{}</code></blockquote>

<b>🗂️ <u>ᴜɴɪᴠᴇʀsᴀʟ ᴅɪʀᴇᴄᴛᴏʀʏ:</u></b>
<blockquote><b>🌟 ᴛᴏᴛᴀʟ ᴘʀᴏғɪʟᴇs:</b> <code>{}</code>
<b>🎭 ᴀᴄᴛᴏʀs:</b> <code>{}</code>
<b>📱 ᴀᴘᴘs:</b> <code>{}</code>
<b>🌐 ᴡᴇʙsɪᴛᴇs:</b> <code>{}</code></blockquote>

<b>⏱️ sʏsᴛᴇᴍ ʀᴜɴɴɪɴɢ sɪɴᴄᴇ:</b> <code>{}</code>"""

    NEW_GROUP_TXT = """<b>#NewGroup 👥\n\n• Title: {}\n• ID: <code>{}</code>\n• Username: {}\n• Total Members: <code>{}</code></b>"""

    NEW_USER_TXT = """<b>#NewUser 👤\n\n• Name: {}\n• ID: <code>{}</code></b>"""

    NOT_FILE_TXT = """<b>❌ ʜᴇʏ {}, "{}" ɪꜱ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ. 

💡 <u>ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ:</u>
» sᴘᴇʟʟɪɴɢ sʜᴏᴜʟᴅ ʙᴇ ᴄᴏʀʀᴇᴄᴛ (ᴄʜᴇᴄᴋ ɢᴏᴏɢʟᴇ)
» sᴇᴀʀᴄʜ ᴡɪᴛʜ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ᴏɴʟʏ ( things like 4k, Bluray, Season, Year हटा दें)</b>"""

    FILE_CAPTION = """<b>{file_name}</b>"""

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞"""

    HELP_TXT = """<b>👋 Hello {},
    
I can filter any movie and series you want.
Just type the movie or series name in my PM, open our Mini App, or add me into your group!

I have many more features for you.
Please check the commands below 👇</b>"""

    ADMIN_COMMAND_TXT = """<b>👑 <u>Bot Admin Commands:</u> 👇

• /stats - View database & user stats
• /delete - Delete specific files from DB
• /delete_all - Wipe entire collection
• /add_prm - Grant premium manually
• /rm_prm - Revoke premium status
• /prm_list - Export premium users list
• /web_users - View Web Dashboard users
• /warmup_thumbs - Update Thumbnails
• /restart - Hard restart the bot session

⚙️ <u>Group Management Guide:</u> 👇

• /search on | off - Toggle Auto Filter
• /settings - Open Group Settings UI
• /button_style - Switch results mode
• /mute | /unmute - Restrict group user
• /ban - Ban user permanently from group
• /warn | /resetwarn - Manage warnings
• /addblacklist | /removeblacklist - Words
• /blacklist - View blacklisted keywords
• /dlink | /removedlink - Auto-delete words
• /dlinklist - View auto-delete triggers</b>"""
    
    PLAN_TXT = """💎 <b>Fast Finder Premium Plans</b> 💎

Activate a premium plan to unlock exclusive, high-speed features!

⚡ <b>Price:</b> <code>₹{} / Per Day</code> ⚡

🚀 <b>Premium Features Include:</b>
» 🍿 Ad-Free Experience (No interruptions)
» 🎬 Online Streaming & Superfast Downloads
» 🔓 No Need to Join Extra Channels (No FSUB)
» ⚡ Zero Verification / Shortlinks Required
» 👑 Dedicated Admin Support

👨‍🚒 <b>Support & Verification:</b> {}"""

    USER_COMMAND_TXT = """<b>👨‍💻 <u>Bot User Commands:</u> 👇

• /start - Check if bot is alive and open Main Menu
• /plan - View premium membership plan details
• /myplan - Check your remaining premium duration
• /id - Extract User ID, Chat ID, and message details
• /fileid - Reply to media to extract its Telegram File ID
• /ask or /ai - Chat with Gemini 2.5 Flash AI Assistant (10m Memory)</b>"""

    LOG_INDEX_TXT = """📢 <b>#Indexing_Report 📊</b>

<b>📂 Storage Parameters:</b>
» Chat Title: <code>{}</code>
» Chat ID: <code>{}</code>
» Collection Targeted: <code>{}</code>

<b>📈 Execution Statistics:</b>
» Total Processed: <code>{}</code> Files
» Successfully Saved: <code>{}</code> Files
» Duplicates Skipped: <code>{}</code> Files
» Unsupported Format: <code>{}</code> Files
» Errors Intercepted: <code>{}</code> Files

<b>⏱️ Engine Performance:</b>
» Status: <code>Completed Successfully ✅</code>
» Triggered By: <code>Authorized Bot Admin 👮‍♂️</code>"""
