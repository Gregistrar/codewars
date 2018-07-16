# My Solution

def human_years_cat_years_dog_years(human_years):
    cat = 0
    dog = 0
    counter_cat = 0
    counter_dog = 0
    while counter_cat < human_years:
        if cat == 0:
          cat += 15
          dog += 15
        elif counter_cat == 1:
          cat += 9
          dog += 9
        else:
          cat += 4
          dog += 5
        counter_cat += 1
    return [human_years, cat, dog]
