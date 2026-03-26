import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Crop

def load_data():
    json_path = os.path.join(os.path.dirname(__file__), 'static', 'data', 'mastercrops.json')
    if not os.path.exists(json_path):
        print(f"File not found: {json_path}")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data:
        Crop.objects.update_or_create(
            name=item['crop'],
            defaults={
                'primary_category': item.get('primary_category', 'Uncategorized'),
                'suitability_reason': item.get('suitability_reason', ''),
                'pro_tips': item.get('pro_tips', ''),
                'categories': item.get('categories', []),
                'soil': item.get('soil', []),
                'climate': item.get('climate', []),
                'districts': item.get('districts', []),
                'water': item.get('water', []),
                'season': item.get('season', ''),
                'months': item.get('months', '')
            }
        )
    print("Crop data loaded successfully!")

if __name__ == '__main__':
    load_data()
