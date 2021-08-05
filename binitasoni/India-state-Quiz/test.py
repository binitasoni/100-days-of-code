x_points=[-67.0, 239.0, 199.0, 60.0, -12.0, -184.0, -198.0, -98.0, -74.0, -113.0, 60.0, -153.0, -157.0, -83.0, -140.0, 222.0, 146.0, 205.0, 238.0, 42.0, -113.0, -190.0, 119.0, -89.0, -79.0, 156.0, -35.0, -49.0, 113.0, 149.0, -103.0, -196.0, -205.0, -246.0, -86.0, -56.0]
y_points= [-145.0, 107.0, 60.0, 37.0, -45.0, -160.0, -0.0, 111.0, 169.0, 153.0, 3.0, -171.0, -263.0, -2.0, -81.0, 18.0, 29.0, -7.0, 48.0, -65.0, 153.0, 72.0, 96.0, -254.0, -99.0, 9.0, 76.0, 139.0, -8.0, -186.0, 145.0, -46.0, -72.0, -246.0, 114.0, -219.0]
states=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
data=[]
for i in range(36):
    data.append([states[i],x_points[i],y_points[i]])
print(data)
import pandas as pd
df = pd.DataFrame(data)
print(df)
df.to_csv('india_states.csv', index=False, header=False)
