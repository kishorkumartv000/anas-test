from ..telegram_helper.bot_commands import BotCommands
from ...core.mltb_client import TgClient

mirror = """<b>Send link along with command line or </b>

/cmd link

<b>By replying to link/file</b>:

/cmd -n new name -e -up upload destination
"""

clone = """Send Gdrive|Gdot|Filepress|Filebee|Appdrive|Gdflix link or rclone path along with command or by replying to the link/rc_path by command.
Use -sync to use sync method in rclone. Example: /cmd rcl/rclone_path -up rcl/rclone_path/rc -sync"""

new_name = """<b>New Name</b>: -n

/cmd link -n new name
Note: Doesn't work with torrents"""

thumb = """<b>Thumbnail for current task</b>: -t

/cmd link -t tg-message-link (doc or photo) or none (file without thumb)"""

split_size = """<b>Split size for current task</b>: -sp

/cmd link -sp (500mb or 2gb or 4000000000)
Note: Only mb and gb are supported or write in bytes without unit!"""

upload = """<b>Upload Destination</b>: -up

/cmd link -up rcl/gdl (rcl: to select rclone config, remote & path | gdl: To select token.pickle, gdrive id) using buttons
You can directly add the upload path: -up remote:dir/subdir or -up Gdrive_id or -up id/username (telegram) or -up id/username|topic_id (telegram)
If DEFAULT_UPLOAD is `rc` then you can pass up: `gd` to upload using gdrive tools to GDRIVE_ID.
If DEFAULT_UPLOAD is `gd` then you can pass up: `rc` to upload to RCLONE_PATH.

If you want to add path or gdrive manually from your config/token (UPLOADED FROM USETTING) add mrcc: for rclone and mtp: before the path/gdrive_id without space.
/cmd link -up mrcc:main:dump or -up mtp:gdrive_id <strong>or you can simply edit upload using owner/user token/config from usetting without adding mtp: or mrcc: before the upload path/id</strong>

To add leech destination:
-up id/@username/pm
-up b:id/@username/pm (b: means leech by bot) (id or username of the chat or write pm means private message so bot will send the files in private to you)
when you should use b:(leech by bot)? When your default settings is leech by user and you want to leech by bot for specific task.
-up u:id/@username(u: means leech by user) This incase OWNER added USER_STRING_SESSION.
-up h:id/@username(hybrid leech) h: to upload files by bot and user based on file size.
-up id/@username|topic_id(leech in specific chat and topic) add | without space and write topic id after chat id or username.

In case you want to specify whether using token.pickle or service accounts you can add tp:gdrive_id (using token.pickle) or sa:gdrive_id (using service accounts) or mtp:gdrive_id (using token.pickle uploaded from usetting).
DEFAULT_UPLOAD doesn't affect on leech cmds.
"""

user_download = """<b>User Download</b>: link

/cmd tp:link to download using owner token.pickle incase service account enabled.
/cmd sa:link to download using service account incase service account disabled.
/cmd tp:gdrive_id to download using token.pickle and file_id incase service account enabled.
/cmd sa:gdrive_id to download using service account and file_id incase service account disabled.
/cmd mtp:gdrive_id or mtp:link to download using user token.pickle uploaded from usetting
/cmd mrcc:remote:path to download using user rclone config uploaded from usetting
you can simply edit upload using owner/user token/config from usetting without adding mtp: or mrcc: before the path/id"""

rcf = """<b>Rclone Flags</b>: -rcf

/cmd link|path|rcl -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
This will override all other flags except --exclude
Check here all <a href='https://rclone.org/flags/'>RcloneFlags</a>."""

rlone_dl = """<b>Rclone Download</b>:

Treat rclone paths exactly like links
/cmd main:dump/ubuntu.iso or rcl(To select config, remote and path)
Users can add their own rclone from user settings
If you want to add path manually from your config add mrcc: before the path without space
/cmd mrcc:main:dump/ubuntu.iso
You can simply edit using owner/user config from usetting without adding mrcc: before the path"""

