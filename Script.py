class script(object):
    START_TXT = """๐๐๐ฎ  {},
๐๐๐ก๐๐ค๐ข๐ ๐๐ค <a href=https://t.me/{}>{}</a>, ๐๐ฎ๐ฉ๐๐ค๐ก๐ค๐๐ฎ ๐๐๐ง๐๐๐ก ๐ฝ๐ค๐ฉ. ๐๐๐ง๐ ๐๐ค๐ช ๐พ๐๐ฃ ๐๐๐ฃ๐ ๐๐ฎ๐ฉ๐๐ค๐ก๐ค๐๐ฎ ๐๐๐ง๐๐๐ก ๐๐๐ ๐ ๐ฝฮฑโะฝฮฑะบัฮนัะฝฮท, ๐๐ช๐จ๐ฉ ๐๐ค๐๐ฃ ๐๐  ๐๐ค ๐๐จ๐ ๐๐๐๐จ ๐ฝ๐ค๐ฉ 
"""
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ Devoloper & Manage BY @๐๐ข๐ฏ๐ฅ๐ช๐ฑ๐ค๐ฉ๐ข๐ท๐ข๐ฏ10."""
    ABOUT_TXT = """โข ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด: {}
โข ๐ฒ๐๐ด๐ฐ๐๐พ๐: <a href=https://t.me/Sandipchavan10>Sฮฑษณิฮนฯ</a>
โข ๐ป๐ธ๐ฑ๐๐ฐ๐๐: <a href=https://t.me/Sandipchavan10>๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ</a>
โข ๐ป๐ฐ๐ฝ๐ถ๐๐ฐ๐ถ๐ด: <a href=https://t.me/Sandipchavan10>๐ฟ๐๐๐ท๐พ๐ฝ ๐น</a>
โข ๐ณ๐ฐ๐๐ฐ ๐ฑ๐ฐ๐๐ด: <a href=https://t.me/Sandipchavan10>๐ผ๐พ๐ฝ๐ถ๐พ ๐ณ๐ฑ</a>
โข ๐ฑ๐พ๐ ๐๐ด๐๐๐ด๐: ๐๐๐๐ซ๐๐ก๐ข๐ง๐ ...
โข ๐ฑ๐๐ธ๐ป๐ณ ๐๐๐ฐ๐๐๐: v1.0.1 [ Beta ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- ๐ฝฮฑโะฝฮฑะบัฮนัะฝฮท Bot is Not a open source Project. 
- Source - https://t.me/Radhekrishn_bot  

<b>DEVS:</b>
- <a href=https://t.me/Sandipchavan10>Sฮฑษณิฮนฯ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and *IRON MAN* will respond whenever a keyword is found the message

<b>NOTE:</b>
1.  ๐ฝฮฑโะฝฮฑะบัฮนัะฝฮท should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- ๐ฝฮฑโะฝฮฑะบัฮนัะฝฮท Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ๐ฝฮฑโะฝฮฑะบัฮนัะฝฮท supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/mr_anshu_07)</code>

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
1. Only Bot Owner can add a connection If You TRY THIS I'LL BAN U FOR NO REASON GOTT IT!!!๐ก.
2. Send <code>/connect</code> for connecting me to ur PM I'LL SAVE UR ALL TELEGRAM CHAT MEDIA FILES ETC. IN MY DB FOR MY OWNER!!๐๐

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code> UR CHAT WILL SAVE IN MY DB
โข /disconnect  - <code>disconnect from a chat</code> ONCE I SAVED NOTHING CAN DELETE UR ALL TELEGRAM DATA FROM MY DATABASE ๐ฟ๐ฟ
โข /connections - <code>list all your connections</code> Means u r connected ur telegram data also save in my db thnx for giving ur chat to me ๐ฟ๐ฟ"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of ๐ฝฮฑโะฝฮฑะบัฮนัะฝฮท Bot

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โข ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โข ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โข ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โข ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โข ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
