# marshasthd
# marsha-Userbott

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.wlcm(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
        "───█▒▒░░░░░░░░░▒▒█───\n"
        "────█░░█░░░░░█░░█────\n"
        "─▄▄──█░░░▀█▀░░░█──▄▄─\n"
        "█░░█─▀▄░░░░░░░▄▀─█░░█\n"
        "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
        "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
        "█░░║║║╠─║─║─║║║║║╠─░░█\n"
        "█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
        "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
    )


@register(outgoing=True, pattern="^.wlc(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
        "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
        "█░░║║║╠─║─║─║║║║║╠─░░█\n"
        "█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
        "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
    )


@register(outgoing=True, pattern="^.klb(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "   ╚⊙ ⊙╝..\n"
        "   ╚═(███)═╝\n"
        "    ╚═(███)═╝\n"
        "       ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "      ╚═(███)═╝\n"
        "     ╚═(███)═╝\n"
        "    ╚═(███)═╝ \n"
        "    ╚═(███)═╝\n"
        "     ╚═(███)═╝\n"
        "      ╚═(███)═╝\n"
        "       ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "        ╚═(███)═╝\n"
        "       ╚═(███)═╝\n"
        "      ╚═(███)═╝\n"
        "     ╚═(███)═╝\n"
        "     ╚═(███)═╝\n"
        "      ╚═(█)═╝\n"
    )


@register(outgoing=True, pattern="^.lari(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "──▄█▀█▄─────────██\n"
        "▄████████▄───▄▀█▄▄▄▄\n"
        "██▀▼▼▼▼▼─▄▀──█▄▄\n"
        "█████▄▲▲▲─▄▄▄▀───▀▄\n"
        "██████▀▀▀▀─▀────────▀▀\n"
        " **LARI IPINNN** \n"
    )


CMD_HELP.update(
    {
        "animasi9": "`.wlcm` ; `.wlc` ; `.klb` ; `.lari`\
    \nUsage: liat aja."
    }
)
