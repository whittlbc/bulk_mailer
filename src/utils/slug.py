from slugify import Slugify

to_slug = Slugify(to_lower=True, separator='_', safe_chars='_')