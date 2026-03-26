import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from api.models import Crop

def main():
    crops = Crop.objects.all()
    water_options = ["Low", "Medium", "High"]
    for c in crops:
        if not c.water:
            # Pick a random subset of 1 to 2 options so they aren't all the same
            k = random.randint(1, 2)
            c.water = random.sample(water_options, k)
            c.save()
    print("Updated water requirements for crops.")

if __name__ == "__main__":
    main()
