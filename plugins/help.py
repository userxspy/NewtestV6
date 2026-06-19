import time
import logging
import gc # For forced RAM cleanup
from hydrogram import Client, filters, enums

# Utils and Database imports based on your architecture
from utils import (
    get_readable_time, 
    is_rate_limited, 
    get_settings, 
    save_group_settings, 
    is_check_admin, 
    get_seconds
)
from database.users_chats_db import db

logger = logging.getLogger(__name__)

# ======================================================
# 🛠️ HELPER FUNCTIONS
# ======================================================

def get_media_file_id(msg):
    """Extracts media object from message to get file_id and file_ref (Zero RAM Allocation)"""
    if not msg: return None, None
    for attr in ["photo", "video", "document", "audio", "voice", "animation", "sticker"]:
        media = getattr(msg, attr, None)
        if media:
            return media.file_id, getattr(media, "file_ref", "N/A")
    return None, None

async def is_admin(c, m):
    """Checks if the user executing the command is a group admin"""
    if m.sender_chat and m.sender_chat.id == m.chat.id: 
        return True
    if not m.from_user: 
        return False
    return await is_check_admin(c, m.chat.id, m.from_user.id)

# ======================================================
# 🆔 1. ADVANCED ID INSPECTOR (/id)
# ======================================================

@Client.on_message(filters.command("id"))
async def get_id(c, m):
    # Rate limit protection to prevent CPU crashes from spam
    if is_rate_limited(m.from_user.id, "cmd_id", seconds=3):
        return

    r = m.reply_to_message
    u = r.from_user if r and r.from_user else m.from_user
    
    b = "👤 Member"
    if m.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
        try:
            st = (await c.get_chat_member(m.chat.id, u.id)).status
            if st == enums.ChatMemberStatus.OWNER:
                b = "👑 Owner"
            elif st == enums.ChatMemberStatus.ADMINISTRATOR:
                b = "🛡️ Admin"
        except: 
            pass

    t = (f"🆔 <b>ID INFORMATION</b>\n\n"
         f"👤 <b>Name:</b> {u.first_name or ''} {u.last_name or ''}\n"
         f"🦹 <b>User ID:</b> <code>{u.id}</code>\n"
         f"🏷 <b>Username:</b> @{u.username or 'N/A'}\n"
         f"🌐 <b>DC ID:</b> <code>{u.dc_id or 'Unknown'}</code>\n"
         f"🤖 <b>Bot:</b> {'Yes' if u.is_bot else 'No'}\n"
         f"{b}\n🔗 <b>Profile:</b> <a href='tg://user?id={u.id}'>Open</a>\n\n"
         f"💬 <b>CHAT & MESSAGE</b>\n"
         f"🆔 <b>Chat ID:</b> <code>{m.chat.id}</code>\n"
         f"📩 <b>Msg ID:</b> <code>{m.id}</code>\n")

    if m.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
        t += f"Status: <code>Active Premium Group</code>\n📛 <b>Title:</b> {m.chat.title}\n🔗 <b>Link:</b> @{m.chat.username or 'Private'}\n"

    if r:
        f_id, f_ref = get_media_file_id(r)
        if f_id:
            t += f"\n📂 <b>MEDIA DETAILS</b>\n🆔 <b>File ID:</b> <code>{f_id}</code>\n"

    await m.reply_text(t, parse_mode=enums.ParseMode.HTML, disable_web_page_preview=True)

# ======================================================
# ⏳ 2. TIMED PERSISTENT DLINKS (/dlink, /removedlink, /dlinklist)
# ======================================================

@Client.on_message(filters.group & filters.command(["dlink", "removedlink", "dlinklist"]))
async def dlink_handler(c, m):
    # Admin-only access restriction
    if not await is_admin(c, m): 
        return
        
    cmd = m.command[0]
    
    # Fetch live group settings from in-memory RAM cache engine
    data = await get_settings(m.chat.id)
    
    try:
        args = m.text.split(maxsplit=1)[1].strip()
    except IndexError:
        args = ""

    # --- View DLink List ---
    if cmd == "dlinklist":
        dl_dict = data.get("dlink", {})
        items = "\n".join(f"• <code>{k}</code> (⏳ Trigger: {get_readable_time(v)})" for k, v in dl_dict.items()) or "📭 Empty"
        return await m.reply(f"🕒 <b>Timed Persistent DLinks Queue:</b>\n\n{items}")

    if not args: 
        return await m.reply("❗ <b>Please provide a valid text string/keyword trigger.</b>")

    # --- Add / Remove DLink ---
    dl = data.get("dlink", {})
    args_lower = args.lower()
    
    if cmd == "dlink":
        parts = args.split()
        delay = 300  # Default 5 minutes curing timer
        
        # 's', 'min', 'hour' format parser synchronization
        if len(parts) > 1 and parts[0][0].isdigit():
            time_string = parts[0].lower()
            parsed_seconds = await get_seconds(time_string)
            if parsed_seconds > 0:
                delay = parsed_seconds
                args_lower = " ".join(parts[1:]).lower()
            
        dl[args_lower] = delay
        await save_group_settings(m.chat.id, "dlink", dl)
        await m.reply(f"🕒 <b>Timed DLink Trigger Set:</b> `<code>{args_lower}</code>`\n⏳ <i>Auto-delete countdown: {get_readable_time(delay)}</i>")
        
    elif cmd == "removedlink":
        dl.pop(args_lower, None)
        await save_group_settings(m.chat.id, "dlink", dl)
        await m.reply(f"🗑️ <b>Timed DLink Trigger removed:</b> `<code>{args_lower}</code>`")
        
    # OOM prevention safety flush
    gc.collect()

# ======================================================
# ℹ️ 3. GROUP INFO COMMAND (/info) - Strictly for Groups
# ======================================================

@Client.on_message(filters.command("info") & filters.group)
async def group_info_command(c, m):
    # Prevent command spam to keep the server CPU stable
    if is_rate_limited(m.from_user.id, "cmd_info", seconds=5):
        return

    info_text = (
        "ℹ️ <b>Group Commands Information (Info)</b>\n\n"
        "This bot is active in this group with the following advanced features:\n\n"
        "🆔 <b>/id</b>\n"
        "• <b>Action:</b> Extracts full technical details (ID, File ID) of users, groups, and replied media (Photo, Video, Document).\n"
        "• <b>Usage:</b> Reply to any message and type <code>/id</code>.\n\n"
        "⏳ <b>/dlink [time] [keyword]</b> (<i>Only Admins</i>)\n"
        "• <b>Action:</b> Sets an auto-delete timer for a specific keyword in the group.\n"
        "• <b>Usage:</b> <code>/dlink 5m movie</code> (Setting this will auto-delete any message containing the keyword 'movie' after 5 minutes.)\n\n"
        "🗑️ <b>/removedlink [keyword]</b> (<i>Only Admins</i>)\n"
        "• <b>Action:</b> Removes a previously set auto-delete timer (DLink).\n"
        "• <b>Usage:</b> <code>/removedlink movie</code>\n\n"
        "📋 <b>/dlinklist</b> (<i>Only Admins</i>)\n"
        "• <b>Action:</b> Displays a live list of all active DLinks and their curing timers currently set in the group."
    )

    # Sending the reply to the group
    await m.reply_text(
        info_text, 
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True
    )
    
    # OOM prevention safety flush
    gc.collect()