extract_zip = """<b>Extract/Zip</b>: -e -z

/cmd link -e password (extract password protected)
/cmd link -z password (zip password protected)
/cmd link -z password -e (extract and zip password protected)
Note: When both extract and zip added with cmd it will extract first and then zip, so always extract first"""

join = """<b>Join Splitted Files</b>: -j

This option will only work before extract and zip, so mostly it will be used with -m argument (samedir)
By Reply:
/cmd -i 3 -j -m folder name
/cmd -b -j -m folder name
if u have link(folder) have splitted files:
/cmd link -j"""

tg_links = """<b>TG Links</b>:

Treat links like any direct link
Some links need user access so you must add USER_SESSION_STRING for it.
Three types of links:
Public: https://t.me/channel_name/message_id
Private: tg://openmessage?user_id=xxxxxx&message_id=xxxxx
Super: https://t.me/c/channel_id/message_id
Range: https://t.me/channel_name/first_message_id-last_message_id
Range Example: tg://openmessage?user_id=xxxxxx&message_id=555-560 or https://t.me/channel_name/100-150
Note: Range link will work only by replying cmd to it"""

sample_video = """<b>Sample Video</b>: -sv

Create sample video for one video or folder of videos.
/cmd -sv (it will take the default values which 60sec sample duration and part duration is 4sec).
You can control those values. Example: /cmd -sv 70:5(sample-duration:part-duration) or /cmd -sv :5 or /cmd -sv 70."""

screenshot = """<b>ScreenShots</b>: -ss

Create screenshots for one video or folder of videos.
/cmd -ss (it will take the default values which is 10 photos).
You can control this value. Example: /cmd -ss 6."""

zip_arg = """<b>Zip</b>: -z password

/cmd link -z (zip)
/cmd link -z password (zip password protected)"""

convert_media = """<b>Convert Media</b>: -ca -cv
/cmd link -ca mp3 -cv mp4 (convert all audios to mp3 and all videos to mp4)
/cmd link -ca mp3 (convert all audios to mp3)
/cmd link -cv mp4 (convert all videos to mp4)
/cmd link -ca mp3 + flac ogg (convert only flac and ogg audios to mp3)
/cmd link -cv mkv - webm flv (convert all videos to mp4 except webm and flv)"""

force_start = """<b>Force Start</b>: -f -fd -fu
/cmd link -f (force download and upload)
/cmd link -fd (force download only)
/cmd link -fu (force upload directly after download finish)"""

gdrive = """<b>Gdrive</b>: link
If DEFAULT_UPLOAD is `rc` then you can pass up: `gd` to upload using gdrive tools to GDRIVE_ID.
/cmd gdriveLink or gdl or gdriveId -up gdl or gdriveId or gd
/cmd tp:gdriveLink or tp:gdriveId -up tp:gdriveId or gdl or gd (to use token.pickle if service account enabled)
/cmd sa:gdriveLink or sa:gdriveId -p sa:gdriveId or gdl or gd (to use service account if service account disabled)
/cmd mtp:gdriveLink or mtp:gdriveId -up mtp:gdriveId or gdl or gd(if you have added upload gdriveId from usetting) (to use user token.pickle that uploaded by usetting)
You can simply edit using owner/user token from usetting without adding mtp: before the id"""

rclone_cl = """<b>Rclone</b>: path
If DEFAULT_UPLOAD is `gd` then you can pass up: `rc` to upload to RCLONE_PATH.
/cmd rcl/rclone_path -up rcl/rclone_path/rc -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue
/cmd rcl or rclone_path -up rclone_path or rc or rcl
/cmd mrcc:rclone_path -up rcl or rc(if you have add rclone path from usetting) (to use user config)
You can simply edit using owner/user config from usetting without adding mrcc: before the path"""

