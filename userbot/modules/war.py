from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.sayang(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("**Cuma Mau Bilang**")
    sleep(3)
    await typew.edit("**Aku Sayang Kamu**")
    sleep(1)
    await typew.edit("**I LOVE YOU 💞**")


# Create by myself @localheart


@register(outgoing=True, pattern=r"^\.kyura(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("**Hai Perkenalkan Nama Ku Kyura**")
    sleep(3)
    await typew.edit("**18 Tahun Dari Jakarta**")
    sleep(1)
    await typew.edit("**Salam Kenal Ya Kontol**")


# Create by myself @localheart


@register(outgoing=True, pattern=r"^\.jamet(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WOII**")
    sleep(1.5)
    await typew.edit("**JAMET KONTOL**")
    sleep(1.5)
    await typew.edit("**CUMA MAU BILANG**")
    sleep(1.5)
    await typew.edit("**GAUSAH SO ASIK**")
    sleep(1.5)
    await typew.edit("**EMANG KENAL?**")
    sleep(1.5)
    await typew.edit("**GAUSAH REPLY**")
    sleep(1.5)
    await typew.edit("**KITA BUKAN KAWAN**")
    sleep(1.5)
    await typew.edit("**GASUKA PC ANJING**")
    sleep(1.5)
    await typew.edit("**BOCAH KAMPUNG**")
    sleep(1.5)
    await typew.edit("**MENTAL TEMPE**")
    sleep(1.5)
    await typew.edit("**LEMBEK NGENTOT🔥**")


@register(outgoing=True, pattern=r"^\.pp(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**PASANG PP DULU NGENTOT,BIAR ORANG-ORANG TAU BETAPA HINA NYA MUKA LU**"
    )


@register(outgoing=True, pattern=r"^\.dp(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU HINA, GAUSAH SOK KERAS YA NGENTOT!!**")


@register(outgoing=True, pattern=r"^\.so(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOKAB SAMA GUA NGENTOT, LU BABU GA LEVEL!!**")


@register(outgoing=True, pattern=r"^\.met(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA BHAHAHA**")


@register(outgoing=True, pattern=r"^\.war(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN...**"
    )


@register(outgoing=True, pattern=r"^\.wartai(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA TOLOL**"
    )


@register(outgoing=True, pattern=r"^\.kismin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU NGENTOT!!**"
    )


@register(outgoing=True, pattern=r"^\.ded(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI**")


@register(outgoing=True, pattern=r"^\.sokab(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SOKAB BET SI LU NGENTOT!!**")


@register(outgoing=True, pattern=r"^\.gembel(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS KONTOL!!**"
    )


@register(outgoing=True, pattern=r"^\.cuih(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**CIH GE KEREN LO BEGITU GOBLOK!!**")


@register(outgoing=True, pattern=r"^\.dih(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU KONTOL!**"
    )


@register(outgoing=True, pattern=r"^\.gcs(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GC SAMPAH KAYA GINI, BUBARIN AJA GOBLOK!!**")


CMD_HELP.update(
    {
        "war": "**Plugin : **`war`\
        \n\n  •  **Syntax :** `.jamet`\
        \n  •  **Function : **Menghina Jamet telegram\
        \n\n  •  **Syntax :** `.pp`\
        \n  •  **Function : **Menghina Jamet telegram yang ga pake foto profil\
        \n\n  •  **Syntax :** `.dp`\
        \n  •  **Function : **Menghina Jamet muka hina!\
        \n\n  •  **Syntax :** `.so`\
        \n  •  **Function : **Ngeledek orang sokab\
        \n\n  •  **Syntax :** `.met`\
        \n  •  **Function : **Ngeledek si jamet caper\
        \n\n  •  **Syntax :** `.war`\
        \n  •  **Function : **Ngeledek orang so keras ngajak war\
        \n\n  •  **Syntax :** `.wartai`\
        \n  •  **Function : **Ngeledek orang so ketrigger ngajak cod minta sharelok\
        \n\n  •  **Syntax :** `.kismin`\
        \n  •  **Function : **Ngeledek orang kismin so jagoan di tele\
        \n\n  •  **Syntax :** `.ded`\
        \n  •  **Function : **Nyuruh orang mati aja goblok wkwk\
        \n\n  •  **Syntax :** `.sokab`\
        \n  •  **Function : **Ngeledek orang so kenal so dekat padahal kga kenal goblok\
        \n\n  •  **Syntax :** `.gembel`\
        \n  •  **Function : **Ngeledek bapaknya si jamet\
        \n\n  •  **Syntax :** `.cuih`\
        \n  •  **Function : **ngatain orang sok keren\
        \n\n  •  **Syntax :** `.dih`\
        \n  •  **Function : **Ngeledek anak haram\
        \n\n  •  **Syntax :** `.gcs`\
        \n  •  **Function : **Ngeledek gc sampah\
        \n\n**Klo mau Req, kosa kata dari lu Hubungi @kyuraonly**\
    "
    }
)
