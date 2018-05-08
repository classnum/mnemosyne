from MyCapytain.resources.prototypes.cts.inventory import CtsTextInventoryCollection, CtsTextInventoryMetadata
from MyCapytain.resolvers.utils import CollectionDispatcher

from capitains_nautilus.cts.resolver import NautilusCTSResolver

# Setting up the collections

general_collection = CtsTextInventoryCollection()

greek_texts = CtsTextInventoryMetadata("mnemosyne:grec", parent=general_collection)
greek_texts.set_label("Greek Texts", "eng")
greek_texts.set_label("Textes Grecs", "fre")

latin_texts = CtsTextInventoryMetadata("mnemosyne:latin", parent=general_collection)
latin_texts.set_label("Latin Texts", "eng")
latin_texts.set_label("Textes Latins", "fre")

misc = CtsTextInventoryMetadata("mnemosyne:misc", parent=general_collection)
misc.set_label("Miscellaneous", "eng")
misc.set_label("Textes Divers", "fre")


organizer = CollectionDispatcher(general_collection, default_inventory_name="mnemosyne:misc")


@organizer.inventory("mnemosyne:grec")
def organize_my_grec(collection, path=None, **kwargs):
    if collection.id.startswith("urn:cts:greekLit:"):
        return True
    return False


@organizer.inventory("mnemosyne:latin")
def organize_my_latin(collection, path=None, **kwargs):
    if collection.id.startswith("urn:cts:latinLit:"):
        return True
    return False


# Parsing the data
resolver = NautilusCTSResolver(["corpora/hchn"], dispatcher=organizer)
resolver.parse()