name_sub = r"""<b>Name Substitution</b>: -ns
/cmd link -ns script/code/s | mirror/leech | tea/ /s | clone | cpu/ | \[mltb\]/mltb | \\text\\/text/s
This will affect on all files. Format: wordToReplace/wordToReplaceWith/sensitiveCase
Word Subtitions. You can add pattern instead of normal text. Timeout: 60 sec
NOTE: You must add \ before any character, those are the characters: \^$.|?*+()[]{}-
1. script will get replaced by code with sensitive case
2. mirror will get replaced by leech
4. tea will get replaced by space with sensitive case
5. clone will get removed
6. cpu will get replaced by space
7. [mltb] will get replaced by mltb
8. \text\ will get replaced by text with sensitive case
"""

transmission = """<b>Tg transmission</b>: -hl -ut -bt
/cmd link -hl (leech by user and bot session with respect to size) (Hybrid Leech)
/cmd link -bt (leech by bot session)
/cmd link -ut (leech by user)"""

thumbnail_layout = """Thumbnail Layout: -tl
/cmd link -tl 3x3 (widthxheight) 3 photos in row and 3 photos in column"""

leech_as = """<b>Leech as</b>: -doc -med
/cmd link -doc (Leech as document)
/cmd link -med (Leech as media)"""

ffmpeg_cmds = """<b>FFmpeg Commands</b>: -ff
list of lists of ffmpeg commands. You can set multiple ffmpeg commands for all files before upload. Don't write ffmpeg at beginning, start directly with the arguments.
Notes:
1. Add <code>-del</code> to the list(s) which you want from the bot to delete the original files after command run complete!
3. To execute one of pre-added lists in bot like: ({"subtitle": ["-i mltb.mkv -c copy -c:s srt mltb.mkv"]}), you must use -ff subtitle (list key)
Examples: ["-i mltb.mkv -c copy -c:s srt mltb.mkv", "-i mltb.video -c copy -c:s srt mltb", "-i mltb.m4a -c:a libmp3lame -q:a 2 mltb.mp3", "-i mltb.audio -c:a libmp3lame -q:a 2 mltb.mp3", "-i mltb -map 0:a -c copy mltb.mka -map 0:s -c copy mltb.srt", "-i mltb -i tg://openmessage?user_id=5272663208&message_id=322801 -filter_complex 'overlay=W-w-10:H-h-10' -c:a copy mltb"]
Here I will explain how to use mltb.* which is reference to files you want to work on.
1. First cmd: the input is mltb.mkv so this cmd will work only on mkv videos and the output is mltb.mkv also so all outputs is mkv. -del will delete the original media after complete run of the cmd.
2. Second cmd: the input is mltb.video so this cmd will work on all videos and the output is only mltb so the extenstion is same as input files.
3. Third cmd: the input in mltb.m4a so this cmd will work only on m4a audios and the output is mltb.mp3 so the output extension is mp3.
4. Fourth cmd: the input is mltb.audio so this cmd will work on all audios and the output is mltb.mp3 so the output extension is mp3.
5. Fifth cmd: You can add telegram link for small size input like photo to set watermark"""

MIRROR_HELP_DICT = {
    "main": mirror,
    "New-Name": new_name,
    "Extract/Zip": extract_zip,
    "Thumb": thumb,
    "Split-Size": split_size,
    "Upload-Destination": upload,
    "Rclone-Flags": rcf,
    "Bulk": bulk,
    "Join": join,
    "Rclone-DL": rlone_dl,
    "Tg-Links": tg_links,
    "Sample-Video": sample_video,
    "Screenshot": screenshot,
    "Convert-Media": convert_media,
    "Force-Start": force_start,
    "User-Download": user_download,
    "Name-Substitute": name_sub,
    "TG-Transmission": transmission,
    "Thumb-Layout": thumbnail_layout,
    "Leech-Type": leech_as,
    "FFmpeg-Cmds": ffmpeg_cmds,
}

CLONE_HELP_DICT = {
    "main": clone,
    "Gdrive": gdrive,
    "Rclone": rclone_cl,
}

PASSWORD_ERROR_MESSAGE = """
<b>This link requires a password!</b>
- Insert <b>::</b> after the link and write the password after the sign.

<b>Example:</b> link::my password
"""

