class Affix:

    def __init__(self, morpheme, gloss, harmony):
        self.morpheme = morpheme
        self.gloss = gloss
        self.harmony = harmony

class Circumfix:

    def __init__(self, prefix, suffix,  prefix_gloss, suffix_gloss, harmony):
        self.prefix = prefix
        self.suffix = suffix
        self.prefix_gloss = prefix_gloss
        self.suffix_gloss = suffix_gloss
        self.harmony = harmony



