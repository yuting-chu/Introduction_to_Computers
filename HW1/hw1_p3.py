#hw1_p3
#經濟系大三 D54101039朱郁庭

#輸入velocity的值，並轉換成float
velocity=float(input("Input velocity: "))

#計算輸入的速度和光速的比例，並印出結果
light_speed_percentage=velocity/299792458
print("Percentage of light speed = ",light_speed_percentage)

#按照公式算出factor的值，分別算出到不同星球的時間並印出
factor=1/((1-light_speed_percentage**2)**0.5)
print("Travel time to Alpha Centauri = ",4.3/factor)
print("Travel time to Barnard's Star = ",6.0/factor)
print("Travel time to Betelgeuse (in the Milky Way) = ", 309/factor)
print("Travel time to Andromeda Galaxy (closest galaxy) = ",2000000 /factor)