user_settings_text = {
    "LEECH_SPLIT_SIZE": f"Send Leech split size in bytes or use gb or mb. Example: 40000000 or 2.5gb or 1000mb. IS_PREMIUM_USER: {TgClient.IS_PREMIUM_USER}. Timeout: 60 sec",
    "LEECH_DUMP_CHAT": """"Send leech destination ID/USERNAME/PM. 
* b:id/@username/pm (b: means leech by bot) (id or username of the chat or write pm means private message so bot will send the files in private to you) when you should use b:(leech by bot)? When your default settings is leech by user and you want to leech by bot for specific task.
* u:id/@username(u: means leech by user) This incase OWNER added USER_STRING_SESSION.
* h:id/@username(hybrid leech) h: to upload files by bot and user based on file size.
* id/@username|topic_id(leech in specific chat and topic) add | without space and write topic id after chat id or username. Timeout: 60 sec""",
    "LEECH_FILENAME_PREFIX": r"Send Leech Filename Prefix. You can add HTML tags. Example: <code>@mychannel</code>. Timeout: 60 sec",
    "THUMBNAIL_LAYOUT": "Send thumbnail layout (widthxheight, 2x2, 3x3, 2x4, 4x4, ...). Example: 3x3. Timeout: 60 sec",
    "RCLONE_PATH": "Send Rclone Path. If you want to use your rclone config edit using owner/user config from usetting or add mrcc: before rclone path. Example mrcc:remote:folder. Timeout: 60 sec",
    "RCLONE_FLAGS": "key:value|key|key|key:value . Check here all <a href='https://rclone.org/flags/'>RcloneFlags</a>\nEx: --buffer-size:8M|--drive-starred-only",
    "GDRIVE_ID": "Send Gdrive ID. If you want to use your token.pickle edit using owner/user token from usetting or add mtp: before the id. Example: mtp:F435RGGRDXXXXXX . Timeout: 60 sec",
    "INDEX_URL": "Send Index URL. Timeout: 60 sec",
    "UPLOAD_PATHS": "Send Dict of keys that have path values. Example: {'path 1': 'remote:rclonefolder', 'path 2': 'gdrive1 id', 'path 3': 'tg chat id', 'path 4': 'mrcc:remote:', 'path 5': b:@username} . Timeout: 60 sec",
    "EXCLUDED_EXTENSIONS": "Send exluded extenions separated by space without dot at beginning. Timeout: 60 sec",
    "NAME_SUBSTITUTE": r"""Word Subtitions. You can add pattern instead of normal text. Timeout: 60 sec
NOTE: You must add \ before any character, those are the characters: \^$.|?*+()[]{}-
Example: script/code/s | mirror/leech | tea/ /s | clone | cpu/ | \[mltb\]/mltb | \\text\\/text/s
1. script will get replaced by code with sensitive case
2. mirror will get replaced by leech
4. tea will get replaced by space with sensitive case
5. clone will get removed
6. cpu will get replaced by space
7. [mltb] will get replaced by mltb
8. \text\ will get replaced by text with sensitive case
""",
    "FFMPEG_CMDS": """Dict of list values of ffmpeg commands. You can set multiple ffmpeg commands for all files before upload. Don't write ffmpeg at beginning, start directly with the arguments.
Examples: {"subtitle": ["-i mltb.mkv -c copy -c:s srt mltb.mkv", "-i mltb.video -c copy -c:s srt mltb"], "convert": ["-i mltb.m4a -c:a libmp3lame -q:a 2 mltb.mp3", "-i mltb.audio -c:a libmp3lame -q:a 2 mltb.mp3"], "extract": ["-i mltb -map 0:a -c copy mltb.mka -map 0:s -c copy mltb.srt"], "metadata": ["-i mltb.mkv -map 0 -map -0:v:1 -map -0:s -map 0:s:0 -map -0:v:m:attachment -c copy -metadata:s:v:0 title={title} -metadata:s:a:0 title={title} -metadata:s:a:1 title={title2} -metadata:s:a:2 title={title2} -c:s srt -metadata:s:s:0 title={title3} mltb -y -del"], "watermark": ["-i mltb -i tg://openmessage?user_id=5272663208&message_id=322801 -filter_complex 'overlay=W-w-10:H-h-10' -c:a copy mltb"]}
Notes:
- Add `-del` to the list which you want from the bot to delete the original files after command run complete!
- To execute one of those lists in bot for example, you must use -ff subtitle (list key) or -ff convert (list key)
Here I will explain how to use mltb.* which is reference to files you want to work on.
1. First cmd: the input is mltb.mkv so this cmd will work only on mkv videos and the output is mltb.mkv also so all outputs is mkv. -del will delete the original media after complete run of the cmd.
2. Second cmd: the input is mltb.video so this cmd will work on all videos and the output is only mltb so the extenstion is same as input files.
3. Third cmd: the input in mltb.m4a so this cmd will work only on m4a audios and the output is mltb.mp3 so the output extension is mp3.
4. Fourth cmd: the input is mltb.audio so this cmd will work on all audios and the output is mltb.mp3 so the output extension is mp3.
5. FFmpeg Variables in last cmd which is metadata ({title}, {title2}, etc...), you can edit them in usetting
6. Telegram link for small size inputs like photo to set watermark.""",
}


