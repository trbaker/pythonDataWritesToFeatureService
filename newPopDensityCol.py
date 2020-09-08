#!/usr/local/bin/python3

from arcgis.gis import GIS

server="https://education.maps.arcgis.com"
username="tbaker"
password=""
gis=GIS(server,username,password)

#read feature service
MappingHourUsers = gis.content.search("id:32e1e9fe09d7420e9386461da7f1add4")

#access the item's feature layers
users_item = MappingHourUsers[0]
users_layers = users_item.layers

# edit or delete the feature service record to indicate account created.
users_fset = users_layers[0].query()
users_features = users_fset.features

users_flayer = users_layers[0]
for x in range(0, 250):
  try:
    OneRecord_feature = [f for f in users_features if (1==1)][x]
  except:
    break

  # AGO account details
  pop19=OneRecord_feature.attributes['F2019']
  sqmi=OneRecord_feature.attributes['SQMI']
  if (pop19 != None) and (sqmi != None):
    print(x,'. Name: ', OneRecord_feature.attributes['F2019'])
    # set up edit
    OneRecord_edit = OneRecord_feature
    OneRecord_edit.attributes['popdensity_2019'] = round(pop19/sqmi, 2)
    # commit update
    update_result = users_flayer.edit_features(updates=[OneRecord_edit])
    #update_result



