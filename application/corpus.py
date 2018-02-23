from MyCapytain.resources.prototypes.cts.inventory import CtsTextInventoryCollection, CtsTextInventoryMetadata
from MyCapytain.resolvers.utils import CollectionDispatcher


from capitains_nautilus.cts.resolver import NautilusCTSResolver

# Setting up the collections

general_collection = CtsTextInventoryCollection()

priapeia = CtsTextInventoryMetadata("priapeia_collection", parent=general_collection)
priapeia.set_label("Priapeia", "eng")
priapeia.set_label("Priapées", "fre")

hchn = CtsTextInventoryMetadata("id:hchn", parent=general_collection)
misc.set_label("HCHN Texts", "eng")
misc.set_label("Textes HCHN", "fre")

@organizer.inventory("priapeia_collection")
def organize_my_priapeia(collection, path=None, **kwargs):
    if collection.id.startswith("urn:cts:latinLit:phi1103"):
        return True
    return False

@organizer.inventory("hchn_collection")
def organize_my_hchn(collection, path=None, **kwargs):
    # If we are not dealing with Priapeia
    if not collection.id.startswith("urn:cts:latinLit:phi1103"):
        # # Textgroups have a wonderful shortcut to their editions and translations : .readableDescendants
        # for text in collection.readableDescendants:
        #     for citation in text.citation:
        #         if citation.name == "line":
                    return True
    return False


# Parsing the data
resolver = NautilusCTSResolver(["corpora/hchn", "corpora/priapeia"], dispatcher=organizer)
resolver.parse()
