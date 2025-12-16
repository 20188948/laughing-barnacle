score_list=[]
name_list=[]
def safe_round(value, decimals=0):
    """Safely round a number to the given decimal places."""
    try:
        num = float(value)  # Convert to float
        return round(num, decimals)
    except ValueError:
        raise ValueError(f"Invalid number: {value}")
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list.append(name,)
        score_list.append(score)
for val in score_list:
    rounded_val = safe_round(val, 2)  
    score_list.append(rounded_val)
lowest=0
second_lowest=0
print(score_list)
'''
for i in score_list:
    if score_list[i]<lowest:
        lowest=lowest+score_list[i]
    elif score_list[i]<second_lowest:
        second_lowest=second_lowest+score_list[i]
print(lowest)
print(second_lowest)
'''