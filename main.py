set1={'A','B','C','D','E'}
set2={'B','Y','C','L','K','Z'}

union=set1.intersection(set2)

total_guests=list(union)

print("total guests to be invited in party are :", len(total_guests))
print("Guest list:",total_guests)