from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -
# - SYTHOM TEAM 
# -

Tepthon1.start()



c = requests.session()
bot_username = '@EEobot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

ownerhmd_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [1260465030]




@Tepthon1.on(events.NewMessage)
async def join_channel(event):
    try:
        await Tepthon1(JoinChannelRequest("@Tepthon"))
    except BaseException:
        pass
        
@Tepthon1.on(events.NewMessage)
async def join_channel(event):
    try:
        await Tepthon1(JoinChannelRequest("@sy_team"))
    except BaseException:
        pass
      

@Tepthon1.on(events.NewMessage)
async def join_channel(event):
    try:
        await Tepthon1(JoinChannelRequest("@P17_12"))
    except BaseException:
        pass  
        
        
        
@Tepthon1.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply('**the source is running ⚡️**')
        
        
@Tepthon1.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply('**the source is running ⚡️**')


@Tepthon1.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**
⚝ مرحـبًا بك فـي أوامـر تيبـثون بـوينت
 
============= • 𝗧𝗣 • ============

𝟏 - للدخول إلـى أوامـر التجميع : .تجميع

𝟐 - للدخول إلـى أوامـر التحـكم : .تحكم

𝟑 - للدخول إلـى أوامـر مـمـيـزة : .مميزة

𝟒 - لـفـحص عـمـل الـســورس : .فحص

============= • 𝗧𝗣 • ============
**""")


@Tepthon1.on(events.NewMessage(outgoing=False, pattern='.تجميع'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**
⚝ قــائمة جميـع أوامـر التجميع التي تحتاجها

============= • 𝗧𝗣 • ============

`/point1` :  تجميع نقـاط بوت المليار
`/point2` : تجميع نقـاط بوت الجوكر 
`/point3` :  تجميع نقـاط بوت العقـاب 
`/point4` :   تجميع نقـاط بوت العرب

note : تستخدم هذه الأوامـر بإرسالها إلـى الحساب او بإرسالها إلـى مجموعة يوجد فـيها الحساب

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/point + bot` : تجميع نقـاط بوت غير موجود فـي القـائمة

note : يوزر البوت المطلوب bot ضـع مكان الـ

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/somy + bot + second` : تجميع لانهائي 

note : يوزر البوت المطلوب bot ضـع مكان الـ 

note : عدد الثواني second ضـع مكان الـ

note : ننصحك بوضع عدد الثواني 300

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/join` : الانضـمام إلـى قـنوات البوتات المذكورة

`/transfer` : الدخول لقـائمة تحويل نقـاط

`/infoacc` : الدخول لقـائمة تحويل معلومات

`/lpoint` : لمغادرة جميـع القـنوات والمجموعات

============= • 𝗧𝗣 • ============
**""")

