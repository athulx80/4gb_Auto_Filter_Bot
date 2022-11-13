class script(object):
    KFC = "𝙔𝙤𝙪 𝘾𝙖𝙣'𝙩 𝙐𝙨𝙚 𝙈𝙚 😏"
    START_TXT = """𝖧𝖾𝗒𝗒 {}, 𝖬𝗒 𝖭𝖺𝗆𝖾 𝖨𝗌 <a href=https://t.me/{}>{}</a>! 𝖭𝗂𝖼𝖾 𝗍𝗈 𝗆𝖾𝖾𝗍 𝗒𝗈𝗎.

𝖨 𝖠𝗆 𝖠 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅𝗅 𝖠𝗎𝗍𝗈𝖥𝗂𝗅𝗍𝖾𝗋 𝖡𝗈𝗍 𝖶𝗂𝗍𝗁 𝖲𝗈𝗆𝖾 𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌..."""
    HELP_TXT = """<b>Here Is My All Modules</b>"""
    ABOUT_TXT = """➲ 𝖬𝗒 𝖭𝖺𝗆𝖾: {}

➲ 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋: <a href=https://t.me/athulx80>𝖠𝗍𝗁𝗎𝗅</a>

➲ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒: 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆

➲ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾: 𝖯𝗒𝗍𝗁𝗈𝗇

➲ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾: <a href=https://www.mongodb.com/>𝖬𝗈𝗇𝗀𝗈𝖣𝖡</a>

➲ 𝖡𝗈𝗍 𝖲𝖾𝗋𝗏𝖾𝗋: 𝖧𝖾𝗋𝗈𝗄𝗎

➲ 𝖴𝗉𝖽𝖺𝗍𝖾𝗌: <a href=https://t.me/+bw750QKrRTRlOWVl>𝖩𝗈𝗂𝗇 𝖧𝖾𝗋𝖾</a>"""
    SOURCE_TXT = """<b>Sorry Not Open Source</b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- The Weeknd Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. The Weeknd Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/+bw750QKrRTRlOWVl)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of The Weeknd Bot!

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚂𝚃𝙾𝚁𝙰𝙶𝙴 𝚄𝚂𝙴𝙳: <code>{}</code> 𝙼𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
✮ 𝐆𝐫𝐨𝐮𝐩 ›› {}(<code>{}</code>)
✮ 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ›› <code>{}</code>
✮ 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ›› {}
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
✮ 𝐈𝐃 ›› <code>{}</code>
✮ 𝐍𝐚𝐦𝐞 ›› {}
"""