help_string = f"""
NOTE: Try each command without any argument to see more detalis.
/{BotCommands.MirrorCommand[0]} or /{BotCommands.MirrorCommand[1]}: Start mirroring to cloud.
/{BotCommands.LeechCommand[0]} or /{BotCommands.LeechCommand[1]}: Start leeching to Telegram.
/{BotCommands.CloneCommand} [drive_url]: Copy file/folder to Google Drive.
/{BotCommands.CountCommand} [drive_url]: Count file/folder of Google Drive.
/{BotCommands.DeleteCommand} [drive_url]: Delete file/folder from Google Drive (Only Owner & Sudo).
/{BotCommands.UserSetCommand[0]} or /{BotCommands.UserSetCommand[1]} [query]: Users settings.
/{BotCommands.BotSetCommand[0]} or /{BotCommands.BotSetCommand[1]} [query]: Bot settings.
/{BotCommands.CancelTaskCommand[0]} or /{BotCommands.CancelTaskCommand[1]} [gid]: Cancel task by gid or reply.
/{BotCommands.ForceStartCommand[0]} or /{BotCommands.ForceStartCommand[1]} [gid]: Force start task by gid or reply.
/{BotCommands.CancelAllCommand} [query]: Cancel all [status] tasks.
/{BotCommands.ListCommand} [query]: Search in Google Drive(s).
/{BotCommands.StatusCommand}: Shows a status of all the downloads.
/{BotCommands.StatsCommand}: Show stats of the machine where the bot is hosted in.
/{BotCommands.PingCommand}: Check how long it takes to Ping the Bot (Only Owner & Sudo).
/{BotCommands.AuthorizeCommand}: Authorize a chat or a user to use the bot (Only Owner & Sudo).
/{BotCommands.UnAuthorizeCommand}: Unauthorize a chat or a user to use the bot (Only Owner & Sudo).
/{BotCommands.UsersCommand}: show users settings (Only Owner & Sudo).
/{BotCommands.AddSudoCommand}: Add sudo user (Only Owner).
/{BotCommands.RmSudoCommand}: Remove sudo users (Only Owner).
/{BotCommands.RestartCommand}: Restart and update the bot (Only Owner & Sudo).
/{BotCommands.LogCommand}: Get a log file of the bot. Handy for getting crash reports (Only Owner & Sudo).
/{BotCommands.ShellCommand}: Run shell commands (Only Owner).
/{BotCommands.AExecCommand}: Exec async functions (Only Owner).
/{BotCommands.ExecCommand}: Exec sync functions (Only Owner).
/{BotCommands.ClearLocalsCommand}: Clear {BotCommands.AExecCommand} or {BotCommands.ExecCommand} locals (Only Owner).
"""