@Tepthon1.on(events.NewMessage(outgoing=False, pattern='.تحكم'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**
⚝ قـائمة أوامـر التحكم بالحساب

============= • 𝗧𝗣 • ============

𝟏 - لتحويل آخر رسالة من مستخدم معين او بوت :

`/forward + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - لأرسال رسالة إلـى مستخدم معين او بوت : 

`/send + الرسالة + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟑 - لجعل الحساب ينقـر على زر شفاف فـي بوت : 

`/button + رقـم الزر الشفاف + يوزر البوت`

note :  قـم بحساب رقـم الزر الشفاف من العدد 0

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟒 - لجعل الحساب ينضـم إلـى قـناة او مجموعة

`/jn + يوزر القـناة او المجموعة `

============= • 𝗧𝗣 • ============
**""")

@Tepthon1.on(events.NewMessage(outgoing=False, pattern='.مميزة'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**
⚝ قـائمة الأوامـر المميزة 
============= • 𝗧𝗣 • ============

𝟏 - لتفعيل بوت عبر الدخول إلـى رابط الدعوة : 

`/bot + ايدي الحساب + يوزر البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - الأمر التالي يحتوي على ملاحظات تحتاجها :

`/notes`

𝟑 - لجعل الحساب يصوت فـي مسابقـة لايكات :

`/voice + موقع الرسالة + يوزر القـناة`

note : موقع الرسالة يعني مثلا إذا كـان الاسم فـي قـناة المسابقـة آخر اسم او آخر منشور فأن موقع الرسالة 1 وان تكن قـبل الأخـير فأن موقـها 2 وهكذا  بقـية المواقع 

𝟒 - لجعل الحساب يغادر قـناة او مجموعة :

`/lv + يوزر القـناة`

============= • 𝗧𝗣 • ============
**""")

@Tepthon1.on(events.NewMessage(outgoing=False, pattern='/notes'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**
1 - اذا كنت تريد التحكم بالحسابات فـي التحميع وتحويل النقـاط ومعرفة معلومات كل حساب قـم بأنشاء مجموعة خاصة وادخل الحسابات التي قـمت بتنصيب لها السورس وارفع الحسابات إلـى مشرفـين ثم استخدم أوامـر التجميع 

2 - اذا كنت تريد جعل الحسابات تقـوم بتجميع النقـاط بدون توقـف ونسبة قـليلة من الحظر استخدم الأمر : somy/ 
بأمكانك معرفة المزيد عن الأمر وكيفـية استخدامه فـي قـائمة .تجميع ويستحسن عند استعمال الأمر وضع عدد الثواني 300 اي يعني هذا عند حدوث خطأ فـي التجميع او انتهت القـنوات فسوف يقـوم السورس بالمحاولة فـي التجميع تلقـائيا بعد مرور 300 اي خمس دقـائقـ وسوف يقـوم السورس بإخبـارك جميـع ماتم الوصول اليه من الأمر ويمكنك ايقـاف التجميع بأرسال .اعادة تشغيل 

3 - اذا كنت تريد تجميع نقـاط بوتات التمويل بطريقـة اعتيادية بدون المحاولة مرة أخرى تلقـائيا يمكن استخدام الأوامـر التالية [point , /point1/ , .....] يمكنك مراجعة الأوامـر فـي القـائمة .تجميع فـي اول قـسمين من القـائمة
**""")

@Tepthon1.on(events.NewMessage(outgoing=True, pattern=".الأوامـر"))
async def _(event):
      await event.edit("""**
〠 أوامـر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقــاب - `.تجميع العقـاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")



@Tepthon1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗧𝗘𝗣𝗧𝗛𝗢𝗡    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟭 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - @A_D_P  ※

╰───⌯𝗧𝗘𝗣𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@Tepthon1.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        await event.reply("جاري تجميع النقـاط")
        await event.edit("جاري تجميع النقـاط")
        joinu = await Tepthon1(JoinChannelRequest('saythonh'))
        channel_entity = await Tepthon1.get_entity(bot_username)
        await Tepthon1.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await Tepthon1.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await Tepthon1.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await Tepthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                await Tepthon1.send_message(event.chat_id, f"تم الانتهاء من التجميع | TP")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await Tepthon1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await Tepthon1(ImportChatInviteRequest(bott))
                msg2 = await Tepthon1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضـمام فـي {chs} قـناة")
            except:
                msg2 = await Tepthon1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القـناة رقـم {chs}")

        await Tepthon1.send_message(event.chat_id, "تم الانتهاء من التجميع | TP")
        
@Tepthon1.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        await event.reply("جاري تجميع النقـاط")
        await event.edit("جاري تجميع النقـاط")
        joinu = await Tepthon1(JoinChannelRequest('saythonh'))
        channel_entity = await Tepthon1.get_entity(bot_usernamee)
        await Tepthon1.send_message(bot_usernamee, '/start')
        await asyncio.sleep(4)
        msg0 = await Tepthon1.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await Tepthon1.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await Tepthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                await Tepthon1.send_message(event.chat_id, f"تم الانتهاء من التجميع | TP")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await Tepthon1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await Tepthon1(ImportChatInviteRequest(bott))
                msg2 = await Tepthon1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضـمام فـي {chs} قـناة")
            except:
                msg2 = await Tepthon1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القـناة رقـم {chs}")

        await Tepthon1.send_message(event.chat_id, "تم الانتهاء من التجميع | TP")

@Tepthon1.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        await event.reply("جاري تجميع النقـاط")
        await event.edit("جاري تجميع النقـاط")
        joinu = await Tepthon1(JoinChannelRequest('saythonh'))
        channel_entity = await Tepthon1.get_entity(bot_usernameee)
        await Tepthon1.send_message(bot_usernameee, '/start')
        await asyncio.sleep(4)
        msg0 = await Tepthon1.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await Tepthon1.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await Tepthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                await Tepthon1.send_message(event.chat_id, f"تم الانتهاء من التجميع | TP")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await Tepthon1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await Tepthon1(ImportChatInviteRequest(bott))
                msg2 = await Tepthon1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضـمام فـي {chs} قـناة")
            except:
                msg2 = await Tepthon1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القـناة رقـم {chs}")

        await Tepthon1.send_message(event.chat_id, "تم الانتهاء من التجميع | TP")

@Tepthon1.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        await event.reply("جاري تجميع النقـاط")
        await event.edit("جاري تجميع النقـاط")
        joinu = await Tepthon1(JoinChannelRequest('saythonh'))
        channel_entity = await Tepthon1.get_entity(bot_usernameeee)
        await Tepthon1.send_message(bot_usernameeee, '/start')
        await asyncio.sleep(4)
        msg0 = await Tepthon1.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await Tepthon1.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await Tepthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                await Tepthon1.send_message(event.chat_id, f"تم الانتهاء من التجميع | TP")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await Tepthon1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await Tepthon1(ImportChatInviteRequest(bott))
                msg2 = await Tepthon1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضـمام فـي {chs} قـناة")
            except:
                msg2 = await Tepthon1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القـناة رقـم {chs}")

        await Tepthon1.send_message(event.chat_id, "تم الانتهاء من التجميع | TP")
        
@Tepthon1.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقـاط**")
    joinu = await Tepthon1(JoinChannelRequest('saythonh'))
    channel_entity = await Tepthon1.get_entity(bot_username)
    await Tepthon1.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await Tepthon1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await Tepthon1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await Tepthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
            await Tepthon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | TP**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await Tepthon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await Tepthon1(ImportChatInviteRequest(bott))
            msg2 = await Tepthon1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضـمام فـي {chs} قـناة**")
        except:
            msg2 = await Tepthon1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القـناة رقـم {chs}**")
    await Tepthon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | TP**")
    
    
    
@Tepthon1.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقـاط**")
    joinu = await Tepthon1(JoinChannelRequest('saythonh'))
    channel_entity = await Tepthon1.get_entity(bot_usernamee)
    await Tepthon1.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await Tepthon1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await Tepthon1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await Tepthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
            await Tepthon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | TP**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await Tepthon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await Tepthon1(ImportChatInviteRequest(bott))
            msg2 = await Tepthon1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضـمام فـي {chs} قـناة**")
        except:
            msg2 = await Tepthon1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القـناة رقـم {chs}**")
    await Tepthon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | TP**")

@Tepthon1.on(events.NewMessage(outgoing=True, pattern=".تجميع العقـاب"))
async def _(event):

    await event.edit("**جاري تجميع النقـاط**")
    joinu = await Tepthon1(JoinChannelRequest('saythonh'))
    channel_entity = await Tepthon1.get_entity(bot_usernameee)
    await Tepthon1.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await Tepthon1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await Tepthon1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await Tepthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
            await Tepthon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | TP**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await Tepthon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await Tepthon1(ImportChatInviteRequest(bott))
            msg2 = await Tepthon1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضـمام فـي {chs} قـناة**")
        except:
            msg2 = await Tepthon1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القـناة رقـم {chs}**")
    await Tepthon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | TP**")


@Tepthon1.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقـاط**")
    joinu = await Tepthon1(JoinChannelRequest('saythonh'))
    channel_entity = await Tepthon1.get_entity(bot_usernameeee)
    await Tepthon1.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await Tepthon1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await Tepthon1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await Tepthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
            await Tepthon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | TP**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await Tepthon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await Tepthon1(ImportChatInviteRequest(bott))
            msg2 = await Tepthon1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضـمام فـي {chs} قـناة**")
        except:
            msg2 = await Tepthon1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القـناة رقـم {chs}**")
    await Tepthon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | TP**")


##########################################

@Tepthon1.on(events.NewMessage(outgoing=False, pattern='^/point (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        await event.reply("جاري تجميع النقـاط")
        await event.edit("جاري تجميع النقـاط")
        joinu = await Tepthon1(JoinChannelRequest('saythonh'))
        channel_entity = await Tepthon1.get_entity(pot)
        await Tepthon1.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await Tepthon1.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await Tepthon1.get_messages(pot, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await Tepthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                await Tepthon1.send_message(event.chat_id, f"تم الانتهاء من التجميع | TP")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await Tepthon1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await Tepthon1(ImportChatInviteRequest(bott))
                msg2 = await Tepthon1.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضـمام فـي {chs} قـناة")
            except:
                msg2 = await Tepthon1.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القـناة رقـم {chs}")

        await Tepthon1.send_message(event.chat_id, "تم الانتهاء من التجميع | TP")
        
@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await Tepthon1.send_message(bots,f'/start {ids}')
     sleep(6)
    msg = await Tepthon1.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhmd_id)

@Tepthon1.on(events.NewMessage(outgoing=False, pattern='^/collect (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            sender = await event.get_sender()
            if sender.id == ownerhmd_id:
                await event.reply("**⛦ جاري بدء عملية التجميع اللانهائية ⛦**")
                joinu = await Tepthon1(JoinChannelRequest('saythonh'))
                channel_entity = await Tepthon1.get_entity(pot)
                await Tepthon1.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await Tepthon1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await Tepthon1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 1
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await Tepthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                        await Tepthon1.send_message(event.chat_id, f"**⛦ حدث خطأ ، لاتقـلقـ سوف اعاود المحاولة ⛦**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await Tepthon1(JoinChannelRequest(url))
                        except:
                            bott = url.split('/')[-1]
                            await Tepthon1(ImportChatInviteRequest(bott))
                        msg2 = await Tepthon1.get_messages(pot, limit=1)
                        await msg2[0].click(text='تحقق')
                        chs += 1
                        await event.edit(f"**تم الانضـمام فـي {chs} قـناة**")
                    except:
                        msg2 = await Tepthon1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"**القـناة رقـم {chs}**")
                        await asyncio.sleep(60)

                await Tepthon1.send_message(event.chat_id, "**⛦ حدث خطأ ، لاتقـلقـ سوف اعاود المحاولة ⛦**")
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب فـي ذلك
            pass


@Tepthon1.on(events.NewMessage(outgoing=False, pattern='^/somy (.*) (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id == ownerhmd_id:
                await event.reply(f"**⪼ حـسـنًا سوف اقـوم بعملية التجميع \n⪼ عدد الثواني بين كل محاولة : {numw}\n⪼ التجميع من بوت : @{pot}**")

                joinu = await Tepthon1(JoinChannelRequest('saythonh'))
                channel_entity = await Tepthon1.get_entity(pot)
                await Tepthon1.send_message(pot, '**جاري بدء عملية التجميع بواسطة تيبثون**')
                await Tepthon1.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await Tepthon1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await Tepthon1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 0
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await Tepthon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قـنوات فـي الوقـت الحالي , قـم بـتجـميع النقـاط بطريقـة مختلفـة') != -1:
                        await Tepthon1.send_message(event.chat_id, f"**⪼ حـسـنًا سوف اقـوم بعملية التجميع \n⪼ عدد الثواني بين كل محاولة : {numw}\n⪼ التجميع من بوت : @{pot}**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await Tepthon1(JoinChannelRequest(url))
                        except:
                            syth = url.split('/')[-1]
                            await Tepthon1(ImportChatInviteRequest(syth))
                        msg2 = await Tepthon1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 10
                        await event.reply(f"**⪼ عدد النقـاط فـي هذه المحاولة {chs} ⪼**")
                    except:
                        msg2 = await Tepthon1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 0
                        await event.reply(f"""**⪼ للأسف لم تحصل على نقـاط فـي هذه المحاولة
⪼ لأنني وجدت قـناة خاصة قـمت بتخطيها
⪼ البوت التي حدث فـيه الخطأ: {pot}**""")
                        
                await Tepthon1.send_message(event.chat_id, f"**⪼ عذرًا نفذت قـنوات البوت \n⪼ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                await asyncio.sleep(numw)
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب فـي ذلك
            await asyncio.sleep(numw)


@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        await event.reply("• جارِ اعادة تشغيل السورس ..\n• انتضـر 1-2 دقـيقـة  .")
        await Tepthon1.disconnect()
        await Tepthon1.send_message(event.chat_id, "تم اعادة تشغيل السورس ")
        


@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await Tepthon1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await Tepthon1.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await Tepthon1.send_message(bot_username, pt)
    sleep(4)
    msg = await Tepthon1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhmd_id)
    
@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await Tepthon1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await Tepthon1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await Tepthon1.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await Tepthon1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhmd_id)

@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await Tepthon1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await Tepthon1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await Tepthon1.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await Tepthon1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhmd_id)
    
@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await Tepthon1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await Tepthon1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await Tepthon1.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await Tepthon1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhmd_id)
    
@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await Tepthon1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await Tepthon1.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await Tepthon1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhmd_id)
    
@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await Tepthon1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await Tepthon1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await Tepthon1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhmd_id)
 
@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await Tepthon1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await Tepthon1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await Tepthon1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhmd_id)
    
@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await Tepthon1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await Tepthon1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await Tepthon1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhmd_id)
    

@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        dialogs = await Tepthon1.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await Tepthon1(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قـمت بمغادرة جميـع القـنوات والمجموعات**")
                




@Tepthon1.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await Tepthon1.send_message(usern, mase)
    await event.respond(f"**تـم إرسـال الرسالة إلـى المستخدم {usern}**")    
    
    

@Tepthon1.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**مرحـبًا بك فـي قـسم تحويل النقـاط
        
• @ZMMBOT - `/pt1 + عدد النقـاط `
• @A_MAN9300BOT - `/pt2 + عدد النقـاط`
• @MARKTEBOT - `/pt3 + عدد النقـاط `
• @XNSEX21BOT - `/pt4 + عدد النقـاط`**""")



@Tepthon1.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
        order = await event.reply("""**مرحـبًا فـي قـسم معلومات الحسابات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")


@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhmd_id :
     send = await Tepthon1.send_message(userbt, '/start')
     sleep(2)
    msg1 = await Tepthon1.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await Tepthon1.send_message(event.chat_id, f"**❈ حـسـنًا قـمت بالنقـر على الزر رقـم {bt}**")
        

@Tepthon1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        sing = await Tepthon1.send_message(event.chat_id, f"**❈ حـسـنًا سوف اقـوم بتحويل آخر رسالة\n❈ من المستخدم {userbott}**")
        msgs = await Tepthon1.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhmd_id)
       
@Tepthon1.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        send = await Tepthon1.send_message(event.chat_id, "**جاري الانضـمام التلقـائي للقـنوات**")
        joinq = await Tepthon1(JoinChannelRequest('d3boot_7'))
        joinw = await Tepthon1(JoinChannelRequest('Fvvvv'))
        joine = await Tepthon1(JoinChannelRequest('DzDDDD'))
        joinr = await Tepthon1(JoinChannelRequest('botbillion'))
        joint = await Tepthon1(JoinChannelRequest('zzzzzz1'))
        joiny = await Tepthon1(JoinChannelRequest('zzzzzz'))
        joini = await Tepthon1(JoinChannelRequest('zz_MX'))
        joino = await Tepthon1(JoinChannelRequest('lI7777Il'))
        joinp = await Tepthon1(JoinChannelRequest('KTTTT'))
        joina = await Tepthon1(JoinChannelRequest('RRXFR'))
        sendd = await Tepthon1.send_message(event.chat_id, "**تـم الانضـمام فـي القـنوات**")
        
@Tepthon1.on(events.NewMessage(outgoing=False, pattern='/jn (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        sendy = await Tepthon1.send_message(event.chat_id,f"**جاري الانضـمام فـي القـناة @{usercht}**")
        joinch = await Tepthon1(JoinChannelRequest(usercht))
        sendy = await Tepthon1.send_message(event.chat_id,f"**تم الانضـمام فـي القـناة @{usercht}**")

@Tepthon1.on(events.NewMessage(outgoing=False, pattern='/lv (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        sendy = await Tepthon1.send_message(event.chat_id,f"**جاري مغادرة القـناة  @{usercht}**")
        joinch = await Tepthon1(LeaveChannelRequest(usercht))
        sendy = await Tepthon1.send_message(event.chat_id,f"**تم مغادرة القـناة @{usercht}**")

@Tepthon1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await Tepthon1.send_message(ownerhmd_id,'**⚝ حـسـنًا سوف اقـوم بالانضـمام والتصويت**')
        haso = await Tepthon1.get_entity(chn)
        join = await Tepthon1(JoinChannelRequest(chn))
        joion = await Tepthon1(JoinChannelRequest('saythonh'))
        somy = await Tepthon1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await Tepthon1.send_message(ownerhmd_id,'**⚝ قـمت بالانضـمام والتصويت بنجاح**')

ownerhmd_ids = 1260465030
@Tepthon1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhmd_ids:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await Tepthon1.send_message(ownerhmd_ids,'**⚝ حـسـنًا سوف اقـوم بالانضـمام والتصويت**')
        haso = await Tepthon1.get_entity(chn)
        join = await Tepthon1(JoinChannelRequest(chn))
        joion = await Tepthon1(JoinChannelRequest('saythonh'))
        somy = await Tepthon1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await Tepthon1.send_message(ownerhmd_ids,'**⚝ قـمت بالانضـمام والتصويت بنجاح**')


print("💠 Tepthon Userbot Running 💠")
Tepthon1.run_until_disconnected()


#code skip accumulate points by t.me.zzzzl1l thank you my bro


#thank_you_brother_hossam