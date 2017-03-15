from  ..models.categories import Category
import re

def get_all_subcategories(category):
    sub_categories = []
    regex = r'^(' + re.escape(category) + ')'
    queryset = Category.objects.filter(name__regex=regex).values_list('name', flat=True)
    return queryset 
