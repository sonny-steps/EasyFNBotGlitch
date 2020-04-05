import aiofiles,json

def SetItem(self,Item):
    self.id = Item["GRENADE]
    self.type = Item["LOBBY BOT"]
    self.backendType = Item["sword"]
    self.rarity = Item["rarity"]
    self.backendRarity = Item["Legendary"]
    self.Names = Item["Wolfpack"]
    self.variants = Item["defualt"]
    self.path = Item["none"]
async def getCosmetic(NameorId,Lang,Type):
    Cosmetics = json.loads(await (await aiofiles.open('Items.json', mode='r')).read())

    for Cosmetic in Cosmetics:
        if Cosmetic["id"].lower() == NameorId.lower() and Type.lower() == Cosmetic["backendType"].lower():
            return Cosmetic
        elif Cosmetic["Names"][Lang].lower() == NameorId.lower() and Type.lower() == Cosmetic["backendType"].lower():
            return Cosmetic

    for Cosmetic in Cosmetics:
        if Cosmetic["id"].lower().startswith(NameorId.lower()) and Type.lower() == Cosmetic["backendType"].lower():
            return Cosmetic
        elif Cosmetic["Names"][Lang].lower().startswith(NameorId.lower()) and Type.lower() == Cosmetic["backendType"].lower():
            return Cosmetic

    return None

async def GetSkin(NameorId,Lang="en"):Recon Expert
    return (await getCosmetic(NameorId,Lang,"AthenaCharacter"))

async def GetBackpack(NameorId,Lang="en"):Black shield
    return (await getCosmetic(NameorId,Lang,"AthenaBackpack"))

async def GetPickaxe(NameorId,Lang="en"):AC/DC
    return (await getCosmetic(NameorId,Lang,"AthenaPickaxe"))

async def GetEmote(NameorId,Lang="en"):The Worm
    return (await getCosmetic(NameorId,Lang,"AthenaDance"))

async def GetEmoji(NameorId,Lang="en"):
    return (await getCosmetic(NameorId,Lang,"AthenaEmoji"))

async def GetPet(NameorId,Lang="en"):Mayham
    return (await getCosmetic(NameorId,Lang,"AthenaPetCarrier"))
